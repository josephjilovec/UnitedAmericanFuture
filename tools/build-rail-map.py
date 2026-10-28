#!/usr/bin/env python3
"""Build a concept map from public-domain Natural Earth land outlines.
Candidate connections and approximate city centers are design hypotheses, not rail alignments.
"""
from pathlib import Path
import math,json,html
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'assets/rail/land-outline.json'
phi1,phi2,phi0,lam0=map(math.radians,[29.5,45.5,37.5,-96])
n=(math.sin(phi1)+math.sin(phi2))/2
C=math.cos(phi1)**2+2*n*math.sin(phi1)
rho0=math.sqrt(C-2*n*math.sin(phi0))/n

def project(lon,lat):
 phi,lam=map(math.radians,[lat,lon]);rho=math.sqrt(C-2*n*math.sin(phi))/n;theta=n*(lam-lam0)
 return rho*math.sin(theta),rho0-rho*math.cos(theta)
features=json.loads(DATA.read_text())['features']
def polygons(f):
 g=f['geometry'];return g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
us=next(f for f in features if f['properties']['ADMIN']=='United States of America')
contig=[p for p in polygons(us) if all(-126<=x<=-66 and 24<=y<=50 for x,y,*_ in p[0])]
assert contig,'Missing continental US geometry'
points=[project(x,y) for p in contig for ring in p for x,y,*_ in ring]
x0,x1=min(p[0] for p in points),max(p[0] for p in points);y0,y1=min(p[1] for p in points),max(p[1] for p in points)
scale=min(1220/(x1-x0),580/(y1-y0));padx=(1400-(x1-x0)*scale)/2;pady=100+(580-(y1-y0)*scale)/2

def xy(lon,lat):
 x,y=project(lon,lat);return padx+(x-x0)*scale,pady+(y1-y)*scale

def landpath(f):
 parts=[]
 for polygon in polygons(f):
  for ring in polygon:
   q=[xy(x,y) for x,y,*_ in ring]
   parts.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'Z')
 return ''.join(parts)
cities={
 'seattle':(-122.33,47.61),'portland':(-122.68,45.52),'sf':(-122.42,37.77),'la':(-118.24,34.05),'sd':(-117.16,32.72),
 'slc':(-111.89,40.76),'vegas':(-115.14,36.17),'phoenix':(-112.07,33.45),'denver':(-104.99,39.74),
 'kc':(-94.58,39.10),'minneapolis':(-93.27,44.98),'stl':(-90.20,38.63),'chicago':(-87.63,41.88),
 'dfw':(-96.80,32.78),'houston':(-95.37,29.76),'austin':(-97.74,30.27),'sa':(-98.49,29.42),
 'neworleans':(-90.07,29.95),'atlanta':(-84.39,33.75),'jax':(-81.66,30.33),'miami':(-80.19,25.76),
 'detroit':(-83.05,42.33),'cleveland':(-81.69,41.50),'pittsburgh':(-80.00,40.44),
 'dc':(-77.04,38.91),'ny':(-74.01,40.71),'boston':(-71.06,42.36)
}
families={
 'pacific':{'name':'Pacific','color':'#328ff1','routes':[['seattle','portland','sf','la','sd']]},
 'mountain':{'name':'Mountain','color':'#0d9996','routes':[['portland','slc','denver'],['denver','phoenix','vegas','la']]},
 'central':{'name':'Central','color':'#d09b26','routes':[['denver','kc','chicago','minneapolis'],['chicago','stl','dfw','houston'],['denver','dfw'],['dfw','austin','sa']]},
 'gulf':{'name':'Gulf & Southeast','color':'#3f8d50','routes':[['houston','neworleans','atlanta','jax','miami'],['atlanta','dc']]},
 'northeast':{'name':'Northeast & Great Lakes','color':'#8255bb','routes':[['chicago','detroit','cleveland','pittsburgh','dc','ny','boston']]}
}
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 820" role="img" aria-labelledby="map-title map-desc">',
'<title id="map-title">Iron Corridor national network concept</title>',
'<desc id="map-desc">A concept map exploring Denver, Chicago and Houston as potential hubs, with five candidate corridor families across the continental United States. Connections are illustrative, not engineered routes, station sites, approved projects or an operating service. Dallas/Fort Worth is shown once, in Texas.</desc>',
'<defs><clipPath id="land-clip"><rect x="25" y="78" width="1350" height="635" rx="8"/></clipPath></defs>',
'<rect width="1400" height="820" rx="10" fill="#0a213c"/>',
'<text x="42" y="38" fill="#e7c45a" font-family="Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="2">IRON CORRIDOR / NATIONAL NETWORK CONCEPT</text>',
'<text x="42" y="62" fill="#cbd8e7" font-family="Arial,sans-serif" font-size="14">Three proposed hubs. Regional corridors evaluated individually. No selected alignments.</text>',
'<g clip-path="url(#land-clip)"><rect x="25" y="78" width="1350" height="635" fill="#c9dce8"/>']
for f in features:
 if f['properties']['ADMIN']!='United States of America':svg.append(f'<path d="{landpath(f)}" fill="#b6c5c8" stroke="#9baeb8" stroke-width="1"/>')
svg.append(f'<path d="{landpath(us)}" fill="#f0ebdf" stroke="#8198a4" stroke-width="1.5"/>')
for key,f in families.items():
 svg.append(f'<g id="family-{key}" fill="none" stroke="{f["color"]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" opacity=".92"><title>{html.escape(f["name"])} candidate connections</title>')
 for route in f['routes']:
  q=[xy(*cities[c]) for c in route];svg.append('<path d="M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'"/>')
 svg.append('</g>')
for key,coords in cities.items():
 x,y=xy(*coords);hub=key in ['denver','chicago','houston']
 if hub:svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="#0a3161" stroke="#e7c45a" stroke-width="5"/>')
 else:svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.8" fill="#fff" stroke="#153e66" stroke-width="2"/>')
labels={
 'seattle':('Seattle',15,-10),'sf':('San Francisco',-10,-14),'la':('Los Angeles',-20,28),'slc':('Salt Lake City',-8,-16),
 'phoenix':('Phoenix',-12,26),'denver':('DENVER',18,-17),'chicago':('CHICAGO',-80,-25),'dfw':('Dallas/Fort Worth',-112,-14),
 'houston':('HOUSTON',20,25),'neworleans':('New Orleans',18,16),'atlanta':('Atlanta',-14,-18),'miami':('Miami',15,18),
 'dc':('Washington',10,22),'ny':('New York',20,2),'boston':('Boston',15,-7)
}
for key,(label,dx,dy) in labels.items():
 x,y=xy(*cities[key]);hub=key in ['denver','chicago','houston'];size=19 if hub else 15
 svg.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" fill="#082546" font-family="Arial,sans-serif" font-size="{size}" font-weight="700" stroke="#f0ebdf" stroke-width="5" paint-order="stroke" stroke-linejoin="round">{html.escape(label)}</text>')
svg.append('</g>')
x=42
for key,f in families.items():
 label=html.escape(f['name']);width=180 if key not in ['gulf','northeast'] else 240
 svg.append(f'<path d="M{x} 747h26" stroke="{f["color"]}" stroke-width="5" stroke-linecap="round"/><text x="{x+37}" y="752" fill="#e4edf7" font-family="Arial,sans-serif" font-size="13">{label}</text>');x+=width
svg += ['<circle cx="43" cy="784" r="7" fill="#0a3161" stroke="#e7c45a" stroke-width="3"/><text x="61" y="789" fill="#d8e3ee" font-family="Arial,sans-serif" font-size="12">Potential hub</text>',
'<text x="225" y="789" fill="#b8cadb" font-family="Arial,sans-serif" font-size="12">Illustrative connections only · Approximate city centers · Land outlines: Natural Earth</text>','</svg>']
result='\n'.join(svg)+'\n';(ROOT/'assets/rail/network-concept.svg').write_text(result)
assert result.count('>Dallas/Fort Worth</text>')==1
assert all(result.count('>'+hub+'</text>')==1 for hub in ['DENVER','CHICAGO','HOUSTON'])
assert -98<cities['dfw'][0]<-95 and 32<cities['dfw'][1]<34
print('Built map: 3 proposed hubs, 5 families, 27 approximate city centers; Dallas/Fort Worth appears once in Texas.')
