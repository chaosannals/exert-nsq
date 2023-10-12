import nsq

buf = []

def process_message(message):
    global buf
    message.enable_async()
    buf.append(message)
    if len(buf) >= 3:
        for msg in buf:
            print(msg)
            msg.finish()
        buf = []
    else:
        print('deferring processing')

r = nsq.Reader(message_handler=process_message,
        lookupd_http_addresses=['http://127.0.0.1:4161'],
        topic='nsq_reader', channel='async', max_in_flight=9)
nsq.run()