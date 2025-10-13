#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix

def callback(data):
    rospy.loginfo(f"GNSS Position: lat={data.latitude}, lon={data.longitude}")

def main():
    rospy.init_node('gnss_navigator')
    rospy.Subscriber('/fix', NavSatFix, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
