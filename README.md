# Streets of London

![Greater London](out.png)

**Related**

* Data source  http://download.geofabrik.de/europe/great-britain/england/greater-london-latest.osm.bz2
* Tutorial https://wiki.openstreetmap.org/wiki/Mapnik/Rendering_OSM_XML_data_directly

**Build Yourself** (Requires Docker)

```
$ docker build -t bencevans/streets-of-london .
$ docker run --rm -v $(pwd):/build bencevans/streets-of-london
```
