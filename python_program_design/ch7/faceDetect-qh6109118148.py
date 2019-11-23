import tkinter
from tkinter import messagebox, filedialog

try:
    import cv2
except:
    tkinter.messagebox.showinfo('错误提示', '你当前的Python环境没有安装OpenCV库')
    exit(0)


def face_recognition(picture, pack_path):
    facesCascade = cv2.CascadeClassifier(
        pack_path + r'\haarcascade_frontalface_default.xml')  # 识别脸
    eyeCascade = cv2.CascadeClassifier(pack_path + r'\haarcascade_eye.xml')  # 识别眼
    smileCascade = cv2.CascadeClassifier(pack_path + r'\haarcascade_smile.xml')  # 识别笑脸
    # BGR色彩体系
    color_face = (0, 255, 0)  # 识别出的人脸的边框格式_绿
    color_eye = (255, 0, 0)  # 识别出的眼的边框格式_蓝
    color_smile = (0, 0, 255)  # 识别出的笑脸的边框格式_红
    faceRects = facesCascade.detectMultiScale(picture, scaleFactor=1.2, minNeighbors=5)
    if len(faceRects) > 0:  # 框出每一张人脸
        for faceRect in faceRects:
            a, b, c, d = faceRect
            #   x  y  w  h
            cv2.rectangle(picture, (a, b), (a + c, b + d), color_face, 2)  # 框出一张脸
            in_face = picture[a:a + c, b:b + d]  # 截取识别到的人脸区域部分
            eyeRects = eyeCascade.detectMultiScale(in_face, scaleFactor=1.1, minNeighbors=5,minSize=(5,5))
            smileRects = smileCascade.detectMultiScale(in_face, scaleFactor=1.1, minNeighbors=5,minSize=(32,32))
            if len(eyeRects) > 0:  # 框出脸中的所有眼睛
                for eyeRect in eyeRects:
                    x, y, w, h = eyeRect
                    cv2.rectangle(in_face, (x, y), (x + w, y + h), color_eye, 2)
            if len(smileRects) > 0:  # 框出脸中的所有笑脸
                for smileRect in smileRects:
                    x, y, w, h = smileRect
                    cv2.rectangle(in_face, (x, y), (x + w, y + h), color_smile, 2)
                    cv2.putText(picture, 'Smile', (a, b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)  # 显示smile
    return picture


def CatchFace_Camera(Window_name, Camera_id, pack_path):
    cv2.namedWindow(Window_name)
    cap = cv2.VideoCapture(Camera_id)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = face_recognition(frame, pack_path)
        cv2.imshow(Window_name, frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def CatchFace_pic(Window_name, pic_url, pack_path):
    cv2.namedWindow(Window_name)  # 创建窗口
    pic = cv2.imread(pic_url, 1)
    pic = face_recognition(pic, pack_path)
    cv2.imshow(Window_name, pic)
    cv2.waitKey(0)


###########################################################################
def set():
    global pack_path
    pack_path = pack_path_input.get()
    start.pack_forget()
    menu.pack()


def pic(event):
    global pack_path
    choice_pic = filedialog.askopenfile(title='选一张图片', defaultextension='.jpg')
    CatchFace_pic('face_recognition', choice_pic.name, pack_path)


def camera(event):
    global pack_path
    CatchFace_Camera('face_recognition', 0, pack_path)


if __name__ == '__main__':
    pack_path = r''
    ###########################################################
    root = tkinter.Tk()
    root.title('简易人脸识别')
    root.geometry('1920x1080+0+0')
    root.propagate(0)
    start = tkinter.Frame(root, width=1920, height=1080)
    start.propagate(0)
    tip1 = tkinter.Label(start, font=('微软雅黑', 24), text='使用前需要正确配置opencv的级联分类器的路径').pack()
    tip1 = tkinter.Label(start, font=('微软雅黑', 24), text=r'示例：你需要输入这样的地址:''\n'
                                                        r'D:\Enviroment\venv\Lib\site-packages\cv2\data').pack()
    pack_path_input = tkinter.StringVar()  # 获取级联分类器的配置路径
    pack_path_input.set(r'D:\Enviroment\venv\Lib\site-packages\cv2\data')
    pack_path_get = tkinter.Entry(start, width=48, font=('consolas', 18), textvariable=pack_path_input).pack()
    start_button = tkinter.Button(start, font=('微软雅黑', 24), text='开始使用', command=set).pack()
    start.pack()
    ###########################################################
    menu = tkinter.Frame(root, width=1920, height=1080, bg='green')
    menu.propagate(0)
    Use_pic = tkinter.Label(menu, bg='blue', font=('微软雅黑', 18), text='选择\n一张\n照片\n(目录不要含有中文)', width=25, height=15)
    Use_pic.propagate(0)
    Use_camera = tkinter.Label(menu, bg='blue', font=('微软雅黑', 18), text='启动\n你的\n摄像头\n(输入q结束)', width=25, height=15)
    Use_camera.propagate(0)
    Use_pic.bind('<Button -1>', pic)
    Use_pic.place(x=190, y=170)
    Use_camera.bind('<Button -1>', camera)
    Use_camera.place(x=850, y=170)
    root.mainloop()