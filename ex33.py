i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "the numbers: "

for num in numbers:
	print num
	
#Drills, 3-4
def countNum (b, inc):
	i = 0
	numbers = []
	
	while i < b:
		print "At the top i is % d" % i
		numbers.append(i)
	
		i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return b
countNum(90, 9)
#
