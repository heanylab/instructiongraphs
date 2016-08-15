## Understanding IG structure

An IG is a graph that consist of vertices and edges. 

The syntax for the graph is:

```G = (V0, [V1,V2..])```

- where, V0 is the initial vertex 
- and, [V1, V2..] is a list of all the other vertices.

```V = (ID, action) ```

- where, ID is the vertex id
- and, action is the action that the vertex does like move, speak etc.


```Action = <action type> <action> <next vertex> ```

- action type -> do, do until, if else, goto
- actions -> move, say
- next vertex -> a valid vertex id.

```Move = (distance_x, rotation, linear_speed, distance_y, angular_direction)```

- where, distance_x = distance to move forward in meters
- rotation = angle to turn (in 90 degrees). So, 1 means 90 degrees and 2 means 180.
- linear_speed = speed to move forward in meters/second.
- distance_y = distance to move side ways. (Does not apply to Tbot)
- angular_direction = Rotating clock wise or anti clockwise. 1 is clockwise and -1 is anti.

## Restrictions

- The bot can either move forward or turn but cannot do them both together.
- The bot can only turn 90 degrees.



