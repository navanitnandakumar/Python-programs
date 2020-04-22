import tkinter as tk
from pytube import YouTube

#fn for downloading video
def downloadVideo():
    global E1
    string =E1.get()
    yt = YouTube(str(string))
    videos = yt.get_videos()
    s=1
    for v in videos:
        print(str(s) + '.' + str(v))
        s +=1
    n=int(input("Enter your choice -->"))
    vid=videos[n-1]
    destination=str(input("Enter your destination -->"))
    vid.download(destination)
    print("Your file has been downloaded.")
root=tk.Tk()

#title
w=tk.Label(root,text="Youtube video downloader")
w.pack()

E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)

#button
button=tk.Button(root,text="Download",fg="red",command=downloadVideo())
button.pack(side=tk.BOTTOM)

root.mainloop()
