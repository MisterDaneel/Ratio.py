from code.process_torrent import process_torrent
import argparse
import json
import sys

def parse_args():
   """Create the arguments"""
   parser = argparse.ArgumentParser()
   
   parser.add_argument("-c", "--configuration", help="Configuration file")
   parser.add_argument("-t", "--torrent", help="Torrent file")
   parser.add_argument("-u", "--upload", help="Upload rate in kb/s")
   parser.add_argument("-C", "--client", help="Client (transmission/qbittorrent)")
   
   return parser.parse_args()

def load_configuration(configuration_file):
    with open(configuration_file) as f:
        configuration = json.load(f)

    if 'torrent' not in configuration:
        return None

    print(configuration)
    return configuration


if __name__ == "__main__":
    args = parse_args()
    if args.configuration:
        configuration = load_configuration(args.configuration)
    elif (args.torrent != None) and (args.upload) and (args.client):
        configuration = {'torrent': args.torrent,
                         'upload': args.upload,
                         'client': args.client
           }
    else:
        sys.exit()
    if not configuration:
        sys.exit()
 
    to = process_torrent(configuration)
    to.tracker_process()

