from confluent_kafka import Producer
import socket
from klein import run, route
import json

def setupKafka():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname(),
        'security.protocol': 'PLAINTEXT'
    }

    global producer
    producer = Producer(conf)

    print(producer.list_topics())

@route("/", methods=["POST"])
def setname(request):
    content = json.loads(request.content.read())
    sendMessage(content['message'])
    return

def sendMessage(message):
    producer.produce('messages', message)


if __name__ == '__main__':
    setupKafka()

    run("localhost", 8080)