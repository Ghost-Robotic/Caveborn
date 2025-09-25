from tkinter import *
from tkinter import ttk
import tkinter as tk
from os import system, name
from tkinter import font

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
#root.iconphoto(True, tk.PhotoImage(file=r"assets\Caveborn_Icon_2.png"))
root.configure(bg="#1c2526")
system(root.state('zoomed') if name == 'nt' else root.attributes('-zoomed', True))

NORMAL_FONT = 'Consolas 14'
BOLD_FONT = font.Font(font='Consolas', size=14, weight='bold')

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
                insertcolor="#ffffff",
                kw="hello")  # Cursor color

style.configure("TFrame", 
                background="#1c2526")


titleframe = ttk.Frame(root, padding="3 3 12 12")
titleframe.grid(column=0, row=0, sticky=(N, W, E, S))


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
                     fg="#ffffff", 
                     borderwidth=0,
                     font=("Courier", 13),
                     wrap="none")
title_text.insert(tk.END, title)
title_text.grid(column=0, row=0, padx=0, ipadx=0, ipady=0, pady=0, sticky=(N, W))

mid_frame = ttk.Frame(root)
mid_frame.grid(column=0, row=1, sticky=(N, W, E, S))

# available moves compass
compass_frame = Canvas(mid_frame, height=101, width=101, bg="#1c2526", relief="groove")
compass_frame.grid(column=0, row=0, sticky=(N, W), padx=16, pady=16)

compass_frame.create_text(52, 51, text='○', font='TkMenuFont, 14', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(52, 33, text='▲', font='TkMenuFont, 14', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(71, 52, text='▶', font='TkMenuFont, 20', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(52, 71, text='▼', font='TkMenuFont, 14', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(34, 52, text='◀', font='TkMenuFont, 20', anchor=tk.CENTER, fill = "#ffffff")

compass_frame.create_text(52, 15, text='N', font='TkMenuFont, 12', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(87, 52, text='E', font='TkMenuFont, 12', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(52, 90, text='S', font='TkMenuFont, 12', anchor=tk.CENTER, fill = "#ffffff")
compass_frame.create_text(14, 52, text='W', font='TkMenuFont, 12', anchor=tk.CENTER, fill = "#ffffff")


# player information
info_frame = ttk.Frame(mid_frame, width=30, height=30) 
info_frame.grid(column=1, row=0, sticky=(N, W), padx=16, pady=16)

ttk.Label(info_frame, font=(BOLD_FONT, 12), text="Health ", foreground="#08de3d").grid(column=0, row=0, sticky=(N, W))
ttk.Label(info_frame, font=(BOLD_FONT, 14), text=": ", foreground="#ffffff").grid(column=1, row=0, sticky=(N, W))
ttk.Label(info_frame, font=(BOLD_FONT, 12), text="Bag ", foreground="#2ca3de").grid(column=0, row=1, sticky=(N, W))
ttk.Label(info_frame, font=(BOLD_FONT, 14), text=": ", foreground="#ffffff").grid(column=1, row=1, sticky=(N, W))

bag_box = tk.Text(info_frame, height=10, width=25)
bag_box.grid(column=0, row=2, sticky=(N, W), columnspan=3)

mode_specific_info = ttk.Frame(mid_frame)
mode_specific_info.grid(column=2, row=0, sticky=(N, W), padx=16, pady=16)
ttk.Label(mode_specific_info, font=(BOLD_FONT, 12), text="Enemies to defeat ", foreground="#ff0808").grid(column=0, row=0, sticky=(N, W))
ttk.Label(mode_specific_info, font=(BOLD_FONT, 14), text=": ", foreground="#ffffff").grid(column=1, row=0, sticky=(N, W))

# cave information
cave_frame = ttk.Frame(root)
cave_frame.grid(column=0, row=2, padx=15, pady=16, sticky=(N, W))

ttk.Label(cave_frame, font=NORMAL_FONT, text="----------").grid(column=0, row=0, sticky=(N, W))
ttk.Label(cave_frame, font=(BOLD_FONT, 13), text="Solace", foreground="#eb3636").grid(column=0, row=1, sticky=(N, W))
ttk.Label(cave_frame, font=NORMAL_FONT, text="----------").grid(column=0, row=2, sticky=(N, W))

# command line
command_frame = ttk.Frame(root)
command_frame.grid(column=0, row=3, padx=10, pady=10, sticky=(S, W))

command = StringVar()
ttk.Label(command_frame, text=">", font=('calibre', 16, 'bold')).grid(column=0, row=1, sticky=(S, W), padx=5)
command_line = Entry(command_frame,textvariable=command)
command_line.configure(width=30, borderwidth=0, insertbackground="#ecf00c", bg="#2f3738", fg="#fbff00", font=('calibre', 13), highlightthickness=3, highlightcolor="#A2D498")
command_line.grid(column=1, row=1, sticky=(S, W))

# frame = tk.Frame(root)
# frame.grid(column=1, row=1)

# compass_font = "Arial"
# ttk.Label(frame, text="N", font=compass_font).grid(column=3, row=1)
# ttk.Label(frame, text="▴", font=compass_font, anchor="s").grid(column=3, row=2)
# ttk.Label(frame, text="○", font=compass_font).grid(column=3, row=3)
# ttk.Label(frame, text="▾", font=compass_font).grid(column=3, row=4)

# ttk.Label(frame, text="W", font=compass_font).grid(column=1, row=3)
# ttk.Label(frame, text="◂", font=compass_font).grid(column=2, row=3)
# ttk.Label(frame, text="▸", font=compass_font).grid(column=4, row=3)

# ttk.Label(frame, text="S", font=compass_font).grid(column=3, row=5)
# ttk.Label(frame, text="E", font=compass_font).grid(column=5, row=3)

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

#command_line.focus()
root.mainloop()