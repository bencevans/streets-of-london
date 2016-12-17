#!/usr/bin/env python

from mapnik import *

mapfile = 'mapnik_style.xml'
map_output = 'out.png'

m = Map(8 * 1024, 4 * 1024)
load_map(m, mapfile)
bbox=(Envelope(-0.611482, 51.2855, 0.415437, 51.6934))

m.zoom_to_box(bbox)
print "Scale = " , m.scale()
render_to_file(m, map_output)
