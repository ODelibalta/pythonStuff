import re
handle  = open( "actual.txt" )
results = [] 
for line in handle:
    if re.findall( "[0-9]+", line.strip() ):
        results += re.findall( "[0-9]+", line )

results = map(int, results)
print sum( results )
