import time
import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def square_number(n):
    time.sleep(2)
    return n**2 

def print_letters():
    for i in "abcde":
        time.sleep(2)
        print(f"Letter:{i}")

urls=[
    'https://www.exceldemy.com/learn-excel/sample-data/',
    'https://app.gigasheet.com/spreadsheet/retail-sales-dataset/cc4d3a1e_496a_42f2_9fa7_af97646479d5?_gl=1*14tk29t*_gcl_au*MTAzODA1NzE1Mi4xNzM5MDc4ODA5'
]
def read_url(url):
    con=requests.get(url)
    soup=BeautifulSoup(con.content,"html.parser")
    print(len(soup))
thread1=threading.Thread(target=read_url,args=(urls[0],))
thread1.start()
thread1.join()
'''
with ThreadPoolExecutor(max_workers=3) as exc:
    res=exc.map(square_number,[1,2,3,4,5])
for r in res:
    print(r)

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_letters():
    for i in "abcde":
        time.sleep(2)
        print(f"Letter:{i}")
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)

t1=time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
t2=time.time()-t1
print(t2)'''