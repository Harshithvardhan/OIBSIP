import tkinter as tk

def calculate_bmi():
    try:
        height_value = float(entry_height.get())
        weight_value = float(entry_weight.get())

        if unit_height.get() == "feet":
            height_value *= 12.0  
            bmi = 703 * (weight_value / (height_value ** 2))
        else:
            bmi = weight_value / ((height_value / 100) ** 2)

        if bmi <= 0 or height_value <= 0 or weight_value <= 0:
            result.set("Please enter valid values.")
        else:
            if bmi <= 18.4:
                result.set("Underweight")
            elif 18.5 <= bmi <= 24.9:
                result.set("Normal")
            elif 25.0 <= bmi <= 39.9:
                result.set("Overweight")
            else:
                result.set("Obesity")
    except ValueError:
        result.set("Please enter valid numeric values.")


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")

window.configure(bg="#f0f0f0") 

unit_height = tk.StringVar()
unit_height.set("feet")

label_height = tk.Label(window, text="Height:", bg="#f0f0f0") 
label_height.grid(row=0, column=0, padx=10, pady=10)

entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1, padx=10, pady=10)

unit_menu = tk.OptionMenu(window, unit_height, "feet", "cm")
unit_menu.configure(bg="#4CAF50", fg="white") 
unit_menu.grid(row=0, column=2, padx=10, pady=10)

label_weight = tk.Label(window, text="Weight:", bg="#f0f0f0")
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

unit_weight = tk.StringVar()
unit_weight.set("pound")

unit_menu = tk.OptionMenu(window, unit_weight, "pound", "kg")
unit_menu.configure(bg="#4CAF50", fg="white") 
unit_menu.grid(row=1, column=2, padx=10, pady=10)

button_calculate = tk.Button(window, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white") 
button_calculate.grid(row=2, column=0, columnspan=3, pady=10)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, bg="#f0f0f0", font=("Helvetica", 14)) 
result_label.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()
