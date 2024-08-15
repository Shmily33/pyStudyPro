from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName('test').setMaster('local[*]')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((6, 7, 8, 9))
rdd3 = sc.parallelize("abcdefh")

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
rdd4 = sc.textFile("../hello.txt")
print(rdd4.collect())
sc.stop()
