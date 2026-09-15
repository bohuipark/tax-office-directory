# 전국 지방국세청 7곳과 그 산하 세무서 목록 (관할 지역/전화번호는 사용자가 제공한
# 자료를 그대로 반영했다. 조직 개편·번호 변경이 있을 수 있으니 정기적으로 최신
# 정보와 대조해 갱신할 것을 권장한다.

# 세무서별 "조직과 기능" 페이지 URL 형식. 국세청 nts.go.kr에 실제 접속해서
# 화성/강남/제주/동대구/은평/김포/인천/세종 등 여러 지역에 대해 검증했다.
ORG_URL_TEMPLATE = "https://www.nts.go.kr/{slug}/ad/tsm/bassInfo.do?mi=8911"

# 아래 3곳은 내부 id(라우팅용)와 국세청 공식 사이트 경로(slug)가 서로 다르다.
# (전국 세무서 목록 페이지 https://www.nts.go.kr/nts/imArea/selectImAreaNmList.do
# 에서 실제 링크를 확인해 대조했다.)
SLUG_OVERRIDES = {
    "eunpyeong": "eunpyung",
    "gimpo": "kimpo",
    "susung": "suseong",
    "jungbu-seoul": "jungbu",
}


def office_org_url(office_id):
    slug = SLUG_OVERRIDES.get(office_id, office_id)
    return ORG_URL_TEMPLATE.format(slug=slug)

REGIONS = [
    {
        "id": "seoul",
        "name": "서울지방국세청",
        "area": "서울특별시",
        "groups": [
            {
                "province": "서울",
                "offices": [
                    ("gangnam", "강남세무서", "02-519-4200"),
                    ("gangdong", "강동세무서", "02-2224-0200"),
                    ("gangseo", "강서세무서", "02-2630-4200"),
                    ("gwanak", "관악세무서", "02-2173-4200"),
                    ("guro", "구로세무서", "02-2630-7200"),
                    ("geumcheon", "금천세무서", "02-850-4200"),
                    ("namdaemun", "남대문세무서", "02-2260-0200"),
                    ("nowon", "노원세무서", "02-3499-0200"),
                    ("dobong", "도봉세무서", "02-944-0200"),
                    ("dongdaemun", "동대문세무서", "02-958-0200"),
                    ("dongjak", "동작세무서", "02-840-9200"),
                    ("mapo", "마포세무서", "02-705-7200"),
                    ("banpo", "반포세무서", "02-590-4200"),
                    ("samsung", "삼성세무서", "02-3011-7200"),
                    ("seodaemun", "서대문세무서", "02-2287-4200"),
                    ("seocho", "서초세무서", "02-3011-6200"),
                    ("seongdong", "성동세무서", "02-460-4200"),
                    ("seongbuk", "성북세무서", "02-760-8200"),
                    ("songpa", "송파세무서", "02-2224-9200"),
                    ("yangcheon", "양천세무서", "02-2650-9200"),
                    ("yeoksam", "역삼세무서", "02-3011-8200"),
                    ("yeongdeungpo", "영등포세무서", "02-2630-9200"),
                    ("yongsan", "용산세무서", "02-748-8200"),
                    ("eunpyeong", "은평세무서", "02-2132-9200"),
                    ("jamsil", "잠실세무서", "02-2055-9200"),
                    ("jongno", "종로세무서", "02-760-9200"),
                    ("jungnang", "중랑세무서", "02-2170-0200"),
                    ("jungbu-seoul", "중부세무서", "02-2260-9200"),
                ],
            },
        ],
    },
    {
        "id": "jungbu",
        "name": "중부지방국세청",
        "area": "경기 일부·강원",
        "groups": [
            {
                "province": "경기",
                "offices": [
                    ("suwon", "수원세무서", "031-250-4200"),
                    ("dongsuwon", "동수원세무서", "031-695-4200"),
                    ("hwaseong", "화성세무서", "031-8019-1200"),
                    ("donghwaseong", "동화성세무서", "031-934-6200"),
                    ("pyeongtaek", "평택세무서", "031-650-0200"),
                    ("anyang", "안양세무서", "031-467-1200"),
                    ("donganyang", "동안양세무서", "031-389-8200"),
                    ("ansan", "안산세무서", "031-412-3200"),
                    ("dongansan", "동안산세무서", "031-937-3200"),
                    ("seongnam", "성남세무서", "031-730-6200"),
                    ("bundang", "분당세무서", "031-219-9200"),
                    ("yongin", "용인세무서", "031-329-2200"),
                    ("giheung", "기흥세무서", "031-8007-1200"),
                    ("icheon", "이천세무서", "031-644-0200"),
                    ("gyeonggigwangju", "경기광주세무서", "031-880-9200"),
                    ("guri", "구리세무서", "031-326-7200"),
                    ("namyangju", "남양주세무서", "031-550-3200"),
                    ("siheung", "시흥세무서", "031-310-7200"),
                ],
            },
            {
                "province": "강원",
                "offices": [
                    ("gangneung", "강릉세무서", "033-610-9200"),
                    ("samcheok", "삼척세무서", "033-570-0200"),
                    ("sokcho", "속초세무서", "033-639-9200"),
                    ("yeongwol", "영월세무서", "033-370-0200"),
                    ("wonju", "원주세무서", "033-740-9200"),
                    ("chuncheon", "춘천세무서", "033-250-0200"),
                    ("hongcheon", "홍천세무서", "033-430-1200"),
                ],
            },
        ],
    },
    {
        "id": "incheon",
        "name": "인천지방국세청",
        "area": "인천·경기 북부 일부",
        "groups": [
            {
                "province": "인천·경기북부",
                "offices": [
                    ("gyeyang", "계양세무서", "032-459-8200"),
                    ("goyang", "고양세무서", "031-900-9200"),
                    ("gwangmyeong", "광명세무서", "02-2610-8200"),
                    ("gimpo", "김포세무서", "031-980-3200"),
                    ("namdong", "남동세무서", "032-460-5200"),
                    ("nambucheon", "남부천세무서", "032-459-7200"),
                    ("donggoyang", "동고양세무서", "031-900-6200"),
                    ("bucheon", "부천세무서", "032-320-5200"),
                    ("bupyeong", "부평세무서", "032-540-6200"),
                    ("seoincheon", "서인천세무서", "032-560-5200"),
                    ("yeonsu", "연수세무서", "032-670-9200"),
                    ("uijeongbu", "의정부세무서", "031-870-4200"),
                    ("incheon", "인천세무서", "032-770-0200"),
                    ("paju", "파주세무서", "031-956-0200"),
                    ("pocheon", "포천세무서", "031-538-7200"),
                ],
            },
        ],
    },
    {
        "id": "daejeon",
        "name": "대전지방국세청",
        "area": "대전·세종·충남·충북",
        "groups": [
            {
                "province": "대전",
                "offices": [
                    ("daejeon", "대전세무서", "042-229-8200"),
                    ("seodaejeon", "서대전세무서", "042-480-8200"),
                    ("bukdaejeon", "북대전세무서", "042-603-8200"),
                ],
            },
            {
                "province": "세종",
                "offices": [
                    ("sejong", "세종세무서", "044-850-8200"),
                ],
            },
            {
                "province": "충남",
                "offices": [
                    ("gongju", "공주세무서", "041-850-3200"),
                    ("nonsan", "논산세무서", "041-730-8200"),
                    ("hongseong", "홍성세무서", "041-630-4200"),
                    ("yesan", "예산세무서", "041-330-5200"),
                    ("cheonan", "천안세무서", "041-559-8200"),
                    ("boryeong", "보령세무서", "041-930-9200"),
                    ("seosan", "서산세무서", "041-660-9200"),
                    ("asan", "아산세무서", "041-536-7200"),
                ],
            },
            {
                "province": "충북",
                "offices": [
                    ("cheongju", "청주세무서", "043-230-9200"),
                    ("yeongdong", "영동세무서", "043-740-6200"),
                    ("chungju", "충주세무서", "043-841-6200"),
                    ("jecheon", "제천세무서", "043-649-2200"),
                    ("dongcheongju", "동청주세무서", "043-229-4200"),
                ],
            },
        ],
    },
    {
        "id": "gwangju",
        "name": "광주지방국세청",
        "area": "광주·전남·전북",
        "groups": [
            {
                "province": "광주",
                "offices": [
                    ("gwangju", "광주세무서", "062-605-0200"),
                    ("bukgwangju", "북광주세무서", "062-520-9200"),
                    ("seogwangju", "서광주세무서", "062-380-5200"),
                    ("gwangsan", "광산세무서", "062-970-2200"),
                ],
            },
            {
                "province": "전남",
                "offices": [
                    ("mokpo", "목포세무서", "061-241-1200"),
                    ("naju", "나주세무서", "061-330-0200"),
                    ("haenam", "해남세무서", "061-530-6200"),
                    ("suncheon", "순천세무서", "061-720-0200"),
                    ("yeosu", "여수세무서", "061-688-0200"),
                ],
            },
            {
                "province": "전북",
                "offices": [
                    ("gunsan", "군산세무서", "063-470-3200"),
                    ("jeonju", "전주세무서", "063-250-0200"),
                    ("iksan", "익산세무서", "063-840-0200"),
                    ("jeongeup", "정읍세무서", "063-530-1200"),
                    ("namwon", "남원세무서", "063-630-2200"),
                    ("bukjeonju", "북전주세무서", "063-249-1200"),
                ],
            },
        ],
    },
    {
        "id": "daegu",
        "name": "대구지방국세청",
        "area": "대구·경북",
        "groups": [
            {
                "province": "대구",
                "offices": [
                    ("dongdaegu", "동대구세무서", "053-749-0200"),
                    ("seodaegu", "서대구세무서", "053-659-1200"),
                    ("bukdaegu", "북대구세무서", "053-350-4200"),
                    ("namdaegu", "남대구세무서", "053-659-0200"),
                    ("susung", "수성세무서", "053-749-6200"),
                ],
            },
            {
                "province": "경북",
                "offices": [
                    ("gyeongju", "경주세무서", "054-779-1200"),
                    ("pohang", "포항세무서", "054-245-2200"),
                    ("yeongdeok", "영덕세무서", "054-730-2200"),
                    ("andong", "안동세무서", "054-851-0200"),
                    ("gimcheon", "김천세무서", "054-420-3200"),
                    ("sangju", "상주세무서", "054-530-0200"),
                    ("yeongju", "영주세무서", "054-639-5200"),
                    ("gumi", "구미세무서", "054-468-4200"),
                    ("gyeongsan", "경산세무서", "053-819-3200"),
                ],
            },
        ],
    },
    {
        "id": "busan",
        "name": "부산지방국세청",
        "area": "부산·울산·경남·제주",
        "groups": [
            {
                "province": "부산",
                "offices": [
                    ("jungbusan", "중부산세무서", "051-240-0200"),
                    ("seobusan", "서부산세무서", "051-250-6200"),
                    ("busanjin", "부산진세무서", "051-461-9200"),
                    ("bukbusan", "북부산세무서", "051-310-6200"),
                    ("dongnae", "동래세무서", "051-860-2200"),
                    ("suyeong", "수영세무서", "051-620-9200"),
                    ("geumjeong", "금정세무서", "051-580-6200"),
                    ("haeundae", "해운대세무서", "051-660-9200"),
                    ("busangangseo", "부산강서세무서", "051-740-9200"),
                ],
            },
            {
                "province": "울산",
                "offices": [
                    ("ulsan", "울산세무서", "052-259-0200"),
                    ("dongulsan", "동울산세무서", "052-219-9200"),
                ],
            },
            {
                "province": "경남",
                "offices": [
                    ("masan", "마산세무서", "055-240-0200"),
                    ("changwon", "창원세무서", "055-239-0200"),
                    ("geochang", "거창세무서", "055-940-0200"),
                    ("tongyeong", "통영세무서", "055-640-7200"),
                    ("jinju", "진주세무서", "055-751-0200"),
                    ("gimhae", "김해세무서", "055-320-6200"),
                    ("yangsan", "양산세무서", "055-389-6200"),
                ],
            },
            {
                "province": "제주",
                "offices": [
                    ("jeju", "제주세무서", "064-720-5200"),
                ],
            },
        ],
    },
]


def get_region(region_id):
    for region in REGIONS:
        if region["id"] == region_id:
            return region
    return None


def get_office(region_id, office_id):
    region = get_region(region_id)
    if region is None:
        return None
    for group in region["groups"]:
        for oid, name, phone in group["offices"]:
            if oid == office_id:
                return {
                    "region_id": region["id"],
                    "region_name": region["name"],
                    "province": group["province"],
                    "id": oid,
                    "name": name,
                    "phone": phone,
                    "org_url": office_org_url(oid),
                }
    return None


def region_office_count(region):
    return sum(len(group["offices"]) for group in region["groups"])
