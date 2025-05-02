from flask import render_template, request, jsonify, redirect, url_for, flash, session
from app import app, db
from models import Simulation, Prediction, QuantumState, OrderBookManipulation, DarkEnergyToken
from quantum_engine.predictor import QuantumMultiversePredictor
from quantum_engine.nanobots import PlasmaNanobotSwarm
from quantum_engine.economics import simulate_dark_energy_token
import json
import numpy as np
import logging
from datetime import datetime

# Make now() function available to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    simulations = Simulation.query.order_by(Simulation.created_at.desc()).limit(10).all()
    return render_template('dashboard.html', simulations=simulations)


@app.route('/simulation/<int:sim_id>')
def simulation_detail(sim_id):
    simulation = Simulation.query.get_or_404(sim_id)
    predictions = Prediction.query.filter_by(simulation_id=sim_id).order_by(Prediction.timestamp.desc()).limit(5).all()
    quantum_states = QuantumState.query.filter_by(simulation_id=sim_id).limit(10).all()
    manipulations = OrderBookManipulation.query.filter_by(simulation_id=sim_id).order_by(OrderBookManipulation.timestamp.desc()).limit(5).all()
    
    return render_template('simulation.html', 
                          simulation=simulation, 
                          predictions=predictions, 
                          quantum_states=quantum_states, 
                          manipulations=manipulations)


@app.route('/api/create_simulation', methods=['POST'])
def create_simulation():
    try:
        data = request.json
        
        # For demo purposes, use a default user ID
        user_id = 1
        
        new_simulation = Simulation(
            name=data.get('name', 'New Simulation'),
            description=data.get('description', ''),
            num_timelines=data.get('num_timelines', 1024),
            user_id=user_id
        )
        
        db.session.add(new_simulation)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'simulation_id': new_simulation.id,
            'message': 'Simulation created successfully'
        }), 201
        
    except Exception as e:
        logging.error(f"Error creating simulation: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/run_prediction', methods=['POST'])
def run_prediction():
    try:
        data = request.json
        simulation_id = data.get('simulation_id')
        
        simulation = Simulation.query.get_or_404(simulation_id)
        
        # Initialize quantum predictor engine
        predictor = QuantumMultiversePredictor(num_timelines=simulation.num_timelines)
        
        # Generate market data for simulation
        market_data = {
            'price': float(data.get('price', 100.0)),
            'volume': float(data.get('volume', 1000.0)),
            'sentiment': float(data.get('sentiment', 0.5))
        }
        
        # Run multiverse prediction
        prediction_results = predictor.simulate_multiverse(market_data)
        
        # Store prediction in database
        new_prediction = Prediction(
            simulation_id=simulation_id,
            probability_landscape=prediction_results['probability_landscape'],
            optimal_strategy=prediction_results['optimal_strategy'],
            quantum_volatility=prediction_results['quantum_volatility'],
            dark_energy_consumption=np.random.uniform(0.1, 10.0)  # Simulated value
        )
        
        db.session.add(new_prediction)
        
        # Store quantum states
        for i, state in enumerate(prediction_results.get('quantum_states', [])[:10]):
            new_state = QuantumState(
                simulation_id=simulation_id,
                timeline_id=f"timeline-{i}",
                state_vector=state,
                market_parameters=market_data,
                entanglement_degree=np.random.uniform(0, 1)
            )
            db.session.add(new_state)
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'prediction_id': new_prediction.id,
            'results': prediction_results
        })
        
    except Exception as e:
        logging.error(f"Error running prediction: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/manipulate_order_book', methods=['POST'])
def manipulate_order_book():
    try:
        data = request.json
        simulation_id = data.get('simulation_id')
        symbol = data.get('symbol', 'DET/USD')
        
        # Initialize nanobots
        nanobots = PlasmaNanobotSwarm("Quantum Market")
        
        # Run order book manipulation
        results = nanobots.reshape_order_book(symbol)
        
        # Store results in database
        manipulation = OrderBookManipulation(
            simulation_id=simulation_id,
            symbol=symbol,
            quark_states=results['quark_states'],
            distorted_geometry=results['distorted_geometry'],
            energy_output=results['energy_output']
        )
        
        db.session.add(manipulation)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'manipulation_id': manipulation.id,
            'results': results
        })
        
    except Exception as e:
        logging.error(f"Error manipulating order book: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/generate_dark_energy', methods=['POST'])
def generate_dark_energy():
    try:
        data = request.json
        address = data.get('address', '0x0000000000000000000000000000000000000000')
        amount = float(data.get('amount', 1.0))
        
        # Simulate dark energy token
        token_data = simulate_dark_energy_token(address, amount)
        
        # Store token data in database
        token = DarkEnergyToken(
            address=address,
            balance=token_data['balance'],
            fluctuation_rate=token_data['vacuum_state']['fluctuation_rate'],
            casimir_effect=token_data['vacuum_state']['casimir_effect'],
            hawking_radiation=token_data['vacuum_state']['hawking_radiation']
        )
        
        db.session.add(token)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'token_id': token.id,
            'token_data': token_data
        })
        
    except Exception as e:
        logging.error(f"Error generating dark energy: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/quantum_metrics', methods=['GET'])
def quantum_metrics():
    try:
        # Get recent simulations and predictions for metrics
        simulations = Simulation.query.order_by(Simulation.created_at.desc()).limit(5).all()
        predictions = Prediction.query.order_by(Prediction.timestamp.desc()).limit(10).all()
        
        # Prepare data for visualizations
        timeline_data = []
        volatility_data = []
        energy_data = []
        
        for prediction in predictions:
            volatility_data.append({
                'timestamp': prediction.timestamp.isoformat(),
                'value': prediction.quantum_volatility
            })
            
            energy_data.append({
                'timestamp': prediction.timestamp.isoformat(),
                'value': prediction.dark_energy_consumption
            })
            
            # Extract probability landscape for timeline data
            if isinstance(prediction.probability_landscape, dict):
                for timeline, prob in prediction.probability_landscape.items():
                    timeline_data.append({
                        'timeline': timeline,
                        'probability': prob
                    })
        
        return jsonify({
            'status': 'success',
            'timeline_data': timeline_data[:50],  # Limit to 50 data points for visualization
            'volatility_data': volatility_data,
            'energy_data': energy_data
        })
        
    except Exception as e:
        logging.error(f"Error retrieving quantum metrics: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
