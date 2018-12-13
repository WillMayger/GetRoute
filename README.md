# GetRoute

# A python application to automate getting route coordinates for a map path.

# To use:
 - clone repo
 - `pip install .`
 - `python getRoute.py -f myfilename.js -v myglobalvariablename -c lng:-1.553632,lat:47.216702 lng:-1.2776176,lat:47.2872625 lng:-0.551790,lat:47.470566`
 - This will output the coordinates as a global variable in a javescript file that you provided the name for.

# API

## -f: filename
- Use this flag to input a filename of your choice.
- Should always be a .js file

## -v: variable name
- Use this flag to input the variable name of which you want to save all your coordinates to.

## -c: coordinates
- Use this to input all the stops/main points on your route
- This must be in the order that you want the route to follow.
- Format should be: `lng:LONG_COORD,lat:LAT_COORD lng:LONG_COORD,lat:LAT_COORD` (A new item in the list is created by a space, NOT A COMMA)
- An Example for an A to B route: `lng:-1.553632,lat:47.216702 lng:-1.2776176,lat:47.2872625`
- An Example for an A to B to C route: `lng:-1.553632,lat:47.216702 lng:-1.2776176,lat:47.2872625 lng:-0.551790,lat:47.470566`
- You can add in as many stops as you like.