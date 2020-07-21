import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

# start time
execution_start_time = time.time()

# change these parameters
promotional_message = "Hi this is Jay, testing whatsapp bulk sms sender hack. If you like it give a *thumbs up!*"
filename = "contacts_sheet.csv"
defaulter_contact_name = "Ren"
country_code = "91"

# constants
partial_text = "https://api.whatsapp.com/send?phone=" + country_code
contacts = []

# read the csv file to get all the contacts
with open(filename, 'r') as contacts_file:
    contacts = contacts_file.read().split("\n")
    

# start script
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then press Enter")
input()
print("Logged In")

# search defaulter
inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(1)
input_box_search.send_keys(defaulter_contact_name)
time.sleep(1)

for _contact in contacts:
    # find the defaulter and open his/her chat
    defaulter_contact_select = driver.find_element_by_xpath("//span[@title='"+defaulter_contact_name+"']")
    defaulter_contact_select.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(1)

    # send api.whatsapp.com link to the defaulter
    whatsapp_api_text = partial_text + _contact
    input_box.send_keys(whatsapp_api_text + Keys.ENTER)
    time.sleep(1)
    
    # click on whatsapp link
    sent_text = driver.find_element_by_xpath("//a[@title='"+whatsapp_api_text+"']")
    sent_text.click()
    time.sleep(1)
    
    # check if the contact is whatsapp number or not
    try:
        ok_button_inp_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
        ok_button = driver.find_element_by_xpath(ok_button_inp_xpath)
        ok_button.click()
        print("Unable to send message to " + _contact)
        time.sleep(1)
        continue
    except:
        # exception means that the contact is whatsapp number
        # find the input text and send the promotional message
        promotional_message_inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        promotional_message_input_box = driver.find_element_by_xpath(promotional_message_inp_xpath)
        promotional_message_input_box.send_keys(promotional_message + Keys.ENTER)
        time.sleep(1)
        

end = time.time()
print("Total execution time: {end - start}")

# wait for all messages to get delivered (10 seconds)
time.sleep(10)

# exit the selenium driver
driver.quit()
