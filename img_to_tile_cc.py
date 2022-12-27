
import requests
from PIL import Image
from split_image import split_image
import os


#   1st step : download the image and put it in /input as img.jpg
    # i'm using random duck api
parameters = {
    "type": "jpg"
}
response = requests.get("https://random-d.uk/api/v2/randomimg", params=parameters)
open("input/img.jpg", "wb").write(response.content)


#  2nd step : resize img to 1000x1000 stretched 
image = Image.open("input/img.jpg")
resized = image.resize((1000, 1000))
resized.save('input/resized.jpg')

#  3rd step : generate tiles
split_image("input/resized.jpg", 2, 2, False, False, False, "output/")

#   4th step : convert each tiles into ntf 
#os.system("py convert_nfp.py output/resized_0.jpg")
directory = 'output'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if f.endswith(".jpg"):
        print(f)
        os.system("py convert_nfp.py "+f)

print()
