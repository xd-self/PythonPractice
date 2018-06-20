# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:27:04 2018

@author: Administrator
"""

from urllib import request,parse
import json
url = "http://fanyi.baidu.com"
data={'kw':'Inputs'}
data=parse.urlencode(data).encode("utf-8")
#eaders={Content-Length:leng(data)}

rsp = request.urlopen(url,data=data)
json_data = rsp.read().decode("utf-8")
json_data=json.loads(json_data)
print(json_data)
    