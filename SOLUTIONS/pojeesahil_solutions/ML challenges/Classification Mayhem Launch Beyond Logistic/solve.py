import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline
from pathlib import Path

script_dir=Path(__file__).resolve().parent
data_dir=script_dir/"data"
train_file=data_dir/"train_2.csv"
test_file=data_dir/"test_2.csv"
submission_file=data_dir/"submission.csv"

def load(file, is_test=False):
    df = pd.read_csv(file)
    if is_test:
        return df
    return (df.iloc[:, 1:3], df.iloc[:, -1]) 

def eda(X_df, Y_df):
    plt.figure(figsize=(8, 6))
    plt.scatter(X_df.loc[Y_df==0, 'X'], X_df.loc[Y_df==0, 'Y'], color='blue', label='Class 0', alpha=0.6)
    plt.scatter(X_df.loc[Y_df==1, 'X'], X_df.loc[Y_df==1, 'Y'], color='red', label='Class 1', alpha=0.6)
    plt.title('Data')
    plt.xlabel('Feature X')
    plt.ylabel('Feature Y')
    plt.legend()
    plt.show()

def score(model, X_test, Y_test):
    y_pred = model.predict(X_test)
    print("Accuracy Score:", accuracy_score(Y_test, y_pred))
    print("\nClassification Report:\n", classification_report(Y_test, y_pred))

def train():
    X_df, Y_df = load(train_file)
    eda(X_df, Y_df)
    X_arr,Y_arr=X_df.to_numpy(),Y_df.to_numpy()
    X_train,X_test,Y_train,Y_test =train_test_split(X_arr, Y_arr, test_size=0.25, random_state=42)
    #svc 64.7 accuracy
    # KNeighborsClassifier(n_neighbors=3) 92.7% accuracy
    model = make_pipeline(StandardScaler(),RandomForestClassifier(n_estimators=100, random_state=42)) #93.9% accuracy
    model.fit(X_train, Y_train)
    score(model, X_test, Y_test) 
    return model

def predict(model):
    X_test_df = load(test_file, is_test=True)
    X_test_features = X_test_df.drop(columns=['ID']).to_numpy()
    final_predictions = model.predict_proba(X_test_features)[:,1]
    submit_df = pd.DataFrame()
    submit_df["ID"] = X_test_df["ID"]
    submit_df["Class"] = final_predictions
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