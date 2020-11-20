# omni_navigation
This version is compaitable with ROS melodic

ROS package navigation to omnibot. Do make sure that Ros-navigation is installed.


- Ros Navigation

		$ sudo apt-get install ros-melodic-navigation

If you plan to use teb or eband planner, do install them too. 

- EBand local planner

		$ sudo apt-get install ros-kinetic-eband-local-planner
		
- TEB local planner

		$ sudo apt-get install ros-kinetic-teb-local-planner
		
## Omni_navigation 
===============================================================================================================
- Clone the package folder

		$ cd ~/catkin_ws/src
		$ git clone https://github.com/Shervina-lim/omni_navigation.git
		$ cd ..
		$ catkin_make

## FT sensor
================================================================================================================
- Install driver for ATI Mini45 FT sensor (refer to: http://wiki.ros.org/netft_utils)
		$ cd ~/catkin_ws/src
		$ git clone https://github.com/UTNuclearRoboticsPublic/netft_utils.git
		$ cd ..
		$ catkin_make

- Configure network settings

		Ethernet network -> Edit connections -> Wired connection _ (usually is the last one) -> edit -> IPV4 settings
		set method to manual 
		Address: 192.168.1.100
		Subnet mask: 255.255.255.0

- Launching FT node
		$ rosrun netft_utils netft_node 192.168.1.1
		$ rostopic echo /netft_data

## Laserscan Merger
================================================================================================================
- Install ira_laser_tools to merge laserscans from both lidars (refer to: http://wiki.ros.org/ira_laser_tools)
## Make sure to install the melodic version.

		$ cd ~/catkin_ws/src
		$ git clone https://github.com/iralabdisco/ira_laser_tools.git
		$ cd ..
		$ catkin_make

## Simulation
================================================================================================================
The launch files can be found in launch/omni_gazebo and config files are in config/omni_gazebo

To run simulation

		$ roslaunch omni_navigation simulation.launch

and another terminal

		$ roslaunch omni_navigation eband.launch


## Real robot (still testing)
================================================================================================================
The launch files can be found in launch/robot and config files are in config/omni_bot
		
		$ roslaunch omni_navigation bot_eband.launch


Learn more about using the ROS navigation stack at http://wiki.ros.org/navigation
