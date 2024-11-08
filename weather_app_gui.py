import requests
import tkinter as tk
from tkinter import messagebox, ttk

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def show_weather():
    city = city_entry.get()
    if city:
        update_weather(city)
        add_to_history(city)

def update_weather(city):
    weather_data = get_weather(city)
    
    if weather_data.get("cod") != 200:
        messagebox.showerror("Error", "City not found!")
    else:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        result_label.config(text=f"Temperature: {temp}°C\nWeather: {description.capitalize()}")

def add_to_history(city):
    if city not in city_history.get(0, tk.END):
        city_history.insert(tk.END, city)

def select_from_history(event):
    selected_indices = city_history.curselection()
    if selected_indices:
        selected_city = city_history.get(selected_indices[0])
        city_entry.delete(0, tk.END)
        city_entry.insert(0, selected_city)
        update_weather(selected_city)

# Set up the main window
root = tk.Tk()
root.title("Weather App")

# Create a frame for input and button
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X)

# Add entry widget for city
city_label = ttk.Label(input_frame, text="Enter city name:")
city_label.pack(side=tk.LEFT, padx=(0, 5))

city_entry = ttk.Entry(input_frame, width=30)
city_entry.pack(side=tk.LEFT, padx=(0, 5))

# Add a button to fetch weather
fetch_button = ttk.Button(input_frame, text="Get Weather", command=show_weather)
fetch_button.pack(side=tk.LEFT)

# Create a frame for results and history
results_frame = ttk.Frame(root, padding="10")
results_frame.pack(fill=tk.BOTH, expand=True)

# Add a label to display the results
result_label = ttk.Label(results_frame, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Add a Listbox for city history
history_label = ttk.Label(results_frame, text="Previously visited cities:")
history_label.pack(anchor=tk.W)

city_history = tk.Listbox(results_frame, height=5)
city_history.pack(fill=tk.BOTH, expand=True)
city_history.bind('<<ListboxSelect>>', select_from_history)

# Run the application
root.mainloop()
