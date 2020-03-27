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

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
