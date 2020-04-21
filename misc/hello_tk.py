from tkinter import *

class App:

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        self.button = Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        self.hi_again = Button(self.frame, text="Hello", command=self.say_hi)
    
    def say_hi(self):
        self.blergh = Button(self.frame, text="Kevin did this",command=self.bye)
        self.blergh.pack()
    def bye(self):
        self.hi_there.destroy()
        self.hi_again.pack()
        
        

root = Tk()

app = App(root)

root.mainloop()
