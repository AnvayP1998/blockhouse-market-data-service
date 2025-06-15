from confluent_kafka import Producer
import json

KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(KAFKA_CONFIG)

def publish_price_event(event: dict, topic: str = "price-events"):
    try:
        payload = json.dumps(event)
        producer.produce(topic, value=payload.encode('utf-8'))
        producer.flush()
        print(f"Published event: {payload}")
        return True
    except Exception as e:
        print(f"Kafka publish error: {e}")
        return False
