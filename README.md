# omni_navigation
<<<<<<< HEAD
ROS package navigation to omnibot
=======
ROS package navigation for omnibot
>>>>>>> 8658b3669b4712ad9a157e81d906397774eae095

## Omni_navigation 
- Clone the package folder

		$ cd ~/catkin_ws/src
		$ git clone https://github.com/LCAD-UFES/p3dx_navigation.git
		$ cd ..
		$ catkin_make

## FT sensor
- Install driver for ATI Mini45 FT sensor (refer to: http://wiki.ros.org/netft_utils)
<<<<<<< HEAD
=======

>>>>>>> 8658b3669b4712ad9a157e81d906397774eae095
		$ cd ~/catkin_ws/src
		$ git clone https://github.com/UTNuclearRoboticsPublic/netft_utils.git
		$ cd ..
		$ catkin_make

- Configure network settings
<<<<<<< HEAD
=======

>>>>>>> 8658b3669b4712ad9a157e81d906397774eae095
		Ethernet network -> Edit connections -> Wired connection _ (usually is the last one) -> edit -> IPV4 settings
		set method to manual 
		Address: 192.168.1.100
		Subnet mask: 255.255.255.0

- Launching FT node
<<<<<<< HEAD
		$ rosrun netft_utils netft_node 192.168.1.1
		$ rostopic echo /netft_data

## Laserscan Merger
- Install ira_laser_tools to merge laserscans from both lidars (refer to: http://wiki.ros.org/ira_laser_tools)
		$ cd ~/catkin_ws/src
		$ git clone https://github.com/iralabdisco/ira_laser_tools.git
		$ cd ..
		$ catkin_make
=======

		$ rosrun netft_utils netft_node 192.168.1.1
		$ rostopic echo /netft_data		
>>>>>>> 8658b3669b4712ad9a157e81d906397774eae095

## Simulation
To run simulation

		$ roslaunch omni_navigation simulation.launch

and another terminal

<<<<<<< HEAD
		$ roslaunch omni_navigation move_base_eband.launch
=======
		$ roslaunch omni_navigation move_base_gazebo.launch
>>>>>>> 8658b3669b4712ad9a157e81d906397774eae095


Learn more about using the ROS navigation stack at http://wiki.ros.org/navigation
