import asyncio
import json
from app.rag.rag_pipeline import generate_rag_context

async def test_hierarchical_rag():
    # TEST 1: Cold (Respiratory disease)
    print("Testing for '감기' (Respiratory)...")
    lifestyle = {
        "smoking_status": "비흡연",
        "drinking_status": "비음주",
        "exercise_frequency": "주 3회 이상",
        "diet_type": "균형 잡힌",
        "sleep_change": "변화없음",
        "weight_change": "변화없음"
    }
    
    # This should trigger filter: { "disease_group": {"$in": ["호흡기 및 간 질환", "공통", "기타"]} }
    # Wait, my new taxonomy uses "호흡기 질환".
    context = generate_rag_context(
        selected_diseases=["감기"],
        other_disease=None,
        lifestyle=lifestyle
    )
    
    print("\n--- RAG Context Result ---")
    print(context)
    print("--------------------------\n")

if __name__ == "__main__":
    asyncio.run(test_hierarchical_rag())
