                                                                                     PART ONE

                                                                  BUDDY FLASK (INTERNATIONAL SPACE STATION(ISS) TRACKER)

This project is based on realtime data that provides us information ISS that helps to determine the speed and location of the system depending on the data collected.The data contains ISS state vectors over an ~15 day period.The determination of speed and the location of the ISS depending on when the data was collected.The speed and location may vary.The data collected helps to get interesting information from the ISS data sets. 


                                                                                    DATA RETRIEVED

The data used fro the project is accessed from the the url link from ISS Trajectory Data website (url:https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml).The from the site https://spotthestation.nasa.gov/trajectory_data.cfm. The url link is loaded into the script through API request from the python requests library.By performing these commands to get access to the data.

  install: pip3 install flask
  install: pip3 install requests
  install: pip3 install xmltodict
  import xmldodict
  import requests


                                                                                     PARTS TWO
Writing Flask application that runs the application on the local port. The application will queries data form the ISSposition and velocity. The curl route will be used to run the data sets in other to get our requests from the Flask application. The Routes used are as follows.

         ROUTES                         RETURS(OUTPUTS)
           /                          The entire data set
          /epochs                     A list of all Epochs in the data set
          /epochs/<epoch>             State vectors for a specific Epoch from the data set
          /epochs/<epoch>/speed       Instantaneous speed for a specific Epoch in the data set (math required!)
                            

                                                                                     INSTUCTIONS CURL OUTPUT
The following commands should be run in terminal to other to run flask.

    flask --app iss_tracker --debug run

This command will start the flask terminal,the command should be exercuted on a different terminal.The following routes should be exercuted with the curl requests to achieved the expected results.
    
                                                                                     ROUTES COMMANDS USING CURL
    
   1.  curl localhost:5000/
    
    The command should returns the following output represent the path of the data set from ISS 
 {
 "EPOCH": "2023-063T11:59:00.000Z",
 "X": { 
     "#text": "2511.5681106492402",
     "@units": "km"
     },
 "X_DOT": {
     "#text": "5.2410359153923798",
     "@units": "km/s"
"Y":{
    "#text": "-5991.3267501460596",
    "@units": "km"
     },
"Y_DOT": {
         "#text": "0.32894397165270001",
         "@units": "km/s"
     }
"Z":{
    "#text": "1991.1683453687999",
    "@units": "km" }, 
"Z_DOT":{
    "#text": "-5.57976406061041",
    "@units": "km/s"
                                                         }
     },
   
   ]



    2  curl localhost:5000/epochs
    
    The command returns the following output of the epoch data set value as shown below
   [
     "2023-048T12:00:00.000Z"
   ]



   3. curl localhost:5000/epochs/<epoch>

    The command returns the following output of the state vector of the specific epoch specified in the angled brackets as shown below
    {
     "EPOCH": "2023-048T12:00:00.000Z",
     "X": {
         "#text": "-5097.51711371908",
         "@units": "km"
                              },
     "X_DOT": {
         "#text": "-4.5815461024513304",
         "@units": "km/s"
     },
     "Y": {
         "#text": "1610.3574036042901",
         "@units": "km"
                                  },
     "Y_DOT": {
         "#text": "-4.8951801207083303",
         "@units": "km/s"
     },
     "Z": {
         "#text": "-4194.4848049601396",
         "@units": "km"
     },
     "Z_DOT": {
         "#text": "3.70067961081915",
         "@units": "km/s"
         }
     }



   4. curl localhost:5000/epochs/<epoch>/speed

    The command returns the following output of the epoch speed in the angled brackets as shown below
    {
            "Cartesian velocity vector_speed": 7.658223206788738
    }




                            
