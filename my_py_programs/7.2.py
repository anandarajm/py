# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    start_index = line.find(':')
    end_index = line.find('\n',start_index)
    confidence = line[start_index+1:end_index]
    confidence = float(confidence)
    #print confidence, type(confidence)
    count = count + 1
    sum = sum + confidence
#print count, sum 
avg = sum / count 
print "Average spam confidence: ", avg
