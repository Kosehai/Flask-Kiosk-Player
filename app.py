from flask import Flask, render_template, send_from_directory
import os
from tinytag import TinyTag
import werkzeug
from threading import Timer

app = Flask(__name__)

media_path = os.path.join(os.getcwd(), "media")

@app.route('/')
def teknologiparken():
    media = []
    files = os.listdir(media_path)
    if not os.path.exists(media_path):
        os.makedirs(media_path)
    if not os.path.exists(os.path.join(media_path, "thumb")):
                os.makedirs(os.path.join(media_path, "thumb"))
    outstr = ""
    for f in files:
        if ".mp4" in f and ".jpg" not in f:
            fp = os.path.join(media_path, f)
            tp = os.path.join(media_path, "thumb", f + ".jpg")
            if not os.path.isfile(tp):
                generate_thumbnail(fp, tp)
            video = {
                "filename": f,
                "thumbnail": f + ".jpg",
                "title": get_title(fp)
            }
            media.append(video)
            outstr += f + "\n"
    return render_template('index.html', media=media)

@app.route('/playvideo/<path:filepath>')
def play(filepath):
    return render_template('player.html', video_path = filepath, type = str)

@app.route('/video/<path:filepath>')
def getvideo(filepath):
    return send_from_directory('media', filepath)


def generate_thumbnail(fp, tp):
    os.system(f"ffmpeg -i {fp} -ss 00:00:01.000 -vframes 1 {tp}")
    

def get_title(path: str) -> str:
    return TinyTag.get(path).title

def open_kiosk():
    os.system("\"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe\" --kiosk http://localhost:5000 --edge-kiosk-type=fullscreen")

if __name__ == "__main__":
    Timer(1, open_kiosk).start()
    app.run()
    #Starter nettleser