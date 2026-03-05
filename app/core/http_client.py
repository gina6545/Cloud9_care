# 우리 서버의 외부 통신 전용 컨트롤 타워
# 싱글톤 관리 : 서버 전체에서 오직 하나의 통신장비(클라이언트)만 생성

import httpx


class AsyncClientManager:
    """
    HTTPX AsyncClient를 싱글톤 패턴으로 관리하는 클래스입니다.
    FastAPI Lifespan을 통해 애플리케이션의 시작과 종료 시점에 맞춰 관리됩니다.
    """

    def __init__(self) -> None:
        self._client: httpx.AsyncClient | None = None

    def init_client(self) -> None:
        """클라이언트를 초기화합니다."""
        if self._client is None or self._client.is_closed:
            # 타임아웃 등 기본 설정을 여기에 정의할 수 있습니다.
            self._client = httpx.AsyncClient(timeout=60.0)

    async def close_client(self) -> None:
        """클라이언트를 안전하게 종료합니다."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    @property
    def client(self) -> httpx.AsyncClient:
        """현재 활성화된 클라이언트를 반환합니다."""
        if self._client is None:
            # 비정상적인 접근 시 자동 초기화 (가급적 lifespan에서 처리 권장)
            self.init_client()
        assert self._client is not None
        return self._client


# 전역 인스턴스 생성
http_client = AsyncClientManager()
