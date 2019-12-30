# _*_ coding: utf-8 _*_
# @Author: taoyanqi 
# @Date: 2019-12-30

from __future__ import print_function

from datetime import datetime, timedelta
from pyspark.sql import SparkSession

import argparse

sql_template = """
SELECT
    order_id
FROM
    tabel
WHERE
    concat(year, month, day) between {begin_day} and {end_day}
    AND order_status = 5
"""

def main():
    start_time = datetime.now()
    
    begin_day, end_day = "20191230", "20191230"
    _sql = sql_template.format(begin_day=begin_day, end_day=end_day)
    order_df = spark.sql(_sql)

    spend_time = (datetime.now() - start_time).seconds
    print("run minutes:", spend_time/60.0)


def add_arguments(parse):
    parse.add_argument("--data_path", type=str, default="data.txt", help="data path")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    add_arguments(parse)
    flags, unparsed = parse.parse_known_args()

    # 添加spark环境
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .enableHiveSupport() \
        .getOrCreate()
    # 制定python环境是打开
    #sc = spark.sparkContext
    #sc.pythonExec = spark.conf.get('spark.yarn.appMasterEnv.PYSPARK_PYTHON')
    main()