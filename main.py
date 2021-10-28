import tkinter as tk

def convert_function():
    temp = float(e1.get())

    if(var.get()==1):
        # F to C
        temp = ((temp-32)*5)/9

    elif(var.get()==2):
        # C to F
        temp =((temp*9/5)+32)

    l1.configure(text="Result: {}".format(temp))

root = tk.Tk()

root.title("Temperature Converter")

e1 = tk.Entry(root)
e1.grid(row=0, column=0, columnspan=2)

var = tk.IntVar()

r1=tk.Radiobutton(root, text="F to C", variable=var, value=1)
r1.grid(row=1, column=0)

r2=tk.Radiobutton(root, text="C to F", variable=var, value=2)
r2.grid(row=1, column=1)

b1 = tk.Button(root, text="CONVERT", command=convert_function, bg="#ff0000", fg="#ffffff")
b1.grid(row=2, column=0, columnspan=2)

l1 = tk.Label(root, text="Result: -")
l1.grid(row=3, column=0, columnspan=2)

root.mainloop()