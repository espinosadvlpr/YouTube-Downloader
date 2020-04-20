import pytube
import tkinter

def pop_up(message):
    toplevel = tkinter.Toplevel(app)
    toplevel.geometry('200x60')
    toplevel.focus_set()
    toplevel.grab_set()
    toplevel.transient(master=app)
    tkinter.Label(toplevel, text=message).pack(padx=10, pady=20)


def download_vid():
    video_url = link.get()
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first().download('./')
    pop_up('File dowloaded.')


app = tkinter.Tk()
app.title('')
app.geometry('500x200')
app.resizable(width=0, height=0)

tkinter.Label(app, text="YouTube Downloader",
              font=('Consolas', 30), fg="black").pack(side=tkinter.TOP, pady=15)
entry = tkinter.StringVar()
link = tkinter.Entry(app, textvariable=entry, width=45).pack(
    side=tkinter.TOP, pady=15)
tkinter.Button(app, text="Download", bg="white", command=download_vid).pack()

app.mainloop()