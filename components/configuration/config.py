from 

def configurations(req):
    
    data = json.loads('../../config.json')

    try:
        print (data[req])
    except KeyError:
        return ('Doesnt exists')
    
    