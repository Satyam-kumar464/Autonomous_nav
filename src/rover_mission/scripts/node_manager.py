#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"Switching to mode: {msg.data}")
    # Add mode-specific logic here

def main():
    rospy.init_node('mode_manager')
    rospy.Subscriber('/mode_select', String, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
