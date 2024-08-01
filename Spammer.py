import pyautogui, time
txt=input("Enter the text u wanna spam: ")
sc=int(input('Enter spam count: '))
time.sleep(2)
for i in range(1,sc):
    pyautogui.typewrite(txt)
    pyautogui.press("enter")
    if(i==int(sc/2)):
        print("half way done")
    time.sleep(0.5)
print("Done")

