import geocoder
from typing import Tuple

class LocationService:
    @staticmethod
    def get_coordinates(city_name: str) -> Tuple[float, float]:
        g = geocoder.osm(city_name)
        if g.ok:
            return g.lat, g.lng
        raise ValueError("Konum bulunamadı")

    @staticmethod
    def get_location_name(lat: float, lng: float) -> str:
        g = geocoder.osm([lat, lng], method='reverse')
        return g.city if g.city else g.country