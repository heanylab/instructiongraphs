import rospy
from std_msgs.msg import String

PUB = rospy.Publisher('instructiongraphs_status',String, queue_size=10)
IS_INIT = False

def initialize():
  global IS_INIT
  global PUB
  if not IS_INIT:
     IS_INIT = True
     rospy.init_node('InstructionGraphs', anonymous=False)
     # PUB = rospy.Publisher('instructiongraphs_status',String, queue_size=10)
     PUB.publish("Initialized")

def publish(msg):
  global IS_INIT
  global PUB
  if not IS_INIT:
    initialize()
  PUB.publish(msg)

if __name__ == "__main__":
  initialize()
	
