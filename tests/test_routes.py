import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from webapp import create_app
from webapp.data.tax_offices import REGIONS, region_office_count


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_shows_seven_regions(client):
    assert len(REGIONS) == 7


def test_index_shows_all_region_names(client):
    response = client.get("/")
    body = response.get_data(as_text=True)
    for region in REGIONS:
        assert region["name"] in body


def test_total_office_count_is_133(client):
    total = sum(region_office_count(region) for region in REGIONS)
    assert total == 133


@pytest.mark.parametrize(
    "region_id,expected_count",
    [
        ("seoul", 28),
        ("jungbu", 25),
        ("incheon", 15),
        ("daejeon", 17),
        ("gwangju", 15),
        ("daegu", 14),
        ("busan", 19),
    ],
)
def test_region_office_counts(client, region_id, expected_count):
    response = client.get(f"/region/{region_id}")
    assert response.status_code == 200

    region = next(r for r in REGIONS if r["id"] == region_id)
    assert region_office_count(region) == expected_count


def test_region_detail_invalid_id_returns_404(client):
    response = client.get("/region/invalid")
    assert response.status_code == 404


def test_office_detail_shows_org_url_and_phone(client):
    response = client.get("/region/jungbu/office/hwaseong")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "화성세무서" in body
    assert "031-8019-1200" in body
    assert "https://www.nts.go.kr/hwaseong/ad/tsm/bassInfo.do?mi=8911" in body


@pytest.mark.parametrize(
    "office_id,expected_slug",
    [
        ("eunpyeong", "eunpyung"),
        ("gimpo", "kimpo"),
        ("susung", "suseong"),
        ("jungbu-seoul", "jungbu"),
        ("gangnam", "gangnam"),
    ],
)
def test_org_url_uses_correct_slug(client, office_id, expected_slug):
    from webapp.data.tax_offices import office_org_url

    assert office_org_url(office_id) == (
        f"https://www.nts.go.kr/{expected_slug}/ad/tsm/bassInfo.do?mi=8911"
    )


def test_office_detail_invalid_office_returns_404(client):
    response = client.get("/region/jungbu/office/invalid")
    assert response.status_code == 404


def test_office_detail_invalid_region_returns_404(client):
    response = client.get("/region/invalid/office/hwaseong")
    assert response.status_code == 404


def test_api_regions_returns_seven(client):
    response = client.get("/api/regions")
    assert response.status_code == 200
    assert len(response.get_json()) == 7


def test_api_region_detail_ok(client):
    response = client.get("/api/regions/seoul")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "서울지방국세청"


def test_api_office_detail_ok(client):
    response = client.get("/api/regions/seoul/office/gangnam")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "강남세무서"
    assert data["phone"] == "02-519-4200"
    assert data["org_url"] == "https://www.nts.go.kr/gangnam/ad/tsm/bassInfo.do?mi=8911"


def test_api_office_detail_invalid_returns_404(client):
    response = client.get("/api/regions/seoul/office/invalid")
    assert response.status_code == 404
