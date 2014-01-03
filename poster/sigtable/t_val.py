import math
import sys

w = int(sys.argv[1])
m = w/300

#t = (m - 0.5) / math.sqrt((w - ((w**2)/300) + 75)/(299*300))
try:
    t = (m - 0.5) / math.sqrt((w - ((w**2)/300))/(299*300))
except ZeroDivisionError:
    t = float("inf")

print("Wins: " + str(w))
print("")
print("T: " + str(t))
print("")
print("Result is " + ("" if abs(t) > 1.644854 else "not ") + "statistically significant with confidence >95%.")
