import os
import sys


def startContainer():
	
	os.system('mkdir aminsbox')
	
	hostname = sys.argv[1]
		
	os.system('tar -zxf ubuntu-focal-oci-amd64-root.tar.gz -C aminsbox')

	os.system("sudo unshare --fork --pid --mount-proc --uts --net --root=/aminsbox bash -c  \"hostname "+hostname+" && /bin/bash\"")
	
	
if __name__ == '__main__':		
	startContainer()

