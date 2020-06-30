import googlemaps
import pandas as pd
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from googlemaps.geocoding import geocode
from googlemaps import Client


def geocode_address(loc):
    gmaps = googlemaps.Client(key="", timeout=80000)
    geocode_result = gmaps.geocode(loc)
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
    except IndexError:
        print('third')
        return 0,0
    return lat,lon



# geocode_address('945 w 2000 n orem ut 84057')

df1 = pd.read_csv(r"/Users/colinmason/Desktop/price lab/USBE Schools Directory Export.csv")
df_address = df1['Address'] + ' ' + df1['City']

geolocator = Nominatim(user_agent='my-data',timeout=5000)


def distance_generator(address_list=df_address, origin_address='BYU'):
    coord_dump = []
    address_dump = []
    # origin_coord = (geolocator.geocode(origin_address).latitude, geolocator.geocode(origin_address).longitude)
    for address in address_list:
        try:
            address_dump.append(address)

            lat_loc2 = geolocator.geocode(address).latitude
            lon_loc2 = geolocator.geocode(address).longitude
            coord_dump.append((lat_loc2, lon_loc2))
            print('first')
        except AttributeError:
            loc3 = geocode_address(address)
            coord_dump.append(loc3)
            print('second')


    df5 = pd.DataFrame({'col1':address_dump, 'col2':coord_dump})
    return df5


f = distance_generator()


# print(f)
f.to_csv(r'/Users/colinmason/Desktop/price lab/addresses13.csv')

# TODO: check that coordinates are correct
# TODO: Create Distance function and execute
# TODO: Append Distances to spreadsheet






