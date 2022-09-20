from os import times_result
from platform import release
from re import X
from turtle import title
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from IPython.display import clear_output
import time
a = 0
liste = []
liste1 = []
liste2 = []

while a<5:            #YOU CAN INSCREASE THE NUMBER OF MOVIES IN THE MEMORY BY INSCREASING THE NUMBER (now 5)
    r = requests.get("https://www.hdfilmcehennemi.live/page/"+str(a)).content
    soup1 = BeautifulSoup(r,"html.parser")
    full_list = soup1.find_all("div",{"class":"col-6 col-sm-3 poster-container px-2 px-sm-1 mb-3 mb-sm-2"})

    for movie in full_list:
        liste = []
        liste1 = []

        link = movie.a.get("href")
        r1 = requests.get(link).content
        soup = BeautifulSoup(r1,"html.parser")
        title = soup.find("div",{"class":"card-header card-post-title"}).find("div").text.strip()

        print(title)

        explanation = soup.find("article",{"class":"text-white"}).find("p").text.strip()

        print(explanation)                                         #YOU CAN SEE ALL MOVIES IN THE MEMORY BY REMOVING # WHICH IS NEAR OF PRINT

        imdb = soup.find("article",{"class":"text-white"}).find("div",{"class":"mb-0 lh-lg"}).find("a",{"class":"text-warning"}).text.strip()

        print(imdb)

        details = soup.find("div",{"class":"mb-0 lh-lg"}).find_all("div",{"class":"pb-2"})
        for detail in details:
            liste.append(detail)
        time = liste[0].find("span",{"class":"badge bg-light-25"}).text.strip()
        releaseTime = liste[2].find("a",{"class":"badge bg-light-25"}).text.strip()
        types = liste[3].find_all("a",{"class":"badge bg-light-25"})
        for type1 in types:
            liste1.append(type1)
        
        try: 
            type2 = f"{liste1[0].text} {liste1[1].text} {liste1[2].text}"   
        except:
            try:
                type2 = f"{liste1[0].text} {liste1[1].text}"
            except:
                type2 = f"{liste1[0].text}"   
        print(type2)     
        print(time)
        print(releaseTime)
        print(f"izle : {link}")
        liste2.append([title,explanation,time,releaseTime,imdb,type2,link])
        
    a = a+1    
print(f"Toplam film sayısı : {20*a}")    

print("-----YOUR MOVIE RECOMMENDATION-----")        
mv = random.choice(liste2)
print(f"İsim : {mv[0]}\nAçıklama : {mv[1]}\nSüre : {mv[2]}\nYayınlanma Zamanı : {mv[3]}\nIMDb Puanı : {mv[4]}\nTürü : {mv[5]}\nİzle : {mv[6]}")