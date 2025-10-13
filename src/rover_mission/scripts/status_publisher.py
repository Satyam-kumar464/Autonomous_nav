#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('status_publisher')
    pub = rospy.Publisher('/status', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "System running"
        pub.publish(msg)
        rospy.loginfo("Status published.")
        rate.sleep()

if __name__ == '__main__':
    main()
