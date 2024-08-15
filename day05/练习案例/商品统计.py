import json

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\python\python.exe"
conf = SparkConf().setAppName("count").setMaster("local[*]")
sc = SparkContext(conf=conf)
rdd = sc.textFile("../orders.txt")
json_str_rdd = rdd.flatMap(lambda x: x.split("|"))  # 这里每个集合都是带引号的字符串
json_rdd = json_str_rdd.map(lambda x: json.loads(x))  # 转json
print(json_rdd.collect())
# 北京市什么商品类别售卖
bj_category_rdd = json_rdd.filter(lambda x: x['areaName'] == "北京").map(lambda x: x['category']).distinct()
print(bj_category_rdd.collect())
# 各个城市销售额排序 大到小
all_money_rdd = json_rdd.map(lambda x: (x['areaName'], int(x['money']))).reduceByKey(lambda a, b: a + b).sortBy(
    lambda x: x[1], ascending=False, numPartitions=1)
print(all_money_rdd.collect())
# 全部城市商品类别
all_category_rdd = json_rdd.map(lambda x: (x['category'])).distinct()
print(all_category_rdd.collect())
