import random
from datetime import datetime
from decimal import Decimal
from matplotlib import pyplot as plt

seed = random.randint(1, 10)
date = datetime.now()
newdate = datetime.strftime(date, '%b %d, %Y')
print(seed)
print(date)
print(newdate)
numbers_a = range(1, 13)
numbers_b = random.sample((range(1000)), 12)
plt.plot(numbers_a, numbers_b)
plt.show()
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Queens\n")
  bad_bands_doc.write("Kings")

with open('testRead.py') as python:
  print(python.read())