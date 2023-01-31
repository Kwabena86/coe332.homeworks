

Part 1
	 The first part of the project is to write a python script that randomly generate latitude and longitude that has a composition of five meteorite landing sites. The script will generate a random pair of latiitudes from region between 16.0 to 18.0 degree North, and also a pair of longitude from 82.0 to 84.0 degree East. The landing site for the robot is choosen randomly to a meteorite composition from a list [stony, iron,stony-iron]. A data called json file is generated and that will be used to calculate trips in part 2 of the project.
 


Part 2
	The second python script will use the data generated in part 1 the robot,called the json file data, the robot will start at the latitude and the longitude specified in part 1.In an assumption that the robot will visit five different site in other of the list index stated. The maximum speed of the robot will be set a 10 km per hour. Any time the robots stops, it takes a sample of each meteorite and the amount of stop depends on the composition of the meteorite. Stony meteorite takes 1 hour, Iron takes 2 hours and stony-iron takes 3 hiurs. The robots trips is over after sampling the last meteorite. All outcome will studied and summarize at each leg of the trip,the summary outcome will then be printed for the whole trip. 
