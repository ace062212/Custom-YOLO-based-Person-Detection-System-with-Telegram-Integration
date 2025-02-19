# 🎥 Real-time Person Detection System
# 🎥 Real-time Person Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Custom-red?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7.0-green?style=for-the-badge&logo=opencv&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-90%25+-success?style=for-the-badge)
![FPS](https://img.shields.io/badge/FPS-30+-orange?style=for-the-badge)

[![GitHub last commit](https://img.shields.io/github/last-commit/ace062212/person-detection-system?style=for-the-badge)](https://github.com/ace062212/person-detection-system)
![Development Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <img src="demo/images/demo.gif" alt="Demo" width="600"/>
</p>

## 📌 프로젝트 소개
YOLO와 텔레그램을 활용한 실시간 사람 감지 및 알림 시스템입니다. Roboflow를 통해 직접 데이터셋을 라벨링하고 학습시킨 커스텀 모델을 사용하여, 높은 정확도의 사람 감지 시스템을 구현했습니다.

### 개발 기간
- 2023 .11 ~ 2023.12

  
## 🔍 모델 학습 과정
### 1. 데이터 준비
- Roboflow 플랫폼 활용
- 직접 데이터셋 라벨링 수행
- 다양한 환경의 이미지 수집
#### 데이터셋 정보
- 총 이미지 수: 1,000장+
- 학습/검증/테스트 비율: 70:20:10
- 데이터 증강 기법: 회전, 밝기 조정, 좌우 반전


### 2. 모델 학습
- YOLOv8 아키텍처 기반
- 커스텀 데이터셋으로 전이학습
- 하이퍼파라미터 최적화

### 3. 성능 개선
- 데이터 증강 기법 적용
- 모델 파라미터 튜닝
- 다양한 환경에서의 테스트

## 🌟 주요 기능
- **커스텀 YOLO 모델**: 직접 라벨링한 데이터로 학습된 고성능 모델
- **실시간 사람 감지**: 커스텀 YOLOv8 모델 기반 객체 감지
- **텔레그램 알림**: 사람 감지 시 즉시 알림 발송
- **다양한 입력 지원**: 웹캠 및 비디오 파일 지원
- **높은 정확도**: 0.9 신뢰도 임계값으로 오탐지 최소화

## 🚀 시작하기

### 필수 요구사항
- Python 3.8+
- OpenCV
- YOLOv8
- 텔레그램 봇 토큰

### 설치 방법
bash

### 저장소 클론
git clone https://github.com/yourusername/Person-Detection-System.git

### 필요한 패키지 설치
pip install -r requirements.txt


### 환경 설정
1. **모델 준비**
   ```python
   # YOLOv8n 모델 사용
   model = YOLO('yolov8n.pt')
   ```

2. **텔레그램 봇 설정**
   - 환경 변수에 봇 토큰 설정
   - `config.py` 파일에서 설정 관리

## 💻 사용 방법

### 실시간 감지
bash
python src/realtime_detection.py

### 비디오 파일 분석
bash
python src/video_detection.py --video_path path/to/video.mp4


## 📊 프로젝트 자료
- [시연 영상](https://drive.google.com/file/d/1aNebAHnF75TrN_dFxguPnt89O7jHPqrN/view?usp=sharing)
- [발표 자료](https://drive.google.com/file/d/1QrfBET8VES3crSho8U7a9lS_zOIV352e/view?usp=sharing)
- [데모 노트북](notebooks/person_detection_demo.ipynb)

## 🛠️ 기술 스택
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

### 사용된 기술
- **YOLOv8**: 객체 감지 모델
- **Roboflow**: 데이터셋 라벨링 및 관리
- **OpenCV**: 이미지 처리 및 비디오 스트림 처리
- **Python Telegram Bot**: 실시간 알림 시스템
- **NumPy**: 데이터 처리
- **Matplotlib**: 시각화

## 📈 성능
- 실시간 처리 속도: 30+ FPS
- 감지 정확도: 90% 이상
- 알림 지연: 5초 이내

### 모델 성능
- **mAP (Mean Average Precision)**: 0.85
- **Recall**: 0.88
- **Precision**: 0.92

## 🔜 향후 계획
- [ ] 다중 객체 추적 기능 추가
- [ ] 웹 인터페이스 구현
- [ ] 야간 감지 성능 개선
- [ ] 알림 메시지 커스터마이징
- [ ] 실시간 모니터링 대시보드 구현

## 🎯 프로젝트 목표 및 성과
1. **커스텀 모델 개발**
   - Roboflow를 활용한 데이터셋 구축
   - YOLOv8 기반 전이학습 수행
   - 높은 정확도의 사람 감지 모델 구현

2. **실시간 처리**
   - 30+ FPS 실시간 처리 달성
   - 지연 없는 알림 시스템 구현

3. **실용성**
   - 간편한 설치 및 설정
   - 다양한 환경 지원
   - 안정적인 성능

## 👨‍💻 개발자 정보
- GitHub: [ace062212](https://github.com/ace062212)
- Email: ace062212@gmail.com

## 📜 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.
