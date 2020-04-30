#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3

max_vel = 0.4
max_turn = 0.4

pub = rospy.Publisher('/omnibase/cmd_vel', Twist, queue_size=10)

def callback(data):
    tmp = Twist()
    tmp.linear = Vector3(max_vel*data.axes[1], max_vel*data.axes[0], 0)
    tmp.angular = Vector3(0, 0, max_turn*data.axes[2])

    pub.publish(tmp)

if __name__ == '__main__':
    rospy.init_node('joy_control', anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)

    print "Start Joy Control"
    rospy.spin()
