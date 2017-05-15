import requests
import urllib
import os
import inspect

current_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
author_name = "George Bernard Shaw"
filename = current_file + "/Author_Images/" + author_name + ".jpg"
urllib.urlretrieve("https://images.gr-assets.com/authors/1271683549p5/5217.jpg", filename)