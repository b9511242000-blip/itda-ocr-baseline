# [참가자 작성용 예시] 주최측이 실행할 메인 추론 스크립트 파일입니다.
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', type=str, required=True, help='입력 이미지 폴더 경로')
    parser.add_argument('--output', type=str, default='submission.csv', help='출력 CSV 파일 경로')
    args = parser.parse_args()

    # TODO: 본인의 모델 및 추론 파이프라인 로직 작성
    print(f"이미지 경로: {args.image_dir} 에서 추론을 시작합니다...")

if __name__ == '__main__':
    main()
