# !/usr/bin/python
# -*-coding:utf-8-*-
import time
from PIL import Image
import pytesseract  # ocr字符识别库
import cv2


###########二值化算法
def binarizing(img, threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


###########去除干扰线算法
def depoint(img):  # input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:
                count = count + 1
            if pixdata[x, y + 1] > 245:
                count = count + 1
            if pixdata[x - 1, y] > 245:
                count = count + 1
            if pixdata[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    return img


########身份证号码识别
def identity_OCR(pic_path):
    #####身份证号码截图
    img_origin = Image.open(pic_path)
    w, h = img_origin.size
    ##将身份证放大3倍
    img_resize = img_origin.resize((w * 3, h * 3), Image.Resampling.LANCZOS)
    Image._show(img_resize)
    cv2.waitKey(0)
    region = (150 * 2.5, 220 * 2.5, 370 * 3, 250 * 3)
    # 裁切身份证号码图片
    cropImg = img_resize.crop(region)
    # print(cropImg)
    # Image._show(cropImg)
    # cv2.waitKey(0)
    # 转化为灰度图
    img = cropImg.convert('L')
    Image._show(img)
    cv2.waitKey(0)
    # 把图片变成二值图像。
    img_binary = binarizing(img, 100)
    img_new = depoint(img_binary)
    code = pytesseract.image_to_string(img_new, lang='chi_sim')
    print("ID No. is: " + str(code))


'''
########身份证号码识别###################
##########英文图片识别####################   
'''


def identity_OCR_Nopro(pic_path):
    image = Image.open(pic_path)
    content = pytesseract.image_to_string(image)  # 解析图片
    print(content)


'''
#####################中文图片识别###############################
要在pytesseract 库的 image_to_string() 方法里加个参数lang='chi_sim'，
这个就是引用对应的中文语言包，中文语言包的全名是 chi_sim.traineddata
'''


def identity_OCR_Chine(pic_path):
    from PIL import Image
    import pytesseract
    image = Image.open(pic_path)
    content = pytesseract.image_to_string(image, lang='chi_sim')  # 解析图片
    print(content)


'''
##############功能：video recognition#############
'''


def identity_OCR_Video(pic_path):
    vid = cv2.VideoCapture(pic_path)
    while True:
        try:
            return_value, frame = vid.read()
            if return_value:
                cv2.imshow("result", frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # image = Image.fromarray(frame)
                # result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                code = pytesseract.image_to_string(frame, lang='chi_sim')
                print("识别该身份证号码是:" + str(code))
                cv2.waitKey(100)
            else:
                raise ValueError("No image!")
        except:
            print()


time1 = time.time()
if __name__ == '__main__':
    pic_path = r"image\1.jpg"
    identity_OCR(pic_path)
    # identity_OCR_Video(0)
    # identity_OCR_Chine(pic_path)
    # identity_OCR_Nopro(pic_path)

    time2 = time.time()
    print(u'Total duration：' + str(time2 - time1) + 's')
