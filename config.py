USE_ROUNDED_COORDS = False
OPENWEATHER_API = "d79aa0aeedbb770d08bb4f87592d6b0a"  # paste API token here
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)