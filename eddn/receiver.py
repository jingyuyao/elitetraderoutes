import zlib
import zmq
import simplejson
import sys
import time
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elitetraderoutes.settings")

import django
django.setup()
from eddn.ingester import Ingester

"""
 "  Configuration
"""
__relayEDDN             = 'tcp://eddn-relay.elite-markets.net:9500'
__timeoutEDDN           = 600000


"""
 "  Start
"""    
def main():
    context     = zmq.Context()
    subscriber  = context.socket(zmq.SUB)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"")
    subscriber.setsockopt(zmq.RCVTIMEO, __timeoutEDDN)

    ingester = Ingester()

    print('EDDN receiver started...')
    while True:
        try:
            subscriber.connect(__relayEDDN)
            
            while True:
                __message   = subscriber.recv()
                
                if __message == False:
                    subscriber.disconnect(__relayEDDN)
                    break
                
                __message   = zlib.decompress(__message)
                __json      = simplejson.loads(__message)

                ingester.ingest(__json)

                sys.stdout.flush()
                
        except zmq.ZMQError as e:
            print ('ZMQSocketException: ' + str(e))
            sys.stdout.flush()
            subscriber.disconnect(__relayEDDN)
            time.sleep(5)
            
        

if __name__ == '__main__':
    main()
