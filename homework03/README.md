
                  WATER EXAMINATION BY DETERMINING THE TURBIDITY CALCULTION AND WATER SAFETY

					PART 1

In part 1,the project calculate the turbidity of water and determine how safe the water is, the determination is based on the calculation output. On the condition if the water is safe or not, the script will calculate how long it willtake the water to be safe,according to turbidity decay.

					DATA

The data used in the expariment is accessed from the link https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json it is loaded into a script through the API request from the library of python.
Using 
	import requests
	import json
				
					EXERCUTION
In the case to calculate the turbidity of the water, the funtion turbidity_calc is used to perform the calculation. In accessing the safeness of the water, the function safe_threshold is used to get the data. 


					SCRIPTS
analyze_water.py
	This script determine the data collected from the requet list and outputs the water's turbidity, if the value is above or below the threshold, the system will prompt whether the water is safe or not, and indicate the time it will take to get back to the normal or below the threshold.

					PART 3
In this part, the test script is run using test.py, this script unit tests the funtion called test.py, the next step is to ensure your test.py pass the test or not. When the test.py run passes, the system will prompt 2 passes in 0.07s,to indication that your test script was succesful.
				
					INSTRUCTIONS TO RUN TEST
The test run should be performed in other to check if your test script will pass. 
	Run: pytest -q test.py to test
	System will indicate 2 passed in 0.07s to inducate success

When test.py is succesful, now you can run the scripts for turbidity_cala and safe_threhold to determine the status of the water safty. 
		
				OUTPUTS

Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours

Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours

The values will changed depending on the system output at a perticlar time. The output changes with time.


