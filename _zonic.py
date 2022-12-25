from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def refresh_metadata(chain, contract, from_id, to_id):

    # setup
    driver = webdriver.Chrome()
    url = "https://zonic.app/asset/{}/{}/{}"

    for id in range(from_id, to_id+1):

        # craft item url
        item_url = url.format(chain, contract, id)
        print(item_url)

        # browse item
        driver.get(item_url)

        # wait until refresh button show
        time.sleep(3)

        # click refresh metadata
        element = driver.find_element(By.CSS_SELECTOR, '.controls-area i')
        element.click()
