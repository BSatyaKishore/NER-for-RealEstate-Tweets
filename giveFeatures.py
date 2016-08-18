import os,sys

execfile('features.py')

s = str(sys.argv[1])
a = str(sys.argv[2])
b = str(sys.argv[3])
# print b+'ing'
train = open(s,'r')
trainWithFeatures = open(a,'w')
shouts = train.readlines()

j = 0
for i in range(len(shouts)):
	xs =shouts[i].strip().split(" ")
	to_write = xs[0]
	if xs[0] == "":
		trainWithFeatures.write('\n')
		j = 0
		continue
	if len(xs) < 1:
		trainWithFeatures.write('\n')
		j = 0
		continue
	to_write = to_write+ "\t"+ str(is_link(shouts[i])) #1
	to_write = to_write+ "\t"+ str(has_9Digits(shouts[i])) #2
	to_write = to_write+ "\t"+ str(NumType(shouts[i])) #3
	to_write = to_write+ "\t"+ str(isInNamesList(shouts[i])) #4
	to_write = to_write+ "\t"+ str(isContact(shouts[i])) #5
	to_write = to_write+ "\t"+ str(isIn(shouts[i])) #6
	to_write = to_write+ "\t"+ str(isAt(shouts[i])) #7
	to_write = to_write+ "\t"+ str(hasLocation(shouts[i])) #8
	to_write = to_write+ "\t"+ str(startsWithHash(shouts[i])) #9
	to_write = to_write+ "\t"+ str(startsWithAt(shouts[i])) #10

	if i > 0:
		to_write = to_write+ "\t"+ str(isPer(shouts[i-1]+shouts[i])) #11
	else:
		to_write = to_write+ "\t"+ 'False'	#11

	to_write = to_write+ "\t"+ str(isPer(shouts[i])) #12

	if i < len(shouts)-2:
		to_write = to_write+ "\t"+ str(isPer(shouts[i]+shouts[i+1])) #13
	else:
		to_write = to_write+ "\t"+ 'False'	#13


	if i > 0:
		to_write = to_write+ "\t"+ str(isAreaUnit(shouts[i-1]+shouts[i])) #14
	else:
		to_write = to_write+ "\t"+ 'False'	#14
	to_write = to_write+ "\t"+ str(isAreaUnit(shouts[i])) #15
	if i < len(shouts)-2:
		to_write = to_write+ "\t"+ str(isAreaUnit(shouts[i]+shouts[i+1])) #16
	else:
		to_write = to_write+ "\t"+ 'False'	#16
	
	#to_write = to_write+ "\t"+ str(hasQuantifier(shouts[i])) #17
	to_write = to_write+ "\t"+ str(isInAttributeList(shouts[i])) #18
	# if i > 0:
	# 	to_write = to_write+ "\t"+ str(isPrice(shouts[i-1]+shouts[i])) #17
	# else:
	# 	to_write = to_write+ "\t"+ 'False'	#17
	# to_write = to_write+ "\t"+ str(isPrice(shouts[i])) #18
	# if i < len(shouts)-2:
	# 	to_write = to_write+ "\t"+ str(isPrice(shouts[i]+shouts[i+1])) #19
	# else:
	# 	to_write = to_write+ "\t"+ 'False'	#19


	if (b == 'Train'):
		to_write = to_write+"\t"+str(xs[1])

	# 
	j = j+1
	trainWithFeatures.write(to_write+" "+'\n')
# print b+'ed'