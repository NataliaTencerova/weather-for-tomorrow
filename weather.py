import os, json, webbrowser

def get_weather():
     cmdGetWeather = 'curl -s -H "Accept: application/json" "https://api.tomorrow.io/v4/timelines?location=49.1533,16.8765&fields=temperatureMin&fields=temperatureMax&fields=precipitationProbability&units=metric&timesteps=1d&startTime=nowPlus1d&endTime=nowPlus2d&apikey=22nEaWvBWcuQ1cWSRAEb8WRpx749RNZs"'
     result = os.popen(cmdGetWeather).read()
     jsonData = json.loads(result)

     return jsonData

def write_html():
     jsonData = get_weather()
     temperatureMin = jsonData['data']['timelines'][0]['intervals'][0]['values']['temperatureMin']
     temperatureMax = jsonData['data']['timelines'][0]['intervals'][0]['values']['temperatureMax']
     rainProbability = jsonData['data']['timelines'][0]['intervals'][0]['values']['precipitationProbability']

     strTemperatureMin = str(temperatureMin)
     strTemperatureMax = str(temperatureMax)
     strRainProbability = str(rainProbability)

     weatherTomorrow = open("weather_for_tomorrow/templateWeatherTomorrow.html").read().format(minTemperature=strTemperatureMin, maxTemperature=strTemperatureMax, probabilityOfRain=strRainProbability)

     htmlFile = open("weather_for_tomorrow/completeWeatherTomorrow.html", "w")
     htmlFile.write(weatherTomorrow)
     htmlFile.close

     copyHtmlFile = open("/home/nitilki/html/1/weather.html", "w")
     copyHtmlFile.write(weatherTomorrow)
     copyHtmlFile.close

# while True:
#      get_weather()

#      write_html()

try:
     get_weather()

     write_html()

     webbrowser.open("file:///home/nitilki/Documents/github_repositories/weather_for_tomorrow/completeWeatherTomorrow.html")

except:
     print("Something went wrong.")

else:
     print("OK")