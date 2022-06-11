import os
import sys


def startContainer():
	print("start")
	hostname = sys.argv[1]
	os.system('mkdir /aminbox')
	
	os.system('sudo apt install --assume-yes debootstrap')
	
	os.system('sudo debootstrap focal ~/aminbox')
	
	os.system('sudo mount -t proc /proc ~/aminbox/proc')
	
	os.system('sudo mount --rbind /sys ~/aminbox/sys')
	
	os.system('sudo mount --rbind /dev ~/aminbox/dev')
	
	os.system(f"unshare --net --mount --pid --uts --fork --map-root-user --mount-proc")
	
	os.system(str('sudo hostname '+hostname))
	
	os.system('sudo chroot ~/aminbox /bin/bash')
	
	

	
	
	
	
if __name__ == '__main__':		
	startContainer()

