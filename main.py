from tkinter import *


def add_digit(digit):
    tmp = window_output.get() + str(digit)
    window_output.delete(0, END)
    window_output.insert(0, f'{tmp}')
    

def delete():
    len_str = len(window_output.get())
    window_output.delete(len_str-1, END)
    

def result():
    result = eval(window_output.get())
    window_output.delete(0, END)
    window_output.insert(0, str(result))


# Settings window.
root = Tk()

root['bg'] = '#303030'
root.title('Calculator')

# Grid size.
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)


# Window_output.
window_output = Entry(root, width=16, font=('Arial', 18), justify=RIGHT)
window_output.grid(row=0, column=0, columnspan=3, stick='nswe')

# Create buttons.
btn_1 = Button(root, text='1', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(1))
btn_1.grid(row=1, column=0, padx=3, pady=3, stick='nswe')

btn_2 = Button(root, text='2', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(2))
btn_2.grid(row=1, column=1, padx=3, pady=3, stick='nswe')

btn_3 = Button(root, text='3', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(3))
btn_3.grid(row=1, column=2, padx=3, pady=3, stick='nswe')

btn_4 = Button(root, text='4', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(4))
btn_4.grid(row=2, column=0, padx=3, pady=3, stick='nswe')

btn_5 = Button(root, text='5', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(5))
btn_5.grid(row=2, column=1, padx=3, pady=3, stick='nswe')

btn_6 = Button(root, text='6', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(6))
btn_6.grid(row=2, column=2, padx=3, pady=3, stick='nswe')

btn_7 = Button(root, text='7', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(7))
btn_7.grid(row=3, column=0, padx=3, pady=3, stick='nswe')

btn_8 = Button(root, text='8', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(8))
btn_8.grid(row=3, column=1, padx=3, pady=3, stick='nswe')

btn_9 = Button(root, text='9', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(9))
btn_9.grid(row=3, column=2, padx=3, pady=3, stick='nswe')

btn_0 = Button(root, text='0', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit(0))
btn_0.grid(row=4, column=0, padx=3, pady=3, stick='nswe')

btn_result = Button(root, text='=', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=result)
btn_result.grid(row=4, column=1,columnspan=2, padx=3, pady=3, stick='nswe')

btn_del = Button(root, text='del', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=delete)
btn_del.grid(row=0, column=3, padx=3, pady=3, stick='nswe')

btn_plus = Button(root, text='+', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit('+'))
btn_plus.grid(row=1, column=3, padx=3, pady=3, stick='nswe')

btn_minus = Button(root, text='-', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit('-'))
btn_minus.grid(row=2, column=3, padx=3, pady=3, stick='nswe')

btn_multiply = Button(root, text='x', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit('*'))
btn_multiply.grid(row=3, column=3, padx=3, pady=3, stick='nswe')

btn_share = Button(root, text='/', bg='#c0c0c0', fg='#303030', font=('Arial', 18), command=lambda: add_digit('/'))
btn_share.grid(row=4, column=3, padx=3, pady=3, stick='nswe')

root.mainloop()