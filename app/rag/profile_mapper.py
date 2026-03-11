# profile_mapper.py: DB 객체를 RAG 입력값으로 바꾸기
# rag_pipeline.py: query 생성, 검색, context 만들기
# GuideService에서 바로 쓰기 편하게 HealthProfile 객체를 RAG 입력 형식으로 바꾸는 함수
# app/rag/profile_mapper.py

from typing import Any


def extract_diseases_from_profile(
    disease_list: list[str] | None = None,
    other_disease: str | None = None,
) -> tuple[list[str], str | None]:
    """
    질환 목록과 기타 질환명을 RAG 입력 형식으로 정리한다.

    현재는 간단하게:
    - 선택된 대표 질환 목록
    - 기타 질환 문자열
    를 그대로 반환한다.
    """
    selected_diseases = disease_list or []
    other_disease = other_disease.strip() if other_disease else None
    return selected_diseases, other_disease


def extract_lifestyle_from_profile(health_profile: Any) -> dict[str, Any]:
    """
    HealthProfile 객체에서 RAG query 생성에 필요한 생활습관 정보만 추출한다.
    """

    return {
        "smoking_status": getattr(health_profile, "smoking_status", None),
        "drinking_status": getattr(health_profile, "drinking_status", None),
        "exercise_frequency": getattr(health_profile, "exercise_frequency", None),
        "diet_type": getattr(health_profile, "diet_type", None),
        "sleep_change": getattr(health_profile, "sleep_change", None),
        "weight_change": getattr(health_profile, "weight_change", None),
    }
