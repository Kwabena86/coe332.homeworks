import json

import requests

import math


def turbidity_calc(calibration_constant: float , detector_current:float) -> float:
        
      #   This fuction take the input aguments of calibratio_constant and that of detector_current that will be use to calculate for turbidity_cal
        turbidity = calibration_constant * detector_current


        # Returns: This returns the calculation for the turbidity

        return turbidity


def safe_threshold(T0: float) -> float:

     # The function that input is the current turbidity and it returns hours elapsed untill the water is safe

    # T0 = is the current turbility

    d = 0.02

    return (-1* math.log(T0))/math.log(1-d) # A math funtion that returns hours until water is safe


def main():
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turb_data = response.json()['turbidity_data']
    
    turbidity = 0


    for i in  range(5):
        turb_current = turb_data[-i-1]
        
        turbidity += turbidity_calc(turb_current['calibration_constant'], turb_current['detector_current'])

    turbidity/=5
    b = 0


    if (turbidity > 1): # A condition the test the turbidity threshold, check if it is within the safe water constant

        b = safe_threshold(turbidity)
        
        print('Average turbidity baed on the most recent five measurement =',turbidity ,'NTU')
        print('Warning:Turbidity is above threshold for safe use')
        print('Minimum time requeted to return below a safe threshold = ',b, 'hours')


    else:
        print('Average turbidity based on the most recent five meassurement =',turbidity ,'NTU')
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time requested to return below a safe threshold =',b, 'hours')





if __name__ == '__main__':

    main()

 
