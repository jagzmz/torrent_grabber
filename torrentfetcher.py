import requests,sys
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable
import os,time
import re
http_proxy="151.80.140.233:54566"

proxyDict = { 
              "http"  : http_proxy
            }

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    address=str(input("Enter the Torrent you want to search: "))
if address is not None:
    res = requests.get('https://proxyfl.info/search/{}/0/7/0'.format(address),proxies=proxyDict)
    res.raise_for_status()
    soup = bs(res.content,"html.parser")
    data=[]
    b=1
    g=0
    for a in soup.select('table td'):
        if len(a.select('div[class="detName"]')) !=0:

            data.append([str(b)+str('.'),a.select('div[class="detName"] a')[0].get_text().encode('ascii','ignore').decode('utf-8'),a.select('div[class="detName"] a')[0].get('href')])
            b=b+1
    i=0
    for ele in soup.select('table td[align="right"]'):
        
        if g%2==0:
            data[i].insert(len(data[i])-1,ele.get_text())
            i=i+1
        g=g+1
    x=PrettyTable(["No.","Torrent Name","Seeds"])
    x.align["Torrent Name"] = "l"
    for gg in data:
        x.add_row(gg[0:3])
    print(x)
    no=int(input("Which torrent you want to download? : "))
    print('+--------------------------------------+')
    res2=requests.get('https://fastpiratebay.co.uk/{}'.format(data[no-1][3]))
    soup2 = bs(res2.content,"html.parser")
    print('Download Successful.\n\nMade by killswitc_h.')
    time.sleep(3)
    os.startfile("{}".format(soup2.select('.download a')[0].get('href')))