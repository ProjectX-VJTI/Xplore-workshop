import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from pathlib import Path

script_dir=Path(__file__).resolve().parent
data_dir=script_dir/"data"
train_file=data_dir/"train_3.csv"
test_file=data_dir/"test_3.csv"
submission_file=data_dir/"submission.csv"

def load(file, is_test=False):
    df = pd.read_csv(file)
    if is_test:
        return df
    return (df.iloc[:, 2:-1], df.iloc[:, -1]) 

def eda(X_df, Y_df):
    features = X_df.columns
    n_features = len(features)
    
    fig, axes = plt.subplots(1, n_features, figsize=(5 * n_features, 5))
    for i, col in enumerate(features):
        reg = LinearRegression()
        x_vals = X_df[[col]].values
        reg.fit(x_vals, Y_df)
        
        x_line = np.linspace(x_vals.min(), x_vals.max(), 100).reshape(-1, 1)
        y_line = reg.predict(x_line)
        
        axes[i].scatter(X_df[col], Y_df, alpha=0.5)
        axes[i].plot(x_line, y_line, color='red', linewidth=3)
        axes[i].set_title(f'{col} vs Score')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Score')
    plt.tight_layout()
    plt.show()
def score(model, X_test, Y_test):
    y_pred = model.predict(X_test)
    print("mean squared error:", np.sqrt(mean_squared_error(Y_test, y_pred)))
    print("\nR2 score:\n", r2_score(Y_test, y_pred))

def train():
    X_df, Y_df = load(train_file)
    eda(X_df, Y_df)
    X_arr,Y_arr=X_df.to_numpy(),Y_df.to_numpy()
    X_train,X_test,Y_train,Y_test =train_test_split(X_arr, Y_arr, test_size=0.25, random_state=42)
    model = make_pipeline(StandardScaler(), LinearRegression()) 
    model.fit(X_train, Y_train)
    score(model, X_test, Y_test) 
    return model

def predict(model):
    X_test_df = load(test_file, is_test=True)
    X_test_features = X_test_df.iloc[: ,2:].to_numpy()
    final_predictions = model.predict(X_test_features)
    submit_df = pd.DataFrame()
    submit_df["ID"] = X_test_df["ID"]
    submit_df["score"] = final_predictions
    save_submission(submit_df)
    print("file saved")
def save_submission(submit_df: pd.DataFrame):
    data_dir.mkdir(parents=True, exist_ok=True)
    submit_df.to_csv(submission_file, index=False)
def main():
    model = train()
    predict(model)
if __name__ == "__main__":
    main()