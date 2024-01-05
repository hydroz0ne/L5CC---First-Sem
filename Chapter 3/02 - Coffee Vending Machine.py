#Exercise 2 - Coffee Vending Machine
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x470")
root.resizable(False, False)
root.configure(bg="#CF9F6E")
root.title("Coffee Vending Machine")

#Function that handles order confirmation
def orderinput():
    coffee = coffeevar.get()
    milk = milkvar.get()
    sugar = sugarlevelvar.get()
    
    #Creates order message based on user input
    order = f"You have ordered a {coffee} with {'milk' if milk else 'no milk'} and with a {sugar} sugar level. Enjoy your coffee!"
    #Shows the order confirmation using a messagebox
    messagebox.showinfo("Order Confirmation", order)

#Loads and displays an image using Pillow (PIL)
photo = Image.open("latte.jpg")
photo = photo.resize((300, 200))
photo = ImageTk.PhotoImage(photo)
photo_label = Label(root, image=photo)
photo_label.pack(padx=10, pady=10)

title = Label(text="Coffee Vending Machine", font=(15), pady=5, bg="#CF9F6E")
title.pack()

#Coffee type selection
coffeelabel = Label(root, text="Select Coffee Type:", bg="#CF9F6E")
coffeelabel.pack()
coffeevar = StringVar()
coffeechoices = ["cappuccino", "espresso", "latte"]
coffeevar.set(coffeechoices[0])
coffeemenu = OptionMenu(root, coffeevar, *coffeechoices)
coffeemenu.pack()

#Milk option checkbox
milkvar = BooleanVar()
milkcheckbox = Checkbutton(root, text="Add Milk", variable=milkvar, pady=10, bg="#CF9F6E")
milkcheckbox.pack()

#Sugar level selection
sugarlabel = Label(root, text="Select Sugar Level:", bg="#CF9F6E")
sugarlabel.pack()
sugarlevelvar = StringVar()
sugarlevelchoices = ["zero", "low", "normal"]
sugarlevelvar.set(sugarlevelchoices[0])
sugarlevelmenu = OptionMenu(root, sugarlevelvar, *sugarlevelchoices)
sugarlevelmenu.pack()

#Places the order button
button = Button(root, text="Place Order", command=orderinput)
button.pack(pady=10)

root.mainloop()