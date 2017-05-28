#!/usr/bin/python

import Tkinter
import tkMessageBox



head = Tkinter.Tk()
head.title("List Of Procsses")

# Code to add widgets will go here...

def helloCallBack():
#run script here
   tkMessageBox.showinfo( "title", "message")



b_start = Tkinter.Button(head, text ="Start", command = helloCallBack)
b_start.pack()



left_list = Tkinter.Listbox(head)
# uploude jason file here
for item in ["one", "two", "three", "four"]:
    left_list.insert(Tkinter.END, item)
left_list.pack()



right_list = Tkinter.Listbox(head)
# uploude jason file here
for item in ["one1", "two", "three2", "four"]:
    right_list.insert(Tkinter.END, item)
right_list.pack()



update_list = Tkinter.Listbox(head)
# uploude jason file here
# update_list = set(left_list) - set(right_list)
# for item in update_list:
#     print item
update_list.pack()



head.mainloop()

