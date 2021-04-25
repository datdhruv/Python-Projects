import tkinter

import databaseHandler


def inFrame(frame, headerText):
    headerText.set("Enter Value to insert")
    for widget in frame.winfo_children():
        widget.destroy()

    textbox = tkinter.Text(width=19, height=5)
    textbox.pack()

    tkinter.Button(frame, text="Done", command=lambda: databaseHandler.insert_generic(textbox.get("1.0","end-1c").split(","))).pack()
    vals = textbox.get("1.0", "end-1c")
    print(vals)

    label = tkinter.Label(frame,text="INSERT FRAME").pack()
    databaseHandler.done()
