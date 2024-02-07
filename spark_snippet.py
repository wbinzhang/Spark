# -*- coding: utf-8 -*-
# @Time    : 2024/2/7 22:22
# @Author  : zhangwenbin

# 启动pyspark-shell
# export PYSPARK_PYTHON=py37/bin/python
# export PYSPARK_DRIVER_PYTHON=/home/work/anaconda3/envs/py37_wenbin/bin/python
# pyspark \n
# --cluster zjyprc-hadoop-spark3.1 \n
# --master yarn \n
# --deploy-mode client \n
# --queue {填写队列资源} \n
# --executor-cores 2 --driver-memory 2G --executor-memory 1G
# --conf spark.yarn.job.owners=zhangwenbin \n
# --conf spark.files.localize=./hive-site.xml \n
# --conf spark.sql.extensions={} \n
# --conf spark.sql.session.token.decrypted={} \n
# --conf spark.security.credentials.hive.enabled=true \n
# --jars {jar包地址} \n
# --conf spark.dynamicAllocation.enabled=true \n
# --conf spark.dynamicAllocation.minExecutors=1 \n
# --conf spark.dynamicAllocation.maxExecutors=500 \n
# --conf spark.yarn.dist.archives={python打包环境的地址}


