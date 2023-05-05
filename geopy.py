# id.city
#Find the location with a few simple texts
from geopy.geocoders import *
import time
from pprint import *
app = Nominatim(user_agent="ir")
location = app.geocode("tehran iran").raw
#city ​​and country^
pprint(location)
def get_location_by_address(address):
    """This script will find your address"""
    time.sleep(1)
    #a certain period of time^
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)
address = "Akbatan"
#Write your position^
location = get_location_by_address(address)
latitude = location["lat"]
longitude = location["lon"]
print(f"{latitude}, {longitude}")
pprint(location)
