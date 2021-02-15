import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os



root=tk.Tk()
root.title("Nigger")

apps = []

if os.path.isfile("save.txt") :
    with open("save.txt", 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def AddApp():

    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("Executables", "*.exe"),("All files","*.*")))
    apps.append(filename)
    #print(apps)

    appss = list(dict.fromkeys(apps))
    for app in appss:
        if app.strip():
            label = tk.Label(frame, text=app, bg="gray")
            label.pack()

def RunApps() :
    for app in apps:
        os.startfile(app)

Canvas= tk.Canvas(root, height= 500, width= 500, bg = "#33CAFF")
Canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx= 0.1, rely= 0.04)

addApp = tk.Button(root, text="Add App", bg="#33CAFF", fg="white", command=AddApp)
addApp.pack()

Launch = tk.Button(root, text="Launch Apps", bg="#33CAFF", fg="white", command=RunApps)
Launch.pack()

for app in apps:
    if app.strip():
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')