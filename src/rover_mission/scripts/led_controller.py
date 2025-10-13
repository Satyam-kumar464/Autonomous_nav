#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

def callback(msg):
    if msg.data:
        rospy.loginfo("LED ON")
    else:
        rospy.loginfo("LED OFF")

def main():
    rospy.init_node('led_controller')
    rospy.Subscriber('/led_control', Bool, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
