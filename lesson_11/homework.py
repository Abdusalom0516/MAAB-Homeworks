# Task 1
# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.

# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.


from bs4 import BeautifulSoup

html_code = ""
# 1.
with open("weather.html", "r") as f:
    html_code = f.read()

soup = BeautifulSoup(html_code, "html.parser")

all_weather_data = soup.find_all("tr")[1:]
max_temperature = -999
temperatures = []

# 2.
for value in all_weather_data:
    children = value.find_all("td")

    temperature = int(str(children[1].text).replace("°C", ""))
    temperatures.append(temperature)

    if temperature > max_temperature:
        max_temperature = temperature

    print(f"{children[0].text}, {children[1].text}, {children[2].text}.")

print("---------------------------")


# 3.
print("Highest Tempreature")
for value in all_weather_data:
    children = value.find_all("td")
    temperature = int(str(children[1].text).replace("°C", ""))

    if temperature == max_temperature:
        print(f"{children[0].text}, {children[1].text}, {children[2].text}.")

print("---------------------------")


# 4.
print("Average Temperature of the Week")
print(f"{sum(temperatures) / len(temperatures)}°C")



