import requests
import tkinter as tk
from tkinter import messagebox
import creds

def get_weather():
    city = city_entry.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_label.config(text=f"Weather in {city}: {temperature}°C, {description.capitalize()}", font=("Helvetica", 14), fg="#333")
    else:
        messagebox.showerror("Error", "City not found")


window = tk.Tk()
window.title("Weather App")

window.configure(bg="#F4F4F4")

city_label = tk.Label(window, text="Enter city:", font=("Helvetica", 12), bg="#F4F4F4", fg="#333")
city_label.pack()

city_entry = tk.Entry(window, font=("Helvetica", 12), bg="#FFF", fg="#333", relief="solid")
city_entry.pack(pady=10, padx=20)

get_weather_button = tk.Button(window, text="Get Weather", font=("Helvetica", 12), bg="#008CBA", fg="white", relief="solid", command=get_weather)
get_weather_button.pack(padx=20)

weather_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#F4F4F4", fg="#333")
weather_label.pack(pady=10)
window.geometry("400x300")

window.mainloop()
