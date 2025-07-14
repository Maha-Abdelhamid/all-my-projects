import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x200")
root.configure(bg="gray")

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))

label=tkinter.Label(root,bg="gray",fg="pink",font=("",30),text="shorten URL").pack()
longurl_label = tkinter.Label(root, text="Enter Long URL",bg="gray",fg="white").pack()
longurl_entry = tkinter.Entry(root).pack()
shorturl_label=tkinter.Label(root, text="Output shortened URL",bg="gray",fg="white").pack()
shorturl_entry = tkinter.Entry(root).pack()
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten,bg="pink",font=("",10)).pack()

root.mainloop()