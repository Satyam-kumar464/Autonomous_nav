#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    if msg.data == "abort":
        rospy.logwarn("Mission aborted!")
        # Add shutdown or emergency logic here

def main():
    rospy.init_node('abort_handler')
    rospy.Subscriber('/mission_status', String, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
