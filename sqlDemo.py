import requests
import pandas as pd
import pymysql
import numpy as np
import string
from sqlalchemy import create_engine


# 导入数据
def conn_sql():
    conn = pymysql.connect(
        host='60.205.181.110',
        port=3306,
        user='root',
        passwd='941207',
        db='tianchi',
        use_unicode=True,
        charset='utf8',
    )

    sql_cmd = "select * from sample_submit limit 10"
    df = pd.read_sql(sql_cmd, conn)
    return df

df = conn_sql()
print(df.head(5))