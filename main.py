import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

# start time
execution_start_time = time.time()

# change these parameters
promotional_message = "Hi this is Jay, testing whatsapp bulk sms sender hack 2.0. If you like it give a *thumbs up!*"
filename = "contacts_sheet.csv"

# constants
partial_execution_script = """
var elementExists = document.getElementById("custom-link-identifier");
if (elementExists != null) {
    elementExists.remove()
}
var a = document.createElement("a");
var text = document.createTextNode("link")
a.appendChild(text);
a.setAttribute("href",'%s');
a.setAttribute("id",'custom-link-identifier');
document.getElementById("main").appendChild(a);
document.getElementById("custom-link-identifier").click();
"""

partial_whatsapp_api = "https://api.whatsapp.com/send?phone="
contacts = []

# read the csv file to get all the contacts
with open(filename, 'r') as contacts_file:
    contacts = contacts_file.read().split("\n")
    

# start script
driver = webdriver.Chrome("__PATH__")
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then press Enter")
input()
print("Logged In")

# find the first contact in chat
first_contact_in_chat = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
first_contact_in_chat.click()
time.sleep(1)

# iterate through each message and send message
for _contact in contacts:
    whatsapp_api_text = partial_whatsapp_api + _contact
    execution_script = partial_execution_script %(whatsapp_api_text)
    driver.execute_script(execution_script)
    time.sleep(1)
    
    try:
        # check if the contact is whatsapp number or not
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
        

print("Total execution time: {0:.2f}".format(time.time() - execution_start_time))

# wait for all messages to get delivered (10 seconds)
time.sleep(10)

# exit the selenium driver
driver.quit()
