from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, StringType
from pyspark.sql.functions import udf, col

spark=SparkSession.builder.master("spark://stcpgrnlp06.options-it.com:7087")\
    .appName("__SPARK_APP_NAME__")\
    .config("spark.executor.memory","50g")\
    .config("spark.eventlog.enabled","true")\
    .config("spark.eventlog.dir",r"/net/share/grid/bin/spark/UAT/SparkLogs/")\
    .config("spark.cores.max",128)\
    .config("spark.sql.crossJoin.enabled", "True") \
    .config("spark.executor.extraLibraryPath","/net/share/grid/bin/spark/UAT/bin/vertica-jdbc-8.0.0-0.jar") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.logConf", "true") \
    .getOrCreate()
sc=spark.sparkContext
sc.setLogLevel("INFO")
print(sc)