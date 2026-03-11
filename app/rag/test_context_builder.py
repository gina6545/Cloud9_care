# app/rag/test_context_builder.py

from app.rag.context_builder import build_context_from_search_results
from app.rag.query_builder import build_queries, normalize_user_diseases
from app.rag.vector_store import build_sample_vector_store, search_similar_documents


def main():
    print("1. 샘플 문서를 Chroma에 저장합니다.")
    build_sample_vector_store()

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

    print("\n2. 사용자 질환 정보를 정리합니다.")
    diseases = normalize_user_diseases(selected_diseases, other_disease)
    for disease in diseases:
        print(disease)

    print("\n3. 검색 query를 생성합니다.")
    queries = build_queries(diseases, lifestyle)
    for query in queries:
        print("-", query)

    print("\n4. 각 query로 유사 문서를 검색합니다.")
    results_list = []
    for query in queries[:5]:
        results = search_similar_documents(query_text=query, n_results=2)
        results_list.append(results)

    print("\n5. 검색 결과를 rag_context로 변환합니다.")
    rag_context = build_context_from_search_results(
        results_list=results_list,
        max_docs=5,
        include_metadata=True,
    )

    print("\n===== RAG CONTEXT =====")
    print(rag_context)


if __name__ == "__main__":
    main()
