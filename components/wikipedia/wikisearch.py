import json
import urllib2
import sys
import ast
import requests

# # req = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=parse&page=China&format=json&prop=text")
# # content = req.read()
# # x =  '{ "name":"John", "age":30, "city":"New York"}'
# # y = json.loads(x)
# # print(y["age"])

def wikiSearch(str,lang):
    req = urllib2.urlopen("https://"+lang+".wikipedia.org/w/api.php?action=opensearch&format=json&search="+str)
    print ("Search for: " + str)
    print "Results... "
    # data = json.loads(req.read().decode())
    data = ast.literal_eval(req.read())
    print (data)
    # data = (json.dumps(data))

# wikiSearch('Apple','pt')

# import json

json_data = '{"name": "Brian", "city": "Seattle"}'
python_obj = json.loads(json_data)
print python_obj["name"]
print python_obj["city"]
