import requests
import bs4
import requests
from django.contrib import messages
from bs4 import BeautifulSoup
import pprint

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html')

s=1
def Newspost(request):
    hn=[]
    global s
    if(request.POST.get("size")):
        s=int(request.POST.get("size"))
        j = f"https://news.ycombinator.com/news?p={s}"
    else:
        s=s+1
        j = f"https://news.ycombinator.com/news?p={s}"
    j = f"https://news.ycombinator.com/news?p={s}"
    res = requests.get(j)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(" .titlelink")
    subtext = soup.select(" .subtext")
    j=0
    k=0
    for i in links:
        href = links[j].get('href')
        vote = subtext[j].select('.score')
        if(len(vote)):
            points=vote[0].getText().replace(' points','')
            points=int(points.replace(' point',''))
            #hn[k]={"title":i.getText(),"link":href,"points":points}
            k=k+1
            hn.append({"title":i.getText()})
            hn.append({"link":href})
            hn.append({"points":points})
            #messages.success(request, i.getText)
        j=j+1
    print(hn)
    return render(request, 'index.html',{"l":hn})
