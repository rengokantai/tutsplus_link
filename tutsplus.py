# pip install --upgrade beautifulsoup4
# pip install html5lib
# Hernan Y.Ke 2/9/2018
from bs4 import BeautifulSoup 
import requests
import sys
import os
def start(args):
    r = requests.get(args)
    soup = BeautifulSoup(r.content, "html5lib")
    file = open("result.txt","w")
    for video in soup.findAll('a',class_="lesson-index__lesson-link", href=True):
        print("Now writing https://webdesign.tutsplus.com"+video['href']+"\n")
        file.write("https://webdesign.tutsplus.com"+video['href']+"\n")
        # print("https://webdesign.tutsplus.com"+video['href'])
    file.close()
    print("Done")

if __name__=='__main__':
    arg=sys.argv[1]
    start(arg)
