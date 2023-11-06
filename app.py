from flask import Flask, Response
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)
video_capture = cv2.VideoCapture(0)
# 0 represents the default camera (your MacBook Air's webcam)
streaming = False


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


@app.route("/start-streaming", methods=["GET"])
def start_streaming():
    global streaming
    streaming = True
    # Add code to start streaming from the webcam
    # Example: use OpenCV to capture frames from the webcam and send them to the frontend
    # return Response(
    #     generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    # )
    return "Streaming started", 200


@app.route("/stop-streaming")
def stop():
    global streaming
    streaming = False
    return Response(
        # stop generate_frames
        # return an ok response
        "Streaming ended",
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001, debug=True)
