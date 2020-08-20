from PIL import ImageFilter
from PIL import Image

imgF = Image.open("p_1.jpg")
conF = imgF.filter(ImageFilter.CONTOUR)             ##找轮廓
edgeF = imgF.filter(ImageFilter.FIND_EDGES)         ##边缘检测
# imgF.show()
conF.save('image_conF.jpg')
edgeF.save('image_edge.jpg')
# edgeF.show()