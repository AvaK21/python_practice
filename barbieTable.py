import pandas as pd
import urllib.request


url = "https://en.wikipedia.org/wiki/Barbie"

# Add a browser-like header   -- So the website will not block it
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

# Fetch the HTML
html = urllib.request.urlopen(req).read()

# Parse tables from the HTML
tables = pd.read_html(html)

print(tables[0])



#Got error 403 - forbideen - CoPilot says that it is because the read_html() function with out a browser mentioned in the http request header
# it looks like a bot and most websites reject those

# url = 'https://en.wikipedia.org/wiki/Barbie'
# tables = pd.read_html(url)
# df = tables[0]
# print(df)