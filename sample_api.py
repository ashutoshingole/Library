import requests
import json
import sys
from xml.dom import minidom
import urllib
from lxml import etree
import xml.etree.ElementTree as ElementTree
import unicodedata

# url = "http://isbndb.com/api/books.xml?access_key=F2Y1NV7I&results=subjects&index1=isbn&value1=9781846276033"

# response_string = requests.get(url).content
# end_index = response_string.find('</Subject>')
# beg_index = response_string.rfind('>',0,end_index) + 1
# print response_string
# print beg_index
# print end_index

# urllib.urlretrieve("https://images.gr-assets.com/authors/1271683549p5/5217.jpg", "bernard.jpg")

# isbn = "9781846276033"

# url = "https://www.goodreads.com/book/review_counts.json?key=i2RVLibRXKLkwrd7fjyT9g&isbns="+isbn

# response = requests.get(url)
# json_data = json.loads(response.text)
# goodreads_book_id = json_data['books'][0]['id']
# goodreads_book_rating = json_data['books'][0]['average_rating']

# url_2 = "https://www.goodreads.com/book/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id="+str(goodreads_book_id)

# response_2 = requests.get(url_2)

# response_2_string = response_2.content

# beg_index = response_2_string.find("<description>") + 22
# end_index = response_2_string.find("</description>") - 3

# final_string = response_2_string[beg_index:end_index].replace('<br /><br />','\n\n')

# beg_index = response_2_string.find("<author>")
# end_index = response_2_string.find("</author>")
# temp_string = response_2_string[beg_index:end_index]
# beg_index = temp_string.find("<id>") + 4
# end_index = temp_string.find("</id>")
# author_id = temp_string[beg_index:end_index]

# orig_stdout = sys.stdout
# f = open('out_1.txt', 'w')
# sys.stdout = f

# print final_string

# sys.stdout = orig_stdout
# f.close()

# url = "https://www.goodreads.com/author/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id=5217"
# response = requests.get(url)
# orig_stdout = sys.stdout
# f = open('author.txt', 'w')
# sys.stdout = f

# print response.content

# sys.stdout = orig_stdout
# f.close()

author_id = 4119155
url = "https://www.goodreads.com/author/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id=" + str(author_id)
response = requests.get(url)
CONTENT_1 = response.content
root = ElementTree.fromstring(CONTENT_1)
for log in root.iter('about'):
	author_info = log.text
	break
print type(author_info)
author_info.encode('utf-8')
author_info = str(author_info)
print type(author_info)
author_info.replace("<br />","\n")
print author_info
# beg_index = response_string.find("<about><![CDATA[") + 1
# end_index = response_string.find("]]></about>")
# author_info = response_string[beg_index:end_index].replace('<br />','\n')
# print author_info
