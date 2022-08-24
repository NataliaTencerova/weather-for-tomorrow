# strTemperatureMin = str(15.4)
# strTemperatureMax= str(12.4)
# strRainProbability = str(90)

# omg = open("weather_for_tomorrow/weatherTomorrow.html").read().format(minTemperature=strTemperatureMin, maxTemperature=strTemperatureMax, probabilityOfRain=strRainProbability)
# print(omg)

def test_function():
    strVarOne = str(15.4)
    strVarTwo = str(16.7)
    strVarThree = str(50)

    return strVarOne, strVarTwo, strVarThree

varOne, varTwo, varThree = test_function()

print(varOne)
