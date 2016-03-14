import json  #for reading oauth info and save the results
import io  #for credential read 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from pprint import pprint  #to better understand the result format

with io.open('yelp_oauth.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    zipstr = '02108, 02109, 02110, 02111, 02113, 02114, 02115, 02116, 02118, 02119, 02120, 02121, 02122, 02124, 02125, 02126, 02127, 02128, 02129, 02130, 02131, 02132, 02134, 02135, 02136, 02151, 02152, 02163, 02199, 02203, 02210, 02215, 02467'
    zips = zipstr.split(', ')

    params = {
            'lang': 'en',
            'sort': 0  #Sort mode: 0=Best matched (default), 1=Distance, 2=Highest Rated
           #'limit': 20   limit can be 1 to 20
           #'offset': 21  we will use this parameter later in the loop
    }

    results = []

    for zipcode in zips:
        for i in range(50):
            n = i * 20 + 1
            params['offset'] = n
            response = client.search(zipcode, **params)
            bizs = response.businesses
            for biz in bizs:
                b = vars(biz)
                b['location'] = vars(biz.location)
                b['location']['coordinate'] = vars(biz.location['coordinate'])
                results.append(b)
                                
            if len(response.businesses) < 20:
                break
            else:
                continue

    with open('my_boston_restaurants_yelp.json', 'wb') as f:
        results_json = json.dumps(results, indent=4, skipkeys=True, sort_keys=True)
        f.write(results_json)
