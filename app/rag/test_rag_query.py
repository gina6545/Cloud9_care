from app.rag.query_builder import normalize_user_diseases, build_queries

selected_diseases = ["고혈압", "당뇨병"]
other_disease = "역류성식도염"

lifestyle = {
    "smoking_status": "비흡연",
    "drinking_status": "비음주",
    "exercise_frequency": "주 1~2회",
    "diet_type": "패스트푸드",
    "sleep_change": "변화없음",
    "weight_change": "증가",
}

diseases = normalize_user_diseases(selected_diseases, other_disease)
queries = build_queries(diseases, lifestyle)

print("정리된 질환 목록:")
for disease in diseases:
    print(disease)

print("\n생성된 query 목록:")
for query in queries:
    print(query)
    