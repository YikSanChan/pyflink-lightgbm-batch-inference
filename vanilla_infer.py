import lightgbm as lgb
from utils import load_data
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    gbm = lgb.Booster(model_file="model.txt")

    print('Starting predicting...')
    _, (X_test, y_test) = load_data()
    # predict
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    # eval
    rmse_test = mean_squared_error(y_test, y_pred) ** 0.5
    print(f'The RMSE of prediction is: {rmse_test}')
