# 표준 질환명 / 질환 그룹 / topic 목록을 모아두는 파일
# app/rag/taxonomy.py

# 질환 분류표
DISEASE_TAXONOMY = {
    "심뇌혈관 및 대사 질환": [
        "고혈압",
        "당뇨병",
        "이상지질혈증",
        "심근경색",
        "뇌졸중",
        "동맥경화증",
    ],
    "호흡기 및 간 질환": [
        "만성 폐쇄성 폐질환(COPD)",
        "천식",
        "만성 간염",
        "간경변증",
    ],
    "근골격계 및 신경계 질환": [
        "관절염",
        "류마티스 관절염",
        "골다공증",
        "치매",
        "통풍",
    ],
    "기타": [
        "암",
        "갑상선 질환",
        "만성 신부전증",
    ],
}

# 검색할 주제 목록
TOPIC_TAXONOMY = [
    "식이",
    "운동",
    "체중관리",
    "수면",
    "금연",
    "절주",
    "복약",
    "모니터링",
    "정기검진",
    "합병증예방",
]

# 사용자 생활습관 입력값을 보고 추가로 검색할 주제를 결정한다.
LIFESTYLE_TOPIC_RULES = {
    "smoking_status": {
        "흡연": ["금연"],
        "과거 흡연": ["금연"],
        "비흡연": [],
    },
    "drinking_status": {
        "음주": ["절주"],
        "과거 음주": ["절주"],
        "비음주": [],
    },
    "exercise_frequency": {
        "안함": ["운동"],
        "주 1~2회": ["운동"],
        "주 3회 이상": [],
    },
    "diet_type": {
        "불규칙적": ["식이"],
        "패스트푸드": ["식이", "체중관리"],
        "균형 잡힌": [],
        "저염": [],
        "저탄수화물": [],
        "고단백": [],
        "채식": [],
        "모름": [],
    },
    "sleep_change": {
        "감소": ["수면"],
        "증가": ["수면"],
        "변화없음": [],
        "모름": [],
    },
    "weight_change": {
        "감소": ["체중관리"],
        "증가": ["체중관리"],
        "변화없음": [],
        "모름": [],
    },
}


def find_disease_group(disease_name: str) -> str:
    """
    질환명을 받아서 어떤 질환 그룹에 속하는지 반환한다.
    없으면 '기타' 반환.
    """
    for group_name, disease_list in DISEASE_TAXONOMY.items():
        if disease_name in disease_list:
            return group_name
    return "기타"


def is_known_disease(disease_name: str) -> bool:
    """
    taxonomy에 등록된 표준 질환인지 확인한다.
    """
    for disease_list in DISEASE_TAXONOMY.values():
        if disease_name in disease_list:
            return True
    return False
