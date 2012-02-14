===========
Logstash
===========

Logstash  provides library for creating logstash messages from Python.
The most useful class is the Event class that formats a JSON object into
a Python class. 

    #!/usr/bin/env python

    import logstash

    event = logstash.Event(json_data)
    
For more information on logstash goto the website `here <http://www.logstash.net/>`_
