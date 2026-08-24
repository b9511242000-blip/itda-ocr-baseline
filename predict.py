# ITDA 3rd 학술제 - 메인 추론 스크립트 (predict.py)
import argparse
import os
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="ITDA OCR 소비기한 추출 추론 스크립트")
    parser.add_argument(
        "--image_dir", type=str, required=True, help="입력 이미지 폴더 경로"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="submission.csv",
        help="출력 결과 파일 경로 (.csv 또는 .json)",
    )
    args = parser.parse_args()

    print(f"이미지 경로: {args.image_dir} 에서 추론을 시작합니다...")

    # ============================================================
    # TODO: 참가자 본인의 모델 및 추론 파이프라인 로직 작성
    # ============================================================
    results = []

    # [예시 추론 루프]
    # image_files = [f for f in os.listdir(args.image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    # for img_name in image_files:
    #     img_path = os.path.join(args.image_dir, img_name)
    #
    #     # 모델 추론 수행 (YYYY-MM-DD 형식 또는 "NONE")
    #     pred_date = "2026-05-29"
    #
    #     results.append({
    #         "image_id": img_name,
    #         "predicted_date": pred_date
    #     })

    # ============================================================
    # 결과 저장 (표준 규격: image_id, predicted_date)
    # ============================================================
    df = pd.DataFrame(results, columns=["image_id", "predicted_date"])

    if args.output.endswith(".json"):
        df.to_json(args.output, orient="records", indent=2, force_ascii=False)
    else:
        df.to_csv(args.output, index=False, encoding="utf-8-sig")

    print(f"추론 완료! 결과가 {args.output} 에 성공적으로 저장되었습니다.")


if __name__ == "__main__":
    main()
