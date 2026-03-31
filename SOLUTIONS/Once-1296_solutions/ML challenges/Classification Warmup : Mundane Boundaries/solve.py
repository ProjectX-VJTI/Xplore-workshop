import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pathlib import Path

script_dir = Path(__file__).resolve().parent
data_dir = script_dir / "data"
train_file = data_dir / "train_1.csv"
test_file =data_dir / "test_1.csv"
submission_file = data_dir / "submission.csv"

def load(file, is_test = False):
    df = pd.read_csv(file)
    if is_test:
        return df
    return (df.iloc[:,:-1] , df.iloc[:,-1]) 

def eda():
    # do your observations here
    pass

def score():
    pass

def train():
    X_df, Y_df = load(train_file)
    X_arr, Y_arr = X_df.to_numpy(), Y_df.to_numpy()
    # eda()
    X_train, X_test, Y_train, Y_test = train_test_split(X_arr,Y_arr, test_size=0.2, random_state=42)
    # do training
    # model = (...)
    # score(...)
    # return model
    pass

def predict(model:None):
    X_test_df = load(test_file,is_test=True)
    # X_test_arr =  X_test_df.to_numpy()
    # Y_rest = model.predict(X_test_arr,..)
    submit_df = pd.DataFrame()
    submit_df["ID"] = X_test_df["ID"]
    submit_df["score"] = [1e-7 + np.random.rand() for _ in range(len(X_test_df))]
    # filler code
    save_submission(submit_df)


def save_submission(submit_df:pd.DataFrame):
    submit_df.to_csv(submission_file, index=False)

def main():
    model = train()
    predict(model)

if __name__ =="__main__":
    main()