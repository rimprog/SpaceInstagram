from fetch_spacex import get_spacex_images_links, fetch_spacex_images
from fetch_hubble import get_hubble_collection_ids, get_hubble_image_links, fetch_hubble_image
from prepare_images import IMAGES_PATH, get_image, save_image, get_file_extension, resize_images


def main():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_images(url,
                        get_spacex_images_links,
                        IMAGES_PATH,
                        get_image,
                        save_image)

    collection_name = 'news'
    hubble_image_ids = get_hubble_collection_ids(collection_name)
    for image_id in hubble_image_ids:
        fetch_hubble_image(image_id,
                           get_hubble_image_links,
                           get_image,
                           get_file_extension,
                           IMAGES_PATH,
                           save_image)

    image_resolution = (1080, 1080)
    resize_images(IMAGES_PATH, image_resolution)


if __name__ == '__main__':
    main()
