import time
import cv2 
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
   # cap=cv2.imread('frame.jpg')
    # Read until video is completed
    while(True):
      # Capture frame-by-frame
        #ret, img = cap.read()
        #if ret == True:
            cap=cv2.imread('frame.jpg')
            img = cv2.resize(cap, (0,0), fx=0.5, fy=0.5) 
         

            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
       # else: 
        #    break
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#if __name__ == '__main__':
def start():
    app.run(host='192.168.1.11', debug=False, threaded=True)