import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

eqdata = json.load(infile)

json.dump(eqdata, outfile, indent=4)

list_of_eqs = eqdata['features']

mags = []
lats = []
lons = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

print(mags[:5])
print(lats[:5])
print(lons[:5])
#only first 5 elements

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquake 1 Day")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='globalarthquakes1day.html')


