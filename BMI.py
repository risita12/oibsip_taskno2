from future.moves import tkinter
from tkinter import Tk, Button, Entry, Label, messagebox


def BMI_Calc(wt, ht):
    ht = ht/100
    BMI = (wt / (ht**2))
    return BMI


def display():
    try:
       ht = float(h_entry.get())
       wt = float(w_entry.get())
       BMI = BMI_Calc(wt, ht)
       ans_entry.config(state='normal')
       ans_entry.delete(0, 'end')
       ans_label.grid(row=2, column=0, padx=10 , pady=10, sticky='ew')
       ans_entry.grid(row=2, column=1, padx= 10, pady=10) 
       ans_entry.insert(0, round(BMI, 2))  
       ans_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror('Error!', 'Please enter the values in numbers')


font = ("Consolas", 20, 'bold')
bg = '#fc8eac'
bg2 = '#fc8eac'
fg = 'black'
 
root = Tk()
root.title('BMI Calculator')
root.config(background=bg)
w_label = Label(root, text= 'ENTER YOUR WEIGHT HERE (in kgs)', 
                font=font , bg = bg, fg=fg)
w_entry = Entry(root, width = 20, font= font, bg = bg2, fg=fg)
h_label = Label(root, text= ' ENTER YOUR HEIGHT HERE (in metres )', 
                font=font, bg = bg, fg=fg)
h_entry = Entry(root, width= 20, font=font, bg=bg2, fg=fg)
calc_button = Button(root, text='Calculate', font=font, bg = 'pink', fg=fg, command=display)
ans_label = Label(root, text= ' BMI', font = font, bg=bg, fg=fg, anchor='w')
ans_entry = Entry(root, width= 20, font=font, readonlybackground=bg2, fg=fg )
ans_entry.config(state='readonly')


h_entry.grid(row=1, column=1, padx=10,pady=10)
w_label.grid(row=0, column=0, padx=10, pady=10)
w_entry.grid(row=0, column=1, padx=10, pady=10)
h_label.grid(row=1, column=0, padx=10, pady=10)
calc_button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=10 , pady=10)

root.mainloop()

