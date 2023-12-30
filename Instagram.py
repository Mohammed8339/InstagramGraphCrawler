import json
import os

from instagrapi import Client
from PIL import Image


def convert_png_to_jpg(png_path, jpg_path):
    try:
        # Open the PNG image
        png_image = Image.open(png_path)

        # Convert and save as JPG
        if png_image.mode != 'RGB':
            png_image = png_image.convert('RGB')
        png_image.save(jpg_path, format='JPEG', quality=95)

        print("Conversion successful!")
    except Exception as e:
        print(f"Error converting the image: {e}")


# Replaces 'input.png' and 'output.jpg' with the actual file paths
input_png_file = 'graph.png'
output_jpg_file = 'refinedGraph.jpg'

convert_png_to_jpg(input_png_file, output_jpg_file)

with open('credentials.json', 'r') as file:
    loginInfo = json.load(file)

if loginInfo['username'] == "":
    print("no username added to credentials.json")
    print("add your username and try again")
    os.system('pause')
    exit()

elif loginInfo['password'] == "":
    print("no password added to credentials.json")
    print("add your password and try again")
    os.system('pause')
    exit()

username = loginInfo['username']
password = loginInfo['password']

client = Client()
print("logging in")
client.login(username, password)

image_path = 'graph.png'
caption = ''

with open('caption.txt', 'r') as file:
    caption = str(file.readline())

print("this is the title of the post, are you sure you want to proceed with the photo? (y or yes)")
print(caption)
choice = str(input())

if str(choice.lower()) == "y" or str(choice.lower()) == "yes":
    print("uploading")
    client.photo_upload('refinedGraph.jpg', caption)
    print('uploaded!')
    exit()
else:
    print('aborted')
    exit()

