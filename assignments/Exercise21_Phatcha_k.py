from tkinter import *

def calculateClickButton(event):
    height = textBoxHeight.get()
    weight = textBoxWeight.get()
    bmi = round(float(weight) / ((float(height)/100)**2), 2)

    if bmi > 30:
        bmi2 = "อ้วนมาก"
    elif bmi >= 25.0 :
        bmi2 = "อ้วน"
    elif bmi >= 23.0:
        bmi2 = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        bmi2 = "น้ำหนักปกติ เหมาะสม"
    else:
        bmi2 = "ผอมเกินไป"

    labelResult.configure(text=bmi)
    labelResult2.configure(text=bmi2,fg="red")

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