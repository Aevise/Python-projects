from bs4 import BeautifulSoup
import requests
import smtplib
import lxml
from email.message import EmailMessage

AMAZON_HEADER = {       #won't work without this header
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
}
BOT_EMAIL = " "
BOT_PASSWORD = " "
SMTP_HOST = 'smtp.poczta.onet.pl'
YOUR_EMAIL = " "
43
def Amazon_Price_Tracker(desired_item:str, desired_price:float)->None:
    """get the information if the item is available for desired price on amazon website

    Args:
        desired_item (str): Amazon website address of desired item
        desired_price (float): price that you are willing to pay for an item
    """
    desired_data = []
    desired_data = get_title_and_price(desired_item)
    if desired_data:
        if float(desired_data[1]) < desired_price:
            send_message(desired_data, desired_item)
            print(f"Desired price: {desired_price}, Current price: {desired_data[1]}\nItem is available for you! And it is {desired_price-float(desired_data[1])} cheaper!")

def get_title_and_price(desired_item_web:str)->list:
    """Search through HTML code provided by Amazon and gets the title and price of an item

    Args:
        desired_item_web (str): Amazon website address of desired item

    Returns:
        list: list containing title and price of an item
    """
    soup_data = connect_and_get_data(desired_item_web)
    if soup_data:
        price = soup_data.find(name="span", class_="a-offscreen").text
        price = price[1:]
        title = soup_data.find(name="span", id="productTitle").text.strip()
        return [title, price]

def connect_and_get_data(desired_item_web:str)->bool or BeautifulSoup:
    """gets the HTML code from the Amazon website

    Args:
        desired_item_web (str): Amazon website address of desired item

    Returns:
        bool or BeautifulSoup: if connection fails returns False in other case returns scrapped data
    """
    response = requests.get(desired_item_web, headers=AMAZON_HEADER)
    if response.status_code < 200 or response.status_code > 299:
        print(f"Error. Status code: {response.status_code}")
        return False
    soup_data  = BeautifulSoup(response.text, "lxml")
    return soup_data

def send_message(desired_item:list, website:str)->bool:
    """uses a bot to send a email to the user

    Args:
        desired_item (list): list containing item name and price
        website (str): Amazon website address of desired item

    Returns:
        bool: inform whether sending mail was successfull or not 
    """
    bot_mail = smtplib.SMTP_SSL(SMTP_HOST, 465)
    try:
        bot_mail.login(BOT_EMAIL, BOT_PASSWORD)
    except smtplib.SMTPAuthenticationError:
        print("Couldn't send and email :(.")
        return False
    else:
        # construct message
        message = EmailMessage()
        message.set_content(f"Your desired item:\n{desired_item[0]}\nis now available for: {desired_item[1]}!\nVisit a site to grab an item!:\n{website}")
        message["Subject"] = "Discount on desired item!"
        message["From"] = BOT_EMAIL
        message["To"] = YOUR_EMAIL
        #send mail
        bot_mail.send_message(message)
        bot_mail.quit()
        return True

#-----------------------------------------------------------------------------------------------------------------
link_to_desired_item = "https://www.amazon.com/X-cosrack-Adjustable-Chalkboards-Vegetables-Toiletries/dp/B07VDD7R2C/ref=sr_1_3?crid=26S1SSNDZVS3Z&keywords=potato+ben&qid=1666639619&qu=eyJxc2MiOiI1LjI4IiwicXNhIjoiNC45MSIsInFzcCI6IjMuMTcifQ%3D%3D&sr=8-3"
desired_price = float(input("What is your desired price for an item?: "))

Amazon_Price_Tracker(link_to_desired_item, desired_price)

