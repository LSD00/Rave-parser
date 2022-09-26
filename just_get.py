import cloudscraper as cl
from rich import print

scraper = cl.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
proxy_list = ["https://multiproxy.org/txt_all/proxy.txt",
"http://alexa.lr2b.com/proxylist.txt",
"https://api.openproxylist.xyz/http.txt",
"https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
"https://sheesh.rip/http.txt",
"https://proxy-spider.com/api/proxies.example.txt",
"https://proxyspace.pro/http.txt",
"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt",
"https://proxyspace.pro/https.txt",
"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
"http://worm.rip/socks4.txt",
"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt"]
class api:
    def __init__(self, lists):
        self.lists = lists

    def gett(self):
        for api in proxy_list:
            print(scraper.get(api).text)
            self.lists.append(scraper.get(api).text)
        with open("proxies.txt", "w") as file:
            file.writelines(self.lists)
