from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import *

# from udf_def import predict


settings = EnvironmentSettings.new_instance().use_blink_planner().build()
exec_env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(exec_env, environment_settings=settings)

# t_env.create_temporary_function("predict", predict)

SOURCE_DDL = """
CREATE TABLE source (
    label INT,
    f1 DOUBLE,
    f2 DOUBLE,
    f3 DOUBLE,
    f4 DOUBLE,
    f5 DOUBLE,
    f6 DOUBLE,
    f7 DOUBLE,
    f8 DOUBLE,
    f9 DOUBLE,
    f10 DOUBLE,
    f11 DOUBLE,
    f12 DOUBLE,
    f13 DOUBLE,
    f14 DOUBLE,
    f15 DOUBLE,
    f16 DOUBLE,
    f17 DOUBLE,
    f18 DOUBLE,
    f19 DOUBLE,
    f20 DOUBLE,
    f21 DOUBLE,
    f22 DOUBLE,
    f23 DOUBLE,
    f24 DOUBLE,
    f25 DOUBLE,
    f26 DOUBLE,
    f27 DOUBLE,
    f28 DOUBLE
) WITH (
    'connector' = 'filesystem',
    'format' = 'csv',
    'csv.field-delimiter' = '\t',
    'path' = '/Users/chenyisheng/source/yiksanchan/pyflink-lightgbm-batch-inference/data/regression.test'
)
"""

SINK_DDL = """
CREATE TABLE sink (
    label INT
) WITH (
    'connector' = 'print'
)
"""

TRANSFORM_DML = """
INSERT INTO sink
SELECT label FROM source
"""

t_env.execute_sql(SOURCE_DDL)
t_env.execute_sql(SINK_DDL)
t_env.execute_sql(TRANSFORM_DML).wait()
