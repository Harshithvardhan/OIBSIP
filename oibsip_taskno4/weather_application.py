import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

def get_weather():
    city = entry_city.get()
    api_key = "2fe62296096278d8f10a9b11f03a78a0" #repalce Your API

    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}" 
    city_weather_data = requests.get(link)
    
    code = city_weather_data.status_code

    if code == 200:
        weather = city_weather_data.json()["weather"][0]["main"]
        temperature = round(city_weather_data.json()["main"]["temp"])
        humidity = round(city_weather_data.json()["main"]["humidity"])

        result_text.set(f"The WEATHER in {city} is: {weather}\n"
                        f"The TEMPERATURE in {city} is: {temperature}°C\n"
                        f"THE HUMIDITY in {city} is: {humidity}%")
    elif code == 404:
        messagebox.showerror("Error", "The City Which you requested is Not Found!")
    else:
        messagebox.showerror("Error", "Please Enter the Correct City!")

window = tk.Tk()
window.title("Weather App")
window.geometry("400x400")  
style = ttk.Style()
style.theme_use("clam")
bold_font = Font(weight="bold")
style.configure("Green.TButton", foreground="white", background="green")
label_city = ttk.Label(window, text="Enter the City Name:")
label_city.pack(pady=10)

entry_city = ttk.Entry(window)
entry_city.pack(pady=10)

button_get_weather = ttk.Button(window, text="Get Weather", command=get_weather, style="Green.TButton")
button_get_weather.pack(pady=10)

result_text = tk.StringVar()
label_result = ttk.Label(window, textvariable=result_text, font=bold_font)
label_result.pack(pady=10)

window.mainloop()
