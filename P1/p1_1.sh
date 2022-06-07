#Creating namespaces:
sudo ip netns add NS1
sudo ip netns add NS2
sudo ip netns add NS3
sudo ip netns add NS4
sudo ip netns add Router1




#Creating bridges:
sudo ip link add br1 type bridge
sudo ip link add br2 type bridge




#Creating links:
sudo ip link add veth1 type veth peer name veth1-br
sudo ip link add veth2 type veth peer name veth2-br
sudo ip link add veth3 type veth peer name veth3-br
sudo ip link add veth4 type veth peer name veth4-br
sudo ip link add veth5 type veth peer name veth5-br
sudo ip link add veth6 type veth peer name veth6-br



#Setting namespaces of the interfaces:
sudo ip link set veth1 netns NS1

sudo ip link set veth2 netns NS2

sudo ip link set veth3 netns Router1

sudo ip link set veth4 netns Router1

sudo ip link set veth5 netns NS3

sudo ip link set veth6 netns NS4


#Setting masters of the bridges:
sudo ip link set veth1-br master br1
sudo ip link set veth2-br master br1
sudo ip link set veth3-br master br1
sudo ip link set veth4-br master br2
sudo ip link set veth5-br master br2
sudo ip link set veth6-br master br2





#Assigning ip addresses:
sudo ip netns exec Router1 ip addr add 172.0.0.1/24 dev veth3
sudo ip netns exec NS1 ip addr add 172.0.0.2/24 dev veth1
sudo ip netns exec NS2 ip addr add 172.0.0.3/24 dev veth2
sudo ip netns exec Router1 ip addr add 10.10.0.1/24 dev veth4
sudo ip netns exec NS3 ip addr add 10.10.0.2/24 dev veth5
sudo ip netns exec NS4 ip addr add 10.10.0.3/24 dev veth6
