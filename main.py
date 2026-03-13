from fastapi import FastAPI
from  weather_client import WeatherClient
from pydantic import BaseModel

app = FastAPI()
wc = WeatherClient()
class skinData(BaseModel):
    #integer for how skin react to sun exposure
    skin_react: int
    #string for area that spend most time in
    area: str
    #string for reason for going out    
    reason: str
    #string for experience with sunburns
    sunburn_experience: str
    #string for weekday time spend
    weekday_time: str
    #string for time of day spend outside
    time_of_day: str
    #string for how often applying sunscreen
    sunscreen: str
    #string for what doing in sun
    do_in_sun: str
class weatherData(BaseModel):
    #string for city name
    city: str
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/weather/")
def get_weather(data: weatherData):
    try:
        response = wc.get_weather(data.city)
        return {"city": data.city, "weather": response}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/skinbuilder/")
async def build_skin(data: skinData):
    try:
     return {"message": "Skin data processed successfully", "data": data}
    except Exception as e:
        return {"error": str(e)}