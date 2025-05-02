from flask import render_template, request, jsonify, redirect, url_for, flash, session
from app import app, db
from models import Simulation, Prediction, QuantumState, OrderBookManipulation, DarkEnergyToken
from quantum_engine.predictor import QuantumMultiversePredictor
from quantum_engine.nanobots import PlasmaNanobotSwarm
from quantum_engine.economics import simulate_dark_energy_token
from quantum_engine.holographic import HolographicMarketEngine, MultiverseEconomyGenerator, simulate_multiverse_collapse
from quantum_engine.wallet import QuantumWalletTransporter, QuantumAsset, ChronoProtection
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


@app.route('/api/holographic_prediction', methods=['POST'])
def holographic_prediction():
    """
    مسیر API برای پیش‌بینی بازار با استفاده از موتور بازار هولوگرافیک
    این API پیشرفته‌ترین روش پیش‌بینی بازار با استفاده از اصل هولوگرافیک را فراهم می‌کند.
    """
    try:
        data = request.json
        simulation_id = data.get('simulation_id')
        
        simulation = Simulation.query.get_or_404(simulation_id)
        
        # اطلاعات بازار را از درخواست استخراج می‌کنیم
        market_data = {
            'price': float(data.get('price', 100.0)),
            'volume': float(data.get('volume', 1000.0)),
            'sentiment': float(data.get('sentiment', 0.5))
        }
        
        # موتور بازار هولوگرافیک را آماده‌سازی می‌کنیم
        holographic_engine = HolographicMarketEngine(num_qubits=5)
        
        # پیش‌بینی هولوگرافیک را اجرا می‌کنیم
        prediction_results = holographic_engine.predict_market_hologram(market_data)
        
        # نتایج را در پایگاه داده ذخیره می‌کنیم
        new_prediction = Prediction(
            simulation_id=simulation_id,
            probability_landscape=prediction_results['probability_landscape'],
            optimal_strategy=prediction_results['optimal_strategy'],
            quantum_volatility=prediction_results['quantum_volatility'],
            dark_energy_consumption=np.random.uniform(0.1, 10.0)  # مقدار شبیه‌سازی شده
        )
        
        db.session.add(new_prediction)
        
        # حالت‌های کوانتومی را ذخیره می‌کنیم
        for i, state in enumerate(prediction_results.get('quantum_states', [])[:10]):
            new_state = QuantumState(
                simulation_id=simulation_id,
                timeline_id=f"holographic-{i}",
                state_vector=state,
                market_parameters=market_data,
                entanglement_degree=np.random.uniform(0.8, 1.0)  # درهم‌تنیدگی بالا در حالت هولوگرافیک
            )
            db.session.add(new_state)
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'prediction_id': new_prediction.id,
            'holographic_results': prediction_results,
            'message': 'Holographic prediction completed successfully'
        })
        
    except Exception as e:
        logging.error(f"Error in holographic prediction: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/multiverse_collapse', methods=['POST'])
def multiverse_collapse():
    """
    مسیر API برای شبیه‌سازی فروپاشی چندجهانی بازارها
    این API امکان شبیه‌سازی بحران‌های شدید بازار و رویدادهای فروپاشی را فراهم می‌کند.
    """
    try:
        data = request.json
        simulation_id = data.get('simulation_id')
        
        # بررسی وجود شبیه‌سازی
        simulation = Simulation.query.get_or_404(simulation_id)
        
        # اجرای شبیه‌سازی فروپاشی چندجهانی
        collapse_results = simulate_multiverse_collapse()
        
        # ایجاد یک پیش‌بینی مرتبط با فروپاشی
        collapse_prediction = Prediction(
            simulation_id=simulation_id,
            probability_landscape={"collapse": 1.0},
            optimal_strategy={
                "direction": "Quantum Collapse",
                "confidence": 0.99,
                "leverage": 0.1,  # اهرم پایین در هنگام فروپاشی
                "protection_measures": ["Multiverse Hedging", "Chronology Protection"]
            },
            quantum_volatility=9.9,  # نوسان بسیار بالا
            dark_energy_consumption=100.0  # مصرف بسیار بالای انرژی تاریک
        )
        
        db.session.add(collapse_prediction)
        
        # ذخیره برخی حالت‌های کوانتومی مرتبط با فروپاشی
        market_states = collapse_results.get('Market_States', [])
        for i, state in enumerate(market_states):
            new_state = QuantumState(
                simulation_id=simulation_id,
                timeline_id=f"collapse-{i}",
                state_vector={"collapse_state": state},
                market_parameters={"collapse": True},
                entanglement_degree=0.99  # درهم‌تنیدگی بسیار بالا در فروپاشی
            )
            db.session.add(new_state)
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'collapse_prediction_id': collapse_prediction.id,
            'collapse_results': collapse_results,
            'message': 'Multiverse collapse simulation completed successfully'
        })
        
    except Exception as e:
        logging.error(f"Error in multiverse collapse simulation: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/quantum_wallet_transfer', methods=['POST'])
def quantum_wallet_transfer():
    """
    مسیر API برای انتقال کوانتومی به کیف پول از طریق کرمچاله
    این API امکان انتقال لحظه‌ای دارایی‌ها بین کیف پول‌ها با استفاده از کرمچاله‌های کوانتومی را فراهم می‌کند.
    """
    try:
        data = request.json
        wallet_address = data.get('wallet_address', 'DARK-QW:0x8f3a...')
        amount = float(data.get('amount', 1000.0))
        asset_name = data.get('asset_name', 'Dark Energy Token')
        
        # ایجاد کیف پول کوانتومی
        wallet = QuantumWalletTransporter(wallet_address)
        
        # ایجاد دارایی کوانتومی
        asset = QuantumAsset(amount, asset_name)
        
        # انجام انتقال کوانتومی
        transfer_result = wallet.transfer(asset, amount)
        
        # ذخیره اطلاعات تراکنش در توکن انرژی تاریک
        token = DarkEnergyToken(
            address=wallet_address,
            balance=amount,
            fluctuation_rate=0.05,
            casimir_effect=0.01,
            hawking_radiation=0.001
        )
        
        db.session.add(token)
        db.session.commit()
        
        # بررسی حفظ علیت
        chrono_protection = ChronoProtection()
        transaction_hash = transfer_result['transaction_hash']
        is_valid = chrono_protection.verify_timeline(transaction_hash)
        
        # ایجاد امضای کوانتومی
        quantum_signature = chrono_protection.apply_quantum_signature(transaction_hash)
        
        # اضافه کردن اطلاعات اضافی به نتیجه
        transfer_result['quantum_signature'] = quantum_signature
        transfer_result['causality_preserved'] = is_valid
        transfer_result['token_id'] = token.id
        
        return jsonify({
            'status': 'success',
            'transfer_result': transfer_result,
            'message': 'Quantum wallet transfer completed successfully'
        })
        
    except Exception as e:
        logging.error(f"Error in quantum wallet transfer: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
