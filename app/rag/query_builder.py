# 사용자 건강 정보를 받아서 검색 query를 만드는 파일
# app/rag/query_builder.py

from typing import Any

from app.rag.taxonomy import (
    LIFESTYLE_TOPIC_RULES,
    find_disease_group,
    is_known_disease,
)


# 사용자의 질환 목록을 RAG에서 쓰기 위한 표준 구조로 정리
def normalize_user_diseases(selected_diseases: list[str], other_disease: str | None = None) -> list[dict[str, str]]:
    """
    사용자 선택 질환 + 기타 입력 질환을 표준 구조로 정리한다.

    반환 예시:
    [
        {"name": "고혈압", "group": "심뇌혈관 및 대사 질환"},
        {"name": "역류성식도염", "group": "기타"}
    ]
    """
    normalized = []

    for disease in selected_diseases:
        normalized.append({"name": disease, "group": find_disease_group(disease)})

    if other_disease:
        other_disease = other_disease.strip()
        if other_disease:
            if is_known_disease(other_disease):
                normalized.append({"name": other_disease, "group": find_disease_group(other_disease)})
            else:
                normalized.append({"name": other_disease, "group": "기타"})

    return normalized


# 생활 습관을 보고, 어떤 주제를 더 검색할지 정함
def extract_topics_from_lifestyle(lifestyle: dict[str, Any]) -> list[str]:
    """
    생활습관 정보를 보고 추가 검색이 필요한 topic을 뽑는다.
    """
    topics = set()

    for field_name, value_topic_map in LIFESTYLE_TOPIC_RULES.items():
        user_value = lifestyle.get(field_name)
        if user_value in value_topic_map:
            for topic in value_topic_map[user_value]:
                topics.add(topic)

    return list(topics)


# 최종 검색 query를 만듬
def build_queries(
    diseases: list[dict[str, str]],
    lifestyle: dict[str, Any],
    include_default_topics: bool = True,
) -> list[str]:
    """
    질환 + 생활습관 기반으로 RAG 검색 query를 만든다.

    예:
    [
        "고혈압 식이 관리",
        "고혈압 운동 관리",
        "고혈압 복약 관리"
    ]
    """
    queries = set()

    default_topics = ["식이", "운동", "복약", "모니터링", "합병증예방"] if include_default_topics else []
    lifestyle_topics = extract_topics_from_lifestyle(lifestyle)

    final_topics = set(default_topics + lifestyle_topics)

    topics_with_manage_suffix = {"식이", "운동", "복약", "모니터링", "금연", "절주", "수면"}

    for disease in diseases:
        disease_name = disease["name"]

        for topic in final_topics:
            if topic in topics_with_manage_suffix:
                queries.add(f"{disease_name} {topic} 관리")
            else:
                queries.add(f"{disease_name} {topic}")

    return sorted(list(queries))
