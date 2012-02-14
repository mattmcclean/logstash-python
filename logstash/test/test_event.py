import unittest
import json
import time
from logstash.event import Event

class Test(unittest.TestCase):
    """Unit tests for logstash."""

    def test_create_new_event(self):
        event = Event()
        
        self.assertEqual(event.getsource(), 'unknown')
        self.assertEqual(event.gettags(), [])
        self.assertEqual(event.getfields(), {})
        self.assertFalse(event.is_cancelled())
        self.assertEqual(event.gettype(), None)

    def test_create_from_json(self):
        now = time.gmtime()
        data = json.dumps({ "@source": "test01.example.com",
                 "@type" : "sometype",
                 "@tags" : [ "tag1", "tag2", "tag3" ],
                 "@fields" : { "key1" : "field1",
                               "key2" : "field2",
                               "key3" : "field3" 
                             },
                 "@timestamp" : time.strftime("%Y-%m-%dT%H:%M:%S",now),
                 "@message" : "This is the message"
                })
        event = Event(data)
        self.assertEqual(event.getsource(), 'test01.example.com')
        self.assertEqual(event.gettags(), ['tag1', 'tag2', 'tag3'])
        self.assertEqual(event.getfields(), { "key1" : "field1",
                                         "key2" : "field2",
                                         "key3" : "field3"
                                       })
        self.assertFalse(event.is_cancelled())
        self.assertEqual(event.gettype(), "sometype")
        self.assertEqual(event.gettimestamp(), time.strftime("%Y-%m-%dT%H:%M:%S",now))
        self.assertEqual(event.getmessage(), "This is the message")

    def test_get_fields(self):
        now = time.gmtime()
        data = json.dumps({ "@source": "test01.example.com",
                 "@type" : "sometype",
                 "@tags" : [ "tag1", "tag2", "tag3" ],
                 "@fields" : { "key1" : "field1",
                               "key2" : "field2",
                               "key3" : "field3" 
                             },
                 "@timestamp" : time.strftime("%Y-%m-%dT%H:%M:%S",now),
                 "@message" : "This is the message"
                })
        event = Event(data)
        self.assertEqual(event.get("@source"), 'test01.example.com')
        self.assertEqual(event.get("@tags"), ['tag1', 'tag2', 'tag3'])
        self.assertEqual(event.get("key1"), "field1")
        self.assertEqual(event.get("key2"), "field2")
        self.assertEqual(event.get("key3"), "field3")
        self.assertEqual(event.get("@type"), "sometype")
        self.assertEqual(event.get("@timestamp"), time.strftime("%Y-%m-%dT%H:%M:%S",now))
        self.assertEqual(event.get("@message"), "This is the message")

    def test_set_source(self):
        event = Event()
        event.setsource("http://www.example.com/some/path")

        self.assertEqual(event.get("@source"), "http://www.example.com/some/path")
        self.assertEqual(event.get("@source_host"), "www.example.com")
        self.assertEqual(event.get("@source_path"), "/some/path")

        event = Event()
        event.setsource("www.example.com")
        self.assertEqual(event.get("@source"), "www.example.com")
        self.assertEqual(event.get("@source_host"), "www.example.com")
        try:
            event.get("@source_path")
        except KeyError:
            pass
        else:
            self.fail("should have thrown KeyError")
                                             
if __name__ == "__main__":
    unittest.main()
