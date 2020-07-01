#Importing required modules

import requests
from bs4 import BeautifulSoup
import smtplib, ssl

URL = "https://www.amazon.in/dp/B081JWZQJB/ref=fs_a_mn_3"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle")

    # To get only the title name of the prouduct

    title = soup.find(id="productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()

    # Get only numerics of price

    con_price = price[2:]

    converted_price = con_price.replace(",", "")

    # Change price into float

    fin_price = float(converted_price)
    print(fin_price)

    # If final price of the product falls below 1.5 lakhs send a mail to notify me

    if fin_price < 150000:
        send_mail()


def send_mail():
    # To secure connection since starttls is insecure but SSP is not
    context = ssl.create_default_context()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()

    # ALTERNATIVE:
    # password = input("Type your password and press enter:")
    # server.login("something@gmail.com", password)

    # Generate password from your gamil account after allowing two step verification
    server.login("something@gmail.com", "fmlkbcbpwxyonrfq")

    subject = "Woo! Price Fell Down"
    body = "Check amazon link https://www.amazon.in/dp/B081JWZQJB/ref=fs_a_mn_3"

    msg = f"Subject:{subject}:\n\n{body}"

    # I have changed the place of original gmail accounts with pseudo names for privacy reasons after executing the script.
    # You can use two different mails for such task.

    server.sendmail(
        "sender@gmail.com",
        "reciever@gmail.com",
        msg
    )

    print("Hey! Email has been sent.")

    server.quit()


########################################################################