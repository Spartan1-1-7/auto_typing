import pyautogui
import time

# to take inputs for the script
print("How many times do the text need to be send: ")
itter=int(input())

print("\nwhat is the text needed to be send: ")
word=str(input())


# Wait for a few seconds to allow switching to the desired input field
time.sleep(5)

# The word to type
# word = "Hello"

# looping to get desired no of outputs
for i in range(0,itter): 
# Type the word
    pyautogui.write(word)

# Press Enter
    pyautogui.press("enter")
