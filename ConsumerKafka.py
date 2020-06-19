# Step 1 : Reading Header File to Consumer Files

from pyspark import SparkContext
from pyspark.sql import SQLContext
from kafka import KafkaConsumer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegressionModel
import os
#os.environ["SPARK_HOME"] = "/usr/local/spark"
os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"

# Create Spark Context for data reading
try:
    sc = SparkContext.getOrCreate()
    sql=SQLContext(sc)
except NameError:
    print("spark Context is already Define ")

# Loading Model

try:
    path='StockLinearRegModel'
    model=LinearRegressionModel.load(path)
except :
    print("Name Error ")

# consumer Reading
import json
import pandas as pd

def stockPrediction():
    consumer=KafkaConsumer('Project')
    for message in consumer:
        stockValue=json.loads(message.value.decode('utf-8')) # load data in json formate from producer with help consumer
        stockRow=list(stockValue.values()) #Read List of row values
        # print(stockRow)
        data=pd.DataFrame([stockRow],columns=['Open','Close','Volume','High','Low'])
        # Create a data frame with Pandas
        dataframe=sql.createDataFrame(data)
        # Convert pandas data frame in to Spark
        sparkFrame=dataframe.selectExpr("cast(Open as double) Open",
                                        "cast(Close as double) Close",
                                        "cast(Volume as double) Volume",
                                        "cast(High as double) High",
                                        "cast(Low as double) Low")
        # Collected list of row values in object dtype and convert to double type

        vectorAssembler=VectorAssembler(inputCols=['Open','High','Low'],outputCol='features')
        # function to spliting input and output as supervised
        DataframeVect=vectorAssembler.transform(sparkFrame)
        # apply data to split input and output
        #print(DataframeVect)
        DataframeVectFeature=DataframeVect.select(['features','Close'])
        # print only feature and close values
        #print(DataframeVectFeature)

        predictions=model.transform(DataframeVectFeature)
        # predict the new stock value with train model
        predictions.select("prediction","Close","features").show()
        # show the prediction data
        prediction_result=predictions.select('prediction').collect()[0].__getitem__("prediction")
        # calc o/p prediction
        close_value=predictions.select('Close').collect()[0].__getitem__('Close')
        # actual output value
        print(message.key)
        data_time=message.key.decode('utf-8')
        # feature estimation

        return prediction_result, close_value, data_time

stockPrediction()