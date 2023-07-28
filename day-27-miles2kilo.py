from tkinter import Tk, Label, Entry, Button

screen = Tk()
screen.title('Mi-Km')
screen.minsize(width=200, height=200)
screen.maxsize(width=200, height=200)
screen.config(padx=10, pady=10)

mile_label = Label(text='Miles')
mile_label.grid(row=0, column=2)

mile_entry = Entry(width=15)
mile_entry.grid(row=0, column=1)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

kilometer = Label(text='0')
kilometer.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

def calculate():
    kilometer['text'] = float(mile_entry.get()) * 1.609
calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)

screen.mainloop()