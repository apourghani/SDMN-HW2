import os
import sys


def startContainer():
	print("start")
	hostname = sys.argv[1]
	os.system('mkdir ~/box')
	
	os.system('sudo apt install --assume-yes debootstrap')
	
	os.system('sudo debootstrap focal ~/box')
	
	os.system('sudo mount -t proc /proc box/proc')
	
	os.system('sudo mount --rbind /sys box/sys')
	
	os.system('sudo mount --rbind /dev box/dev')
	
	#os.system(f"unshare --mount --net --uts --pid --fork --map-root-user --mount-proc bash -c")	
	os.system(f"unshare --net --mount --pid --uts --fork --map-root-user --mount-proc")
	
	os.system('sudo chroot ~/box /bin/bash')
	
	os.system(str('hostname '+hostname))

	
	
	
	
if __name__ == '__main__':		
	startContainer()

