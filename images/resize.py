from PIL import Image
 
#读取图像
im = Image.open("favicon1.jpg")
# im = im.crop((0,200,1920,1200))
im = im.resize((32, 32))
im.save("favicon.jpg")
im.show()
 
#原图像缩放为128x128
