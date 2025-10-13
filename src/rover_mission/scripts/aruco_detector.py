#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

def callback(msg):
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
    # ArUco detection logic placeholder
    rospy.loginfo("ArUco marker detection triggered.")

def main():
    rospy.init_node('aruco_detector')
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
