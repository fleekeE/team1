import math
from algo import *
from in_out import *
import numpy as np


def main(filename):

    # Read in waypoints
    waypoints = readWaypointFile(filename)

    # Determine path
    path = determinePath(waypoints)

    # Export path
    for i in path:  # Print out order of Lat Long
    	print("Latitude: "+str(waypoints['latitude'][i])
    	      + " Longitude: "+str(waypoints['longitude'][i]))

    print(str(waypoints['latitude'][0]))

    waypointH = np.array(
        (waypoints['latitude'][0], waypoints['longitude'][0], waypoints['altitude'][0]))

    print(waypointH)


#donato
if __name__ == '__main__':
	main("waypoint_1.txt")
