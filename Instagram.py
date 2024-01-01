import json
import os

from instagrapi import Client
from PIL import Image

import logger

logger.Initialize(os.path.basename(__file__))
log = logger.log


def convert_png_to_jpg(png_path, jpg_path):

    log(f"running convert_png_to_jpg() arguments: {png_path} | {jpg_path}")

    try:
        # Open the PNG image
        png_image = Image.open(png_path)

        # Convert and save as JPG
        log("<convert_png_to_jpg()> converting image file to JPEG")
        if png_image.mode != 'RGB':
            png_image = png_image.convert('RGB')
        png_image.save(jpg_path, format='JPEG', quality=95)

        log("<convert_png_to_jpg()> conversion successful")
        print("Conversion successful!")

    except Exception as e:
        log(f"<convert_png_to_jpg()> ERROR failed converting the image | {e}")
        print(f"Error converting the image: {e}")
        os.system('pause')
        exit()


# Replaces 'input.png' and 'output.jpg' with the actual file paths
input_png_file = 'graph.png'
output_jpg_file = 'refinedGraph.jpg'

log("running convert_png_to_jpg()")
convert_png_to_jpg(input_png_file, output_jpg_file)

log('opening credentials.json | READ MODE')
with open('credentials.json', 'r') as file:
    loginInfo = json.load(file)
    log("loaded credentials")

if loginInfo['username'] == "":
    log("no username in credentials.json")
    print("no username in credentials.json")
    print("add your username and try again")
    exit()

elif loginInfo['password'] == "":
    log("no password in credentials.json")
    print("no password in credentials.json")
    print("add your password and try again")
    exit()

username = loginInfo['username']
password = loginInfo['password']

client = Client()
log("logging into account")
print("logging in")
client.login(username, password)
log("logged in")
print("logged in")

image_path = 'graph.png'

log("opening caption.txt")
with open('caption.txt', 'r') as file:
    caption = str(file.readline())

print("this is the title of the post, are you sure you want to proceed with the photo? (y or yes)")
print(caption)
log("taking users input (TITLE OF POST)")
choice = str(input())
log(f"user inputted {choice}")

if str(choice.lower()) == "y" or str(choice.lower()) == "yes":

    log("uploading image")
    print("uploading")
    # client.photo_upload('refinedGraph.jpg', caption)
    log("image successfully uploaded")
    print('uploaded!')
    exit()
else:
    log("aborted")
    print('aborted')
    exit()

