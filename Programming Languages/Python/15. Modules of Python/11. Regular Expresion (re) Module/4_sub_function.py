import re

print(re.sub('ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))

print(re.sub('ub', '~*', 'Subject has Uber booked already'))