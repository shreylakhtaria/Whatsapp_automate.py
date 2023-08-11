
import time
import pyautogui
import random

# Function to open WhatsApp and send a message
def send_whatsapp_message(contact_name, message, count):
    
    
    # Open WhatsApp Desktop
    pyautogui.hotkey("win", "s")
    time.sleep(0.5)
    pyautogui.write("WhatsApp")
    pyautogui.press("enter")
    time.sleep(1)  # Adjust the delay as needed for WhatsApp to open

    # Search for the contact
    pyautogui.hotkey("ctrl", "f")
    pyautogui.write(contact_name)
    time.sleep(1)  # Wait for search results

    #Press down arrow key to select the contact
    pyautogui.press("down")
    
    # Open the chat of the specified contact
    pyautogui.press("enter")
    
    time.sleep(10)  # Wait for chat to open
    # Type and send the message
    for i in range(count):
        # message 
        pyautogui.write(message)        
        pyautogui.press("enter")
        time.sleep(0.3)   # Adjust the delay as needed to send the message
        
# Get user input
contact_name = input("Enter the contact name or number: ")
message = input("Enter the message: ")
count = int(input("Enter message count: "))

# Call the function to send the message
send_whatsapp_message(contact_name, message, count)
