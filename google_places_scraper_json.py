import json  #for reading oauth info and save the results
import io 
from googleplaces import GooglePlaces, types, lang
from pprint import pprint

with io.open('google_places_key.json') as cred:
    creds = json.load(cred)
    google_places = GooglePlaces(**creds)

    result = []
    #Put your lantitude and longtitude pairs in the list and run the search in turns
    lat_lng_list = [{'lat': 2.356357, 'lng': -71.0623345},  #Park Street Station
                    {'lat': 42.356357, 'lng': -71.0623345},  #China Town Station
                    {'lat': 42.3555885, 'lng': -71.0646816}] #Downtown Crossing Station
    for pair in lat_lng_list:
        query_result = google_places.nearby_search(
            lat_lng = pair, rankby = 'distance', types = [types.TYPE_FOOD])

        for place in query_result.places:
            place.get_details()
            tmp = vars(place)
            results.append(tmp)
                
    with open('my_boston_restaurants_google_places.json', 'wb') as f:
        results_json = json.dumps(results, indent=4, skipkeys=True, sort_keys=True)
            f.write(results_json)
