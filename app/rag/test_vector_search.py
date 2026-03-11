# app/rag/test_vector_search.py

from app.rag.vector_store import (
    build_sample_vector_store,
    pretty_print_results,
    search_similar_documents,
)


def main():
    print("1. 샘플 문서를 Chroma에 저장합니다.")
    build_sample_vector_store()

    print("\n2. 유사 문서를 검색합니다.")
    query = "고혈압 식이 관리"
    print(f"검색어: {query}")

    results = search_similar_documents(query_text=query, n_results=3)
    pretty_print_results(results)


if __name__ == "__main__":
    main()
