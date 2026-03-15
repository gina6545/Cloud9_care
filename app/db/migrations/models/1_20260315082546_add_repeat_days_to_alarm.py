from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` VARCHAR(100) NOT NULL PRIMARY KEY COMMENT '사용자 ID (이메일 주소)',
    `nickname` VARCHAR(40) NOT NULL,
    `name` VARCHAR(20) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    `provider` VARCHAR(20) NOT NULL DEFAULT 'local',
    `social_id` VARCHAR(100),
    `phone_number` VARCHAR(11) NOT NULL,
    `birthday` VARCHAR(10) NOT NULL,
    `gender` VARCHAR(10) NOT NULL,
    `alarm_tf` BOOL NOT NULL,
    `fcm_token` VARCHAR(255),
    `is_terms_agreed` BOOL NOT NULL DEFAULT 0,
    `is_privacy_agreed` BOOL NOT NULL DEFAULT 0,
    `is_marketing_agreed` BOOL NOT NULL DEFAULT 0,
    `is_alarm_agreed` BOOL NOT NULL DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='서비스의 사용자 계정 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `uploads` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `file_path` VARCHAR(512) NOT NULL,
    `original_name` VARCHAR(255),
    `file_type` VARCHAR(20) NOT NULL,
    `category` VARCHAR(50),
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_uploads_users_5a3e4278` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 업로드한 원본 파일 정보(처방전, 약품 사진 등)를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `pill_recognitions` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `model_version` VARCHAR(50),
    `pill_name` VARCHAR(255) NOT NULL,
    `pill_description` LONGTEXT,
    `confidence` DOUBLE NOT NULL,
    `raw_result` JSON,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    `back_upload_id` INT UNIQUE,
    `front_upload_id` INT NOT NULL UNIQUE,
    CONSTRAINT `fk_pill_rec_users_2e103417` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_pill_rec_uploads_796ec903` FOREIGN KEY (`back_upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_pill_rec_uploads_461a6fb8` FOREIGN KEY (`front_upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='AI 모델을 통한 알약 외형 이미지 분석 이력을 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `current_meds` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `medication_name` VARCHAR(255) NOT NULL,
    `one_dose` VARCHAR(255),
    `daily_dose_count` VARCHAR(255),
    `one_dose_count` VARCHAR(255),
    `dose_time` VARCHAR(4) NOT NULL COMMENT '복용 시간',
    `added_from` VARCHAR(5) NOT NULL COMMENT '출처',
    `start_date` VARCHAR(255),
    `user_id` VARCHAR(100) NOT NULL,
    `pill_recognition_id` INT UNIQUE,
    CONSTRAINT `fk_current__users_425eb8b1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_current__pill_rec_9a5f78e7` FOREIGN KEY (`pill_recognition_id`) REFERENCES `pill_recognitions` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 현재 실제로 복용 중인 약물 목록을 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `alarms` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `alarm_type` VARCHAR(20) NOT NULL DEFAULT 'MED',
    `alarm_time` TIME(6) NOT NULL,
    `is_active` BOOL NOT NULL DEFAULT 1,
    `repeat_days` VARCHAR(32),
    `current_med_id` INT,
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_alarms_current__65ab2c31` FOREIGN KEY (`current_med_id`) REFERENCES `current_meds` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_alarms_users_00f32162` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 설정한 알람 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `alarm_history` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `sent_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `delivered_at` DATETIME(6),
    `read_at` DATETIME(6),
    `is_confirmed` BOOL NOT NULL DEFAULT 0,
    `snoozed_until` DATETIME(6),
    `snooze_count` INT NOT NULL DEFAULT 0,
    `alarm_id` INT NOT NULL,
    CONSTRAINT `fk_alarm_hi_alarms_9f73e320` FOREIGN KEY (`alarm_id`) REFERENCES `alarms` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='알람 발송 내역과 사용자의 확인 여부를 기록하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `allergies` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `allergy_type` VARCHAR(100),
    `allergy_name` VARCHAR(100),
    `symptom` VARCHAR(100),
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_allergie_users_cc13c577` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 보유한 알러지 성분 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `llm_life_guides` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_current_status` LONGTEXT NOT NULL,
    `generated_content` JSON NOT NULL,
    `activity` BOOL NOT NULL DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_llm_life_users_9bda261a` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='AI가 생성한 환자 맞춤형 복약 및 생활 가이드 전문을 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `chat_messages` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `session_id` VARCHAR(100) NOT NULL,
    `role` VARCHAR(20) NOT NULL,
    `message` LONGTEXT NOT NULL,
    `is_deleted` BOOL NOT NULL DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `reference_guide_id` INT,
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_chat_mes_llm_life_f5df1902` FOREIGN KEY (`reference_guide_id`) REFERENCES `llm_life_guides` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_chat_mes_users_91f55345` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자와 챗봇 간의 대화 메시지 이력을 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `chronic_diseases` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `disease_name` VARCHAR(100) NOT NULL,
    `when_to_diagnose` VARCHAR(10) NOT NULL,
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_chronic__users_a03285c9` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 앓고 있는 기저 질환(고혈압, 당뇨 등) 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `multimodal_assets` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `source_table` VARCHAR(50) NOT NULL,
    `source_id` INT NOT NULL,
    `asset_type` VARCHAR(20) NOT NULL,
    `asset_url` VARCHAR(512) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='텍스트 기반 가이드를 바탕으로 생성된 시각/청각 에셋 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `ocr_history` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `raw_text` LONGTEXT NOT NULL,
    `is_valid` BOOL NOT NULL DEFAULT 0,
    `inference_metadata` JSON,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    `back_upload_id` INT UNIQUE,
    `front_upload_id` INT NOT NULL UNIQUE,
    CONSTRAINT `fk_ocr_hist_users_de674177` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_ocr_hist_uploads_1cf26d91` FOREIGN KEY (`back_upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_ocr_hist_uploads_2ee6bf89` FOREIGN KEY (`front_upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='이미지 내 텍스트 추출(OCR) 엔진의 분석 원본 이력을 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `prescriptions` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `hospital_name` VARCHAR(255),
    `prescribed_date` DATE,
    `drug_list_raw` LONGTEXT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    `upload_id` INT NOT NULL UNIQUE,
    `ocr_history_id` INT UNIQUE,
    CONSTRAINT `fk_prescrip_users_75d98828` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_prescrip_uploads_02e6e99e` FOREIGN KEY (`upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_prescrip_ocr_hist_0b5733ff` FOREIGN KEY (`ocr_history_id`) REFERENCES `ocr_history` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자가 업로드한 처방전의 분석 결과를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `prescription_drugs` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `standard_drug_name` VARCHAR(255) NOT NULL,
    `dosage_amount` DOUBLE,
    `daily_frequency` INT,
    `duration_days` INT,
    `is_linked_to_meds` BOOL NOT NULL DEFAULT 0,
    `current_med_id` INT,
    `prescription_id` INT NOT NULL,
    CONSTRAINT `fk_prescrip_current__39f1e88e` FOREIGN KEY (`current_med_id`) REFERENCES `current_meds` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_prescrip_prescrip_c35d9dcd` FOREIGN KEY (`prescription_id`) REFERENCES `prescriptions` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='처방전에 포함된 개별 약품 상세 정보를 관리하는 모델입니다.';
        CREATE TABLE IF NOT EXISTS `system_logs` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `api_path` VARCHAR(255) NOT NULL,
    `method` VARCHAR(10) NOT NULL,
    `response_ms` INT NOT NULL,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='서비스 API의 성능 및 에러 여부를 모니터링하기 위한 로그 모델입니다.';
        CREATE TABLE IF NOT EXISTS `blood_pressure_records` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `systolic` INT NOT NULL COMMENT '수축기(mmHg)',
    `diastolic` INT NOT NULL COMMENT '이완기(mmHg)',
    `measure_type` VARCHAR(2) NOT NULL COMMENT '측정 상황',
    `created_at` DATETIME(6) NOT NULL COMMENT '서버 저장 시각' DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL COMMENT '사용자',
    CONSTRAINT `fk_blood_pr_users_67a78557` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='혈압 기록(수축기/이완기)';
        CREATE TABLE IF NOT EXISTS `blood_sugar_records` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `glucose_mg_dl` DOUBLE NOT NULL COMMENT '혈당(mg/dL)',
    `measure_type` VARCHAR(6) NOT NULL COMMENT '측정 상황(공복/식후 2시간/취침전/임의)',
    `created_at` DATETIME(6) NOT NULL COMMENT '서버 저장 시각' DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL COMMENT '사용자',
    CONSTRAINT `fk_blood_su_users_6db13992` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='혈당 기록(mg/dL + 측정상황)';
        CREATE TABLE IF NOT EXISTS `health_profiles` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `family_history` VARCHAR(5) NOT NULL COMMENT '가족력',
    `family_history_note` LONGTEXT COMMENT '사용자 입력 텍스트',
    `height_cm` DOUBLE NOT NULL COMMENT '신장(cm)',
    `weight_kg` DOUBLE NOT NULL COMMENT '체중(kg)',
    `weight_change` VARCHAR(4) NOT NULL COMMENT '최근 체중 변화',
    `sleep_hours` DOUBLE COMMENT '수면 시간(시간)',
    `sleep_change` VARCHAR(4) NOT NULL COMMENT '최근 수면 변화',
    `smoking_status` VARCHAR(5) NOT NULL COMMENT '흡연 상태',
    `smoking_years` INT COMMENT '흡연 기간(년)',
    `smoking_per_week` DOUBLE COMMENT '주 평균 흡연량(팀 기준 단위 통일)',
    `drinking_status` VARCHAR(5) NOT NULL COMMENT '음주 상태',
    `drinking_years` INT COMMENT '음주 기간(년)',
    `drinking_per_week` DOUBLE COMMENT '주 평균 음주량(팀 기준 단위 통일)',
    `exercise_frequency` VARCHAR(7) NOT NULL COMMENT '운동 빈도',
    `diet_type` VARCHAR(5) NOT NULL COMMENT '식습관 유형',
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL UNIQUE COMMENT '사용자',
    CONSTRAINT `fk_health_p_users_35ba10a2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='사용자 건강 프로필(정적/준정적 정보)';
        CREATE TABLE IF NOT EXISTS `plan_check_list` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `content` VARCHAR(255) NOT NULL,
    `plan_type` VARCHAR(20) NOT NULL DEFAULT 'self',
    `is_completed` BOOL NOT NULL DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(100) NOT NULL,
    CONSTRAINT `fk_plan_che_users_e7d8e98d` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='오늘 계획 체크 리스트';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `blood_sugar_records`;
        DROP TABLE IF EXISTS `health_profiles`;
        DROP TABLE IF EXISTS `current_meds`;
        DROP TABLE IF EXISTS `llm_life_guides`;
        DROP TABLE IF EXISTS `prescriptions`;
        DROP TABLE IF EXISTS `pill_recognitions`;
        DROP TABLE IF EXISTS `alarms`;
        DROP TABLE IF EXISTS `multimodal_assets`;
        DROP TABLE IF EXISTS `prescription_drugs`;
        DROP TABLE IF EXISTS `blood_pressure_records`;
        DROP TABLE IF EXISTS `chat_messages`;
        DROP TABLE IF EXISTS `uploads`;
        DROP TABLE IF EXISTS `users`;
        DROP TABLE IF EXISTS `chronic_diseases`;
        DROP TABLE IF EXISTS `alarm_history`;
        DROP TABLE IF EXISTS `system_logs`;
        DROP TABLE IF EXISTS `ocr_history`;
        DROP TABLE IF EXISTS `plan_check_list`;
        DROP TABLE IF EXISTS `allergies`;"""


MODELS_STATE = (
    "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"
    "9JTYrmZR2VZ3/uv/ATXk2iI="
)
