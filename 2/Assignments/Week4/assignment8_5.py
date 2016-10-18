# fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

fh = open("mbox-short.txt")
count = 0

for line in fh:
    # print dir(line)
    if line.startswith("From"):
        splited = line.split()
        if len(splited) == 2:
            print splited[1]
            count +=1


print "There were", count, "lines in the file with From as the first word"

stuff = dict()
print stuff.get('candy',-1)
