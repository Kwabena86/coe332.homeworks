from flask import Flask
import requests
import xmltodict # Helps to access the xml data
import math


app = Flask(__name__)




# The function returns all data set, that represent the data the ISS provide at apprimately every 15 days.
# Present a list of dictionaries that represent data from ISS.


def get_data():
    
    url =' https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    return data['ndm']['oem']['body']['segment']['data']['stateVector']

 



# The function returns all data set, that represent all the data in set ISS provide at apprimately every 15 days.
# Present a list of dictionaries that represent data from ISS.

@app.route('/', methods=['GET'])
def location():
    

   data = get_data()
   return data





# The function returns all data set for 'EPOCH', that represent the data the ISS.
# Present a list of Strings dictionaries of 'EPOCH' sets.

@app.route('/epochs/', methods=['GET'])
def all_Epochs():
    data = get_data()
    epochs = []
    for e in data:
        epochs.append(e['EPOCH'])
        return epochs




# The function returns the state vector, by taking the EPOCH string values for a specific period of time.
# Present a dictionary of data given by a specific epoch.

@app.route('/epochs/<epoch>', methods=['GET'])
def specific_Epoch(epoch):
    data = get_data()
    for e in data:
        if (e['EPOCH'] == epoch):
            return e

    return 'Epoch value error, not found\n'


# The function takes a specific EPOCH string values and returns the cartasian vector velocity speed of the ISS at a particular epoch.EPOCH is a string value for a specific time by the data generated.
# Returns the speed of the ISS at a given EPOCH.

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def epochs_speed(epoch):
    data = get_data()
    for e in data:
        if (e['EPOCH'] == epoch):
            vec_x = float(e['X_DOT']['#text'])
            vec_y = float(e['Y_DOT']['#text'])
            vec_z = float(e['Z_DOT']['#text'])
            cart_vel_Vector_speed = math.sqrt(vec_x**2 +vec_y**2 + vec_z**2)
            return {'Cartesian velocity vector_speed': cart_vel_Vector_speed}

    return 'Epoch value error, not found\n'




if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

