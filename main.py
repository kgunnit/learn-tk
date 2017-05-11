# working on getting familiar with creating gui in python

import tkinter


def main():
#   creates the window container
    base = tkinter.Tk()
# creates the label, pack actually adds the label to the window
    label1 = tkinter.Label(base, text="Hello, this is a window.")
    label1.pack()
# mainloop keeps the window displayed until closed
    base.mainloop()
    
if __name__ == '__main__':
    main()
