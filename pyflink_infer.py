import logging
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table.udf import ScalarFunction, udf
from pyflink.table import DataTypes, EnvironmentSettings, StreamTableEnvironment

class Predict(ScalarFunction):
    def open(self, function_context):
        import lightgbm as lgb

        logging.info("Loading model...")
        self.model = lgb.Booster(model_file="archive.zip/model.txt")

    def eval(self, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28):
        import pandas as pd

        logging.info("Predicting, batch size=%d...", len(f1))
        df = pd.concat([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28], axis=1)
        return pd.Series(self.model.predict(df))


settings = EnvironmentSettings.new_instance().use_blink_planner().build()
exec_env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(exec_env, environment_settings=settings)

predict = udf(Predict(), result_type=DataTypes.DOUBLE(), func_type="pandas")

t_env.create_temporary_function("predict", predict)

SOURCE = """
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

SINK = """
CREATE TABLE sink (
    prediction DOUBLE
) WITH (
    'connector' = 'print'
)
"""

TRANSFORM = """
INSERT INTO sink
SELECT PREDICT(
    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28
) FROM source
"""

t_env.execute_sql(SOURCE)
t_env.execute_sql(SINK)
t_env.execute_sql(TRANSFORM)
