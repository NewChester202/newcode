import random
from datetime import datetime

seed = random.randint(1, 10)
date = datetime.now()
newdate = datetime.strftime(date, '%b %d, %Y')
print(seed)
print(date)
print(newdate)