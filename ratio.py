from code.process_torrent import process_torrent
import argparse
import json
import sys

def parse_args():
   """Create the arguments"""
   parser = argparse.ArgumentParser('\nratio.py -c <configuration-file.json>')
   parser.add_argument("-c", "--configuration", help="Configuration file")
   return parser.parse_args()

def load_configuration(configuration_file):
    with open(configuration_file) as f:
        configuration = json.load(f)

    if 'torrent' not in configuration:
        return None

    return configuration


if __name__ == "__main__":
    args = parse_args()
    if args.configuration:
        configuration = load_configuration(args.configuration)
    else:
        sys.exit()
   
    if not configuration:
        sys.exit()
 
    to = process_torrent(configuration)
    to.tracker_process()

