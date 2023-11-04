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
# Login Button
button_image_path = 'login.png'

# Set a confidence level for image recognition (adjust as needed)
confidence = 0.8

# Try to locate the button image on the screen
button_location = pyautogui.locateOnScreen(button_image_path, confidence=confidence)

if button_location:
    # Get the center coordinates of the located button
    x, y = pyautogui.center(button_location)

    # Move the mouse to the center of the button and click
    pyautogui.moveTo(x, y)
    pyautogui.click()
else:
    print("Button image not found on the screen.")
# Signup button
pyautogui.click(1056,887)   
sleep(8)
# Continue with facebook
button_image_path = 'facebook.png'

# Set a confidence level for image recognition (adjust as needed)
confidence = 0.8

# Try to locate the button image on the screen
button_location = pyautogui.locateOnScreen(button_image_path, confidence=confidence)

if button_location:
    # Get the center coordinates of the located button
    x, y = pyautogui.center(button_location)

    # Move the mouse to the center of the button and click
    pyautogui.moveTo(x, y)
    pyautogui.click()
else:
    print("Button image not found on the screen.")

facebook_popup_image = 'path_to_facebook_popup_image.png'  # Replace with the actual image path
if pyautogui.locateOnScreen(facebook_popup_image):
    # Perform the Facebook login steps here
    print("Facebook popup found, proceeding with Facebook login.")
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
    # Add your code to log in with Facebook here

    # You can use the same approach to check for other elements or popups on the screen.
else:
    print("Facebook popup not found. Logging in with another method.")
import csv



# Login successful
pyautogui.click(1644,159)
sleep(20)
pyautogui.click(967,758)
