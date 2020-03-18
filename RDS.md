# ROS Development Studio
> The page gives the instructions for using RDS platform.

## Create an account on ROS Development Studio
Create an account on https://rds.theconstructsim.com/ or login to your account if you already have an account.

## Creating a project
Click New ROSject from the left navigation bar.<br>
Give a name for the ROSject.<br>
For the ROS Configuration, select Ubuntu 16.04 + ROS Kinetic + Gazebo 7<br>
Scroll down and select Create.<br>
Open the ROSject with the Basic hardware.<br>

## Start a 3D simulator called Gazebo
Click on Simulations.<br>
Select corridor world and Turtlebot2 as a robot. <br>
A robot will appear in a simulation environment. <br>

## Starting 3D visualization tool called Rviz
Click Tools → Graphical Tools

To open a terminal, click on Tools --> Shell and type the following command

`roslaunch turtlebot_rviz_launchers view_navigation.launch`

In a new terminal, run the follwoing two commands:

```
roscd turtlebot_navigation/launch/includes/gmapping
cp gmapping.launch.xml ../
```

In a new terminal,

`roslaunch turtlebot_gazebo gmapping_demo.launch`

## Building a map

In a new terminal, type the following command:

`roslaunch turtlebot_teleop keyboard_teleop.launch`

Now using teleoperation, navigate TurtleBot around the entire area you wish to map.<br>
You need to use “i” to move forward and “j” and “l” to move left and right respectively.

## To save the map

Open a terminal and type:

```
mkdir maps
rosrun map_server map_saver -f maps/corridor_map
```

In the maps folder, corridor_map.pgm and corridor_map.yaml will be generated.

Close all the ROS applications.

## Localization and Navigation

To start a 3D simulator called Gazebo, click on Simulations. <br>
Select corridor world and Turtlebot2 as a robot. <br>
A robot will appear in a simulation environment. <br>

Open a terminal and type:

```
roscd turtlebot_navigation/launch/includes/amcl/
cp amcl.launch.xml ../
```


Open a new terminal:

`roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/user/maps/corridormap.yaml`


## Starting 3D visualization tool called Rviz
Click Tools → Graphical Tools

Open a terminal and type the following command

`roslaunch turtlebot_rviz_launchers view_navigation.launch`

Then use the 2D Pose estimate button to give an initial pose of the robot. 
Now, using the 2D Navigation goal button you can give a goal to the robot.
The robot will then autonomously navigate to the 2D coordinate.


