from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Set the path of Chromedriver to be used with Selenium
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')


def fetch_classes(url):

    '''
    Given a paper.nu url to a class schedule, fetch_classes() extracts the class codes and puts them into a list 
    '''

    # load webpage
    driver.get(url)

    # Close the pop-up & wait a few seconds for webpage elements
    driver.find_element_by_xpath("//*[@id='headlessui-dialog-panel-:r3:']/div[2]/button[1]").click()

    #-----------------------------------------------------------------------------------------------
    # Credit to code in this section: "How to Fix Your Computer" (YouTube)
    # Source: https://www.youtube.com/watch?v=5M0n90mLKD8 (0:43)
    delay = 3
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,
    'IdOfMyElement')))
    except TimeoutException:
        pass
    #-----------------------------------------------------------------------------------------------

    # Create a BeautifulSoup object & quit the Chromedriver
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Find all the "class block" elements
    class_names = soup.find_all("p", class_="text-sm font-semibold m-0 p-0 text-black dark:text-white")

    # Make a list to store strings of class names extracted from BeautifulSoup object
    class_schedule = []
    for Class in class_names:
        # Extract just the string, not whole "class block" element
        name = Class.string
        # Avoid duplicates in the list
        if(name not in class_schedule):
            class_schedule.append(name)
            
    return class_schedule


    







