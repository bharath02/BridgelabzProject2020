from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
#conf=(SparkConf().setAppName("App_name").setMaster("local[4]"))
sc=SparkContext(master="local",appName="SparkDemo")
spark=SparkSession(sc)
stockData=spark.read.csv("/home/hduser/Project/HistoricalQuotes.csv",header='true')
print(stockData.printSchema())
stockData.cache()
def clearString(value : str) -> str:
    value =value.repalce('$'," ")
    return float(value)
from pyspark.sql.types import DoubleType, StringType
from pyspark.sql.functions import udf, col
rmStringVal=udf(lambda value: clearString(value), DoubleType())

stockData=stockData.withColumn("Date",stockData["Date"].cast("string")
                                   ).withColumn("Close/Last",rmStringVal(col("Close/Last"))
                                   ).withColumn("Volume",rmStringVal(col("Volume"))
                                   ).withColumn("Open",rmStringVal(col("Open"))
                                   ).withColumn("High",rmStringVal(col("High"))
                                   ).withColumn("Low",rmStringVal(col("Low")))
print(stockData.printSchema())