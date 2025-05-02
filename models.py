from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    simulations = db.relationship('Simulation', backref='user', lazy=True)


class Simulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    num_timelines = db.Column(db.Integer, default=1024)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    predictions = db.relationship('Prediction', backref='simulation', lazy=True)
    quantum_states = db.relationship('QuantumState', backref='simulation', lazy=True)


class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'), nullable=False)
    probability_landscape = db.Column(db.JSON)
    optimal_strategy = db.Column(db.JSON)
    quantum_volatility = db.Column(db.Float)
    dark_energy_consumption = db.Column(db.Float)


class QuantumState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'), nullable=False)
    timeline_id = db.Column(db.String(64), nullable=False)
    state_vector = db.Column(db.JSON)
    market_parameters = db.Column(db.JSON)
    entanglement_degree = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class OrderBookManipulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'), nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    quark_states = db.Column(db.JSON)
    distorted_geometry = db.Column(db.JSON)
    energy_output = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class DarkEnergyToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(42), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    fluctuation_rate = db.Column(db.Float)
    casimir_effect = db.Column(db.Float)
    hawking_radiation = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
