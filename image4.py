import pytesseract
from PIL import Image


def get_code():
    code = ''
    for i in range(1, 5):
        image_dir = 'D:/picture/'
        # image = Image.open('verify_del_crop' + str(i) + '.jpg')  # type:Image.Image
        image = Image.open(image_dir + 'crop/' + str(i)+'_0' + '.jpg')
        code += pytesseract.image_to_string(image,
                                            config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(code)
    return code
