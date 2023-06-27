import requests
import bs4
import pandas

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.58',
    'Cookie': 'SINAGLOBAL=4692489639954.9375.1663489545427; UOR=,,www.bing.com; wb_view_log=1536*8641.25; '
              'XSRF-TOKEN=ouvOrxAVNu8bFjiLHmwmWeDc; _s_tentry=weibo.com; Apache=9011790255638.373.1687743259052; '
              'ULV=1687743259151:3:2:2:9011790255638.373.1687743259052:1687741690895; PC_TOKEN=db719cb388; '
              'login_sid_t=a36235c7334642a2178ac60c32bdb526; cross_origin_proto=SSL; '
              'SUB=_2A25JnJuYDeRhGeFJ4lMR9S7PyzmIHXVq64pQrDV8PUNbmtAGLXWhkW9Nfs21Lz4dSMcXwhb394Ygtuz0j4NzF7rt; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhdJxuQmclZ6-eWMrxJB7TC5JpX5KzhUgL.FoMN1K27SK50eh'
              '-2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0.peh-7e05f; ALF=1719279432; SSOLoginState=1687743432; '
              'WBPSESS=c_qEkUFwjhlStXswyQ4PAowAV0tEqnZdA3slFZBREyTXB0_HYT24btL6Q0WAgQwZm1LGCrriRuLhI6In9JFgIfQmH8'
              '-lmlW6fh0-3XuWCpx7XA8Ya7FJuhcJSzSJOcAR1co8R-POhcAgx3hQMtKutA=='
}

url = 'https://m.weibo.cn/profile/5346889203'


html = requests.get(url, headers=headers)
html.encoding = html.apparent_encoding
print(html.text)
