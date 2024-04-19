def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = celsius_temp * (9/5) + 32
    return fahrenheit_temp

def main():
    temperature_input = float(input("What is the temperature? "))
    scale_input = input("Fahrenheit or Celsius (F/C)? ").upper()
    
    if scale_input == 'C':
        temperature_input = celsius_to_fahrenheit(temperature_input)
    
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature_input, wind_speed)
        print(f"At temperature {temperature_input:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()
