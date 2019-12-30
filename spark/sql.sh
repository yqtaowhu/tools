#!/bin/sh

set -x

# 指定python环境,conda环境
PYSPARK_DRIVER_PYTHON=./conda_env/bin/python \
spark-submit --queue *** \
    --conf 'spark.executor.cores=5' \
    --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./mypython/conda_env/bin/python \
    --archives ./conda_env.zip#mypython \
    --jars '**.jars' \
    --py-files '**.zip' \
    --py-files '**.py' \
    sql.py 
