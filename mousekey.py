import pyautogui 
pyautogui.keyDown('win')
pyautogui.press('s')
pyautogui.keyUp('win')
print("Please Tell me the app Boss")
app = input()
for i in app:
    print(i)
    pyautogui.press(i)

