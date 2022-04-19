from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("1000x600")
earth_image= ImageTk.PhotoImage(Image.open ("Earth.jpg"))
#-----------------Japan-----------------
Japan_label = Label(root,text="Japan")
Japan_label.place(relx=0.2,rely=0.05, anchor= CENTER)

Japan_earth=Label(root)
Japan_earth["image"]=earth_image
Japan_earth.place(relx=0.2,rely=0.35, anchor= CENTER)


Japan_time = Label(root)
Japan_time.place(relx=0.2,rely=0.65, anchor= CENTER)
#-----------------------US---------------
Australia_label = Label(root,text="Australia")
Australia_label.place(relx=0.7,rely=0.05,anchor= CENTER)

Australia_earth=Label(root) 
Australia_earth.place(relx=0.7,rely=0.35, anchor= CENTER)
Australia_earth["image"]=earth_image

Australia_time = Label(root)
Australia_time.place(relx=0.7,rely=0.65, anchor= CENTER)

class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        Japan_time["text"]="Time :"+ current_time
        Japan_time.after(200,self.times)
class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        Australia_time["text"]="Time :"+ current_time
        Australia_time.after(200,self.times)
        
obj_Japan=Japan()
obj_Australia=Australia()
Japan_btn=Button(root,text="Show Time",command=obj_Japan.times)
Japan_btn.place(relx=0.2,rely=0.8, anchor= CENTER)
Australia_btn=Button(root,text="Show Time",command=obj_Australia.times)
Australia_btn.place(relx=0.7,rely=0.8, anchor= CENTER)
root.mainloop()