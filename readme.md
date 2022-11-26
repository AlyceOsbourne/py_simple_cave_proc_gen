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
- use A* to connect the larger caves, using drunkards walk at eeach step of the path, 
using random heuristic functions from a list to increase variation
- validates that all starting points are connected, this makes sure that the whole system is connected
if this fails recursively generate a new map, this is fast and fairly cheap

###How do I use it?

```python
from cave_carver import make_caves

caves = make_caves(
    size=(120, 120),                    # the width and height of the map
    max_attempts=100,                   # the maximum number of attempts to generate a map
    num_rooms=7,                        # the number of larger caves to generate
    num_corridors=9,                    # the number of corridors to generate
    room_min_steps=30,                  # the minimum number of steps for drunkards walk to take
    room_max_steps=70,                  # the maximum number of steps for drunkards walk to take
    room_iterations=30,                 # the number of times to run drunkards walk for each room
    room_max_distance_from_start=None,  # the maximum distance from the starting point for drunkards walk to take
    corridor_min_steps=3,               # the minimum number of steps for drunkards walk to take for corridors
    corridor_max_staps=5,               # the maximum number of steps for drunkards walk to take for corridors
    corridor_max_distance_from_start=6, # the maximum distance from the starting point for drunkards walk to take for corridors
    border_padding=20,                  # the padding around the edge of the map
    min_room_distance=15,               # the minimum distance between rooms
    carvable_values=[0, 1],             # the values that can be carved
    passable_values=[1],                # the values that are passable, used to validate the map
    carve_value=1,                      # the value carving will use
    heuristic_methods=[                 # the heuristic methods to use for A*
    'euclidean', 
    'octile', 
    'manhattan', 
    'chebyshev'], 
)
```

###What does it look like?
![cave_0](/examples/cave_0.png)

![cave_1](/examples/cave_1.png)

![cave_2](/examples/cave_2.png)

![cave_3](/examples/cave_3.png)

![cave_4](/examples/cave_4.png)