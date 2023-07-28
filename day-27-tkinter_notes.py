from tkinter import *

screen = Tk()
screen.title('this be a title')
screen.minsize(width=500, height=500)


# labels
label = Label(text='some text', font=('arial', 24, 'bold'))
label.pack(expand=True) # actually puts the label on the screen


# entry
input = Entry(width=10)
input.pack()
input.get()


# buttons
def button_clicked():
    # if label['text'] == 'button clicked':
    #     label['text'] = 'button unclicked'
    # else:
    #     label['text'] = 'button clicked'

    label['text'] = input.get()
button = Button(text='click me', command=button_clicked)
button.pack(expand=True)

# Textbox
text = Text(height=5,width=30)
text.focus() # puts cursor in textbox by default
text.insert(END, 'some sample text')
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkedbutton
def checkbutton_used():
    # prints 1 if on otherwise prints 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apples', 'Oranges', 'Bananas', 'Pineapples']

for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind('<<ListboxSelect>>',listbox_used) # prints selected item
listbox.pack()

screen.mainloop()
