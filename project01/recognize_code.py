import pytesseract
from PIL import Image


def get_code():
    code = ''
    for i in range(4):
        image = Image.open('verify_image_1_del' + str(i) + '.jpg')  # type:Image.Image
        code += pytesseract.image_to_string(image,
                                            config='--psm 10 --oem 3 -c '
                                                   'tessedit_char_whitelist'
                                                   '=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(code)
    return code
