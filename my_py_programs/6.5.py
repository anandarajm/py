text = "X-DSPAM-Confidence:    0.8475";
index = text.find('0')
length = len(text)
num = text[index:length]
num = float(num)
print num