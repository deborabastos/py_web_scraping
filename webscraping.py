import math
import os
import re
import sys

# import pandas as pd
import requests
# from bs4 import BeautifulSoup as BS

# print(sys.version)
print(sys.executable)

r = requests.get('https://github.com/deborabastos/py_web_scraping')
print(r.status_code)


