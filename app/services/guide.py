from app.dtos.guide import GuideRequest, GuideResponse


class GuideService:
    # ==========================================
    # [추가된 기능] 필수 1: LLM 기반 안내 가이드 생성
    # ==========================================
    async def generate_guide(self, request: GuideRequest) -> GuideResponse:
        """
        사용자의 진료/복약 상세 정보를 결합하여 맞춤형 건강 가이드를 생성합니다.
        멀티모달 에셋 생성을 위한 기본 메타데이터를 포함합니다.

        Args:
            request (GuideRequest): 사용자 ID 및 의료 정보 (진료 기록, 복약 정보 등)

        Returns:
            GuideResponse: 생성된 가이드 텍스트, 분류, 위험도 및 구조화된 요약 정보
        """
        # TODO: LLM 연동 또는 ai_worker 통신 로직 구현 (진료 기록 + 복약 정보 결합)
        # 1. request.medical_records와 request.medication_info를 바탕으로 프롬프트 생성
        # 2. AI 모델 기반 응답 생성
        dummy_data = {
            "section1": {
                "title": "복약 안전성 및 주의사항",
                "status": "주의 필요",
                "content": "현재 복용 중인 약물과 알레르기 성분 사이에 경미한 상호작용 가능성이 있습니다.",
                "general_cautions": ["권장 용량을 초과하지 마세요.", "음주는 피해야 합니다."],
            },
            "section2": {
                "title": "질환 기반 생활습관 가이드",
                "disease_guides": [
                    {"name": "고혈압", "tips": ["저염식을 실천하세요.", "매일 30분 걷기를 추천합니다."]}
                ],
                "integrated_point": "심혈관 건강을 위해 식단과 운동 병행이 필수적입니다.",
            },
            "section3": {
                "title": "오늘의 실행 플랜",
                "checklist": ["물 1.5L 마시기", "약 제시간에 복용하기", "30분 산책하기"],
            },
            "section4": {
                "title": "왜 이런 가이드가 생성되었나요?",
                "reason": "사용자의 고혈압 병력과 현재 복용 중인 약물 정보를 바탕으로 작성되었습니다.",
            },
            "disclaimer": "본 서비스는 의료 진단이나 처방을 제공하지 않으며, 참고용 안내입니다.",
        }
        return GuideResponse(
            id=999,
            guide_data=dummy_data,
            created_at="2026-03-01T20:00:00",
            multimodal_assets=[],
        )
