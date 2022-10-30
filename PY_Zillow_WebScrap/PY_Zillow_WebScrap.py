from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import lxml
import time

class ZillowScrap():
    """Copies house offers from zillow website. 
    Set parameters on zillow.com website, and past website to self.ZILLOW.WEB
    """
    def __init__(self, zillow_link:str, googlespreadsheet_link:str)->None:
        """Initializes class and realizes all the proccess of fetching, composes and inputting data into the spreadsheet.
        When finished closes the google chrome tab.

        Args:
            zillow_link (str): link to zillow website containing information on house prices
            googlespreadsheet_link (str): link to google spreadsheet
        """
        FOLDER = os.path.dirname(os.path.abspath(__file__))
        HEADER ={       #won't work without this header
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
        }
        WEBSITE = FOLDER + "/chromedriver.exe"
        self.GOOGLE_SPREADSHEET = googlespreadsheet_link
        self.ZILLOW_WEB = zillow_link
        self.driver = webdriver.Chrome(executable_path=(WEBSITE))
        self.driver.get(self.GOOGLE_SPREADSHEET)
        self.properties_data = self.compose_data(HEADER)
        self.driver.close()
        
    def compose_data(self, header:dict)->None:
        """Receives data from Zillow website using BeautifulSoup and transforms it into the list of dictionaries

        Args:
            header (dict): contains information that allow to identify application, operating system, vendor, and/or version of the requesting user agent
        """
        REQ = requests.get(self.ZILLOW_WEB, headers=header)
        data = BeautifulSoup(REQ.text, "lxml")
        properties_data = [{"Property:":name, "Price:":price, "Link:":link} for name, price, link in zip(self.get_property_name(data), self.get_property_price(data), self.get_links(data))]
        self.fill_formulas(properties_data)

    def get_links(self, links_data:BeautifulSoup)->list:
        """Reads the information fetched from Zillow website and searches for the link to each offered house.

        Args:
            links_data (BeautifulSoup): information fetched from Zillow website

        Returns:
            list: link directly leading to rent offert.
        """
        links = links_data.select(".StyledPropertyCardDataWrapper-c11n-8-73-8__sc-1omp4c3-0 a")
        links_data = []
        for link in links:
            if "http" not in link:
                links_data.append(f"https://www.zillow.com{link['href']}")
            else:
                links_data.append(link["href"])
        return links_data

    def get_property_name(self, links_data:BeautifulSoup)->list:
        """_Reads the information fetched from Zillow website and searches for the properties name.

        Args:
            links_data (BeautifulSoup): information fetched from Zillow website

        Returns:
            list: names of the properties
        """
        properties_data = []
        properties = links_data.find_all(class_ = "ListItem-c11n-8-73-8__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation")    
        for property in properties:
            if len(property.text) > 1:
                try:
                    properties_data.append(property.text[:property.text.index(" |")]) 
                except ValueError:
                    properties_data.append(property.text[:property.text.index(", ")])
        return properties_data

    def get_property_price(self, links_data:BeautifulSoup)->list:
        """Reads the information fetched from Zillow website and searches for the monthly rent of each house.

        Args:
            links_data (BeautifulSoup): information fetched from Zillow website
        Returns:
            list: monthly rent in $
        """
        price_data = []
        prices = links_data.find_all(class_ = "ListItem-c11n-8-73-8__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation")    
        for price in prices:
            if len(price.text) > 1:
                cash = float(price.text[price.text.index("$")+1:price.text.index("$")+6].replace(",","."))
                price_data.append(cash) 
        return price_data        

    def fill_formulas(self, data:list, speed:int = 0.25)->None:
        """Fills the textboxes on the google spreadsheet with provided information. 

        Args:
            data (list): composed data in form of list of dictionaries
            speed (int, optional): Scaleable speed of data insertions. Defaults to 0.25.
        """
        time.sleep(speed*8)
        data_keys = list(data[0].keys())

        for item in range(len(data)):
            time.sleep(speed)
            textboxes = self.driver.find_elements(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/*/div/div/div[2]/div/div[1]/div/div[1]/input')
            send_button = self.driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            for value in range(len(textboxes)):
                time.sleep(speed/2)
                textboxes[value].send_keys(str(data[item][data_keys[value]]))

            send_button.click()
            time.sleep(speed)
            next_item = self.driver.find_element(by="xpath", value = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            next_item.click()

google_link = "https://docs.google.com/forms/d/e/1FAIpQLSeDQ2csJzaVFLU6yWBjqhNC0C2H8eY87WEFhcMNPGK59oRs5Q/viewform"
zillow_link = "https://www.zillow.com/birmingham-al/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Birmingham%2C%20AL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-87.25032812207031%2C%22east%22%3A-86.44695287792969%2C%22south%22%3A33.29383681016042%2C%22north%22%3A33.74835540537816%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10417%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A575278%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
add_data = ZillowScrap(zillow_link, google_link)