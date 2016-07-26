import rospy
from geometry_msgs.msg import Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
import publisher
from math import radians

SETUP_DONE = False

def setup():
  publisher.initialize()
  #SETUP_DONE = True
  #rospy.init_node("IG", anonymous=False)

def say(speech):
  if not SETUP_DONE: setup()
  rospy.loginfo(speech)

def move(distance, angular, speed, delta_y, rotation):
  if not SETUP_DONE: setup()
  cmd_vel = rospy.Publisher("cmd_vel_mux/input/navi", Twist, queue_size=10)
  rospy.sleep(1)
  
  # create a Twist message, fill it in to drive forward
  twist = Twist()
  if speed != 0:
    move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    move_base.wait_for_server(rospy.Duration(10))
    for i in range(int(distance*2)):
      goal = MoveBaseGoal()
      goal.target_pose.header.frame_id = 'base_link'
      goal.target_pose.header.stamp = rospy.Time.now()
      goal.target_pose.pose.position.x = 0.5 #3 meters
      goal.target_pose.pose.orientation.w = 1.0 #go forward
      
      move_base.send_goal(goal)

      success = move_base.wait_for_result(rospy.Duration(10))

      if not success:
        move_base.cancel_goal()
        #rospy.loginfo("The base failed to move forward 3 meters for some reason")
        break
      else:
        # We made it!
        state = move_base.get_state()
        if state == GoalStatus.SUCCEEDED:
          continue
  # create a twist message, fill it in to turn
  else:
    twist.angular.z = radians(90)*rotation #0.785398*2*rotation    # 90 deg/s
    for i in range(int(2*angular)):
      cmd_vel.publish(twist)
      rospy.sleep(0.5)



