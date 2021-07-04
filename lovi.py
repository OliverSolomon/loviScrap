import pandas as pd

URL = 'http://wdi.worldbank.org/table/2.13'
table = pd.read_html(URL, match='measles')

print(table)