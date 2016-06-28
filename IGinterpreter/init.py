import rospy
from std_msgs.msg import String

def initialize():
        pub = rospy.Publisher('instructiongraphs/run/status/',String, queue_size=10)
	rospy.init_node('InstructionGraphs', anonymous=True)
	pub.publish("stopped")

if __name__ == "__main__":
	initialize()

