import nsq
import tornado.ioloop
import time

def finish_pub(conn, data):
    print(data)
    
def pub_message():
    writer.pub(
        'exert',
        bytes(time.strftime('%H:%M:%S'), encoding='utf8'),
        finish_pub
    )

writer = nsq.Writer(['127.0.0.1:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()