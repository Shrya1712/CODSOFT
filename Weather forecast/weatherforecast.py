from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root =  Tk()
root.title("Weather Forecast")
root.geometry("900x600+400+300")
root.resizable(False,False)

def getWeather():
    try:
        city = textentry.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng= location.longitude, lat= location.latitude)
        home= pytz.timezone(result)
        localtime= datetime.now(home)
        currenttime= localtime.strftime("%I:%M: %p")
        clock.config(text=currenttime)
        name.config(text="Current Weather")

        #weatherAPI
        api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a9108dd85e51a4acd38d0e0533cc497c"
        jsondata= requests.get(api).json()
        condition = jsondata['weather'][0]['main']
        description = jsondata['weather'][0]['description']
        temperature = int(jsondata['main']['temp']-273.15)
        pressure = jsondata['main']['pressure']
        humidity = jsondata['main']['humidity']
        wind = jsondata['wind']['speed']

        t.config(text=(temperature, "°"))
        c.config(text=(condition, "|","Feels", "Like", temperature, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=(pressure, "°"))
        d.config(text=description)
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")

#search box
searchbox = PhotoImage(file="searchbox.png")
searchbox1 = Label(image=searchbox)
searchbox1.place(x=20, y=20)

#text entry
textentry = tk.Entry(root, justify="center", width=17, font= ("poppins", 20, "bold"), bg= "#404040", border=0, fg= "white")
textentry.place(x=60, y=40)
textentry.focus()

#search icon
searchicon = PhotoImage(file="searchicon.png")
searchicon1 = Button(image=searchicon, borderwidth=0,  cursor="hand2", bg= "#404040", command = getWeather)
searchicon1.place(x=400, y=34)

#logo
logo = PhotoImage(file="logo.png")
logo1 = Label(image=logo)
logo1.place(x=160, y=100)

#framebox
framebox = PhotoImage(file="box.png")
framebox1 = Label(image=framebox)
framebox1.pack(padx=5, pady=5, side=BOTTOM)

#timedisplay
name = Label(root, font=("arial", 15, "bold"))
name.place(x=20, y=200)
clock = Label(root, font=("helvetica", 20))
clock.place(x=30, y=230)

#parameters
parameter1= Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg= "white", bg="#1ab5ef")
parameter1.place(x=120, y=500)

parameter2= Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg= "white", bg="#1ab5ef")
parameter2.place(x=250, y=500)

parameter3= Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg= "white", bg="#1ab5ef")
parameter3.place(x=430, y=500)

parameter4= Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg= "white", bg="#1ab5ef")
parameter4.place(x=600, y=500)

t= Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=250)
c= Label(font=("arial", 15, "bold"))
c.place(x=400, y=350)

w= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=530)
h= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=530)
p= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=450, y=530)
d= Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=620, y=530)

root.mainloop()