from kafka import KafkaConsumer

# Kafka 브로커의 IP 주소와 포트를 설정합니다.
bootstrap_servers = 'localhost:9092'

# 컨슈머 객체를 생성합니다.
consumer = KafkaConsumer('test_topic', bootstrap_servers=bootstrap_servers)

# 메시지를 수신합니다.
for message in consumer:
    print(message.value.decode('utf-8'))

# 컨슈머를 닫습니다.
consumer.close()