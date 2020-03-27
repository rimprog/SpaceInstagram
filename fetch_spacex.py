import argparse
import requests

from main import IMAGES_PATH
from main import get_image
from main import save_image


def get_spacex_images_links(url):
    response = requests.get(url)
    response.raise_for_status()

    spacex_images_links = response.json()['links']['flickr_images']

    return spacex_images_links

def fetch_spacex_images(url,
                        get_spacex_image_links,
                        images_path,
                        get_image,
                        save_image):
    spacex_images_links = get_spacex_images_links(url)

    for image_number, image_link in enumerate(spacex_images_links):
        url = image_link
        image = get_image(url)

        filename = 'spacex{}.jpg'.format(image_number)
        save_image(image, filename, images_path)

def main():
    parser = argparse.ArgumentParser(
        description='This script downloads images from launching spacex.'
    )
    parser.add_argument('--url', help='Spacex_api_launch_url. Default: https://api.spacexdata.com/v3/launches/latest')
    args = parser.parse_args()

    url = args.url if args.url else 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_images(url,
                        get_spacex_images_links,
                        IMAGES_PATH,
                        get_image,
                        save_image)

if __name__ == '__main__':
    main()
