import unittest
import json
import time
from event import LogEvent

class Test(unittest.TestCase):
    """Unit tests for logstash."""

    def test_create_new_event(self):
        event = LogEvent()
        
        self.assertEqual(event.source, 'Unknown')
        self.assertEqual(event.tags, ())
        self.assertEqual(event.fields, {})
        self.assertFalse(event.isCancelled)
        self.assertEqual(event.type, None)

    def test_create_from_json(self):
        now = time.time()
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
        event = LogEvent(data)
        self.assertEqual(event.source, 'test01.example.com')
        self.assertEqual(event.tags, ('tag1', 'tag2', 'tag3'))
        self.assertEqual(event.fields, { "key1" : "field1",
                                         "key2" : "field2",
                                         "key3" : "field3"
                                       })
        self.assertFalse(event.isCancelled)
        self.assertEqual(event.type, "sometype")
        self.assertEqual(event.timestamp, time.strftime("%Y-%m-%dT%H:%M:%S",now))
        self.assertEqual(event.message, "This is the message")
                                             
if __name__ == "__main__":
    unittest.main()
