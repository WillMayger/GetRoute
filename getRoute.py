import requests
import argparse

class getRoute:
  def __init__(self, filename, coordinates, varname):
    self.apiCall = 'http://router.project-osrm.org/route/v1/driving/%s?overview=false&geometries=geojson&steps=true' % (coordinates)
    self.coords = []
    self.filename = filename
    self.varname = varname

  def get_geo_json(self):
    # call the api
    res = requests.get(self.apiCall)

    # save json res to class variable
    self.geojson = res.json()

  def extract_coords(self):
    print('extracting coords...')
    start = self.geojson['routes'][0]

    # loop over each item in each array to get all coordinates
    for leg in start['legs']:
      for step in leg['steps']:
        for coord in step['geometry']['coordinates']:
          # append each coordinate in order to class List variable 
          self.coords.append({ 'lng': coord[0], 'lat': coord[1] })
    print('All coords collected to .coords')
  
  def create_file(self):
    # create or open a file with the filename provided
    f = open(self.filename, 'w+')
    # save coordinates as a global variable (.js)
    f.write('window.%s = %s;' % (self.varname, str(self.coords)))
    # close file
    f.close()
    print('file saved to "%s"' % (self.filename))

  def go(self):
    # run all methods that are required
    self.get_geo_json()
    self.extract_coords()
    self.create_file()


# Get args passed in from terminal
parser = argparse.ArgumentParser(description='Create a file with a global variable with coordinates stored inside.')

parser.add_argument('-f', help='Filename to be saved. ( .js )')
parser.add_argument('-v', help='Variable name to be used. ( myvariable )')
parser.add_argument('-c', nargs='+', help='Coordinates to be used. ( lng:-2.0089883,lat:43.3072873 lng:-1.7200615,lat:42.8157447 )')

args = parser.parse_args()

# Sort args passed in
coords = ';'.join(args.c)
coords = coords.replace('lat:', '').replace('lng:', '')

# Make sure coords exists
if coords != '' or coords != None:
  # Set some defaults
  filename = 'mycoords.js'
  variablename = 'myvariable'


  # overwrite defaults if they have passed them in as an arg
  if args.f != None:
    filename = args.f

  if args.v != None:
    variablename = args.v

  # Create instance of getRoute with provided args
  instance = getRoute(filename, coords, variablename)

  # Run instance
  instance.go()

