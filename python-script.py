import dependency_module
import logging
import time
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
#chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome("driver/chromedriver", chrome_options=chrome_options)

#time.sleep(30)

driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

filePath = "logs/test-" + time.strftime("%Y-%m-%d") + ".log"
logging.basicConfig(level=logging.INFO, format = '%(asctime)s [%(levelname)s]-%(message)s',
                    filename = filePath)
logger = logging.getLogger();


def save_file():
    with open('data/myfile.txt', 'a+', encoding='utf-8') as f:
        f.write("This is my file")
        current_time = datetime.now().strftime("%H:%M:%S")
        f.write("Current time : {}".format(current_time))
        f.write("\n")
        driver.get('https://timesofindia.indiatimes.com/home/environment/pollution/mumbai-gets-lions-share-of-govts-pollution-fund/articleshow/74585292.cms')
        page_source = driver.page_source
        f.write("PAGE : {}".format(page_source))
        

def main():
    print('this is main')
    dependency_module.func("Print my string")
    print("module printed successfully...")
    logger.info("This is logger")
    save_file()
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    main()


