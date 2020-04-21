#!/usr/bin/env python
import time
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback
from actionlib_msgs.msg import *


def moveToGoal(xIn,yIn):
    # goalReached variable keeps track if the robot has reached the desired location
    goalReached = False

    # the while loop runs until the robot reaches the goal
    while not goalReached:
    	
        # The SimpleActionClient is a client from the actionlib library of ROS which is mainly used for robot navigation
        move = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        # The following while loop checks if the server is active and once it is active the while loop is exited
        while(not move.wait_for_server(rospy.Duration.from_sec(5.0))):
            rospy.loginfo("Waiting for the move_base action server to come up")
                
                
        #simplegoal stores an instance of MoveBaseGoal, where MoveBaseGoal has the following variables that we can set
        simplegoal = MoveBaseGoal()

        # The goal is given with respect to the frame map, there are different reference frames in ROS, but widely used one is map
        simplegoal.target_pose.header.frame_id = "map"
        # Timestamp of the current goal
        simplegoal.target_pose.header.stamp = rospy.Time.now()
        # In the following lines, we set the position and orientation of the points where we want the robot to go, here x and y coordinates are used from the function parameters
        simplegoal.target_pose.pose.position.x = xIn
        simplegoal.target_pose.pose.position.y = yIn
        simplegoal.target_pose.pose.position.z = 0
        simplegoal.target_pose.pose.orientation.x = 0.0
        simplegoal.target_pose.pose.orientation.y = 0.0
        simplegoal.target_pose.pose.orientation.z = 0.0
        simplegoal.target_pose.pose.orientation.w = 1.0
        
        # Now we pass this simplegoal to the SimpleActionClient
        move.send_goal(simplegoal)

        # Here we check if the robot has reached the goal
        move.wait_for_result(rospy.Duration(60))

        # GoalStatus stores the status of the goal and GoalStatus.SUCCEEDED refers to the state where the robot has succesfully reached the goal and then we update the goalReached variable and set it to True
        if(move.get_state() ==  GoalStatus.SUCCEEDED):
            goalReached = True




if __name__ == '__main__':
    try:
        #Name of the ROS node -- feel free to write anything you want to name it
        rospy.init_node('fri_move_goal')
        # x1,y1 are the 2D coordinates of the Point where you want the robot to navigate
        x1 = -2.46
        y1 = 3.92
        
        # moveToGoal function takes the point where the robot should navigate
        moveToGoal(x1,y1)

    except rospy.ROSInterruptException:
        print "finished!"
