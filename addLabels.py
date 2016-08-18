import os,sys

s = str(sys.argv[1])
a = str(sys.argv[2])
b = str(sys.argv[3])

train = open(s,'r')
train2 = open(a, 'r')
trainWithFeatures = open(b,'w')
shouts = train.readlines()
shouts1 = train2.readlines()

for i in range(len(shouts)):
	xs =shouts[i].strip()
	#print xs
	if len(xs.split()) < 2:
		trainWithFeatures.write('\n')
		continue
	to_write = xs +'\t'+ shouts1[i].strip().split()[-1]
	trainWithFeatures.write(to_write+'\n')