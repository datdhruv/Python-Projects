import tkinter
from guiStuff import frameStuff
window = tkinter.Tk()
window.geometry("700x400")
headerText = tkinter.StringVar()
headerText.set("Hello! What would you like to do today?")

# Text varibale = cmnd:object of foreg StringVar, leads to faster updation
# and code minimization
headerDisp = tkinter.Label(textvariable=headerText, width=400, font=("Courier", 20))
headerDisp.pack()

frame = tkinter.Frame()

def initFrame(frame):
    #frame = tkinter.Frame()
    insert_button = tkinter.Button(frame, text="Insert", command=lambda: frameStuff.inFrame(frame, headerText)).pack()
    delete_button = tkinter.Button(frame, text="Delete", command= lambda: headerText.set("Deleted!")).pack()
    show_button = tkinter.Button(frame, text="Show Database", command=lambda: headerText.set("Show")).pack()

def inFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    label = tkinter.Label(frame,text="INSERT FRAME").pack()
initFrame(frame)
frame.pack()

window.mainloop()