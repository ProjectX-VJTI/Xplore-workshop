# Scikit-Learn (Machine Learning)
# -------------------------------
# A robust library for machine learning in Python. It features various classification, 
# regression, and clustering algorithms.
#
# NOTE: Per instructions, this script contains NO terminal output (no print statements).
# It will silently train 6 different models and display their decision boundaries 
# on a single matplotlib window.

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.inspection import DecisionBoundaryDisplay

# Importing 6 different Machine Learning Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

# 1. Dataset Generation
# ---------------------
# make_moons generates a 2D binary classification dataset that is non-linearly separable.
X, y = make_moons(n_samples=400, noise=0.25, random_state=42)

# Splitting the data into training (70%) and testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Model Initialization
# -----------------------
# Storing our 6 models in a dictionary for easy iteration
models = {
    "Logistic Regression (Linear)": LogisticRegression(),
    "Decision Tree (Blocky)": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest (Ensemble)": RandomForestClassifier(n_estimators=50, random_state=42),
    "SVM (RBF Kernel)": SVC(gamma=2, C=1, random_state=42),
    "K-Nearest Neighbors (K=3)": KNeighborsClassifier(n_neighbors=3),
    "Neural Network (MLP)": MLPClassifier(alpha=1, max_iter=1000, random_state=42)
}

# 3. Plotting Setup
# -----------------
# Create a single window with a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("Scikit-Learn Classifier Comparison on 'Moons' Dataset", fontsize=18)

# Color maps for boundaries and data points
cm_background = plt.cm.RdBu
cm_points = ListedColormap(["#FF0000", "#0000FF"])

# 4. Training and Visualization Loop
# ----------------------------------
for ax, (name, model) in zip(axes.flatten(), models.items()):
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Draw the decision boundaries (colored background areas)
    DecisionBoundaryDisplay.from_estimator(
        model, X, cmap=cm_background, alpha=0.6, ax=ax, eps=0.5
    )
    
    # Plot the training points (solid colors)
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_points, edgecolors="white", s=40)
    
    # Plot the testing points (slightly transparent to differentiate from training)
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_points, edgecolors="black", alpha=0.5, s=40)
    
    # Formatting the subplot
    ax.set_title(name, fontsize=12)
    ax.set_xticks(())
    ax.set_yticks(())

# Adjust layout and display the single window containing all 6 models
plt.tight_layout()
plt.show()