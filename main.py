import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains



def main():
    # Name of the CSV file
    csv_file = "user_credentials.csv"


    # # Open the CSV file for reading
    # with open(csv_file, mode='r') as file:
    #     reader = csv.DictReader(file)
        
    #     # Read the first row from the CSV
    #     first_row = next(reader)
    
    # # Access and print the first row's data
    # email = first_row['Email']
    # password = first_row['Password']
    # print(f"First row - Email: {email}, Password: {password}")
    # Initialize empty lists to store email and password
    emails = []
    passwords = []

    # Open the CSV file for reading
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Read and store data from the CSV
        for row in reader:
            emails.append(row['Email'])
            passwords.append(row['Password'])

    # Now, you can work with the email and password lists
    for email, password in zip(emails, passwords):
        print(f"Email: {email}, Password: {password}")
    
        # Define the proxy server URL
        proxy_server = "http://34.82.224.175:33333"

        # Set up Chrome options with the proxy server
        chrome_options = webdriver.ChromeOptions()
        # chrome_options = add_extension()
        chrome_options.add_argument(f'--proxy-server={proxy_server}')

        # Create the WebDriver instance with the Chrome options
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        print('1')

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
            # print(i)
            # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(i)
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input").send_keys(i)
            time.sleep(2)

        
        for i in password:
            # print(i)
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input").send_keys(i)
            time.sleep(2)
        
        driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]").click()
        time.sleep(10)

        # window_handles[0] is a first window 
        driver.switch_to.window(driver.window_handles[0])
        print("coming back to first to window title = " + driver.title)
        time.sleep(20)

        # click on upload video
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[3]/div[1]/a").click()
        time.sleep(5)

        # Now upload dummy videos
        
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div[1]/a").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/input").send_keys(r'C:\Users\user\Desktop\PROJECTS\Multiple email\demo.mp4')
        
        #add caption
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div").send_keys('CAPTIONS')
        
        #post videos
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button").click()

        # quit driver 
        driver.quit()

if __name__ == '__main__':
    main()
