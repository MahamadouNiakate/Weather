from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('Weather application')
root.geometry("400x170")

# Create city Lookup Function
def city1Lookup():
    # city1.get()
    # cityLabel = Label(root, text=city1.get())
    # cityLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city1.get()+"&appid=e246d1945df92a13f33ff4528989ad0c")
        api = json.loads(api_request.content)
        city = api["name"]
        country = api["sys"]["country"]
        description_weather = api["weather"][0]["description"]
        # Celsius = nombre - 273.15
        temperature = api["main"]["temp"] - 273,15

        if temperature[0] <= 10:
            weather_color = "#1E90FF"
        elif temperature[0] <= 15:
            weather_color <= "#9400D3"
        elif temperature[0] <= 20:
            weather_color = "#FFD700"
        elif temperature[0] <= 30:
            weather_color = "#FFDEAD"
        elif temperature[0] <= 40:
             weather_color = "#FFA500"
        elif temperature[0] <= 50:
             weather_color = "#FF4500"

        root.configure(background=weather_color)
        myLabel = Label(root, text = city + "\n " + country + "\n " + "Weather description: " + description_weather + "\n " + str(round(temperature[0])) + " °C", font=("Helvetica", 20), background=weather_color )
        myLabel.grid(row=1, column=0, columnspan=2,pady=20)
    
    except Exception as e:
        api = "Error..." 
 

city1 = Entry(root)
city1.grid(row=0, column=0, stick=W+E+N+S)

city1_Button = Button(root, text="Lookup City", command=city1Lookup)
city1_Button.grid(row=0, column=1, stick=W+E+N+S)

# print(str(api["main"]["temp"])+" "+str(api["name"])+ " " + str(api["sys"]["country"])+" "+str(api["weather"][0]["description"]))

root.mainloop()