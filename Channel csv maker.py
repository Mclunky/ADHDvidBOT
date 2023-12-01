import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# prompt user for the YouTube channel link
channel_link = input("Enter the YouTube channel link: ")

# create a new Chrome browser instance
driver = webdriver.Chrome(options=options)

# navigate to the YouTube channel link
driver.get(channel_link)
driver.set_window_size(1273, 1266)# wait for the page to load
time.sleep(8)

# find the link to the "videos" section and click on it
videos_link = driver.find_element(By.XPATH, value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]/div")
videos_link.click()

# wait for the page to load
time.sleep(2)

# find all the video links on the page
WebElement = driver.find_elements(By.XPATH, value="//*[@id=\"thumbnail\"]")


#keep stalled so can scroll to however many videos you want
input("Press any key to continue after scrolling to the right amount of videos...")

y=0
# iterate through the list of video links and copy each url
URL_list=[]
title_list=[]
for link in WebElement:
    url = link.get_attribute('href')
#    driver.execute_script("window.open('{}', '_blank')".format(url))
    if url == None:
        print("skip")
    
    else:
        new_url=str(url)
        URL_list.append(new_url)
        y = y + 1
        print(y)
        title_list.append("Family Guy Clip Scene " + str(y))


combineList=[(URL_list), (title_list)]
newCombList=zip(*combineList)        



def create_csv(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # Writing header
        writer.writerow(["URL", "Title"])
        # Writing data
        for item in data:
            writer.writerow(item)


# Specify the filename for the CSV file
csv_filename ="C:/Users/Ohio/Documents/Shorts Scraper/my_file.csv"

# Call the function to create the CSV file
create_csv(csv_filename, newCombList)

     

# close the browser
driver.quit()



