from tkinter import *
from tkinter import ttk
import tkinter as tk
from os import system, name

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# Create main window
root = Tk()
root.title("Caveborn")
#root.iconbitmap("assets\Caveborn_Icon_2.ico")
root.iconphoto(True, tk.PhotoImage(file=r"assets\Caveborn_Icon_2.png"))
root.configure(bg="#1c2526")
system(root.state('zoomed') if name == 'nt' else root.attributes('-zoomed', True))

# Create style
style = ttk.Style()

style.theme_use("clam")

# Configure styles for various widgets
style.configure("TButton", 
                background="#2e3b3e", 
                foreground="#ffffff", 
                bordercolor="#4a5b5e",
                font=("Helvetica", 10),
                padding=5)
style.map("TButton", 
          background=[("active", "#3e4f52")],  # Color when clicked
          foreground=[("active", "#ffffff")])

style.configure("TLabel", 
                background="#1c2526", 
                foreground="#ffffff",
                font=("Helvetica", 10))

style.configure("TEntry", 
                fieldbackground="#2e3b3e", 
                foreground="#ffffff",
                insertcolor="#ffffff")  # Cursor color

style.configure("TFrame", 
                background="#1c2526")


titleframe = ttk.Frame(root, padding="3 3 12 13")
titleframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = r"""╔───────────────────────────────────────────────╗
│    ___                _                       │
│   / __\__ ___   _____| |__   ___  _ __ _ __   │
│  / /  / _` \ \ / / _ \ '_ \ / _ \| '__| '_ \  │
│ / /__| (_| |\ V /  __/ |_) | (_) | |  | | | | │
│ \____/\__,_| \_/ \___|_.__/ \___/|_|  |_| |_| │
│                                               │
╚───────────────────────────────────────────────╝"""

title_text = tk.Text(titleframe, 
                     height=8, 
                     width=49, 
                     bg="#1c2526", 
                     fg="#eb3636", 
                     borderwidth=0,
                     font=("Courier", 17),
                     wrap="none")
title_text.insert(tk.END, title)
title_text.grid(column=0, row=0, padx=0, ipadx=0, ipady=0, pady=0, sticky=(N, W))

compass = ttk.Frame(root, padding="3 3 12 12")
compass.grid(column=0, row=1, sticky=(N, W, E, S))

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

root.mainloop()