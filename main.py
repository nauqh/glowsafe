from fastapi import FastAPI
from  WeatherClient import WeatherClient
app = FastAPI()
wc = WeatherClient()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/weather/{city}")
def get_weather(city: str):
    try:
        data = wc.get_weather(city)
        return {"city": city, "weather": data}
    except Exception as e:
        return {"error": str(e)}