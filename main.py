import requests
from pathlib import Path


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

def get_spacex_images_links(url):
    response = requests.get(url)
    response.raise_for_status()

    spacex_images_links = response.json()['links']['flickr_images']

    return spacex_images_links

def fetch_spacex_images(url,
                        get_hubble_image_links,
                        images_path,
                        get_image,
                        save_image):
    spacex_images_links = get_spacex_images_links(url)

    for image_number, image_link in enumerate(spacex_images_links):
        url = image_link
        image = get_image(url)

        filename = 'spacex{}.jpg'.format(image_number)
        save_image(image, filename, images_path)

def get_hubble_image_links(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url)
    response.raise_for_status()

    hubble_image_links = response.json()['image_files']
    hubble_image_links = ['http:{}'.format(image_link['file_url']) for image_link in hubble_image_links]

    return hubble_image_links

def get_file_extension(filename):
    file_extension = filename.split('.')[-1]

    return file_extension

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

    ids = [collection_element['id'] for collection_element in collection]

    return ids


def main():
    images_path = "images/"

    url = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_images(url,
                        get_spacex_images_links,
                        images_path,
                        get_image,
                        save_image)


    collection_name = 'news'
    hubble_image_ids = get_hubble_collection_ids(collection_name)
    for image_id in hubble_image_ids:
        fetch_hubble_image(image_id,
                           get_hubble_image_links,
                           get_image,
                           get_file_extension,
                           images_path,
                           save_image)


if __name__ == '__main__':
    main()
