---

## ⚠️ 채점 환경 필수 공지 (반드시 읽어주세요)

### 1) 팀 저장소 공개 범위
- 팀 저장소는 **Public** 으로 생성해 주세요.
- Private 으로 운영할 경우, 마감 전까지 운영진 계정 **`b9511242000-blip`** 을
  Collaborator 로 초대해야 합니다.
  (Settings → Collaborators → Add people)
- 마감 시각 기준 운영진이 접근할 수 없는 저장소는 채점 대상에서 제외됩니다.

### 2) 채점 서버는 오프라인입니다
채점은 **인터넷이 차단된 Standard 4-Core vCPU 환경**에서 진행됩니다.

- EasyOCR, PaddleOCR 등 상당수 라이브러리는 최초 실행 시 가중치를
  인터넷에서 **자동 다운로드** 합니다. 오프라인 환경에서는 이 단계가 실패해
  실행 오류(정량 0점)가 발생합니다.
- 모든 가중치는 **노트북 실행 전에 로컬에 존재**해야 합니다.
  - `download_weights.sh` 는 채점 실행 **전에** 운영진이 1회 실행합니다.
  - `predict.ipynb` 의 Run All **도중에** 다운로드하는 코드는 동작하지 않습니다.
- EasyOCR 사용 예시:
```python
  reader = easyocr.Reader(
      ['en'], gpu=False,
      model_storage_directory='./weights',
      download_enabled=False,   # 오프라인 강제
  )
```
- 이 설정으로 로컬에서 한 번 검증해 보시면 확실합니다.
  (네트워크를 끄고 Run All 이 끝까지 돌아가면 통과)

### 3) 환경 설치 시간은 속도 점수에 포함되지 않습니다
- `pip install -r requirements.txt` 및 `download_weights.sh` 소요 시간은
  속도 점수(10점) 산정에서 **제외** 됩니다.
- 속도 점수는 `predict.ipynb` 의 Run All 실행 시간(최대 2400초)만으로 산정합니다.

---
