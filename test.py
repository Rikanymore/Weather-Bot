import requests
import geocoder
from dotenv import load_dotenv
import os

# Çevresel değişkenleri yükle
load_dotenv()

# Konum testi
def test_location():
    location = "Istanbul"
    g = geocoder.osm(location)
    if g.ok:
        print(f"📍 {location} koordinatları: {g.lat}, {g.lng}")
        return g.lat, g.lng
    else:
        print("Konum bulunamadı")
        return None

# Hava durumu API testi
def test_weather_api(lat, lon):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(f"🌡️ Sıcaklık: {data['main']['temp']}°C")
        print(f"☁️ Durum: {data['weather'][0]['description']}")
        return True
    except Exception as e:
        print(f"API hatası: {str(e)}")
        return False

# Ana test
if __name__ == "__main__":
    print("🔥 Hava Durumu Botu Testi 🔥")
    print("="*30)
    
    coords = test_location()
    if coords:
        test_weather_api(coords[0], coords[1])