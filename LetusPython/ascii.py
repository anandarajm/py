import traceback
import sys

while True:
    try:
        print "Enter any character"
        asc = ord(raw_input(">>>"))
        break
    except:
        print "Enter only characters"
        print traceback.format_exc()
        continue


if asc >= 65 and asc <= 90:
    print "Capital letter"
elif asc >= 97 and asc <= 122:
    print "Small letter"
elif 48 <= asc <= 57:
    print "Single digit number"
elif 0 <= asc <= 47 or 58 <= asc <= 64 or 91 <= asc <= 96 or 123 <= asc <= 127:
    print "Special character"
