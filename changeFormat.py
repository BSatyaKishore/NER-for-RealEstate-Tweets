import sys
in_file_user = open(sys.argv[1],"r")

lines_user = in_file_user.readlines()

for line in lines_user:
	if len(line.strip().strip()) > 0:
		print line.strip().split()[0]+" "+line.strip().split()[-1]
	else:
		print ""