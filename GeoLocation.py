# importing geopy library
from geopy.geocoders import Nominatim

# calling Nominatim tool
locatn = Nominatim(user_agent="GetLoc")

# entering the location name
getLocatn = locatn.geocode("jaipur")

# printing address
print(getLocatn.address)

# printing latitude and longitude
print("Latitude = ", getLocatn.latitude, "\n")
print("Longitude = ", getLocatn.longitude)
