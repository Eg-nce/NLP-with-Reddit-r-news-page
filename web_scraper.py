from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def reddit_scrapper():
    chromeOptions = Options()
    chromeOptions.headless = True
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver_path = "/home/ege/Documents/python/chromedriver_linux64/chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path)

    time.sleep(3)
    news_list = []
    browser.get("https://www.reddit.com/r/news/") 
    last_height = browser.execute_script("return document.body.scrollHeight")  
    while True:
        elems = browser.find_elements_by_class_name("_eYtD2XCVieq6emjKBH3m")

        
        time.sleep(3)
        for elem in elems:
             news_list.append(elem.text)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = browser.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height
    

    
    time.sleep(3)



    news_df = pd.DataFrame(data = news_list, columns = ["r/news"] )    
   
    return news_df , news_list


if __name__ == "__main__":
    
    df , a =  reddit_scrapper()
    [print(x) for x in a]
    df.to_csv('/home/ege/selenium/r_news.csv', index=True)

