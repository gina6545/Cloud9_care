# 재적재 전용 스크립트
from app.rag.vector_store import build_sample_vector_store


def main():
    print("Chroma vector store를 다시 구축합니다.")
    build_sample_vector_store()
    print("재구축 완료")


if __name__ == "__main__":
    main()
    