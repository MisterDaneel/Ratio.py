import random
import string

class Transmission292():
    def __init__(self, info_hash):
        self.name = "Transmission 2.92 (14714)"
        parameters = {}
        # urlencoded 20-byte SHA1 hash of the value of the info key from the Metainfo file
        parameters['info_hash'] = info_hash
        # urlencoded 20-byte string used as a unique ID for the client
        parameters["peer_id"] = self.generate_peer_id()
        # The port number that the client is listening on
        parameters["port"] = random.randint(1025, 65535)
        # Number of peers that the client would like to receive from the tracker
        parameters["numwant"] = 80
        # An additional identification that is not shared with any other peers
        parameters["key"] = self.generate_key()
        # Setting this to 1 indicates that the client accepts a compact response
        parameters["compact"] = 0
        # Setting this to 1 indicates that the client accepts crypto
        parameters["supportcrypto"] = 1
        self.parameters = parameters

    def get_headers(self):
        headers = {}
        headers['User-Agent'] = 'Transmission/2.92'
        headers['Accept'] = '*/*'
        headers['Accept-Encoding'] = 'Accept-Encoding: gzip;q=1.0,  deflate, identity'
        return headers

    def get_query(self, uploaded, downloaded, left=0, event=None):
        # The total amount uploaded (since the client sent the 'started' event)
        self.parameters["uploaded"] = uploaded
        # The total amount downloaded (since the client sent the 'started' event)
        self.parameters["downloaded"] = downloaded
        # The number of bytes this client still has to download
        self.parameters["left"] = left
        # If specified, must be one of started, completed, stopped
        if event:
            self.parameters["event"] = event
        params = '&'.join('{}={}'.format(k, v)
                          for k, v in self.parameters.items())
        return params

    def id_generator(self, chars, size):
        id = ''
        for _ in range(size):
            id += random.choice(chars)
        return id

    def generate_peer_id(self):
        chars = string.ascii_lowercase + string.digits
        rand_id = self.id_generator(chars, 12)
        peer_id = "-TR2920-" + rand_id
        return peer_id

    def generate_key(self):
        chars = 'ABCDEF' + string.digits
        key = self.id_generator(chars, 8)
        return key
