import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and Scale Data
data = load_breast_cancer()
X = StandardScaler().fit_transform(data.data) # Normalization is vital for Sigmoid
y = data.target.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class MyNeuralNet:
    def __init__(self, dims, alpha=0.1):
        self.alpha = alpha
        self.weights = [np.random.randn(dims[i], dims[i+1]) * 0.01 for i in range(len(dims)-1)]
        self.biases = [np.zeros((1, dims[i+1])) for i in range(len(dims)-1)]
        self.history = []

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def sigmoid_deriv(self, a):
        # derivative in terms of the output activation a = sigmoid(z)
        return a * (1 - a)

    def forward(self, X):
        self.A = [X]
        self.Z = []
        for w, b in zip(self.weights, self.biases):
            z = self.A[-1] @ w + b
            self.Z.append(z)
            self.A.append(self.sigmoid(z))
        return self.A[-1]

    def backward(self, y):
        m = y.shape[0]
        # Initial error at output layer (BCE + Sigmoid shortcut)
        dz = self.A[-1] - y 
        
        for i in reversed(range(len(self.weights))):
            dw = (self.A[i].T @ dz) / m
            db = np.sum(dz, axis=0, keepdims=True) / m
            
            if i > 0:
                # Backpropagate error to the previous layer
                dz = (dz @ self.weights[i].T) * self.sigmoid_deriv(self.A[i])
            
            # Update weights
            self.weights[i] -= self.alpha * dw
            self.biases[i] -= self.alpha * db

    def fit(self, X, y, epochs=1000):
        for e in range(epochs):
            yhat = self.forward(X)
            loss = -np.mean(y * np.log(yhat + 1e-8) + (1 - y) * np.log(1 - yhat + 1e-8))
            self.backward(y)
            if e % 100 == 0:
                self.history.append(loss)
                print(f"Epoch {e}, Loss: {loss:.4f}")

# Initialize and Train
nn = MyNeuralNet([X_train.shape[1], 16, 8, 1], alpha=0.5)
nn.fit(X_train, y_train, epochs=2000)

# Visualization
plt.plot(nn.history)
plt.title("Training Loss (Binary Cross Entropy)")
plt.xlabel("Epochs (x100)")
plt.ylabel("Loss")
plt.show()

# Evaluation
preds = (nn.forward(X_test) > 0.5).astype(int)
accuracy = np.mean(preds == y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")