from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=100,pady=200)

#Labels
label = Label(text="is equal to")
label.grid(column=1,row=3)

#Entry
entry = Entry(width=30)
#Add some text to begin with
# entry.insert(END, string="insert Number")
#Gets text in entry
entry.grid(column=4,row=2)

#Labels for Miles
label2 = Label(text="Miles")
label2.grid(column=5,row=2)




#Labels for Km
label_km = Label(text="Km")
label_km.grid(column=5,row=3)


#button for convertdef action():
def action():
    miles_value =entry.get()

    if miles_value:
        km_value = float(miles_value)*1.6
        km_value=round(km_value,2)

    else:
        km_value=0    
    label3.config(text=km_value)

#calls action() when pressed
button = Button(text="Convert", command=action)
button.grid(column=4,row=4)

#Labels for result
label3 = Label(text="")
label3.grid(column=4,row=3)


window.mainloop()