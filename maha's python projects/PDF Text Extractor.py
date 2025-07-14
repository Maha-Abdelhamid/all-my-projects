import pypdf
from tkinter import *
from tkinter import filedialog 

def openfile():
    filename = filedialog.askopenfilename(initialdir=r'C:\Users\pc1\Desktop\for maha only\Dady\images\\dad.pdf')                                                   

    print(filename)
    reader = pypdf.PdfReader(filename)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        outputfile_text["text"]=text
                                
root = Tk()
root.title("PDF Text Extractor")  

filename_label = Label(root, text="No File Selected")
outputfile_text = Label(root,text="",width=120,height=50)
openfile_button = Button(root, text="Open PDF File", command=openfile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()