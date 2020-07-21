import tkinter as tk

win = tk.Tk()
win.title("welcome to programming language")
label = tk.Label(win,text='hello brindha',bg='purple')
label.pack()
button = tk.Button(win,text='click here',height=5,width=5,bg='grey',fg='green')
button.pack()

rad1 = tk.Radiobutton(win,text='admin',value=1).pack()
rad2 = tk.Radiobutton(win,text='user',value=2).pack()
rad3 = tk.Radiobutton(win,text='password',value=3).pack()



win.mainloop()

