# import module
from urllib.request import urlopen
from urllib.error import *

# try block to read URL
try:
        html = urlopen("https://atg.world/")

# except block to catch
# exception
# and identify error
except HTTPError as e:
        print("HTTP error", e)

except URLError as e:
        print("Opps test fail", e)

else:
        print('test pass')
