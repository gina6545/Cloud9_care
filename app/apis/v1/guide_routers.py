import asyncio
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends

from app.dependencies.security import get_optional_user
from app.dtos.llm_life_guide import LlmLifeGuideResponse
from app.models.user import User
from app.services.guide import GuideService

guide_router = APIRouter(prefix="/guides", tags=["guide"])


@guide_router.post("/refresh")
async def refresh_all_guides(
    background_tasks: BackgroundTasks,
    user: Annotated[User | None, Depends(get_optional_user)] = None,
):
    """
    모든 가이드 섹션에 대해 갱신을 트리거합니다. (지연 실행용)
    """
    if not user:
        return {"status": "skipped", "message": "사용자 정보가 없습니다."}

    service = GuideService()
    user_id = str(user.id)
    # 병렬로 모든 섹션 트리거
    await asyncio.gather(
        service.generate_modular_guide(user_id, "MEDICATION", background_tasks),
        service.generate_modular_guide(user_id, "DISEASE", background_tasks),
        service.generate_modular_guide(user_id, "PROFILE", background_tasks),
    )
    return {"status": "success", "message": "모든 가이드 갱신 태스크가 등록되었습니다."}


@guide_router.get("", response_model=LlmLifeGuideResponse)
async def get_guide(
    background_tasks: BackgroundTasks,
    user: Annotated[User | None, Depends(get_optional_user)] = None,
):
    service = GuideService()
    return await service.get_saved_guide(user, background_tasks)


@guide_router.get("/{id}")
async def get_guide_detail(id: int, user: Annotated[User | None, Depends(get_optional_user)] = None):
    return {"id": id, "guide_type": "복약"}


@guide_router.patch("/{id}")
async def update_guide(id: int, user: Annotated[User | None, Depends(get_optional_user)] = None):
    return {"id": id, "detail": "갱신되었습니다."}
