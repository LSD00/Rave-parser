from rich.console import Console
from rich.table import Table
from rich import print
import os
from threading import Thread
import all
import just_get
from PyRoxy import ProxyUtiles, ProxyChecker
from rich.progress import track

def starter(lists):
    api = just_get.api(lists)
    proxy = all.parse(lists)
    Thread(target=proxy.hidemyname).start()
    Thread(target=proxy.foxtools).start()
    Thread(target=proxy.freeproxylist).start()
    Thread(target=proxy.proxy_download).start()
    Thread(target=api.gett).start()
    Thread(target=proxy.hidemylife).start()
def listt():
    table = Table(title="sites(list will be updates)")

    table.add_column("No.", style="cyan", no_wrap=True)
    table.add_column("url", style="magenta")

    table.add_row("1", "hide my name")
    table.add_row("2", "foxtools")
    table.add_row("3", "sslproxies")
    table.add_row("4", "freeproxylist.ru")
    table.add_row("5", "www.proxy-list.download")
    table.add_row("6", "multiproxy.org")
    table.add_row("7", "alexa.lr2b.com")
    table.add_row("8", "api.openproxylist.xyz")
    table.add_row("9", "api.proxyscrape.com")
    table.add_row("10", "sheesh.rip")
    table.add_row("11", "proxy-spider.com(example)")
    table.add_row("12", "proxyspace.pro")
    table.add_row("13", "github(6 lists)")
    table.add_row("14", "hidemy.life")

    console = Console()
    console.print(table)
def logo(ccc):
    print('''
__________
\______   \_____  ___  __  ____
 |       _/\__  \ \  \/ /_/ __  \ 
 |    |   \ / __ \_\   / \  ___/
 |____|_  /(____  / \_/   \___  >
        \/      \/            \/ parser
    ''')
    for x in range(ccc):
        os.system('color B')
        os.system('color a')
        os.system('color 4')
        os.system('color D')
def main():
    logo(10)
    print('''
[1] return info
[2] parse
[3] checker''')
    while True:
        a = input("parse@LSD:~$")
        if a == "1" or a =="[1]":
            listt()
            input()
        if a == "2" or a == "[2]":
            mainlist = []
            starter(mainlist)
        if a == "3" or a == "[3]":
            for _ in track(range(100), description='[green]Checking proxy'):
                ps = ProxyUtiles.readFromFile("proxies.txt")
                pc = ProxyChecker.checkAll(ps)
            print(pc)
            with open("checked.txt", "w") as file:
                file.write(pc)
if __name__ == '__main__':
    main()
    input()
