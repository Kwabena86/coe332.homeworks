






import json

import random



my_lat = []

my_long = []

my_meteo_composition = ["stony", "iron", "stony_iron"]

my_sites = {}

my_sites["my_sites"] = []

for i in range(5):

        my_lat.append(random.uniform(16.0,18.0))

        my_long.append(random.uniform(82.0,84.0))

        my_sites["my_sites"].append({"my_site_id":i+1, "my_lat":my_lat[i], "my_long":my_long[i], "composition": random.choice(my_meteo_composition)})



with open('data.json', 'w') as out:

       json.dump(my_sites, out, indent=2)







