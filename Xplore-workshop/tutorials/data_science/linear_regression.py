import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load Data
housing = fetch_california_housing()
X = StandardScaler().fit_transform(housing.data)
y = housing.target.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class MyLinearRegression:
    def __init__(self, n_features, alpha=0.01):
        # Initialize Weights and Bias
        self.W = np.random.randn(n_features, 1) * 0.01
        self.b = np.zeros((1, 1))
        self.alpha = alpha
        self.history = []

    def forward(self, X):
        # Linear Function: y = XW + b
        return X @ self.W + self.b

    def backward(self, X, y, yhat):
        m = y.shape[0]
        # MSE Gradient: dL/dyhat = (yhat - y)
        # Using Chain Rule: dL/dW = dL/dyhat * dyhat/dW
        error = yhat - y
        
        dW = (X.T @ error) / m
        dB = np.sum(error) / m
        
        # Update parameters
        self.W -= self.alpha * dW
        self.b -= self.alpha * dB

    def fit(self, X, y, epochs=500):
        for e in range(epochs):
            yhat = self.forward(X)
            # MSE Loss: 1/2m * sum((yhat - y)^2)
            loss = np.mean((yhat - y)**2) / 2
            self.backward(X, y, yhat)
            
            if e % 50 == 0:
                self.history.append(loss)
                print(f"Epoch {e}, MSE Loss: {loss:.4f}")

# Train the model
model = MyLinearRegression(n_features=X_train.shape[1], alpha=0.1)
model.fit(X_train, y_train, epochs=1000)

# 3. Visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot Loss Curve
ax1.plot(model.history)
ax1.set_title("Training Loss (MSE)")
ax1.set_xlabel("Iterations (x50)")
ax1.set_ylabel("Loss")

# Plot Predicted vs Actual
y_pred = model.forward(X_test)
ax2.scatter(y_test, y_pred, alpha=0.3, color='green')
ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
ax2.set_title("Predictions vs Actual")
ax2.set_xlabel("Actual Price")
ax2.set_ylabel("Predicted Price")

plt.tight_layout()
plt.show()

# Evaluation
final_mse = np.mean((y_pred - y_test)**2)
print(f"Final Test MSE: {final_mse:.4f}")

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(f"R^2 Score: {r2:.4f}")