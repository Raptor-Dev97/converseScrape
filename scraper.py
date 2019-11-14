import requests
from bs4 import BeautifulSoup
import smtplib

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pandora.masti4@gmail.com','102030405060708090100')

    subject= "CONVERSE prices has fallen!!"
    body= 'Check out the link:: '+URL
    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pandora.masti4@gmail.com',
        'soumyaraj.kundu@aot.edu.in',
        msg
    )
    print('The message has been sent')

    server.quit()


URL = 'https://www.amazon.in/Converse-Unisex-Navy-Sneakers-150767C/dp/B012TRZKII/ref=sr_1_18?dchild=1&pf_rd_i=1983396031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=23731f00-9446-4488-b587-ee18085db352&pf_rd_r=W7XTCFA39J58D4VKB2JV&pf_rd_s=merchandised-search-7&qid=1573219649&refinements=p_n_pct-off-with-tax%3A0-&s=shoes&sr=1-18'
headere = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page = requests.get(URL, headers = headere)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("div", {"id":"titleSection"}).text
price= soup.find(id="priceblock_ourprice").text
print('Current price range:: ',price.strip())

# retrieving the price range and storing the range in an array.
# ',' & '.' removed from the string in order to access the numbers and then the numbers are divided by 0 in order to eliminate the paisa part.
formatted_price= price.replace(",","");
formatted_price= formatted_price.replace(".","");
res = [int(i) for i in formatted_price.split() if i.isdigit()]
lower= res[0]/100;
upper= res[1]/100;
print(lower," ",upper)

if (lower<=2100 and upper<=2500):
    send_mail()

