#!/bin/bash 
#Defining the node that pings
pingSource=""
#Defining the node that is being pinged
pingDest=""

flag="right"

if [ "$1" == "NS1" ];
  then
    pingSource="NS1"
elif [ "$1" == "NS2" ];
  then
    pingSource="NS2"
elif [ "$1" == "NS3" ];
  then
    pingSource="NS3"
elif [ "$1" == "NS4" ];
  then
    pingSource="NS4"
elif [ "$1" == "Router1" ];
  then
    pingSource="Router1"
fi



if [ "$2" == "NS1" ]
  then
    pingDest="172.0.0.2"
elif [ "$2" == "NS2" ]
  then
    pingDest="172.0.0.3"
elif [ "$2" == "NS3" ]
  then
    pingDest="10.10.0.2"
elif [ "$2" == "NS4" ]
  then
    pingDest="10.10.0.3"
elif [ "$2" == "Router1" && $flag == "right" ]
  then
    pingDest="10.10.0.1"
elif [ "$2" == "Router1" && $flag == "left" ]
  then
    pingDest="172.0.0.1"
fi


#Pinging:
sudo ip netns exec $pingSource ping $pingDest


