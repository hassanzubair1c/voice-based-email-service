from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Base Url for testing
APP_BASE_URL = "http://127.0.0.1:8000/"

# driver initialization
options = Options()
options.add_argument('--headless')
options.page_load_strategy = 'normal'
web_driver = webdriver.Chrome(executable_path="./88/chromedriver", options=options)


def signup_test():
    # Go to SignUp Page
    driver.get(APP_BASE_URL)
    # get all fields
    username = driver.find_elements(By.ID, 'username')
    first_name = driver.find_elements(By.ID, 'first_name')
    last_name = driver.find_elements(By.ID, 'last_name')
    email = driver.find_elements(By.ID, 'email')
    password1 = driver.find_elements(By.ID, 'password1')
    password2 = driver.find_elements(By.ID, 'password2')

    username[0].send_keys('hbot')
    first_name[0].send_keys('hbot')
    last_name[0].send_keys('hbot')
    email[0].send_keys('hbot@gmail.com')
    password1[0].send_keys('Admin123@')
    password2[0].send_keys('Admin123')

    # Click signup button
    signup_button = driver.find_elements(By.ID, 'submit')
    signup_button[0].submit()

    driver.implicitly_wait(10)

    current_url = driver.current_url

    self.assertEqual(current_url, 'http://127.0.0.1:8000/inbox/')


def login_test(self):
    driver.get(APP_BASE_URL)

    # Go to Login Page
    login_button = driver.find_elements(By.ID, 'signin')
    login_button[0].submit()

    # get fields
    email_input = driver.find_elements(By.ID, 'username')
    password_input = driver.find_elements(By.ID, 'password')

    # Valid Inputs
    email_input[0].send_keys('xbot')
    password_input[0].send_keys('Admin123@')

    # Click login button
    login_button = driver.find_elements(By.ID, 'submit')
    login_button[0].submit()

    driver.implicitly_wait(10)
    current_url = driver.current_url
    self.assertEqual(current_url, 'http://127.0.0.1:8000/inbox/')


def compose_email_test(self):
    # Login
    driver.get(APP_BASE_URL)
    login_button = driver.find_elements(By.ID, 'signin')
    login_button[0].submit()
    email_input = driver.find_elements(By.ID, 'username')
    password_input = driver.find_elements(By.ID, 'password')
    email_input[0].send_keys('xbot')
    password_input[0].send_keys('Admin123@')
    login_button = driver.find_elements(By.ID, 'submit')
    login_button[0].submit()

    # Compose Email
    driver.find_elements(By.TAG_NAME, 'a')[0].click()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    self.assertEqual(current_url, 'http://127.0.0.1:8000/compose/')


def inbox_test(self):
    # Login
    driver.get(APP_BASE_URL)
    login_button = driver.find_elements(By.ID, 'signin')
    login_button[0].submit()
    email_input = driver.find_elements(By.ID, 'username')
    password_input = driver.find_elements(By.ID, 'password')
    email_input[0].send_keys('xbot')
    password_input[0].send_keys('Admin123@')
    login_button = driver.find_elements(By.ID, 'submit')
    login_button[0].submit()

    # Inbox Email
    driver.find_elements(By.TAG_NAME, 'a')[1].click()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    self.assertEqual(current_url, 'http://127.0.0.1:8000/inbox/')


def sent_email_test(self):
    # Login
    driver.get(APP_BASE_URL)
    login_button = driver.find_elements(By.ID, 'signin')
    login_button[0].submit()
    email_input = driver.find_elements(By.ID, 'username')
    password_input = driver.find_elements(By.ID, 'password')
    email_input[0].send_keys('xbot')
    password_input[0].send_keys('Admin123@')
    login_button = driver.find_elements(By.ID, 'submit')
    login_button[0].submit()

    # Sent Email
    driver.find_elements(By.TAG_NAME, 'a')[2].click()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    self.assertEqual(current_url, 'http://127.0.0.1:8000/sent/')
