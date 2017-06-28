#crawler section
from urllib.request import urlopen
from bs4 import BeautifulSoup

#three category about guokr:

#1. question (WenDa):
#   http://www.guokr.com/question/6-dig number

#2. Xiaozu:
#   http://www.guokr.com/post/6-dig number

#3. Articles (KePu), this happens to be Guokr's major business
#   http://www.guokr.com/article/6-dig number
def getpage(postlink):
    html