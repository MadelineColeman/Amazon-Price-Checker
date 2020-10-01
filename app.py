#%% Import Packages

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen 
import smtplib
import time

#%% Declare Varibles

headers = {'User-Agent':'Mozilla/5.0'}

#%%Get Price from Amazon

def getPrice():
    url = input("Enter the Amazon Link: ")
    email = input("Please enter email to recieve alert: ")
    password = input('Please enter  email password: ')
    req = Request(url, headers = headers)
    page = urlopen(req).read()
    soup = BeautifulSoup(page)

    price = soup.find(id = 'priceblock_ourprice').get_text()
    title = soup.find(id = "productTitle").get_text()

    price = float(price.split("$", 1)[1])
    title = title.strip()

    print("The price of " + title + " is ${}".format(price) )
    alertPrice = float(input("\nEnter the price you would like to be alerted at: "))

    if price <= alertPrice:
        sendEmail(title, alertPrice, url, email, password)
    else:
        time.sleep(3600)
        getPrice()



# %% Send Email

def sendEmail(title, alertPrice, url, email, password):
    subject = "Amazon Price Alert"
    body = "{} is below ${:.2f}. Check out the link below\n{}".format(title, alertPrice, url)
    msg = f"Subject: {subject},\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.connect('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, email, msg)
    server.quit()

# %% Run Script

getPrice()
