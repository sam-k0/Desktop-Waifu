import sys, time, random
from tkinter import *
from win32api import *
from PIL import Image, ImageTk
import playsound as ps
from pypresence import Presence


startTime = int(time.time())

CLIENT_ID = "822935463244464138"
RPC = Presence(CLIENT_ID)
RPC.connect()
RPC.update(state="👙Where are they?👙",
    details="🔥Looking for panties🔥",
    start=startTime,
    large_image="panty",
    large_text="The panties (Where are they?)",
    buttons = [{"label": "get panties", "url": "https://github.com/ManuelStaffa/"}]
    )


#Load image---------------------------------------------------------------------
file_name = "neko.png"
def getPath(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'
image_path = getPath(file_name)


def changePos(xpos, ypos):
    window.geometry("+{}+{}".format(xpos, ypos))


def moveToCursor():
    xpos, ypos = GetCursorPos()
    x = round(xpos-width/2)
    y = round(ypos-height/2)
    window.geometry("+{}+{}".format(x, y))

    window.after(1,moveToCursor)


def playSound():
    ps.playsound(getPath('animegirl.mp3'))
    xpos, ypos = GetCursorPos()
    x = round(xpos-width/2)
    y = round(ypos-height/2)
    window.geometry("+{}+{}".format(x, y))


#Variables----------------------------------------------------------------------
#Get screen size
display_width = GetSystemMetrics(0)
display_height = GetSystemMetrics(1)

#Set window size equal to image size+
image = Image.open(image_path)
width, height = image.size
window_width = width
window_height = height

#Window position
window_xpos = round((display_width-window_height)/2)
window_ypos = round((display_height-window_height)/2)


#Window-------------------------------------------------------------------------
#Create an instance of tkinter frame


window = Tk()

#Define the size of the windowdow or frame
window.geometry("{}x{}".format(window_width, window_height))
window.geometry("+{}+{}".format(window_xpos, window_ypos))
#To Make it transparent use alpha property to define the opacity of
#window.attributes('-alpha', 1)
window.wm_attributes("-transparentcolor", "green")
window.overrideredirect(True)

#Window content
frame = Frame(window)
canvas = Canvas(frame,
                bg="green",
                width=window_width,
                height=window_height,
                borderwidth = 0,
                highlightthickness = 0,
                cursor="hand2")

button = Button(background="black",
                activebackground="black",
                foreground="white",
                disabledforeground="white",
                activeforeground="white",
                highlightthickness=0,
                relief=FLAT,
                width=10,
                height=7,
                text="censored",
                command=playSound)



photoimage = ImageTk.PhotoImage(file=image_path)
canvas.create_image(window_width/2, window_height/2, image=photoimage)

canvas.pack()
button.place(x=window_width/2-40, y=window_height/2-70)
#button.pack()
frame.pack()

#window.after(1, moveToCursor)
window.mainloop()
