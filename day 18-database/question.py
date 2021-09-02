from tkinter import *
window=Tk()                  #create window object
window.geometry("250x400")
window.title("Question and Answer")
window.config(bg="cyan")

question=Label(text="1.Who developed the Python language?",bg="cyan",font=('courier',15))
question.grid(row=0,column=0)

answer1=Radiobutton(text="Zim Den",bg="cyan",font=('courier',15))
answer1.grid(row=1,column=0)

answer2=Radiobutton(text="Guido van Rossum",bg="cyan",font=('courier',15))
answer2.grid(row=2,column=0)

answer3=Radiobutton(text="Niene Stom",bg="cyan",font=('courier',15))
answer3.grid(row=3,column=0)

answer4=Radiobutton(text="Wick van Rossum",bg="cyan",font=('courier',15))
answer4.grid(row=4,column=0)

btn=Button(text="Submit",font=('courier',15),bg="gray")
btn.grid(row=5,column=0)
window.mainloop()