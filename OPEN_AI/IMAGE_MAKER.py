from openai import OpenAI
import os
import urllib.request 
from PIL import Image

def main():
    os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'
    description = input("Enter: ")
    hd = input("HD? y/n: ")
    if hd == "y" or hd == "Y":
        image_quality = "hd"
    else:
        image_quality = "standard"
    client = OpenAI()
    completion = client.images.generate(
          #image=open("example.png", "rb"),
          model="dall-e-3",
          prompt=description,
          size="1024x1024",
          quality=image_quality,
          n=1,
    )
    image_url = completion.data[0].url
    #print(image_url)
    url = image_url
    urllib.request.urlretrieve(url, "image.png") 
    #img = Image.open(r"image.png")
    #img.show()

    


main()
