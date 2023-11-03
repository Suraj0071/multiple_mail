import pyautogui
from time import sleep

# pyautogui.click(1075,1051)
# sleep(2)
# pyautogui.click(998,601)
# pyautogui.hotkey("ctrl","t")
# pyautogui.write("https://www.tiktok.com/en/")
# first import the module 
import webbrowser 
  
# then make a url variable 
url = "https://www.tiktok.com/en/"
  
# then call the default open method described above 
webbrowser.open(url)

sleep(2)


pyautogui.hotkey("enter")
sleep(10)
pyautogui.click(1715,180)
sleep(10)
pyautogui.click(1056,887)
sleep(8)
pyautogui.click(933,548)
sleep(8)

import csv


# Specify the path to your CSV file
csv_file = 'csv_credentials.csv'

# Initialize empty variables for email and password
em = None
ps = None

# Open the CSV file for reading
with open(csv_file, mode='r', newline='') as file:

    reader = csv.DictReader(file)
    
    # Read the first row from the CSV
    first_row = next(reader, None)
    
    if first_row:
        em = "cojikiw933@qianhost.com"
        ps = "Hello@2413#"

# Check if data was found and print or use it
if em is not None and ps is not None:
    print(f"First Email: {em}, Password: {ps}")
else:
    print("No data found in the CSV.")

pyautogui.click(1019,223)
# Select the text in the text box (you might need to adjust the number of times Ctrl+A is pressed)
pyautogui.hotkey('ctrl', 'a')

# Press the "Delete" key to clear the text
pyautogui.press('delete')
sleep(5)


pyautogui.write(em)
sleep(5)
pyautogui.click(886,277)
sleep(5)
pyautogui.write(ps)
sleep(5)
pyautogui.click(892,329)

