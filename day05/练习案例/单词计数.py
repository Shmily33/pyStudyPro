from pyspark import SparkConf, SparkContext
import os



os.environ['PYSPARK_PYTHON'] = "D:\python\python.exe"
conf = SparkConf().setAppName("hello").setMaster("local[*]")
sc = SparkContext(conf=conf)
rdd = sc.textFile("../hello.txt")
# print(rdd.collect())
words = rdd.flatMap(lambda x: x.split(" "))  # 得到所有单词
# print(words.collect())
word_one = words.map(lambda x: (x, 1))  # 得到每个单词：1的元组
word_count = word_one.reduceByKey(lambda x, y: x + y)  # reduceByKey去计算 ByKey根据key分组了
print(word_count.collect())
