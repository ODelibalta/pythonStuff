# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# Create a dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# Read through the dictionary using a maximum loop to find the most prolific committer.


# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open( "mbox-short.txt" )
counts = dict()

for line in handle:
    if line.startswith("From"):
        splited = line.split()
        if len(splited) == 2:
            counts[splited[1]] = counts.get( splited[1], 0 ) + 1

bigCount = None
bigWord  = None

for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print bigWord + " " + str( bigCount )
