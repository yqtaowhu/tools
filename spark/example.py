# -*- coding: utf-8 -*-
# @Author: yupengarthur
# @Dependence: findspark, numpy, shapely
# python examply.py
import logging

import numpy as np

g_pyspark_py_path = "./mypython/yup_conda/bin/python"
g_pyspark_archives_path = "hdfs:///user/map_point_pickup/rd/yupengarthur/tools/yup_conda2/yup_conda.zip#mypython"
# 上面两句修改时注意保持一致性


# 输出远端主机名，使用的python环境，以及远端当前目录的文件，测试第三方包python-Levenshtein
def mymapper(x):
    import os
    import sys
    import socket

    from shapely.geometry import Point
    from pyspark.sql import Row

    current_files = '||'.join(os.listdir("./"))
    row = Row(host_name=socket.gethostname(),
              py_exec=sys.executable,
              current_files=current_files,
              p=Point(x).to_wkt())
    return row


def main(sc):
    rdd = sc.parallelize([i for i in np.random.randn(100, 2)], 5)
    res = rdd.map(mymapper).collect()
    for i in res:
        logging.info(i)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='./app.log',
        filemode='w')
    logging.info("begin!!!")
    import findspark
    findspark.init(python_path=g_pyspark_py_path)
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName('yup_example') \
        .config("spark.yarn.queue", "root.xinyewusibu-yanfayizu.pickup") \
        .config("spark.executor.memory", "10g") \
        .config("spark.driver.memory", "4g") \
        .config("spark.yarn.dist.archives", g_pyspark_archives_path) \
        .enableHiveSupport() \
        .getOrCreate()
    sc = spark.sparkContext
    try:
        main(sc)
        logging.info("success!!!")
    except Exception as e:
        logging.error(e)
    logging.info("over!!!")

