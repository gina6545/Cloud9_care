import os
from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile, status

from app.dependencies.security import get_request_user
from app.models.user import User
from app.services.upload import UploadService

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "uploads")

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

upload_router = APIRouter(prefix="/uploads", tags=["upload"])


@upload_router.post("", status_code=status.HTTP_201_CREATED)
async def upload_file(
    user: Annotated[User, Depends(get_request_user)],
    files: list[UploadFile] = File(...),  # noqa: B008
):
    """
    [UPLOAD] 이미지 업로드(처방전/알약 앞/뒤)
    """
    upload_service = UploadService()
    return await upload_service.file_save(user, files)
