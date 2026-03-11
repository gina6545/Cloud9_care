from app.rag.rag_pipeline import generate_rag_context
from app.rag.vector_store import build_sample_vector_store


def main():
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

    rag_context = generate_rag_context(
        selected_diseases,
        other_disease,
        lifestyle,
    )

    print("\n===== RAG CONTEXT =====")
    print(rag_context)


if __name__ == "__main__":
    main()
