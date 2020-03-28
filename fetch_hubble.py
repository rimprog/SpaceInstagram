import argparse
import requests

from prepare_images import IMAGES_PATH
from prepare_images import get_image
from prepare_images import get_file_extension
from prepare_images import save_image


def get_hubble_image_links(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url)
    response.raise_for_status()

    hubble_image_links = response.json()['image_files']
    hubble_image_links = ['http:{}'.format(image_link['file_url']) for image_link in hubble_image_links]

    return hubble_image_links


def fetch_hubble_image(image_id,
                       get_hubble_image_links,
                       get_image,
                       get_file_extension,
                       images_path,
                       save_image):
    hubble_image_links = get_hubble_image_links(image_id)
    hubble_image_link = hubble_image_links[-1]
    hubble_image = get_image(hubble_image_link)

    file_extension = get_file_extension(hubble_image_link)
    filename = 'hubble{}.{}'.format(image_id,
                                  file_extension)

    save_image(hubble_image, filename, images_path)


def get_hubble_collection_ids(collection_name):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)

    response = requests.get(url, verify=False)
    collection = response.json()

    hubble_images_ids = [collection_element['id'] for collection_element in collection]

    return hubble_images_ids


def main():
    parser = argparse.ArgumentParser(
        description='This script downloads images from hubble telescope.'
    )
    parser.add_argument('-c', '--collection_name', help='Input name of hubble images collection. Default: "news" collection')
    args = parser.parse_args()

    collection_name = args.collection_name if args.collection_name else 'news'
    hubble_images_ids = get_hubble_collection_ids(collection_name)
    for image_id in hubble_images_ids:
        fetch_hubble_image(image_id,
                           get_hubble_image_links,
                           get_image,
                           get_file_extension,
                           IMAGES_PATH,
                           save_image)


if __name__ == '__main__':
    main()
