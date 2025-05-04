import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import ZZFeatureMap, TwoLocal
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.optimizers import COBYLA, SPSA, ADAM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class VQCModel:
    def __init__(self, feature_dim, ansatz_reps=3, optimizer_name='COBYLA'):
        self.feature_dim = feature_dim
        self.feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=2)
        self.ansatz = TwoLocal(num_qubits=feature_dim, reps=ansatz_reps, rotation_blocks='ry', entanglement_blocks='cz')
        
        if optimizer_name == 'COBYLA':
            self.optimizer = COBYLA(maxiter=200)
        elif optimizer_name == 'SPSA':
            self.optimizer = SPSA(maxiter=200)
        elif optimizer_name == 'ADAM':
            self.optimizer = ADAM(maxiter=200)
        else:
            raise ValueError(f"Unsupported optimizer: {optimizer_name}")
        
        self.vqc = VQC(feature_map=self.feature_map, ansatz=self.ansatz, optimizer=self.optimizer)
        self.scaler = StandardScaler()

    def prepare_data(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        self.vqc.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        y_pred = self.vqc.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.vqc.predict(X_scaled)
