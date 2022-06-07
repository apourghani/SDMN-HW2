#Creating namespaces
sudo ip netns add NS1
sudo ip netns add NS2
sudo ip netns add NS3
sudo ip netns add NS4
sudo ip netns add Router1

#Creating bridges
sudo ip link add br1 type bridge
sudo ip link add br2 type bridge


#Creating links
sudo ip link add veth1-ns type veth peer name veth1-br

sudo ip link add veth2-ns type veth peer name veth2-br

sudo ip link add veth3-br type veth peer name veth3-rt

sudo ip link add veth4-br type veth peer name veth4-rt

sudo ip link add veth5-ns type veth peer name veth5-br

sudo ip link add veth6-ns type veth peer name veth6-br

#Connecting links
sudo ip netns list





