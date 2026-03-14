from fastapi import FastAPI
from  weather_client import WeatherClient
from pydantic import BaseModel
from app.services.sun_profile import analyze_sun_safety
from app.schemas.quiz import SkinProfile
app = FastAPI()
wc = WeatherClient()
'''
class skinProfile(BaseModel):
    #string for how skin react to sun exposure
    skinTypeId: str
    #string for area that spend most time in
    locationId: str
    #string for reason for going out    
    activityIds: list[str]
    #string for experience with sunburns
    burnHistory: str
    #string for weekday time spend
    workPattern: str
    #string for time of day spend outside
    peakSunExposure: str
    #string for how often applying sunscreen
    sunscreenFrequency: str
    #string for what doing in sun
    act_in_sun: str
'''
class weatherData(BaseModel):
    #string for city name
    city: str

#endpoint for getting weather data for a city
@app.post("/weather/")
def get_weather(data: weatherData):
    try:
        response = wc.get_weather(data.city)
        return {"city": data.city, "weather": response}
    except Exception as e:
        return {"error": str(e)}
    
#endpoint for sending skin profile data to database?
@app.post("/skinprofile/")
async def build_skin(data: SkinProfile):
    try:
        #database code to save skin profile data?
        
        return {"message": "Skin data received successfully", "data": data}
    except Exception as e:
        return {"error": str(e)}

#endpoint for analysing skin profile and weather data from llm
@app.post("/analyse/")
async def get_recommendations(skin_data: SkinProfile):
    try:
        res = analyze_sun_safety(skin_data)
        return {"recommendations": res}
    except Exception as e:
        return {"error": str(e)}