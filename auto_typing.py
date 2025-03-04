import pyautogui
import time

# Wait for a few seconds to allow switching to the desired input field
time.sleep(5)

# The word to type
word = "Hello"

# Type the word
pyautogui.write(word)

# Press Enter
pyautogui.press("enter")
