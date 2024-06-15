import selenium
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# contacts list
with open("contacts.txt", "r") as f:
    contacts_string = f.read()

contacts_list = contacts_string.split("\n")

# what message you want to send to everyone:
message = "automated message test"

LINK = "https://web.whatsapp.com/"

# setting up the driver and getting the website
driver = Safari()
driver.get(LINK)
wait = WebDriverWait(driver, 100)


# the search bar we will use to find the contacts
search_x_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
search_bar = wait.until(EC.presence_of_element_located((By.XPATH, search_x_path)))

# going through each contact and sending the message
for contact_name in contacts_list:
    target = '"' + contact_name + '"'
    search_text = contact_name  # same as target but without the inside quotes

    # searching for the chat so that we can click on it
    search_bar.click()
    search_bar.send_keys(search_text)

    # clicking on the chat
    x_arg = "//span[contains(@title, " + target + ")]"
    target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    target.click()

    type_message_box_x_path = (
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    )

    type_message_box = wait.until(
        EC.presence_of_element_located((By.XPATH, type_message_box_x_path))
    )
    type_message_box.click()
    type_message_box.send_keys(message)
    type_message_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # clearing the search bar
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH, search_x_path)))
    search_bar.click()
    time.sleep(2)
    print("clcked")
    for i in range(len(contact_name)):
        search_bar.send_keys(Keys.DELETE)
    print("done")

driver.quit()
