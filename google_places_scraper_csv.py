import json  #for reading oauth info and save the results
import io 
import csv
from pandas.io.json import json_normalize
from googleplaces import GooglePlaces, types, lang
from pprint import pprint

with io.open('google_places_key.json') as cred:
    creds = json.load(cred)
    google_places = GooglePlaces(**creds)

    results = []
    #Put your lantitude and longtitude pairs in the list and run the search in turns
    lat_lng_list = [{'lat': 42.5050848, 'lng': 1.5116108},  #Andorra la Vella
                    {'lat': 42.542445, 'lng': 1.7281864},  #El Pas de la Casa
                    {'lat': 42.5434343, 'lng': 1.5056623}] #La Massana
    for pair in lat_lng_list:
        query_result = google_places.nearby_search(
            lat_lng = pair, rankby = 'distance', types = [types.TYPE_FOOD])

        for place in query_result.places:
            place.get_details()
            tmp = {}
            tmp['place_id'] = place.place_id
            tmp['formatted_address'] = place.formatted_address
            tmp['local_phone_number'] = place.local_phone_number
            tmp['lat'] = place.geo_location['lat']
            tmp['lng'] = place.geo_location['lng']
            tmp['types'] = place.types
            tmp['name'] = place.name
            tmp['url'] = place.url
            results.append(tmp)
                
    '''
    with open('my_boston_restaurants_google_places.json', 'wb') as f:
        results_json = json.dumps(results, indent=4, skipkeys=True, sort_keys=True)
        f.write(results_json)
    '''
    
    t = json_normalize(results)
    t.to_csv('google_places_andorra.csv', encoding='utf-8')

