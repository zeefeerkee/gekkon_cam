from flask import Flask, render_template, Response, request
import cv2
from flask.json import jsonify


app = Flask(__name__)
camera = cv2.VideoCapture(0)


def getFramesGenerator():
    """Генератор фреймов для вывода в веб-страницу"""
    while True:
        success, frame = camera.read()  # Получаем фрейм с камеры
        if success:
            # уменьшаем разрешение кадров
            frame = cv2.resize(frame, (1080, 720), interpolation=cv2.INTER_AREA)

            _, buffer = cv2.imencode(".jpg", frame)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
            )



@app.route("/")
def index():
    return render_template("base.html")


@app.route("/video_feed")
def video_feed():
    """
    Генерируем и отправляем изображения с камеры
    """
    return Response(
        getFramesGenerator(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
