import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Canon-EOS-550D-Digital-3-5-5-6/dp/B0718ZS647/ref=sr_1_5?crid=39SY5XE965UV5&keywords=camera+canon+1500d+dslr&qid=1575389654&sprefix=camera+ca%2Caps%2C397&sr=8-5' 
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
        page=requests.get(URL, headers=headers)

        soup=BeautifulSoup(page.content, 'html.parser')

        title=soup.find(id="productTitle").get_text()
        price=soup.find(id="priceblock_ourprice").get_text()
        k=price.replace(',','')
        converted_price=float(k[2:7])

        if(converted_price < 61000):
            send_mail()
        print(converted_price)
        print(title.strip())

        
        if(converted_price > 61000):
            send_mail()

def send_mail():
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('chamschamanthi36@gmail.com','chamsleepyhead')

        subject='price fell down!!!'
        body='check the amazon link https://www.amazon.in/Canon-EOS-77D-Digital-3-5-5-6/dp/B0718ZS647/ref=sr_1_5?crid=39SY5XE965UV5&keywords=camera+canon+1500d+dslr&qid=1575389654&sprefix=camera+ca%2Caps%2C397&sr=8-5 '

        msg=f"Subject: {subject}\n\n{body}"

        server.sendmail('chamschamanthi36@gmail.com','chamanthiaki00@gmail.com', msg)

        print("email has been sent!!!")

        server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)

