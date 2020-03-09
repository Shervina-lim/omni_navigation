# omni_navigation
ROS package navigation to omnibot

## Omni_navigation 
- Clone the package folder

		$ cd ~/catkin_ws/src
		$ git clone https://github.com/LCAD-UFES/p3dx_navigation.git
		$ cd ..
		$ catkin_make

## FT sensor
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
- Install ira_laser_tools to merge laserscans from both lidars (refer to: http://wiki.ros.org/ira_laser_tools)
		$ cd ~/catkin_ws/src
		$ git clone https://github.com/iralabdisco/ira_laser_tools.git
		$ cd ..
		$ catkin_make

## Simulation
To run simulation

		$ roslaunch omni_navigation simulation.launch

and another terminal

		$ roslaunch omni_navigation move_base_eband.launch


Learn more about using the ROS navigation stack at http://wiki.ros.org/navigation
