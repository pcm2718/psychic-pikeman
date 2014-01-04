import math
import sys

w = int(sys.argv[1])

try:
    t = (w - 150) / math.sqrt(w - ((w**2) / 300))
except ZeroDivisionError:
    t = float("inf")

print("Wins: " + str(w))
print("")
print("T: " + str(t))
print("")
print("Result is " + ("" if abs(t) > 1.96792966 else "not ") + "statistically significant with confidence >95%.")
