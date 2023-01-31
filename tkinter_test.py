import os
from tkinter import *
from tkinter import ttk

# Set $DISPLAY to allow start gui over ssh
os.environ['DISPLAY'] = ':0.0'

# Control screensaver: DISPLAY=:0 xset
# Turn screen off: subprocess.call('xset dpms force off', shell=True)
# Turn screen on: subprocess.call('xset dpms force on', shell=True)


# window = _test()

from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):

        root.title("Feet to Meters")
        # root.attributes('-fullscreen', True)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.feet = StringVar()
        self.feet_entry = ttk.Entry(mainframe, width=14, textvariable=self.feet, name='feet_entry')
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()
        self.meter_entry = ttk.Entry(mainframe, width=14, textvariable=self.meters, name='meter_entry')
        self.meter_entry.grid(column=2, row=2, sticky='we')

        # ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        # ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # mainframe.columnconfigure([1,2,3], weight=1, minsize=75)
        # mainframe.rowconfigure([1,2,3], weight=1, minsize=50)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.feet_entry.focus()
        root.bind("<Return>", self.calculate) # Pressing return key triggers calculation
        
    def calculate(self, *args):
        try:
            current_focus = root.focus_get()
            if current_focus == self.feet_entry:
                value = float(self.feet.get())
                self.meters.set(int(0.3048 * value * 10000)/10000)
            elif current_focus == self.meter_entry:
                value = float(self.meters.get())
                self.feet.set(int(3.2808 * value * 10000)/10000)
        except ValueError:
            pass
        print(root.focus_get())
        print(type(root.focus_get()))
        print(root.focus_get() == self.meter_entry)
        print(root.focus_get() == self.feet_entry)

root = Tk()
FeetToMeters(root)
root.mainloop()