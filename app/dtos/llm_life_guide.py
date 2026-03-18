# guide.py : 프론트 응답용 / llm_life_guide.py : DB 저장용
from pydantic import BaseModel


class LlmLifeGuideResponse(BaseModel):
    user_current_status: str
    generated_content: dict
    activity: bool  # Aggregate of the three below (for backward compatibility)
    activity_medication: bool = False
    activity_disease: bool = False
    activity_profile: bool = False
    created_at: str


class LlmLifeGuideRequest(BaseModel):
    user_current_status: str
    activity_medication: bool = False
    activity_disease: bool = False
    activity_profile: bool = False
