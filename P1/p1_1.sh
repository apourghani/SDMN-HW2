sudo apt ip netns add NS1
sudo apt ip netns add NS2

sudo ip netns list


sudo ip netns add Router1



sudo ip link add veth1-ns type veth peer name veth1-rt

