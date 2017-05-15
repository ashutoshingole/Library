import requests
import json
import sys
from xml.dom import minidom
import urllib
import os
import inspect
from lxml import etree
import xml.etree.ElementTree as ElementTree


def get_book_rating_and_info_and_genre(isbn):

	url = "https://www.goodreads.com/book/review_counts.json?key=i2RVLibRXKLkwrd7fjyT9g&isbns="+isbn

	response = requests.get(url) 
	json_data = json.loads(response.text)
	goodreads_book_id = json_data['books'][0]['id']
	goodreads_book_rating = json_data['books'][0]['average_rating']

	url_2 = "https://www.goodreads.com/book/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id="+str(goodreads_book_id)

	response_2 = requests.get(url_2)
	response_2_string = response_2.content
	beg_index = response_2_string.find("<description>") + 22
	end_index = response_2_string.find("</description>") - 3
	final_string = response_2_string[beg_index:end_index].replace('<br />','\n')


	beg_index = response_2_string.find("<author>")
	end_index = response_2_string.find("</author>")
	temp_string = response_2_string[beg_index:end_index]
	beg_index = temp_string.find("<id>") + 4
	end_index = temp_string.find("</id>")
	author_id = temp_string[beg_index:end_index]

	beg_index = temp_string.find("<![CDATA[") + 9
	end_index = temp_string.find("]]>")
	image_url = temp_string[beg_index:end_index]

	url_3 = "http://isbndb.com/api/books.xml?access_key=F2Y1NV7I&results=subjects&index1=isbn&value1="+isbn

	response_string = requests.get(url_3).content
	end_index = response_string.find('</Subject>')
	beg_index = response_string.rfind('>',0,end_index) + 1
	if end_index == -1:
		genre = ""
	else:
		genre = response_string[beg_index:end_index]

	return [goodreads_book_rating, final_string, genre, author_id, image_url]

def get_author_info_and_image(author_id, author_name, image_url):

	url = "https://www.goodreads.com/author/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id=" + str(author_id)
	response = requests.get(url)
	response_string = response.content
	beg_index = response_string.find("<about><![CDATA[") + 1
	end_index = response_string.find("]]></about>")
	author_info = response_string[beg_index:end_index].replace('<br />','\n')
	current_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	filename = current_file + "/Author_Images/" + author_name + ".jpg"
	urllib.urlretrieve(image_url, filename)
	return author_info