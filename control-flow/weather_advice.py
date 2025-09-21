
# Prompt the user to input today's weather
weather_today = str(
    input("What's the weather like today? (sunny/rainy/cold): "))

# Provide recommendations based on the input
if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather_today == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
