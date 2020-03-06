import time
import requests
from bs4 import BeautifulSoup
import re
for page in range(1,8):
    time.sleep(2)
    url = 'https://www.nabeulvoyages.com/reservationhotels?page={}'.format(page)
    print(url)




def url_to_transcript(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    regex = re.compile('floatlef')
    content_lis = soup.find_all('div', attrs={'class': regex})
    list=[]
    for x in range(len(content_lis)):
        list.append(content_lis[x].text)
    return list

urls=['https://www.nabeulvoyages.com/reservationhotels?page=1','https://www.nabeulvoyages.com/reservationhotels?page=2','https://www.nabeulvoyages.com/reservationhotels?page=3',
'https://www.nabeulvoyages.com/reservationhotels?page=4',
'https://www.nabeulvoyages.com/reservationhotels?page=5',
'https://www.nabeulvoyages.com/reservationhotels?page=6','https://www.nabeulvoyages.com/reservationhotels?page=7']
transcripts = [url_to_transcript(u) for u in urls]

def clean(text):
    
    text = re.sub(r"\n\t\t\t\t\t\t\t\t\t\t\t\t\t", " ", text)
    text = re.sub(r"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n\n", " ", text)
    text = re.sub(r"\t\t\t\t\t\t\t\t\t\t\t\t", " ", text)
    
    return text


clean_transcripts = []
for x in range(len(transcripts)):
    for trans in transcripts[x]:
        clean_transcripts.append(clean(trans))



#################  www.jektis.com  ############

def url_to_transcript(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    regex = re.compile('floatlef')
    ville = soup.find_all('span', attrs={'class': 'ville'})
    hotel = soup.find_all('a', attrs={'class': 'titre_listing'})
    start=soup.find_all('span', attrs={'class': 'Stars'})
    price=soup.find_all('span', attrs={'class': 'pricetotal'})
    description=soup.find_all('div', attrs={'class': 'ContentBlocHotel'})
    logement=soup.find_all('span', attrs={'class': 'logement'})
    Ville=[]
    Hotel=[]
    Start=[]
    Description=[]
    Price=[]
    Logement=[]
    for x in range(len(ville)):
        Ville.append(ville[x].text)
        Hotel.append(hotel[x].h1)
        Start.append(start[x].img)
        Description.append(description[x].p.text)
        Price.append(price[x].text)
        Logement.append(logement[x].text)
    return Ville,Hotel,Start,Description,Price,Logement
    
   jektis = [url_to_transcript(u) for u in urls]