# Space Instagram

Script fetch_spacex.py downloads images from launching spacex by [SPACEX API](https://documenter.getpostman.com/view/2025350/RWaEzAiG?version=latest#bc65ba60-decf-4289-bb04-4ca9df01b9c1). By default downloads images from [last spacex launch](https://api.spacexdata.com/v3/launches/latest). You can pass your download url on the command line. Use optional argument --url

```
python3 fetch_spacex.py --url https://api.spacexdata.com/v3/launches/latest
```

More info: 
```
python3 fetch_spacex.py -h
```

Script fetch_hubble.py downloads images from hubble telescope collections by [HUBBLE API](http://hubblesite.org/api/documentation). By default downloads images from ["news" collection](http://hubblesite.org/api/v3/images/news). You can pass collection's name on the command line. Use optional argument -c

```
python3 fetch_hubble.py -c news
```

More info: 
```
python3 fetch_hubble.py -h
```

All images are downloaded to the images folder of your script root directory.

Script prepare_images.py resizes downloads images. All images must be in the images folder of your script root directory. By default, script resize all images at a width of 1080 and heigth of 1080. Resized images stored in resized_images folder into your '''./image folder'''. You can pass width and height on the command line. Use optional arguments --width and --height

```
python3 prepare_images.py --width 1080 --height 1080
```

More info: 
```
python3 prepare_images.py -h
```

Script main.py launch all scripts together by default. First it download spacex images, then download hubble images. And last it resize downloaded images.
```
python3 main.py
```

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
