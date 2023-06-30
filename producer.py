from kafka import KafkaProducer

# Kafka 브로커의 IP 주소와 포트를 설정합니다.
bootstrap_servers = 'localhost:9092'

# 프로듀서 객체를 생성합니다.
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# 메시지를 보냅니다.
producer.send('test_topic', b'Hello, Kafka!')

# 프로듀서를 닫습니다.
producer.close()