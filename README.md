# 전국 세무서 전화번호 안내

담당자가 인사이동으로 바뀌어도, 관할 세무서의 국세청 공식 "조직과 기능" 페이지로
바로 연결할 수 있도록 만든 사내용 웹앱입니다. 지방국세청(7곳) → 세무서 선택
순서로 화면을 좁혀가며 원하는 세무서의 조직·담당 부서 정보 페이지로 이동합니다.

## 주요 기능

- 1단계: 전국 지방국세청 7곳(서울·중부·인천·대전·광주·대구·부산) 중 선택
- 2단계: 선택한 지방국세청 산하 세무서를 지역(도)별로 묶어서 표시, 세무서 선택
- 3단계: 선택한 세무서의 국세청 공식 "조직과 기능" 페이지로 새 탭 이동 (대표전화도 함께 표시)
- 전국 133개 세무서의 조직과 기능 페이지 링크·대표전화를 JSON으로 제공하는 API
- 존재하지 않는 지방국세청/세무서 요청 시 404 처리

## 사용 기술

- Python 3.11+
- Flask
- Jinja2
- Bootstrap 5
- (DB 없음, 로그인 기능 없음)

## 프로젝트 구조

```text
tax_office_directory/
├── app.py
├── requirements.txt
├── README.md
├── webapp/
│   ├── __init__.py
│   ├── routes.py
│   ├── data/
│   │   └── tax_offices.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── regions.html
│   │   ├── region.html
│   │   ├── office.html
│   │   └── 404.html
│   └── static/
│       └── css/style.css
└── tests/
    └── test_routes.py
```

## 설치 방법

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
python app.py
```

브라우저에서 http://127.0.0.1:5000 접속

## 테스트 방법

```bash
pytest
```

## 관할 지방국세청 7곳

| 지방국세청 | 주요 관할 | 세무서 수 |
|---|---|---|
| 서울지방국세청 | 서울특별시 | 28 |
| 중부지방국세청 | 경기 일부·강원 | 25 |
| 인천지방국세청 | 인천·경기 북부 일부 | 15 |
| 대전지방국세청 | 대전·세종·충남·충북 | 17 |
| 광주지방국세청 | 광주·전남·전북 | 15 |
| 대구지방국세청 | 대구·경북 | 14 |
| 부산지방국세청 | 부산·울산·경남·제주 | 19 |

## 데이터 출처 안내

세무서 목록과 대표 전화번호는 요청 시 제공된 자료를 그대로 반영했습니다
(`webapp/data/tax_offices.py`). 조직 개편이나 번호 변경이 있을 수 있으니,
정기적으로 국세청 공식 자료와 대조해 갱신하는 것을 권장합니다.

## "조직과 기능" 링크 형식

각 세무서 버튼은 아래 형식의 국세청 공식 URL로 연결됩니다.

```text
https://www.nts.go.kr/{세무서 영문 슬러그}/ad/tsm/bassInfo.do?mi=8911
```

슬러그는 국세청 "전국 세무관서 - 이름으로 찾기"
(`https://www.nts.go.kr/nts/imArea/selectImAreaNmList.do?mi=6762`) 페이지에서
확인한 실제 경로를 사용했습니다. 내부 라우팅 id와 슬러그가 다른 3곳은
`webapp/data/tax_offices.py`의 `SLUG_OVERRIDES`에서 관리합니다
(은평→eunpyung, 김포→kimpo, 수성→suseong).
