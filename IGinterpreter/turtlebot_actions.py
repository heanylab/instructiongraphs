import rospy
from geometry_msgs.msg import Twist

SETUP_DONE = False

def setup():
  SETUP_DONE = True
  rospy.init_node("IG", anonymous=False)

def say(speech):
  if not SETUP_DONE: setup()
  rospy.loginfo(speech)

def move(distance, angular):
  if not SETUP_DONE: setup()
  cmd_vel = rospy.Publisher("cmd_vel_mux/input/navi", Twist, queue_size=10)
  rospy.sleep(1)
  
  # create a Twist message, fill it in to drive forward
  twist = Twist()
  twist.linear.x = 0.5 # m/s
  for i in range(int(4*distance)):
      cmd_vel.publish(twist)
      rospy.sleep(1)
  # create a twist message, fill it in to turn
  twist = Twist()
  twist.angular.z = 0.785398*2    # 90 deg/s
  for i in range(int(2*angular)):
      cmd_vel.publish(twist)
      rospy.sleep(1)