from bs4 import BeautifulSoup
import cloudscraper as cl
from rich import print
scraper = cl.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
class parse:
    def __init__(self, lists):
        self.lists = lists

    def hidemyname(self):

        count_1 = 0
        count_2 = 64

        for x in range(186):
            req  = scraper.get(f"https://hidemy.name/ru/proxy-list/?type=hs&start={count_2}#list")

            soup = BeautifulSoup(req.text, "lxml")
            res = soup.find("tbody").find_all("tr")

            for td in res:
                tr = td.find_all("td")
                print(f"{tr[0].text}:{tr[1].text}")
                self.lists.append(f"{tr[0].text}:{tr[1].text}")
            count_1 = count_1 + 1
            count_2 = count_2 + 64
            print(f"[bold magenta]hidemyname page: {count_1}[/bold magenta]")
        print("[bold magenta]DONE[/bold magenta]")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)

    def sslproxies(self):
        req = scraper.get("https://www.sslproxies.org/")

        soup = BeautifulSoup(req.text, "lxml")
        res = soup.find("tbody").find_all("tr")

        for td in res:
            tr = td.find_all("td")
            print(f"{tr[0].text}:{tr[1].text}")
            self.lists.append(f"{tr[0].text}:{tr[1].text}")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)

    def foxtools(self):
        x = 1
        for x in range(3):
            req = scraper.get(f"http://foxtools.ru/Proxy?page={x}")

            soup = BeautifulSoup(req.text, "lxml")
            res = soup.find("tbody").find_all("tr")

            for td in res:
                tr = td.find_all("td")
                print(f"{tr[1].text}:{tr[2].text}")
                self.lists.append(f"{tr[1].text}:{tr[2].text}")
            x = x + 1
            print(f"[bold magenta]foxtools page: {x}[/bold magenta]")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)
        print("[bold magenta]DONE[/bold magenta]")

    def freeproxylist(self):
        count = 1
        for count in range(27):
            count = count + 1
            req = scraper.get(f"https://freeproxylist.ru/proxy-list?page={count}")

            soup = BeautifulSoup(req.text, "lxml")
            res = soup.find("tbody", class_='table-proxy-list').find_all("tr")
            for x in res:
                iplis = x.find_all("th", class_='w-30 tblport')
                portlist = x.find_all("td", class_='w-10 tblport')
                print(f"{iplis[0].text}:{portlist[0].text}")
                self.lists.append(f"{iplis[0].text}:{portlist[0].text}")
            print(f"[bold magenta]freeproxylist.ru page: {count}[/bold magenta]")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)

    def proxy_download(self):
        scraper = cl.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
        req = scraper.get("https://www.proxy-list.download/HTTPS")

        soup = BeautifulSoup(req.text, "lxml")
        res = soup.find("tbody", id="tabli").find_all("tr")
        for td in res:
            tr = td.find_all("td")
            ip = "".join(tr[0].text.split())
            port = "".join(tr[1].text.split())
            print(f"{ip}:{port}")
            self.lists.append(f"{ip}:{port}")
        print(f"[bold magenta]DONE[/bold magenta]")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)

    def hidemylife(self):
        req = scraper.get("https://hidemy.life/ru/proxy-list-servers")
        soup = BeautifulSoup(req.text, "lxml")
        td = soup.find("tbody").find_all("tr")

        for i in td:
            pr = i.find_all("td")
            print(f'{pr[0].text}:{pr[1].text}')
            self.lists.append(f'{pr[0].text}:{pr[1].text}')
        print(f"[bold magenta]DONE[/bold magenta]")
        with open("proxies.txt", "w") as file:
                file.writelines("%s\n" % i for i in self.lists)
