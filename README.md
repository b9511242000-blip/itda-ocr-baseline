# ITDA 3rd 학술제 - 소비기한 추출 제출 템플릿 📌

본 저장소는 **제3회 ITDA 연합학술제** 참가자를 위한 공식 제출 템플릿 및 환경 검증용 저장소입니다.

---

## 1. 대회 개요 및 과제 정의

* **주제**: OCR 기반 상품 소비기한 정보 추출 아키텍처 설계 및 도메인 활용 기획
* **주최**: 수도권 데이터사이언스 연합학회 ITDA (경희대 CODE, 서강대 INSIGHT, 성균관대 DScover, 인하대 IBAS, 한국외대 DAT)
* **입력 (Input)**: 상품 뒷면 이미지 (`ITDA_INPUT_DIR` 환경변수로 경로 주입)
* **출력 (Output)**: `submission.csv` (`ITDA_OUTPUT_PATH` 환경변수 경로에 저장)

### submission.csv 표준 스키마
| image_id | year | month | day | final_date |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 2026 | 05 | 29 | 2026-05-29 |
| 2 | NONE | NONE | NONE | NONE |

* `image_id`: 확장자를 제외한 이미지 파일명 (예: 1)
* `year`: 4자리 연도 문자열 (예: 2026, 미인식 시 NONE)
* `month`: 2자리 월 문자열 (예: 05, 미인식 시 NONE)
* `day`: 2자리 일 문자열 (예: 29, 미인식 시 NONE)
* `final_date`: 하이픈(-)으로 연결된 정규화 날짜 (예: 2026-05-29, 미인식 시 NONE)

---

## 2. 파일 및 저장소 구조

```text
itda3-[학회영문]-[영문팀명]/
├── predict.ipynb              # 메인 추론 노트북 (운영진 채점용 필수)
├── requirements.txt           # 실행 환경 패키지 목록 (필수)
├── README.md                  # 가중치 다운로드 및 실행 가이드 (필수)
├── download_weights.sh        # [선택] 외부 가중치 다운로드 스크립트
├── notebooks/                 # [선택] 실험·분석 노트북 (채점 대상 아님)
└── weights/                   # [선택] 모델 가중치 저장 폴더
```

---

## 3. 시작하기 및 실행 방법

### 1) 가상환경 구축 및 패키지 설치
```bash
git clone <본인 팀 저장소 URL>
cd <저장소 디렉토리>
pip install -r requirements.txt
```

### 2) 가중치 파일 설정
용량이 큰 모델 가중치 파일(`.pt`, `.pth`, `.safetensors` 등)은 Git에 직접 푸시하지 마시고, Google Drive, HuggingFace 링크 또는 Release Assets를 통해 `download_weights.sh` 스크립트 등으로 내려받도록 설정하세요.

### 3) 채점 재현성 검증 (운영진 채점 표준 명령어)
운영진은 Standard 4-Core vCPU 환경에서 아래 명령어를 실행하여 순차 실행(Run All) 및 채점을 진행합니다.

```bash
export ITDA_INPUT_DIR=./val_images
export ITDA_OUTPUT_PATH=./submission.csv

jupyter nbconvert --to notebook --execute predict.ipynb \
    --ExecutePreprocessor.timeout=2400 \
    --output /tmp/executed.ipynb
```

---

## 4. 제출 전 필수 체크리스트

1. **CONFIG 셀 수정 금지**: `predict.ipynb` 최상단의 환경변수 주입 코드는 절대 변경하거나 값을 직접 하드코딩 대입하지 마세요.
2. **대화형 코드 제거**: 실행 중 사용자 입력을 대기하는 코드(`input()`, `getpass()` 등)가 있으면 타임아웃(0점) 처리됩니다.
3. **인덱스 제외 저장**: CSV 저장 시 반드시 인덱스를 제외해야 합니다. (`df.to_csv(OUTPUT_PATH, index=False)`)
4. **결과 스키마 준수**: 누락된 컬럼이 없도록 `image_id, year, month, day, final_date` 5개 컬럼 스키마를 엄격히 지켜주세요.
