from tkinter import *

def calculateClickButton(event):
    height = textBoxHeight.get()
    weight = textBoxWeight.get()
    bmi = round(float(weight) / ((float(height)/100)**2), 2)
    
    if bmi < 18.5:
        bmi2 = "อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม"
    elif 18.5 <= bmi < 24.9:
        bmi2 = "อยู่ในเกณฑ์ปกติ"
    elif bmi >= 24.9:
        bmi2 = "น้ำหนักเกิน"

    labelResult.configure(text=bmi)
    labelResult2.configure(text=bmi2)

mainWindow = Tk()
labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(mainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(mainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', calculateClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(mainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
labelResult2 = Label(mainWindow, text="")
labelResult2.grid(row=3, column=1)

mainWindow.mainloop()