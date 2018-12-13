import requests
import argparse

class main:
  def __init__(self, filename, coordinates, varname):
    self.apiCall = 'http://router.project-osrm.org/route/v1/driving/%s?overview=false&geometries=geojson&steps=true' % (coordinates)
    self.coords = []
    self.filename = filename
    self.varname = varname

  def get_geo_json(self):
    res = requests.get(self.apiCall)
    self.geojson = res.json()

  def extract_coords(self):
    print('extracting coords...')
    start = self.geojson['routes'][0]

    for leg in start['legs']:
      for step in leg['steps']:
        for coord in step['geometry']['coordinates']:
          self.coords.append({ 'lng': coord[0], 'lat': coord[1] })
    print('All coords collected to .coords')
  
  def create_file(self):
    f = open(self.filename, 'w+')
    f.write('window.%s = %s;' % (self.varname, str(self.coords)))
    f.close()
    print('file saved to "%s"' % (self.filename))


parser = argparse.ArgumentParser(description='Create a file with a global variable with coordinates stored inside.')

parser.add_argument('-f', help='Filename to be saved. ( .js )')
parser.add_argument('-v', help='Variable name to be used. ( myvariable )')
parser.add_argument('-c', nargs='+', help='Coordinates to be used. ( lng:-2.0089883,lat:43.3072873 lng:-1.7200615,lat:42.8157447 )')

args = parser.parse_args()


coords = ';'.join(args.c)
coords = coords.replace('lat:', '').replace('lng:', '')

if coords != '' or coords != None:
  filename = 'mycoords.js'
  variablename = 'myvariable'


  if args.f != None:
    filename = args.f

  if args.v != None:
    variablename = args.v

  inst = main(filename, coords, variablename)

  inst.get_geo_json()
  inst.extract_coords()
  inst.create_file()
