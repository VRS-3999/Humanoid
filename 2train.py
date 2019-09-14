import json
import base64
import PIL
import io
from io import BytesIO
#from BytesIO import BytesIO
from io import StringIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
import base64
import text_to_image
import numpy as np
#from array import array

data = requests.get("http://localhost:3000/ImageData").json()
print(data)
#with open('E:\Humanoid\FacialRecognizationProject\db.json', 'rb') as datas:
    #data = json.load(datas)
    #Image.open(BytesIO(datas))
    #data.show()
    #data.save('E:\\Humanoid\FacialRecognizationProject\ImageData\1.jpeg')
#print(data)
image = list(list(data.values())[0])[0]
#image = str(image, "utf-8")
#image = list(data[1].values())[0]

#image = list(data[1].values())[0]
#encode_string = base64.b64encode(image.read())
#f=open("E:/Humanoid/FacialRecognizationProject/ImageData/test.jpeg", 'wb')
#f.write(encode_string)
#f.close()

#imagedata = base64.b64decode(image)
#with open("E:\Humanoid\FacialRecognizationProject\ImageData", 'wb') as f:
#    f.write(imagedata)
#bytes = bytearray(image.read())
#im = Image.open(BytesIO(bytes))
#im.save("E:\Humanoid\FacialRecognizationProject\ImageData")

#img = Image.frombuffer('RGB', (320,420), image)
#draw = ImageDraw.Draw(img)
#font = ImageFont.truetype("arial.ttf",14)
#draw.text((0,220),"this is test",(255,255,0),font=font)
#draw = ImageDraw.Draw(img)
#img.save("test.jpg")

#image = Image.open(io.BytesIO(image1))
#image.save("test.jpg")
#image.show()

#encoded_image_path = text_to_image.encode(image,"image")

#image = Image.frombytes('RGBA',(128,128),image, 'raw')

#image = Image.open(io.BytesIO(image))
#image.show()

#img = Image.open(StringIO().StringIO(image))
img = Image.fromarray(image)
img.save("piraret.jpeg")
#img = Image.open(BytesIO(image))



