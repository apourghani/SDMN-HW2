import sys
import os
args_num = len(sys.argv)

#When just hostname specified:
if args_num == 2:

	print(sys.argv[1])
	os.system(f"python3 ./CLIone.py {sys.argv[1]}")
#When hostname and memory specified:
elif args_num == 3:
	os.system(f"python3 ./CLIone.py {sys.argv[1]} {sys.argv[2]}")


#Wrong number of inputs:
else:
	print("CLI takes one or two input arguments")

