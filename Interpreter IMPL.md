## Interpreter implementation
 
### main.py

- Runs interpreter.
- Call publisher.
- Call parser.
- Call statics.
- Call dynamics.

### publisher.py

- Initializes node.
- Initializes topics (goal and status).
- Publishes on the topics.

### lexer.py

- Tokenizes the IG input.

### parser.py

- parses the tokens input vertex and edges.

### statics.py

- Performs static checks on the graph created.

### dynamics.py

- executes the graph
- calls actions.

### turtlebot_move_base_action.py

- Moves the bot forward using move_base
- Turns the bot using cmd_vel

### turtlebot_action.py

- Moves the bot forward using cmd_vel
- Turns the bot using cmd_vel





