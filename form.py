from tkinter import *
root = Tk()
def getvals():
    print("Submitting form...")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")
    with open("records.txt", 'a') as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")

root.geometry("400x400")
#Heading
Label(root, text = "Welcome to Sandip's Travel", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text-Forms
name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
gender = Label(root, text = "Gender")
paymentmode = Label(root, text = "Payment Mode")

#Pack text
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentmode.grid(row=4, column=2)

#Tkinter Variable for entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#Entries
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

#Packing Entries
nameentry.grid(row=1, column = 3)
phoneentry.grid(row=2, column = 3)
genderentry.grid(row=3, column = 3)
paymentmodeentry.grid(row=4, column = 3)


#Checkbox
foodservice = Checkbutton(text="Want to pre-book meals?", variable = foodservicevalue)
foodservice.grid(row=5, column=3)


#Button, packing it, and assigning command
Button(text="Let's Go!!", command=getvals).grid(row=7,column=3)
root.mainloop()