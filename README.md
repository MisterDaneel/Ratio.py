# Ratio.py

Ratio.py is a small command line RatioMaster.Net like in Python3. It fakes upload stats of a torrent. 
Current emulators available are:
* Transmission 2.92

## Requirements:
1. Python 3.x
2. pip install -r requirements.txt

## Usage:
```console
foo@bar:~/ratio.py$ python ratio.py -c configuration.json 
```

## Configuration example
```js
{
   "torrent": "<Torrent file path>",
   "upload": "<Upload speed (kB/s)>",
   "client: "<transmission/qbittorrent>""
}
```
