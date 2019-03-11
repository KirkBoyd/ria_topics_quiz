#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
vel = Twist()
vel.linear.x = 0
vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
vel.angular.z = 0
turn = False


def callback(msg):


rospy.init_node('infinity_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
