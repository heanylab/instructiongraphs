# Instruction Graphs

This is a 15-400 research project based off the work on instruction graphs
described in https://www.cs.cmu.edu/~mmv/papers/14aamas-MericliEtAl.pdf.

## Dependencies
- python2
- ply (installable via `pip install ply`)
- ros-indigo-turtlebot-simulator (try `sudo apt-get install ros-indigo-turtlebot-simulator` on Ubuntu)

## Running the interpreter
- `git clone https://github.com/anuragkanungo/instructiongraphs`
- `cd instructiongraphs/IGinterpreter`
- `roslaunch turtlebot_stage turtlebot_in_stage.launch &`
- `python main.py new.ig`

### Alternately, run tbot using move_base
- `roslaunch turtlebot_bringup minimal.launch`
- `roslaunch turtlebot_navigation amcl_demo.launch`
- `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`

## Notes about Implementation
- The interpreter by default requires a running instance of the turtlebot
  simulator, which is very slow and will cause your computer to become slow to
  respond. You have been warned. Alternatively, you could edit the code pretty
  easily in `dynamics.py` to disable calls to the simulator and merely print
  things instead.
- The `move` command takes two arguments. The first refers to distance, and the
  second to angular rotation.
- In order to detect obstacles, the interpreter relies on user input. Enter 'y',
  'yes', or an empty string to respond with 'yes', else 'no'.

## Checking run status and goal
- `rostopic echo instructiongraphs_status`
- `rostopic echo instructiongraphs_goal`

## Writing a new instruction graph
- Please refer to `IG implementation readme` in the root.

## Understanding implementation of interpreter
- Please refer to `Interpreter implementation readme` in  the root.

## Report
The final report for 15-400 is in the `report` subdirectory. The paper itself is
`paper.tex`, but the report also contains several appendices which are the other
tex files in the directory.
