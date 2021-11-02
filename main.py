import tkinter as tk

# convert_function gets the number from the user, checks to see which conversion is chosen, and then displays the output.
def convert_function():
    temp = float(e1.get())
    if(var.get()==1):
        # F to C
        temp = ((temp-32)*5)/9

    elif(var.get()==2):
        # C to F
        temp =((temp*9/5)+32)

    l1.configure(text="Result: {}".format(temp))

# key_pressed will run when the "Enter" key is pressed and then it will run the convert function()
def key_pressed(event):
        if(event.char == "\r"):
            convert_function() 

root = tk.Tk()
root.geometry('300x200') # width and height of the window

root.title("Temperature Converter") # Title of the window
root.iconbitmap('temperature_icon.ico') # displays icon

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Entry widget for input from user
e1 = tk.Entry(root)
e1.grid(row=0, column=0, columnspan=2)

var = tk.IntVar()

# Radio button widget (F to C)
r1=tk.Radiobutton(root, text="F to C", variable=var, value=1, bg="#eea698")
r1.grid(row=1, column=0)

# Radio button widget (C to F)
r2=tk.Radiobutton(root, text="C to F", variable=var, value=2, bg="#eea698")
r2.grid(row=1, column=1)

# Button widget ("CONVERT")
b1 = tk.Button(root, text="CONVERT", command=convert_function, bg="#ff0000", fg="#ffffff")
b1.grid(row=2, column=0, columnspan=2)

# Label widget (displays the output)
l1 = tk.Label(root, text="Result: -", bg="#eea698")
l1.grid(row=3, column=0, columnspan=2)

root.bind("<KeyPress>", key_pressed)

root.configure(bg ="#eea698")
root.minsize(width=300, height=200) #restrict minimum size of window
root.maxsize(width=300, height=200) #restrict maximum size of window
root.mainloop()