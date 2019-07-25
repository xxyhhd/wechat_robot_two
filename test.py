import re

a = '{123456}'
a = re.sub('{|}','',a)
print(a)