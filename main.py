import os
import requests
from pathlib import Path
from PIL import Image


def get_image(url):
    url = url
    response = requests.get(url, verify=False)
    response.raise_for_status()

    image = response.content

    return image

def save_image(image, filename, images_path):
    Path(images_path).mkdir(parents=True, exist_ok=True)

    image_path = images_path + filename
    with open(image_path, 'wb') as file:
        file.write(image)

def get_file_extension(filename):
    file_extension = filename.split('.')[-1]

    return file_extension

def resize_images(images_path, image_resolution):
    resized_images_folder_name = 'resized_images'
    resized_images_path = images_path + resized_images_folder_name + '/'
    Path(resized_images_path).mkdir(parents=True, exist_ok=True)

    images_names = os.listdir(images_path)
    images_names.remove(resized_images_folder_name)

    for image_name in images_names:
        image = Image.open(images_path + image_name)
        image.thumbnail(image_resolution)
        resized_image_name = 'resized_{}.jpg'.format(image_name.split('.')[0])

        rgb_im = image.convert('RGB')
        rgb_im.save(resized_images_path + resized_image_name , format="JPEG")

def main():
    images_path = "images/"

    image_resolution = (1080, 1080)
    resize_images(images_path, image_resolution)

if __name__ == '__main__':
    main()
