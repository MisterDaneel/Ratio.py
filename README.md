# Ratio.py

Ratio.py is a small command line RatioMaster.Net like in Python3. It fakes upload stats of a torrent. 
Current emulators available are:
* Transmission 3.00

## Requirements:
1. Python 3.x
2. pip install -r requirements.txt

## Usage:

```bash
foo@bar: ~/Ratio.py $ python3 ratio.py -c config.json 
```

To run (multiple instances) in background :

```bash
foo@bar: ~/Ratio.py $ nohup python3 ratio.py -c config.json &
foo@bar: ~/Ratio.py $ nohup python3 ratio.py -c config.json &> nohup2.out &
```

View logs :

```bash
foo@bar: ~/Ratio.py $ tail -f nohup.out
```

## Configuration example

```js
{
   "torrent": "<Torrent file path>",
   "upload": "<Upload speed (kB/s)>"
}
```

*This project is an updated fork of [this project](https://github.com/MisterDaneel/Ratio.py).*

