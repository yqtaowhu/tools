# 如何在spark上使用自己的python环境

## 1. conda使用
```
# 创建conda环境指定目录-p
conda create -p your_path -q python=2.7
# conda 环境列表
conda env list
# 激活conda 
source activate your_path
# 释放
source deactivate you_path
```

## 2. 安装打包用spark
```
# 打包
zip -r -q tyq_conda.zip tyq_conda
# 上传hdfs
```

## 3. jupyter 配置
```

import os
import sys
import json
import findspark

# 指定python环境, 注意统一
g_pyspark_py_path = "./mypython/tyq_conda/bin/python"
g_pyspark_archives_path = "hdfs://DClusterNmg3/user/map_point_pickup/taoyanqi/tyq_conda.tar.gz#mypython"
findspark.init(python_path=g_pyspark_py_path)

def spark_init(app_name='pyspark-shell'):
    spark_home = os.environ.get('SPARK_HOME', None)
    user = os.environ.get('USER', None)
    print("\nuser", user,
          "\nspark_home:", spark_home
    )

    sys.path.insert(0, spark_home + '/python')
    if '16' in spark_home:
        sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.9-src.zip'))
    else:
        sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.4-src.zip'))

    os.environ['PYSPARK_SUBMIT_ARGS'] = "pyspark-shell"
    # 设置属性
    from pyspark.context import SparkContext
    SparkContext.setSystemProperty('spark.yarn.queue', 'root.xinyewusibu-yanfayizu.search')
    SparkContext.setSystemProperty('spark.files.overwrite', 'true')
    SparkContext.setSystemProperty('spark.speculation.quantile', '0.9')
    SparkContext.setSystemProperty('spark.speculation.multiplier', '1.5')
    SparkContext.setSystemProperty('spark.app.name', '{}-{}'.format(app_name, user))
    SparkContext.setSystemProperty('spark.kryoserializer.buffer.max', '256m')
    SparkContext.setSystemProperty('spark.kryoserializer.buffer', '64m')
    SparkContext.setSystemProperty('spark.executor.memory', '13g')
    SparkContext.setSystemProperty('spark.executor.cores', '1')
    #SparkContext.setSystemProperty('spark.default.parallelism', '600')
    SparkContext.setSystemProperty('spark.yarn.dist.archives', g_pyspark_archives_path)
    return os.path.join(spark_home, "python/pyspark/shell.py")

path = spark_init()
exec(open(path).read())
```

## 4. python脚本
    见example.py
