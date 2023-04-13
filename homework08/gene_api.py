import os
from flask import Flask,request, send_file
import requests
import redis 
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date
import io

app = Flask(__name__)

def get_redis_client():
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    rd=redis.Redis(host=redis_ip, port=6379, db=0)
    return rd
def get_redis_image_db():
    redis_ip = os.environ.get('REDIS-IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=1)

rd = get_redis_client()

rd_image = get_redis_image_db()





@app.route('/image', methods = ['POST', 'GET', 'DELETE'])
def ret_image():
    """
    Handles image data with the application og  GET, POST, and DELETE methods
    
    Args: N/A
    Methods:
        The "DELETE" method: deletes all data in the redis database
        The "POST" method: posts data into redis database
        The "GET" method: returns data from redis database
    Returns:
        The "DELETE":Will return a string confirming data deletion
        The "POST": Will returna  string confirming data posted
        The "GET" : will returns data from redis db in the form of a list of dictionaries
        
    """


    if request.method == 'GET':
        plot_bytes = rd_image.get("Plot")

        
        buf = io.BytesIO(plot_bytes)
        buf.seek(0)
        
        return send_file(buf, mimetype='image/png')
        
            
    elif request.method == 'POST':
        daysSince2000List = []
        HGNClist = []
        for item in rd.keys():
            
            value = rd.get(item).decode('utf-8')
            value = json.loads(value)
            date_str = value["date_approved_reserved"]
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            reference_date = date(2000, 1, 1)
            delta = parsed_date - reference_date
            days_since_2000 = delta.days
            daysSince2000List.append(days_since_2000)
            HGNClist.append(int(value["hgnc_id"][5:]))

        fig, ax = plt.subplots()
        ax.scatter(daysSince2000List, HGNClist,s=5,alpha=0.5)
        ax.set_title('ID Number vs Date Approved')
        ax.set_xlabel('Day approved since 2000')
        ax.set_ylabel('HGNC ID number')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        rd_image.set("Plot", buf.getvalue())

        return 'Data has been posted\n'

    elif request.method == 'DELETE':
        rd_image.flushdb()
        return f'Data deleted. There are {len(rd.keys())} plots in the db\n'

    
    
    else:
        return 'the method you tried does not work\n'



app.route('/data', methods=['POST','GET','DELETE'])
def ret_data():
    
    """
    This operates by manipujating the data with GET,POST,DELETE methods
    Args: N/A
    Methods:
        "GET" method: returns data from redis db
        "POST" method: Post data into the redis db
        "DELETE" method: Deletes all data from redis db
    
    Returns:
        ""DELETE"" method: String confirmimg data that was deleted
        "POST" method : Comfirms posted data in string""
        ""GET"" method : Returns a list of dictionaries from the redis db
    """


    if request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list


    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            rd.set(key,json.dumps(item))
        return 'Data has been posted\n'


    elif request.method == 'DELETE':
        rd.flushdb()
        return f'Data had neen deleted. There are {len(rd.keys())} keys in the db\n'



    else:
        return 'Method requested you tried does not work\n'



@app.route('/genes', methods=['GET'])
def get_hgnc_list() -> list:


    """
    This creates and returns a list of all hgnc_ids
    Args: N/A
    Returns:
        hgnc_list: List all the hgnc IDs
    """

    hgnc_list = []

    for key in rd.keys():
        key = key.decode('utf-8')
        hgnc_list.append(key)
    return hgnc_list


@app.route('/genes/<hgnc_id>', methods=['GET'])
def get_hgnc(hgnc_id) -> dict:


    """
    Returns all data associated with <hgnc_id>
    Args:
        hgnc_id : The unique hgnc ID of the genes in the data set
    Returns:
        Tha data associated with the given <hgnc_id>
    """

    if len(rd.keys()) == 0:
        return 'Empty database, Please post the data first\n'


    for key in rd.keys():
        if key.decode('utf-8') == hgnc_id:
            return json.loads(rd.get(key))

    return 'The hgnc_id did not match any in the database\n'




if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
