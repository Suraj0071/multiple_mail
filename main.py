# import time
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from mailtm import Email

# def listener(message):
#     print("\nSubject: " + message['subject'])
#     return("Content: " + message['text'] if message['text'] else message['html'])

# def main():
#     # Get a random email address
#     email = Email().register()
#     print("\nEmail Address: " + str(email.address))

#     # Set up ChromeOptions with a proxy server
#     proxy_server = "http://34.82.224.175:33333"
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f'--proxy-server={proxy_server}')

#     # Create the WebDriver instance with the Chrome options
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
#     try:
#         # Visit TikTok homepage
#         driver.get("https://www.tiktok.com/en/")
#         print(driver.title)
#         time.sleep(7)

#         # Interact with TikTok's registration page
#         search_bar = driver.find_element(By.CLASS_NAME, "e1b6crsh1")
#         search_bar.click()
#         print("Signup")

#         time.sleep(5)
#         search_bar = driver.find_element(By.CLASS_NAME, "e1cgu1qo0")
#         search_bar.click()
#         print("Click email")
#         time.sleep(3)
#         search_bar = driver.find_element(By.CLASS_NAME, "ep888o80")
#         search_bar.click()
#         print("Email page")

#         # Fill in the birthdate
#         time.sleep(2)
#         search_bar = driver.find_element(By.CLASS_NAME, "e1phcp2x1")
#         search_bar.click()
#         print("Months")
#         time.sleep(2)

#         search_bar = driver.find_element(By.CLASS_NAME, "e1phcp2x5")
#         search_bar.click()
#         print("Month")
#         time.sleep(2)

#         search_bar = driver.find_element(By.CLASS_NAME, "tiktok-13o6q3w-DivSelectLabel")
#         search_bar.click()
#         print("Days")
#         time.sleep(2)

#         search_bar = driver.find_element(By.ID, "Day-options-item-1")
#         search_bar.click()
#         print("Day")
#         time.sleep(2)

#         search_bar = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div[3]/div[1]')
#         search_bar.click()
#         print("Years")
#         time.sleep(2)

#         search_bar = driver.find_element(By.ID, "Year-options-item-29")
#         search_bar.click()
#         print("Year")
#         time.sleep(2)

#         # Enter email and password
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[5]/div/input").send_keys(email.address)
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div/1/div[1]/div[2]/form/div[6]/div/input").send_keys('Testing123@')
#         print('Send code 1')
#         time.sleep(5)
#         print('Send code 2')

#         # Wait for an email with a code
#         print("\nWaiting for new emails...")
#         time.sleep(10)
#         print('Timeout')
#         while email.start(listener) is None:
#             print('Waiting')
#         message = email.start(listener)

#         # Use regex to find a 6-digit number in the content
#         six_digit_code = re.findall(r'\b\d{6}\b', message['text'])

#         # Enter the code and submit
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[7]/div/div/input").send_keys(six_digit_code)
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[8]/div/label/i/svg").click()
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/button").click()
#         print("Signing in...")

#         # Now, log in to TikTok
#         driver.get("https://www.tiktok.com")
#         driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/button").click()
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/a[2]").click()
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/a").click()

#         # Fill in the email and password fields
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(email)
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input").send_keys('Testing123@')
#         driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/button").click()
#         print("Logging in...")

#         # Now, upload dummy videos
#         driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div[1]/a").click()
#         time.sleep(1)
        
#         # Upload video and add a caption
#         # driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/input").send_keys('C:\Users\user\Desktop\PROJECTS\Multiple email\demo.mp4')
#         driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div").send_keys('CAPTIONS')
        
#         # Post videos
#         driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button").click()
#     finally:
#         # Quit the driver, even in case of exceptions
#         driver.quit()

# if __name__ == '__main__':
#     main()
import csv
import random,re
import string
from mailtm import Email

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


from selenium import webdriver
import time, re
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
    # Use regex to find a 6-digit number in the content
    six_digit_numbers = re.findall(r'\b\d{6}\b', message['text'])
    
    if six_digit_numbers:
        print("Found 6-digit number(s): " + ", ".join(six_digit_numbers))
    else:
        print("No 6-digit numbers found in the content")
    return six_digit_numbers


def main():
    # Name of the CSV file
    csv_file = "user_credentials.csv"


    # Open the CSV file for reading
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Read the first row from the CSV
        first_row = next(reader)
    
    # Access and print the first row's data
    email = first_row['Email']
    password = first_row['Password']
    print(f"First row - Email: {email}, Password: {password}")

    # Get Domains
    # test = Email()

    # Make new email address
    # email=test.register()
    # print("\nEmail Adress: " + str(test.address))

    # test.start(listener)

    
    # Define the proxy server URL
    proxy_server = "http://34.82.224.175:33333"

    # Set up Chrome options with the proxy server
    chrome_options = webdriver.ChromeOptions()
    # chrome_options = add_extension()
    chrome_options.add_argument(f'--proxy-server={proxy_server}')

    # Create the WebDriver instance with the Chrome options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    print('1')
    # Create EdgeOptions
    # Set up Chrome options for Brave browser
    # brave_options = webdriver.ChromeOptions()

    # Specify the path to the Brave browser executable (replace with your actual path)
    # brave_options.binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

    # If you want to configure proxy settings, add them here:
    # brave_options.add_argument('--proxy-server=http://your-proxy-server')

    # Create the WebDriver instance with ChromeDriverManager and Brave options
    # driver = webdriver.Chrome(ChromeService(ChromeDriverManager().install()), options=brave_options)
    # driver = webdriver.Chrome(executable_path='chromedriver.exe', options=brave_options)
    

    
    
    
    # driver.get("https://www.tiktok.com")
    # time.sleep(5)
    # print(driver.title)
    # time.sleep(1)
    driver.get("https://www.tiktok.com/en/")
    print(driver.title)
    time.sleep(8)

    #testing
    # time.sleep(5)
    search_bar = driver.find_element(By.CLASS_NAME,"e1b6crsh1")
    search_bar.click()
    print("signup")

    time.sleep(5)
    
    # search_bar = driver.find_elements(By.CLASS_NAME,"e1cgu1qo0")
    # print(len(search_bar))
    search_bar = driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div[3]/p")
    
    # search_bar = driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/svg")
    # search_bar = driver.find_element(By.CSS_SELECTOR,"#loginContainer > div > div > div:nth-child(3) > div:nth-child(3) > p")
    
    search_bar.click()
    print("click email")
    
    time.sleep(10)
    # window_handles[1] is a second window 
    driver.switch_to.window(driver.window_handles[1]) 
    
    # prints the title of the second window 
    print("Second window title = " + driver.title)
    
    for i in email:
        print(i)
        # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(i)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input").send_keys(i)
        time.sleep(2)

    
    for i in password:
        print(i)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input").send_keys(i)
        time.sleep(2)
    
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]").click()
    while True:
        pass
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
    
    search_bar = driver.find_element(By.CLASS_NAME,"ep888o80")
    search_bar.click()
    print(" email page")

    time.sleep(2)
    search_bar = driver.find_element(By.CLASS_NAME,"e1phcp2x1")
    search_bar.click()
    print("months")
    # print(driver.current_url)
    time.sleep(2)

    search_bar = driver.find_element(By.CLASS_NAME,"e1phcp2x5")
    search_bar.click()
    print("month")
    time.sleep(2)

    search_bar = driver.find_element(By.CLASS_NAME,"tiktok-13o6q3w-DivSelectLabel")
    search_bar.click()
    print("days")
    time.sleep(2)

    search_bar = driver.find_element(By.ID,"Day-options-item-1")
    search_bar.click()
    print("day")
    time.sleep(2)

    search_bar = driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[2]/form/div[2]/div[3]/div[1]')
    search_bar.click()
    print("years")
    time.sleep(2)

    search_bar = driver.find_element(By.ID,"Year-options-item-29")
    search_bar.click()

    print("year")
    time.sleep(2)

    #enter mail
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[5]/div/input").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[6]/div/input").send_keys('Testing123@')

    #send code
    time.sleep(7)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[7]/div/button'))).click()
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '//button[@data-e2e="send-code-button"]'))).click()
    # send_code=
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[7]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[7]/div/button").click()
    # send_code.click()
    print('send code 1')
    
    print('send code 2')


    # Start listening
    
    print("\nWaiting for new emails...")
    # time.sleep(10)
    # print(test.start(listener),'te')
    # print(type(test.start(listener)),'type')
    # text = test.start(listener)
    # while text is None:
    #     text = test.start(listener)
    #     if text is not None :
    #         exit()
    #     print('waiting')
    # print(test.start(listener), 'OOOO')
    # message=test.start(listener)
    # Use regex to find a 6-digit number in the content
    # six_digit_code = re.findall(r'\b\d{6}\b', message['text'])

    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[7]/div/div/input").send_keys('six_digit_code')
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[8]/div/label/i/svg").click()

    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/button").click()
    print("Signing in...")

    # now login tiktok
    driver.get("https://www.tiktok.com")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/a[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/a").click()
    


    # # Fill in the email and password fields
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input").send_keys('Testing123@')
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div[2]/form/button").click()

    # time.sleep(5)
    
    print("Logging in...")
 
    # Now upload dummy videos
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div[1]/a").click()
    time.sleep(1)

    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/input").send_keys('C:\Users\user\Desktop\PROJECTS\Multiple email\demo.mp4')
    
    #add caption
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div").send_keys('CAPTIONS')
    
    #post videos
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button").click()

    # quit driver 
    driver.quit()

if __name__ == '__main__':
    main()
