from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\python\python.exe"
conf = SparkConf().setAppName('test').setMaster('local[*]')
sc = SparkContext(conf=conf)
rdd = sc.parallelize([1, 2, 3, 4, 5])


def func(data):
    return data * 10


rdd2 = rdd.map(lambda x: x * 5 + 5)
print(rdd2.collect())
sc.stop()
