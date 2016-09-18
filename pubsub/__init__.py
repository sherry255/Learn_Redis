import time
import threading
import redis

def publisher(n):
    time.sleep(1)
    for i in xrange(n):
        conn.publish('channel', i)
        time.sleep(1)

def run_pubsub():
    threading.Thread(target=publisher, args=(3,)).start()
    pubsub = conn