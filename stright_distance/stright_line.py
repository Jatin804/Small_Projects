
# Finding best routs using python libraries

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geocoder = Nominatim(user_agent="user")

location1 = input("Enter the first location: ")
location2 = input("Enter the second location: ")

coord1 = geocoder.geocode(location1)
coord2 = geocoder.geocode(location2)

# to print the coordinates of location1 and location2
# print(coord1.longitude, coord1.latitude)

lat1, long1 = coord1.latitude, coord1.longitude
lat2, long2 = coord2.latitude, coord2.longitude

place1 = (lat1, long1)
place2 = (lat2, long2)

print("The distance between the two locations is: ", geodesic(place1, place2).kilometers, "km")
