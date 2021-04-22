import tkinter
from guiStuff import frameStuff
window = tkinter.Tk()
headerText = tkinter.StringVar()
headerText.set("Hello! What would you like to do today?")

# Text varibale = cmnd:object of foreg StringVar, leads to faster updation
# and code minimization
headerDisp = tkinter.Label(textvariable=headerText)
headerDisp.pack()

frame = tkinter.Frame()

def initFrame(frame):
    #frame = tkinter.Frame()
    insert_button = tkinter.Button(frame, text="Insert", command=lambda: headerText.set("inserted!")).pack()
    delete_button = tkinter.Button(frame, text="Delete", command= lambda: headerText.set("Deleted!")).pack()
    show_button = tkinter.Button(frame, text="Show Database", command=lambda: headerText.set("Show")).pack()


initFrame(frame)
frame.pack()

window.mainloop()