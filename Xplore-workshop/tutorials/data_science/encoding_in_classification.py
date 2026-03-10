"""
Encoding Techniques Showcase for Classification

This script compares Ordinal Encoding, One-Hot Encoding, and Hybrid Encoding
strategies using Logistic Regression, visualizing loss curves and confusion maps.
"""

# -------------------- Imports --------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

# -------------------- Dataset Generation --------------------
# Generate numerical data
import numpy as np
import pandas as pd

np.random.seed(42)
N = 3000

df = pd.DataFrame({
    # Numerical features
    "age": np.random.randint(21, 65, N),
    "experience": np.random.randint(0, 40, N),
    "salary": np.random.normal(60000, 15000, N),
    "hours_per_week": np.random.randint(20, 60, N),

    # Ordinal categorical (true ordering)
    "education": np.random.choice(
        ["HighSchool", "Bachelors", "Masters", "PhD"],
        N,
        p=[0.3, 0.4, 0.2, 0.1]
    ),
    "job_level": np.random.choice(
        ["Junior", "Mid", "Senior", "Lead"],
        N,
        p=[0.35, 0.35, 0.2, 0.1]
    ),
    "risk_appetite": np.random.choice(
        ["Low", "Medium", "High"],
        N,
        p=[0.4, 0.4, 0.2]
    ),

    # Nominal categorical (no ordering)
    "department": np.random.choice(
        ["Tech", "HR", "Finance", "Sales", "Marketing"],
        N
    ),
    "city": np.random.choice(
        ["A", "B", "C", "D", "E", "F"],
        N
    ),
    "employment_type": np.random.choice(
        ["FullTime", "Contract", "Intern"],
        N
    ),
})

# ----- Ground truth logic (THIS is what makes encoding matter) -----
education_weight = {
    "HighSchool": 0,
    "Bachelors": 1,
    "Masters": 2,
    "PhD": 3
}

job_weight = {
    "Junior": 0,
    "Mid": 1,
    "Senior": 2,
    "Lead": 3
}

risk_weight = {
    "Low": -1,
    "Medium": 0,
    "High": 1
}

score = (
    0.03 * df["age"]
    + 0.05 * df["experience"]
    + 0.00004 * df["salary"]
    + df["education"].map(education_weight)
    + 1.5 * df["job_level"].map(job_weight)
    + df["risk_appetite"].map(risk_weight)
    + np.random.normal(0, 1, N)
)

df["target"] = (score > np.median(score)).astype(int)

# -------------------- Train-Test Split --------------------
X_train, X_test, y_train, y_test = train_test_split(
    df, df["target"], test_size=0.25, random_state=42
)

num_cols = [
    "age", "experience", "salary", "hours_per_week"
]

ord_cols = [
    "education", "job_level", "risk_appetite"
]

nom_cols = [
    "department", "city", "employment_type"
]

# -------------------- Helper Function --------------------
def train_logreg(X_train, X_test, y_train, y_test, epochs=10):
    # Train logistic regression and track log loss
    from sklearn.linear_model import SGDClassifier
    model = SGDClassifier(
        loss="log_loss",
        learning_rate="optimal",
        max_iter=100,
        warm_start=True,
        random_state=42
    )
    losses = []

    for _ in range(epochs):
        model.fit(X_train, y_train)
        probas = model.predict_proba(X_test)
        losses.append(log_loss(y_test, probas))

    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)
    acc = accuracy_score(y_test, preds)

    return losses, cm, acc

# -------------------- Encoding Strategies --------------------
losses_all = []
cms_all = []
titles = ["Ordinal Encoding", "One-Hot Encoding", "Hybrid Encoding"]

# -------- 1. Ordinal Encoding --------
ordinal_pipeline = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("ord", OrdinalEncoder(), ord_cols + nom_cols),
])

Xtr = ordinal_pipeline.fit_transform(X_train)
Xte = ordinal_pipeline.transform(X_test)

losses, cm, acc = train_logreg(Xtr, Xte, y_train, y_test)
losses_all.append(losses)
cms_all.append(cm)

# -------- 2. One-Hot Encoding --------
onehot_pipeline = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(), ord_cols + nom_cols),
])

Xtr = onehot_pipeline.fit_transform(X_train)
Xte = onehot_pipeline.transform(X_test)

losses, cm, acc = train_logreg(Xtr, Xte, y_train, y_test)
losses_all.append(losses)
cms_all.append(cm)

# -------- 3. Hybrid Encoding --------
hybrid_pipeline = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("ord", OrdinalEncoder(), ord_cols),
    ("nom", OneHotEncoder(), nom_cols),
])

Xtr = hybrid_pipeline.fit_transform(X_train)
Xte = hybrid_pipeline.transform(X_test)

losses, cm, acc = train_logreg(Xtr, Xte, y_train, y_test)
losses_all.append(losses)
cms_all.append(cm)

# -------------------- Visualization --------------------
fig, axes = plt.subplots(2, 3, figsize=(15, 8))


# can you explain the funny looking graphs 🤣, assignment for yall

# Top row: Log loss curves
for i in range(3):
    axes[0, i].plot(losses_all[i])
    axes[0, i].set_title(titles[i])
    axes[0, i].set_xlabel("Epochs")
    axes[0, i].set_ylabel("Log Loss")

# Bottom row: Confusion matrices
for i in range(3):
    sns.heatmap(cms_all[i], annot=True, fmt="d", cmap="Blues", ax=axes[1, i])
    axes[1, i].set_title(f"{titles[i]} Confusion Matrix")
    axes[1, i].set_xlabel("Predicted")
    axes[1, i].set_ylabel("Actual")

plt.tight_layout()
plt.show()