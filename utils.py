from pathlib import Path
import pandas as pd

def load_data():
    print('Loading data...')
    # load or create your dataset
    regression_example_dir = Path.cwd() / 'data'
    df_train = pd.read_csv(str(regression_example_dir / 'regression.train'), header=None, sep='\t')
    df_test = pd.read_csv(str(regression_example_dir / 'regression.test'), header=None, sep='\t')

    y_train = df_train[0]
    y_test = df_test[0]
    X_train = df_train.drop(0, axis=1)
    X_test = df_test.drop(0, axis=1)

    return (X_train, y_train), (X_test, y_test)