import json
import time
import urlparse
import copy

class Event(object):

    def __init__(self, json_obj = None):
        self.cancelled = False
        if json_obj is None:
            self.data = { "@source": "unknown", 
                          "@type": None,
                          "@tags": [],
                          "@fields": {},
                          "@timestamp": time.strftime("%Y-%m-%dT%H:%M:%S",time.gmtime()),
                          "@message": None
                          }
        else:
            self.data = json.loads(json_obj)

    def cancel(self):
        self.cancelled = true

    def is_cancelled(self):
        return self.cancelled

    def __str__(self):
        return self.data["@timestamp"] + "," + self.data["@source"] + "," + self.data["@message"]

    def getsource(self):
        return self.data["@source"]

    def setsource(self, source):
        val = urlparse.urlparse(source)
        if (val.scheme != ''):
            self.data["@source"] = val.geturl()
            self.data["@source_host"] = val.netloc
            self.data["@source_path"] = val.path
        else:
            self.data["@source"] = source
            self.data["@source_host"] = source

    def gettimestamp(self):
        return self.data["@timestamp"]

    def settimestamp(self, val):
        self.data["@timestamp"] = val

    def getmessage(self):
        return self.data["@message"]
    
    def setmessage(self, val):
        self.data["@message"] = val

    def gettype(self):
        return self.data["@type"]

    def settype(self, val):
        self.data["@type"] = val

    def gettags(self):
        return self.data["@tags"]
    
    def settags(self, val):
        self.data["@tags"] = val

    def overwrite(self, event):
        self.data = hash(event)

    def __hash__(self):
        return hash(data)

    def getfields(self):
        return self.data["@fields"]

    def to_json(self):
        return json.dumps(self.data)

    def get(self, key):
        if key not in self.data["@fields"] and key[0] == '@':
            return self.data[key]
        else:
            return self.data["@fields"][key]

    def put(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            self.data["@fields"][key] = value

    def includes(self, key):
        return (key in self.data or key in self.data["@fields"])

    def remove(self, field):
        if (field in self.data):
            del self.data[field]
        else:
            del self.data["@fields"][field]

    def __eq__(self, other):
        if self.__class__ == other._class__:
            return hash(self) == hash(other)
        else:
            return False

        

   
          
        
