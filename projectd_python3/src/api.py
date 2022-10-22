import os
import pafy
import cv2
from fastapi import FastAPI
import subprocess
from subprocess import PIPE
from time import sleep
import mysql.connector
from fastapi.responses import FileResponse

app = FastAPI()

# スタートボタン
@app.get("/detect/")
async def root(id: int = 0):
    conn = mysql.connector.connect(
    host='host.docker.internal',
    port='3306',
    user='user',
    password='password',
    database='laravel_project'
    )
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT cameras_url FROM cameras WHERE cameras_id = %s" % id)
    db_lis = cur.fetchall()
    sql = ("UPDATE cameras SET cameras_status = %s WHERE cameras_id = %s")
    param = ('Run', id)
    cur.execute(sql, param)
    conn.commit()
    cur.close()  
    subprocess.Popen('python ./Python/Yolov5_DeepSort_Pytorch_test/main.py --save-crop --source "%s" --camera_id %s --yolo_model ./Python/Yolov5_DeepSort_Pytorch_test/model_weight/best.pt' % (db_lis[0][0],int(id)),shell=True)

# ラベル付け設定
@app.get("/label/")
async def label(id: int = 0):
    conn = mysql.connector.connect(
        host='host.docker.internal',
        port='3306',
        user='user',
        password='password',
        database='laravel_project'
    )
    cur = conn.cursor(buffered=True)
    cur.execute("SELECT cameras_url FROM cameras WHERE cameras_id = %s" % id)
    db_lis = cur.fetchall()

    dir_path = './label_imgs'
    ext = 'jpg'

    if os.path.isfile('./label_imgs/%s.jpg' % id):
        os.remove('./label_imgs/%s.jpg' % id)

    video = pafy.new(db_lis[0][0])
    best = video.getbest(preftype="mp4")
    cap = cv2.VideoCapture(best.url)

    if not cap.isOpened():
        return
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, str(id))

    ret, frame = cap.read()
    cv2.imwrite('{}.{}'.format(base_path, ext), frame)

    return FileResponse('./label_imgs/%s.jpg' % id)

# 自転車の画像
@app.get("/bicycle/")
async def bicycle(camera_id: int = 0, bicycle_id: int = 0):
    return FileResponse('./bicycle_imgs/%s/%s.jpg' % (camera_id, bicycle_id))
