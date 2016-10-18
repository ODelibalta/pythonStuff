# Read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
import re
handle = open( "mbox-short.txt" )
hours = dict()

for line in handle:
    if line.startswith("From"):
        splited = line.split()
        if len(splited) > 2:
            hours[splited[-2][0:2]] = hours.get( splited[-2][0:2], 0 ) + 1

# for k, v in sorted(hours.items()):
#      print k, v
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print y
