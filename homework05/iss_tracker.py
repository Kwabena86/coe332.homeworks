
from flask import Flask,request
import requests
import xmltodict 
import math


app = Flask(__name__)



def get_data():
    """
    The function returns all of the data in the corresponding ste
    
    Args:
        N/A
   
   Returns:
        List of dictionaries that will represent the collected data in the set of ISS locations
    """

    url ='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    return data['ndm']['oem']['body']['segment']['data']['stateVector']


data = get_data()

# The defaul curl command method without more aguments


@app.route('/', methods=['GET'])
def location():
    """
    The funtion returns all the data in the set

    Args:
        N/A
    Returns:
        List of dictionaries that will represent the collected data in the set of ISS loctions
    """
    try:
        data = get_data()
        return data
    except NameError:
        return "Data has been deleted, must be repost first using /post-data\n"
    return data



@app.route('/epochs/', methods= ['GET'])
def all_Epochs():

    """
    This function returns all of the EPOCHs in the set

    Args:
        N/A
    Returns:
        It will return a list of strings the represents the EPOCHs in the data set
    """


    data = get_data()

    try:
        limit = int(request.args.get('list',10))
    except ValueError:
        return "Error input. Please enter ant integer\n",400
    
    try:
        offset = int(request.args.get('offset', 0))
    except ValueError:
        return 'Error input. Please enter ant integer\n",400'


    epochs = []
    total_Results = 0
    index = 0
    for e in data:
        if (total_Results == limit):
            break
        if (index >= offset):
             epochs.append(e['EPOCH'])
             total_Results+= 1
      
        index += 1
    return epochs



@app.route('/epochs/<epoch>', methods=['GET'])
def specific_Epoch(epoch):
    """
    The funtion take a perticular EPOCHs string value and returns its state vector 

    Args:
        N/A

    Returns:
        Returns a specific data for a perticular epoch
    """
    data = get_data()

    try: 
        for e in data:
            if (e['EPOCH'] == epoch):
                return e
    except NameError:
        return "Data has been deleted, must be repost first using /post-data\n "
    return 'Epoch value error, not found\n'

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def epoch_Speed(epoch):

    """
    It take in a specific EPOCH string values for a particular time duration that is recorded for the ISS

    Args:
        (String) epoch: EPOCH string value for a particular time that is recorded for the ISS

    Returns:
        The speed of the ISS at the given EPOCH

    """
    data = get_data()
    for e in data:
            if (e['EPOCH'] == epoch):
                vec_x = float(e['X_DOT']['#text'])
                vec_y = float(e['Y_DOT']['#text'])
                vec_z = float(e['Z_DOT']['#text'])
                cart_vel_Vector_speed = math.sqrt(vec_x**2 +vec_y**2 + vec_z**2)
                return {"Cartesian velocity vector_speed":cart_vel_Vector_speed}
    return 'Epoch value error, not found\n'


@app.route('/delete-data', methods=['DELETE'])
def delate_Data():
    """
    The funtion deletes the global data object dictionary

    Args:
        N/A

    Returns:
        A data delete comfirmation message if calling the data variable which causes a NamrError
    """
    data = get_data()

    try:
        del data
    except NameError:
        return  "Data has been deleted, must be repost first using /post-data\n "
    return "Data deleted\n"



@app.route('/help', methods=['GET'])
def help() -> str:
    
    """
    The funtion return all tools needed in a summary discrption of all associated and avaailable routes and thier corresponding methods for this API

    Args:
        N/A

    Returns:
        Outputs in a form of text that enumerate all available routes and its corresponding methods

    """
    return '''
    Available Routes:
    
    GET / 
    Return entire data set


    GET /epochs
    Return list of all Epochs in the data set

    GET /epochs?limit=int&offset=int
    Return modified list of Epochs given query parameters

    GET/ epochs/<epoch>
    Return state vectors for a specific Epoch from the data set

    GET /epochs/<epoch>/speed
    Return instantaneous speed for a specific Epoch in the data set (math required!)

    GET /help
    Return help text (as a string) that briefly describes each route

    DELETE /delete-data
    Delete all data from the dictionary object

    POST /post-data
    Reload the dictionary object with data from the web

    '''


@app.route('/post-data', methods=['POST'])
def post_Data():

    """
    The function post data to the global data dictionary objects

    Args:
        N/A

    Returns:
        Data Post Successfully after setting the global data variable to the requested data sets
    """
    data = get_data()

    return "Data Posted\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
