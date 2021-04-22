window = tkinter.Tk()
cmnd = tkinter.StringVar().set("Hello! What would you like to do today?")

insert_button = tkinter.Button(window, text="insert", command=lambda: print("*"*10))
insert_button.pack()
if __name__ == "__main__":
    window.mainloop()
"""