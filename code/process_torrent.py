from code.decoding_bencoded import bencoding
from code.torrentclientfactory import Transmission292
from code.pretty import pretty_data, pretty_GET

from hashlib import sha1
from urllib.parse import quote_plus
import requests
import logging
import random
from tqdm import tqdm
from time import sleep

from struct import unpack

logging.basicConfig(level=logging.DEBUG)

class process_torrent():

    def __init__(self, configuration):
        self.configuration = configuration
        self.open_torrent()
        self.torrentclient = Transmission292(self.tracker_info_hash())

    def open_torrent(self):
        torrent_file = self.configuration['torrent']
        with open(torrent_file, 'rb') as tf:
            data = tf.read()
        self.b_enc = bencoding()
        self.metainfo = self.b_enc.bdecode(data)
        self.info = self.metainfo['info']
        if 'length' not in self.info:
            self.info['length'] = 0
            for file in self.info['files']:
                self.info['length'] += file['length']
            print(pretty_data(self.info['files']))

    def tracker_info_hash(self):
        raw_info = self.b_enc.get_dict('info')
        hash_factory = sha1()
        hash_factory.update(raw_info)
        hashed = hash_factory.hexdigest()
        sha = bytearray.fromhex(hashed)
        return str(quote_plus(sha))

    def send_request(self, params, headers):
        url = self.metainfo['announce']
        print(pretty_GET(url, headers, params))
        while True:
            try:
                r = requests.get(url, params=params, headers=headers)
            except requests.exceptions.ConnectionError as e:
                sleep(1)
                continue
            break
        return r.content

    def tracker_start_request(self):
        tc = self.torrentclient
        headers = tc.get_headers()
        params = tc.get_query(uploaded=0,
                              downloaded=0,
                              event='started')

        print('----------- First Command to Tracker --------')
        content = self.send_request(params, headers)
        self.tracker_response_parser(content)

    def tracker_response_parser(self, tr_response):
        b_enc = bencoding()
        response = b_enc.bdecode(tr_response)
        print('----------- Received Tracker Response --------')
        print(pretty_data(response))
        raw_peers = b_enc.get_dict('peers')
        i = 0
        peers = []
        while i<len(raw_peers)-6:
            peer = raw_peers[i:i+6]
            i+=6
            unpacked_ip = unpack('BBBB', peer[0:4])
            ip = ".".join(str(i) for i in unpacked_ip)
            unpacked_port = unpack('!H', peer[4:6])
            port = unpacked_port[0]
            peers.append((ip, port))
        self.interval = response['interval']

    def wait(self):
        random_badtime = random.randint(10,15)*60   # interval to send request betwen 10min and 15min
        self.interval = random_badtime
        pbar = tqdm(total=self.interval)
        print('sleep: {}'.format(self.interval))
        t = 0
        while t < (self.interval):
            t += 1
            pbar.update(1)
            sleep(1)
        pbar.close()

    def tracker_process(self):
        while True:
            self.tracker_start_request()

            print('----------- Sending Command to Tracker --------')

            # get upload
            min_up = self.interval-(self.interval*0.1)
            max_up = self.interval
            randomize_upload = random.randint(min_up, max_up)
            uploaded = int(self.configuration['upload'])*1000*randomize_upload

            # get download
            downloaded = 0

            tc = self.torrentclient
            headers = tc.get_headers()
            params = tc.get_query(uploaded=uploaded,
                                  downloaded=downloaded,
                                  event='stopped')
            content = self.send_request(params, headers)
            self.tracker_response_parser(content)
            self.wait()
