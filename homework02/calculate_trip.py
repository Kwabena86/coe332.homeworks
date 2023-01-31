



import random


import math

def time_to_sample(the_composition):



    if (len(the_composition) == 5): 
        time_samp =  1
    elif (len(the_composition) == 4): 

         time_samp = 2
    else:                    

         time_samp = 3
    return time_samp
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float: lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( 3389.2 * d_sigma )
 
def time_traveled(distance_traveled):

     speed = 10 #km per hour 

     time = distance_traveled/speed

     return time
def main():

     with open('data.json', 'r') as f:
         ml_data = json.load(f)
     starting_latitude = 16.0
     starting_longitude = 82.0
     total_time = 0
     for i in range(len(ml_data['my_sites'])):


         distance = calc_gcd(starting_latitude,starting_longitude, ml_data['my_sites'][i]'my_lat'], ml_data['my_sites'][i]['my_long']) 

         total_time = total_time + time_traveled(distance) + time_to_sample(ml_data['my_sites'][i]['composition'])

         print("leg = " + str(i+1) + ", "  + "time to travel = " + str(time_traveled(distance)) + " hr" + ", "  + "time to sample = " + str (time_to_sample(ml_data['my_sites'][i]['composition'])) + " hr" )
         starting_latitude = ml_data['my_sites'][i]['my_lat']
         starting_longitude = ml_data['my_sites'][i]['my_long']
    print("==============================================")
    print("number legs = " + str(i+1) +  " , total time elapsed = " + str(total_time) + " hr")
if __name__ == '__main__':

     main()


                                                                                                                                                                                              
