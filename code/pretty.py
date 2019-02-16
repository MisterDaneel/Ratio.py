import requests
from pprint import pformat


def get_headers(headers):
    res = ''
    for k, v in headers.items():
        res += '{}: {}\n'.format(k, v)
    return res


def pretty_GET(url, headers, params):
    req = requests.Request('GET', url, headers=headers, params=params)
    s = requests.Session()
    prepared = s.prepare_request(req)
    p = '-----START-----\n'
    p +=('{} {}\n{}'.format(prepared.method, prepared.url,
                            get_headers(prepared.headers),
                            )
    )
    if prepared.body:
        pi += prepared.body
    p += '------END------'
    return p


def pretty_data(data):
    return pformat(data)
