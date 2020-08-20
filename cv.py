# -*- coding=GBK -*-
import cv2 as cv
from PIL import Image
import pytesseract


def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)  # ������Ϊ��ɫ
    cv.imshow("ת��", open_out)
    textImage = Image.fromarray(open_out)
    text = pytesseract.image_to_string(textImage)
    print("This OK:%s" % text)


src = cv.imread("p_1.jpg")
cv.imshow("ԭ��", src)
recognize_text()
cv.waitKey(0)
cv.destroyAllWindows()