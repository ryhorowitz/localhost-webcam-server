from flask import Flask, Response
import cv2

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)
# 0 represents the default camera (your MacBook Air's webcam)


def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )


@app.route("/")
def index():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
