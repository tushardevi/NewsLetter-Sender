import urllib
import json
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# set api key
api_key = '5fd0aa8401724592ae5062d9bee2f319'

# define the url from where i will retrieve json
url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=5fd0aa8401724592ae5062d9bee2f319')

# store all the data into a variable
response = urllib.request.urlopen(url).read()

json_obj = str(response, 'utf-8')

data = json.loads(json_obj)

# declare a string which will store all the contents e.g text, buttons
html = ""
html2 = ""
i = 1
msgAlternate = MIMEMultipart()
msg = MIMEMultipart()
# get the data imported from api file

for item in data['articles']:

       # add title
       html += """<html>
                   <head></head>
                   <body style="background-color:#FFD700;">
                   <font size="6.5"><div class='container'>{0}
                   </div></font><br></body>""".format(item['title'])

       # add description
       html += """<body style="background-color:#DC143C;">
                  <font size="4"><div class='container'>{des}
                  </div></font><br><img src="{img}" width="500" height="500 align="right""></body>""".format(des = item['description'], img = item['urlToImage'])


       i = i + 1

       # add button to link it to the url
       button = """ <html>
          <head>
             <title>Title of the document</title>
          </head>
          <body>
           <form action= {ur}>
           <input type="submit" value="Go to Site" />
       </form>
          </body>
       </html>""".format(ur = item['url'])

       # add the button to the html string
       html += button

       html += "<br>"
       html += "<br>"



