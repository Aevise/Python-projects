from selenium import webdriver
import os
import time

import selenium

FOLDER = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER = FOLDER + "/chromedriver.exe"
COOKIE_WEB = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)


#driver.get("https://www.python.org/")

#dates = driver.find_elements(by="xpath", value ='/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/*/time') # * - so that thing in between does not matter
#event_name = driver.find_elements(by="xpath", value = '/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/*/a')

#dict comprehesion with two lists
#upcoming_events = {event_name[i].text:dates[i].text for i in range(len(dates))}
# upcoming_events = dict(zip(list1, list2))

#print(upcoming_events)

#price = driver.find_element(by="class name", value="a-price-whole")
#print(price.text)

#driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")
#wikipedia_articles = driver.find_element(by="xpath", value="/html/body/div[3]/div[3]/div[5]/div[1]/div/div[1]/div[1]/p/a[4]")
#wikipedia_search = driver.find_element(by="xpath", value="/html/body/div[4]/div[1]/div[2]/div/div/form/div/input[1]")
#print(wikipedia_articles.text)
#wikipedia_articles.click()
#wikipedia_search.send_keys("Python", webdriver.common.keys.Keys.ENTER)

def get_money()->int:
    """Get your current money

    Returns:
        int: money
    """
    return int(driver.find_element(by="id", value="money").text.replace(",","_"))

def get_items_value_and_names(items:list)->dict:
    """get prices and names of items from cookie site

    Args:
        items (list): items from a website

    Returns:
        dict: name:price
    """
    items_list= [item.text for item in items]
    items_text = items_list[0].split("\n")
    prices = []
    names = []
    for item in items_text:
        find_value_index = item.find("- ")
        find_name_index = item.find(" -")
        if find_value_index != -1:
            prices.append(int(item[find_value_index+2:].replace(",", "_")))
        if find_name_index != -1:
            names.append("buy"+item[:find_name_index])
    #items = {names[i]:prices[i] for i in range(len(names))}
    items = dict(zip(names, prices))
    return items

def shopping_spree(prices:dict)->None:
    """Buys items from a shop

    Args:
        prices (dict): dictionary containing name:price
    """
    for item, price in reversed(prices.items()):
        money = get_money()
        if int(price) < money:
            time.sleep(0.01)
            try:
                driver.find_element(by="id", value=item).click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue

driver.get(COOKIE_WEB)
cookie = driver.find_element(by="id", value="cookie")
store = driver.find_elements(by="id", value ="store")
assortment = get_items_value_and_names(store)
timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        print("timeout")
        shopping_spree(assortment)
        timeout = time.time() + 5

#driver.close() close one tab
#driver.quit() #close browser
