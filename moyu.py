import pyautogui, time
while True:
    pyautogui.moveRel(0,-100,duration=1)
    time.sleep(5)
    pyautogui.click()
    pyautogui.moveRel(0,100,duration=1)
    time.sleep(3)
    pyautogui.moveRel(200,0,duration=1)
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveRel(-200,0,duration=1)
    time.sleep(13)
    pyautogui.click()
    time.sleep(4)