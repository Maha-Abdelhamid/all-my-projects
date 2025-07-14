from tkinter import *
root=Tk()


def donothing():    
    filewin=Toplevel(root)
    button=button(filewin,Text="this button doesn't do any thing....!")
    button.pack()



menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="new",command=donothing)
filemenu.add_command(label="open",command=donothing)
filemenu.add_command(label="save",command=donothing)
filemenu.add_command(label="save as....",command=donothing)
filemenu.add_command(label="close",command=donothing)

filemenu.add_separator

filemenu.add_command(label="exit" , command=root.quit)

menubar.add_cascade(label="file",menu=filemenu)
editmenu= Menu (menubar, tearoff=0)
editmenu.add_command(label="Undo" , command=donothing)

editmenu.add_separator()

editmenu.add_command(label="cut", command=donothing)
editmenu.add_command(label="copy", command=donothing)
editmenu.add_command(label="paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="select all", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)


helpmenu= Menu (menubar, tearoff=3)
helpmenu.add_command(label="Help endex" , command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="About......!" , command=donothing)

menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)

root.mainloop()