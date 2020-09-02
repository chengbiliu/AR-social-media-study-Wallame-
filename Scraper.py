from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib, time
import csv, io

def scrape_url(url):
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Chrome()
    driver.get(url)
    i=0
    # Get scroll height
    lastHeight = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Calculate new scroll height and compare with last scroll height
        # driver.execute_script("return document.body.scrollHeight")
        # time.sleep(10)

        # lastHeight = driver.execute_script("return document.body.scrollHeight")
        # top = driver.execute_script("return document.body.scrollTop")
        # window = driver.execute_script('return window.innerHeight')
        # if lastHeight == top + window:
        #     break
        # else:
        #     print ("ohoh")

        try:
            WebDriverWait(driver, 1000).until(EC.invisibility_of_element_located((By.ID, "infscr-loading")))

        except TimeoutError:
            break
        lastHeight = driver.execute_script("return document.body.scrollHeight")
        print(lastHeight)
        if lastHeight > 170000:
            break
        # newHeight = driver.execute_script("return document.body.scrollHeight")
        # if newHeight == lastHeight:
        #     break
        # lastHeight = newHeight

    walls = driver.find_elements_by_class_name('wall')
    for wall in walls:
        wallid = wall.get_attribute('data-item-id')
        print (wallid)
        if wallid is None:
            continue
        location = wall.get_attribute('data-location')
        datetime = wall.find_element_by_class_name(
            'footer').find_element_by_tag_name(
            'time').get_attribute('datetime')
        user = wall.find_element_by_class_name(
            'title-wrapper').find_element_by_class_name('nick').text
        images = "http://api.wallame.com/1/fullWall/{!s}".format(wallid)

        with io.open('ScrapedData1.csv', 'a', newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([wallid, user, location, datetime, images])
        urllib.request.urlretrieve(images, "C:/Users/Chengbi/OneDrive - George Mason University/Research/WebScraper/images/{!s}.png".format(wallid))
        # urllib.request.urlretrieve(images,"C:/Users/golfbrother/OneDrive - George Mason University/Research/WebScraper/images/{!s}.png".format(wallid))
scrape_url("http://walla.me")


    
