import re
import logging
import binascii
class bencoding():

    def __init__(self):
        self.decimal_match = re.compile('\d')
        self.data = b''
        self.dict = {}

    def get_dict(self, key):
        if key not in self.dict:
            return ''
        start = self.dict[key][0]
        end = self.dict[key][1]
        return self.data[start:end]

    def get_item(self, chunks):
        item = chunks[self.i]
        self.i += 1
        if not type(item) == str:
            item = bytes([item])
            try:
                item = item.decode('utf-8')
            except:
                item = '\\x{}'.format(binascii.hexlify(item))
        return item

    def decoding_byte_string(self, chunks, item):
        # logging.debug('decoding string')
        num = ''
        while self.decimal_match.search(item):
            num += item
            item = self.get_item(chunks)
        line = ''
        for i in range(int(num)):
            line += self.get_item(chunks)
        return line

    def decoding_integer(self, chunks):
        # logging.debug('decoding integer')
        item = self.get_item(chunks)
        num = ''
        while item != 'e':
            num += item
            item = self.get_item(chunks)
        return int(num)

    def decoding_list(self, chunks):
        # logging.debug('decoding list')
        item = self.get_item(chunks)
        list = []
        while item != 'e':
            self.i -= 1
            list.append(self._dechunk(chunks))
            item = self.get_item(chunks)
        return list

    def decoding_dictionnary(self, chunks):
        # logging.debug('decoding dictionnary')
        item = self.get_item(chunks)
        hash = {}
        while item != 'e':
            self.i -= 1
            key = self._dechunk(chunks)
            start = self.i
            hash[key] = self._dechunk(chunks)
            end = self.i
            self.dict[key] = (start, end)
            item = self.get_item(chunks)
        return hash

    def _dechunk(self, chunks):
        item = self.get_item(chunks)
        if item == 'd':
            return self.decoding_dictionnary(chunks)
        elif item == 'l':
            return self.decoding_list(chunks)
        elif item == 'i':
            return self.decoding_integer(chunks)
        elif self.decimal_match.search(item):
            return self.decoding_byte_string(chunks, item)
        raise "Invalid input!"

    def bdecode(self, data):
        self.data = data
        chunks = list(self.data)
        self.i = 0
        root = self._dechunk(chunks)
        return root
