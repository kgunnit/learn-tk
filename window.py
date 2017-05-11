# working on getting familiar with creating gui in python

import tkinter


def main():
    base = tkinter.Tk()
    label1 = tkinter.Label(base, text="Hello, this is a window.")
    label1.pack()
    base.mainloop()
    
if __name__ == '__main__':
    main()
