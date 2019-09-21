# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/17 21:45
"""
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:9092",
        "localhost:9093",
        "localhost:9094"
    ]
)

future = producer.send("user-event", b'I am rito yan')
try:
    record_metadata = future.get(timeout=10)
    print(record_metadata)
except KafkaError as e:
    print(e)

producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:9092",
        "localhost:9093",
        "localhost:9094"
    ],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)

future = producer.send("user-event", {
    "name": "燕睿涛",
    "age": 26,
    "friends": [
        "ritoyan",
        "luluyrt"
    ]
})
