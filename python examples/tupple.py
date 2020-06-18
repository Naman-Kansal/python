fname = input('Enter the file name: ')
fhand = open(fname)
hour = list()
counts = dict()
for line in fhand:
    line = line .rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    stime = time.split(':')
    hrs = stime[0]
    hour.append(hrs)
#print(hour)
for hr in hour:
    counts[hr] = counts.get(hr,0) + 1
#print(counts)
for key,val in sorted(counts.items()):
    print(key , val)
