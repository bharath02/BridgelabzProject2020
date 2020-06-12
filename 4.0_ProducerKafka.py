# header file to producer
from time import sleep
from kafka import KafkaProducer
from alpha_vantage.timeseries import TimeSeries
import random
import json

# Read data from GOOGL Stock Price
def Data():
    lines=open('aws.txt').read().splitlines() # alpha_vantage key for access from file
    keys=random.choice(lines[2]) # read a key values
    time = TimeSeries(key=keys,output_format='json') # wedsite access function formate of data reading
    data,metadata=time.get_intraday(symbol='GOOGL',interval='1min',outputsize='full') # which company stock data interval
    return data

# Read data with kafka with producer
def Message(producerKey,key,data_key):
    key_byte=bytes(key,encoding='utf-8') # provide key
    producerKey.send("Project",json.dumps(data[key]).encode('utf-8'),key_byte)
    print("message published")
# Connection of producer kafka
def kafkaProducerConnection():
    producer=KafkaProducer(bootstrap_servers=['localhost:9092'])
    return producer
# main function to access the producer
if __name__=="__main__":
    data=Data()
    if(len(data)>0):
        producer=kafkaProducerConnection()
        for key in sorted(data):
            Message(producer,key,data[key])
            sleep(2)
