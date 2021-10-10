import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('US_fires_9_14.json','r')

firedata = json.load(infile)

brightness,lats,lons,hover_texts = [],[],[],[]

for fire in firedata:
    lat = fire['latitude']
    lon = fire['longitude']
    bright = fire['brightness']
    title = fire['acq_date']
    if bright > 450:
        brightness.append(bright)
    lats.append(lat)
    lons.append(lon)
    hover_texts.append(bright)



print(brightness[:20])
print(lats[:5])
print(lons[:5])

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[0.05*b for b in brightness],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]



my_layout = Layout(title="Fire Brightness 9/14-9/20")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='firebrightness9-14.html')

