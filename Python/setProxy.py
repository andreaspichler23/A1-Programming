import os

def set_proxy():
    proxy_addr = 'http://<user>:<pw>@proxy.austria.local:8080'
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr

def unset_proxy():
    os.environ.pop('http_proxy')
    os.environ.pop('https_proxy')

set_proxy()
… API AUSFÜHREN …
unset_proxy()
