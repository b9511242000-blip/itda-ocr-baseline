# ITDA 3rd 학술제 - 소비기한 추출 베이스라인 📌

본 저장소는 ITDA 3rd 학술제 참가자를 위한 공식 규칙 기반(Rule-based) 베이스라인 코드를 제공합니다.

---

## 📋 대회 개요 및 과제 정의

* **주제**: OCR 기반 상품 소비기한 정보 추출 아키텍처 설계 및 도메인 활용 기획
* **주최**: 수도권 데이터사이언스 연합학회 ITDA (경희대 CODE, 서강대 INSIGHT, 성균관대 DScover, 인하대 IBAS, 한국외대 DAT)
* **입력 (Input)**: 소비기한, 제조일자, 바코드, 영양성분 등이 얽혀 있는 상품 뒷면 이미지 1장
* **출력 (Output)**: 정규화된 소비기한 날짜 문자열 (`YYYY-MM-DD` 형식, 미인식 시 `"NONE"`)
* **핵심 난이도**: 수많은 숫자(제조일, 품목보고번호, 고객센터 번호 등) 중 위치, 앵커 키워드('까지', '유통기한'), 문맥을 통해 진짜 소비기한을 판별하는 해석 로직 구축

---

## 📁 파일 구성

* `ITDA_베이스라인_FINAL_3.ipynb`: 전처리, 방향성 앵커 스코어링, 디버깅 툴이 포함된 통합 노트북
* `predict.py`: 평가 데이터 추론 및 제출 파일 생성 스크립트
* `requirements.txt`: 대회 실행 환경 패키지 목록

---

## 🚀 시작하기

1. 본 저장소를 Fork 또는 Clone 합니다.
2. `ITDA_베이스라인.ipynb` 내 `IMAGE_DIR` 경로를 본인의 데이터셋 경로에 맞게 수정합니다.
3. 시각화 및 디버깅 툴을 활용해 모델 및 알고리즘을 고도화하세요.

### 💡 실행 환경 주의사항 (NumPy 버전 이슈)
* 로컬 아나콘다 환경 실행 중 `ImportError: numpy.core.multiarray...` 관련 오류가 발생하는 경우, 터미널에서 버전을 조절해 주세요.
  ```bash
  pip install "numpy<2"
✉️ 제출 규칙
1차 예선 제출 시 참가자 본인의 GitHub 저장소에 predict.py, requirements.txt, 모델 가중치 파일(필요 시), README.md를 포함하여 URL을 이메일로 제출해야 합니다.

제출 양식 예시 (submission.csv / submission.json):

JSON
[
  {"image_id": "val_0001.jpg", "predicted_date": "2026-05-29"},
  {"image_id": "val_0002.jpg", "predicted_date": "NONE"}
]

---
* **Troubleshooting 섹션**: 참가자들이 NumPy 2.x 환경 오류로 문의하는 것을 사전 방지하기 위한 안내를 추가했습니다.
* **제출 양식 구체화**: 예선 제출용 JSON 규격을 직관적으로 명시했습니다.
