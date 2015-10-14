import sys

if len(sys.argv) != 3:
	print "usage weka.py <*.data.txt> <number of attribute>"
	exit(1)
else :
	try :
		fin = open(sys.argv[1], 'r')
	except :
		print "file : " + str(sys.argv[1]) + " not Found"
		exit(1)

x = sys.argv[1]
y = x.find('.')

fout = open(x[0:y]+".arff", 'w')

attr = raw_input("enter file attribute > ")

try :
	fin_a = open(attr, 'r')
except :
	print "file not found"
	exit(1)

for line in fin_a:
	fout.write(line)

fin_a.close()

fout.write("\n\n")
fout.write("@data\n")

temp = [0 for x in range(int(sys.argv[2]))]

for line in fin:
    o = line.rstrip().split(',')
    temp[30] = o[1]
    for z in range(30):
    	temp[z] = o[z+2]

    #print o, len(o) = 33
    
    for i in range(len(temp)):
        if i == len(temp)-1:
            fout.write(temp[i])
            break

        fout.write(temp[i] + ', ')
    
    fout.write("\n")


print "Done"

fout.close()
fin.close()
