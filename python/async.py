import nsq

conn = nsq.AsyncConn(
    host='127.0.0.1',
    port=4150
)