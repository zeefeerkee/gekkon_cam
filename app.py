from flask import Flask, render_template, Response, request
import cv2
from flask.json import jsonify


app = Flask(__name__)
camera = cv2.VideoCapture(0)

current_colormap = None

id_control = {
    "1": (lambda: set_colormap(None), "STANDART"),
    "2": (lambda: set_colormap(cv2.COLORMAP_COOL), "COOL"),
    "3": (lambda: set_colormap(cv2.COLORMAP_HOT), "HOT"),
    "4": (lambda: set_colormap(cv2.COLORMAP_RAINBOW), "RAINBOW"),
}


def set_colormap(colormap):
    global current_colormap
    current_colormap = colormap


def getFramesGenerator():
    """Генератор фреймов для вывода в веб-страницу"""
    while True:
        success, frame = camera.read()  # Получаем фрейм с камеры

        if success:
            # уменьшаем разрешение кадров
            # frame = cv2.resize(frame, (1080, 720), interpolation=cv2.INTER_AREA)

            if current_colormap:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.applyColorMap(gray_frame, current_colormap)

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


@app.route("/update_values", methods=["POST"])
def update_values():
    """
    Обработка обновления значений direction и progress
    """
    move_id = request.form["move"]
    id_control[move_id][0]()
    print(
        f"COLORMAP HAS BEEN CHANGED: {id_control[move_id][1]}",
    )
    return "200"
