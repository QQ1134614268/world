# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/17 21:46
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "user-event",
    group_id="user-event-test",
    bootstrap_servers=[
        "localhost:9093",
        "localhost:9094"
    ]
)
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
