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

inp = None

print "write your header (relation and attribute) here \n"

while inp != 'q':

    inp = raw_input("> ")
    inp.rstrip()    
    if inp == "":
        inp = "\n"
        fout.write(inp)
        continue

    if (inp == 'q') :
        break

    fout.write(inp + "\n")

fout.write("\n\n")
fout.write("@data\n")

temp = [0 for x in range(int(sys.argv[2]))]

for line in fin:
    o = line.rstrip().split(',')
    temp[0] = o[4]
    temp[1] = o[7]
    temp[2] = o[5]
    temp[3]	= o[6]
    temp[4] = o[8]
    temp[5] = o[3]
    temp[6] = o[2]
    temp[7] = o[0]
    temp[8] = o[1]

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
