import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

eqdata = json.load(infile)

json.dump(eqdata, outfile, indent=4)

list_of_eqs = eqdata['features']

mags,lats,lons,hover_texts = [],[],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]
    title = eq['properties']['title']
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
    hover_texts.append(title)

print(mags[:5])
print(lats[:5])
print(lons[:5])
#only first 5 elements

#data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*m for m in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]

#for m in mags:
#   m*5


my_layout = Layout(title="Global Earthquake 1 Day")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='globalarthquakes1day.html')


