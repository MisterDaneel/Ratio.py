# Ratio.py

Ratio.py is a small command line RatioMaster.Net like in Python3. It fakes upload stats of a torrent. 
Current emulators available are:
* Transmission 2.92
* qBittorrent 4.25

## Requirements:
1. Python 3.x
2. pip install -r requirements.txt

## Usage:
```
usage: ratio.py [-h] [-c CONFIGURATION] [-t TORRENT] [-u UPLOAD] [-C CLIENT]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIGURATION, --configuration CONFIGURATION
                        Configuration file
  -t TORRENT, --torrent TORRENT
                        Torrent file
  -u UPLOAD, --upload UPLOAD
                        Upload rate in kb/s
  -C CLIENT, --client CLIENT
                        Client (transmission/qbittorrent)
```

## Configuration example
```js
{
   "torrent": "<Torrent file path>",
   "upload": "<Upload speed (kB/s)>",
   "client: "<transmission/qbittorrent>""
}
```
