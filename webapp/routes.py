from flask import Blueprint, abort, jsonify, render_template

from .data.tax_offices import (
    REGIONS,
    get_office,
    get_region,
    office_org_url,
    region_office_count,
)

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("regions.html", regions=REGIONS, count=region_office_count)


@bp.route("/region/<region_id>")
def region_detail(region_id):
    region = get_region(region_id)
    if region is None:
        abort(404)
    return render_template("region.html", region=region)


@bp.route("/region/<region_id>/office/<office_id>")
def office_detail(region_id, office_id):
    office = get_office(region_id, office_id)
    if office is None:
        abort(404)
    return render_template("office.html", office=office)


@bp.route("/api/regions")
def api_regions():
    return jsonify(
        [
            {
                "id": region["id"],
                "name": region["name"],
                "area": region["area"],
                "office_count": region_office_count(region),
            }
            for region in REGIONS
        ]
    )


@bp.route("/api/regions/<region_id>")
def api_region_detail(region_id):
    region = get_region(region_id)
    if region is None:
        abort(404)
    return jsonify(
        {
            "id": region["id"],
            "name": region["name"],
            "area": region["area"],
            "groups": [
                {
                    "province": group["province"],
                    "offices": [
                        {
                            "id": oid,
                            "name": name,
                            "phone": phone,
                            "org_url": office_org_url(oid),
                        }
                        for oid, name, phone in group["offices"]
                    ],
                }
                for group in region["groups"]
            ],
        }
    )


@bp.route("/api/regions/<region_id>/office/<office_id>")
def api_office_detail(region_id, office_id):
    office = get_office(region_id, office_id)
    if office is None:
        abort(404)
    return jsonify(office)


@bp.app_errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
