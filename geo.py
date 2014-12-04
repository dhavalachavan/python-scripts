from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Las Vegas")
print(location.address)
print(location.latitude, location.longitude)
