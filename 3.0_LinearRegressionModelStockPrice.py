# Step 1: Reading and Preprocessing Data

import pandas as pd
import boto3
from boto.s3.connection import S3Connection

# Data Reading Using Pandas from AWS
try:
    client = boto3.client('s3')
    with open('aws.txt')as f:
        lines = f.read().splitlines()
    conn = S3Connection(lines[0], lines[1], host='s3.ap-south-1.amazonaws.com')
    Path = 's3://historicaldata03jun2020/HistoricalQuotes.csv'
    data=pd.read_csv(Path)
    print(data.head(2))
except NameError:
    print("Path is in correct")

# PreProcess Data are Cleaning Data
try:
    data.rename(columns={c: c.strip() for c in data.columns.tolist()},inplace=True)
    data.rename(columns={"Close/Last" : "Close"},inplace=True)
    print(data.columns)
except:
    print("function Value errors ")
# Removing Special Characters and converting in to float.
try:
    for val in ['Close','Open','High','Low']:
        data[val]=data[val].str.replace(',','').str.replace('$','').astype(float)
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.strftime('%m/%d/%Y')
    print(data.head(2))
    print(data.dtypes)
    data.to_csv('Newstockdata.csv',index=False)
except:
    print("Values of error")

# Step 2 : Implementation in spark to Train Model and Develop Model

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import csv
from pyspark.sql import SparkSession
# Read Data of Stock in Pyspark
try:
    #sc=SparkContext('local','example')
    #sql=SQLContext(sc)
    #spark=SparkSession.builder.appName("ProcessingPySparkProject").config("Spark.some.config.option","some-value").getOrCreate()
    #StockData=spark.read.format('csv').option('header','true').load(data)
    #print(StockData.take(3))
    #print(StockData.cache())
    sc = SparkContext(master="local", appName="SparkDemo")
    spark = SparkSession(sc)
    stockData = spark.read.csv('Newstockdata.csv', inferSchema="true",header='true')
    print(stockData.cache())
    print(stockData.printSchema())
    print(stockData.describe().toPandas().transpose())
except TypeError:
    print(" Data should be list or RDD ")
except:
    print("Version python Configaration error")

# Splitting data for Creating Model
trainData=stockData.select(['Open','High','Low','Close'])
trainData.show(5) # Important columns to build model from stock data
from pyspark.ml.feature import VectorAssembler
try:
    vectorAssembler=VectorAssembler(inputCols=['Open','High','Low'],outputCol='features')
    stockVecAss=vectorAssembler.transform(trainData)
    stockVecAss=stockVecAss.select(['features','Close'])
    stockVecAss.show(2)
except NameError:
    print("VectorAssembler Problem")

# Data Spliting
#split = stockVecAss.randomSplit([0.7, 0.3])
#train_X = split[0]
#test_X = split[1]
# Model Implementing
from pyspark.ml.regression import LinearRegression
#Model Trainig
try:
    linearRegression=LinearRegression(featuresCol='features',labelCol='Close',maxIter=10,regParam=0.3,elasticNetParam=0.8)
    linearRegressionModel=linearRegression.fit(stockVecAss)
    SplitsTraingTesting = stockVecAss.randomSplit([0.7, 0.3])
    testDataframe = SplitsTraingTesting[1]
except:
    print("Model training Error")
# Model Testing
try:
    Prediction=linearRegressionModel.transform(testDataframe)
    Prediction.select("Prediction","Close","features").show(5)
except:
    print("Testing Model Error")
# Model Summary
from pyspark.ml.evaluation import RegressionEvaluator

try :
    modelEvaluator=RegressionEvaluator(predictionCol='Prediction',labelCol='Close',metricName='r2')
    print(Prediction)

    # Coefficient and Interception
    print("coefficients : "+ str(linearRegressionModel.coefficients))
    print("Intercept  : "+ str(linearRegressionModel.intercept))

    # training Summary
    trainingSummary=linearRegressionModel.summary
    print("RMSE: %f"%trainingSummary.rootMeanSquaredError)
    print("r2: %f" % trainingSummary.r2)
except:
    print(" Model Test have a Problem")

# Step 3 : Saving Linear regression Models

import sys
linearRegressionModel.save('StockLinearRegModel')

import pickle
data='MyPickelFileLRModel'
with open(data,'wb') as f:
    pickle.dump(linearRegressionModel,f)