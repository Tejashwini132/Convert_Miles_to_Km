import tkinter

window = tkinter.Tk()


window.title("My First GUI Project")
window.minsize(width=500, height=300)
# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
window.mainloop()
