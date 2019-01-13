# Custom Script I made for cycling through proxies

# Put this in the header space.

from lxml.html import fromstring
import requests
from itertools import cycle

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


proxies = get_proxies()
proxy_pool = cycle(proxies)


# Later in your code, put this in the loop or place where you fetch the source code with BS4 multiple times:

#loop
  proxy = next(proxy_pool)
  source_code = requests.get(url, proxies={"http": proxy})
  #other code
#end loop
