# whatsapp_bulk_sms_sender [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
Python script to read contact information from csv and send WhatsApp messages to the users


## Installation
Install python packages:
```bash
pip3 install -r requirements.txt
```

Download [Chrome Webdriver](https://chromedriver.chromium.org/downloads) and paste the file into the root folder of the project. Download the same version of Webdriver as your Chrome browser's version.


### Things to take care of while running this
1. Update promotional message as per your needs.
2. Update the contacts list in csv with country code. (ex. 91 is the country code for India)
3. Replace "\_\_PATH\_\_" with the path of Chrome Webdriver that you downloaded earlier.


## Usage
```bash
python3 main.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.