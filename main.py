# working on getting familiar with creating gui in python

from tkinter import *

def main():
#   creates the window container
    base = Tk()
#   Add labels to different regions in a window
    topLabel = Label(base, text="Top", bg="Orange", fg="blue")
    topLabel.pack()

    middleLabel = Label(base, text="Second Label - Fill X", bg="black", fg="Orange")
    middleLabel.pack(fill=X)

    bottomLabel = Label(base, text="Third Label - Fill Y", bg="red", fg="white")
    bottomLabel.pack(side=LEFT, fill=Y)

    lastLabel = Label(base, text="Last Label - Fill Both", bg="yellow", fg="black")
    lastLabel.pack(fill=BOTH, expand=True)

# mainloop keeps the window displayed until closed
    base.mainloop()
    
if __name__ == '__main__':
    main()
