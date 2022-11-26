##Simple Cave Proc Gen
___
###What is it?
This is a simple, numpy based cave generator for games built in python. 
###How does it work?
The generator uses a mix of A* and Drunkards walk to generate a cave. 
The steps are as follows:
- create the map grid
- create a number of random starting points for the larger caves
- iteratively use drunkards walk to create the larger caves at the starting points
- use A* to connect the larger caves, using drunkards walk at each step of the path, 
using random heuristic functions from a list to increase variation
- validates that all starting points are connected, this makes sure that the whole system is connected
if this fails recursively generate a new map, this is fast and fairly cheap

###How do I use it?

```python
from cave_carver import make_caves

caves = make_caves(
    size=(120, 120),
    max_attempts=3,
    num_rooms=7,
    num_corridors=9,
    room_min_steps=30,
    room_max_steps=80,
    room_iterations=30,
    room_max_distance_from_start=None,
    corridor_min_steps=3,
    corridor_max_staps=10,
    corridor_max_distance_from_start=6,
    border_padding=20,
    min_room_distance=20,
    carvable_values=[0, 1],
    passable_values=[1],
    carve_value=1,
    heuristic_methods=[
        'euclidean', 
        'octile', 
        'manhattan', 
        'chebyshev'
    ],
)
```

`size`: Size of the map grid

`max_attemps`: How many times it will try and generate a cave system with these settings

`num_rooms`: number of large cave will be generated

`num_corridors`: number of connecting corridors

`room_min_steps` and `room_max_steps`: the range of steps that will be taken by the drunkards walk for the rooms

`room_iterations`: number of times to run drunkards walk per room

`room_max_distance_from_start`: only useful for larger maps, use to control how far from the starting point 
drunkards walk can go

`corridor_min_steps`, `corridor_max_steps` and `corridor_max_distance_from_start`: Same as the room variants, but for corridors

`border_padding`: padding from edge for the center of the rooms

`min_room_distance`: minimum distance between rooms

`carve_value`: the value that carved caves will yield

`carvable_values`: the values allowed to be carved

`passable_values`: used for validating the map

`heuristics_methods`: a list or heuristic function names that will be used for corridor generation, namely
`'euclidean'`, `'octile'`, `'manhattan'` and `'chebyshev'`



###What does it look like?
![cave_0](examples/cave_0.png)

![cave_1](examples/cave_1.png)

![cave_2](examples/cave_2.png)

![cave_3](examples/cave_3.png)

![cave_4](examples/cave_4.png)