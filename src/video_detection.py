import cv2
from ultralytics import YOLO
import requests
import time
from config import TELEGRAM_BOT_TOKEN, CHAT_ID, MODEL_CONFIDENCE

class VideoPersonDetector:
    def __init__(self, video_path):
        self.model = YOLO('best.pt')
        self.model.conf = MODEL_CONFIDENCE
        self.video_path = video_path
        self.last_message_time = 0

    def send_telegram_alert(self):
        current_time = time.time()
        if current_time - self.last_message_time >= 5:
            message = "비상상황! 사람 검출!!"
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            params = {
                "chat_id": CHAT_ID,
                "text": message,
                "notification": True
            }
            requests.get(url, params=params)
            self.last_message_time = current_time

    def run_detection(self):
        cap = cv2.VideoCapture(self.video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model(frame)
            res_plotted = results[0].plot()
            
            cv2.imshow('YOLOv8 Video Detection', res_plotted)

            if results[0].boxes:
                self.send_telegram_alert()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "path/to/your/video.mp4"
    detector = VideoPersonDetector(video_path)
    detector.run_detection()