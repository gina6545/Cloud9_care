from pydantic import BaseModel, Field, field_validator

VALID_REPEAT_DAYS = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"}


class AlarmResponse(BaseModel):
    id: int
    alarm_type: str
    medication_name: str | None = None
    alarm_time: str
    is_active: bool
    current_med_id: int | None = None
    repeat_days: list[str] = Field(default_factory=list)


class AlarmCreateRequest(BaseModel):
    alarm_type: str = Field(default="MED")
    current_med_id: int | None = Field(None)
    alarm_time: str
    repeat_days: list[str] | None = None

    @field_validator("repeat_days")
    @classmethod
    def validate_repeat_days(cls, value: list[str] | None) -> list[str] | None:
        if value is None:
            return None

        normalized = [day.upper() for day in value]
        invalid = [day for day in normalized if day not in VALID_REPEAT_DAYS]
        if invalid:
            raise ValueError(f"유효하지 않은 요일 값입니다: {invalid}")

        return normalized


class AlarmUpdateRequest(BaseModel):
    alarm_time: str | None = None
    is_active: bool | None = None
    repeat_days: list[str] | None = None

    @field_validator("repeat_days")
    @classmethod
    def validate_repeat_days(cls, value: list[str] | None) -> list[str] | None:
        if value is None:
            return None

        normalized = [day.upper() for day in value]
        invalid = [day for day in normalized if day not in VALID_REPEAT_DAYS]
        if invalid:
            raise ValueError(f"유효하지 않은 요일 값입니다: {invalid}")

        return normalized


class AlarmToggleRequest(BaseModel):
    is_active: bool


class AlarmHistoryResponse(BaseModel):
    history_id: int
    alarm_id: int
    alarm_type: str
    title: str
    body: str
    sent_at: str
    is_confirmed: bool


class DashboardAlarmItemResponse(BaseModel):
    time: str
    label: str
    is_confirmed: bool


class DashboardAlarmSummaryResponse(BaseModel):
    previous_alarm: DashboardAlarmItemResponse | None = None
    next_alarm: DashboardAlarmItemResponse | None = None
    remaining_text: str
