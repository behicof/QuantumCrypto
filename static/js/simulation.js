document.addEventListener('DOMContentLoaded', function() {
    // Initialize simulation page functionality
    initializeSimulationPage();
    
    // Set up event listeners for the simulation controls
    setupSimulationControls();
});

function initializeSimulationPage() {
    // Get simulation ID from page data
    const simulationElement = document.getElementById('simulation-data');
    if (!simulationElement) return;
    
    const simulationId = simulationElement.getAttribute('data-simulation-id');
    if (!simulationId) return;
    
    // Update simulation info displays
    updateSimulationInfo(simulationId);
}

function setupSimulationControls() {
    // Run prediction button
    const runPredictionBtn = document.getElementById('run-prediction-btn');
    if (runPredictionBtn) {
        runPredictionBtn.addEventListener('click', handleRunPrediction);
    }
    
    // Manipulate order book button
    const manipulateOrderBookBtn = document.getElementById('manipulate-order-book-btn');
    if (manipulateOrderBookBtn) {
        manipulateOrderBookBtn.addEventListener('click', handleManipulateOrderBook);
    }
    
    // Generate dark energy button
    const generateDarkEnergyBtn = document.getElementById('generate-dark-energy-btn');
    if (generateDarkEnergyBtn) {
        generateDarkEnergyBtn.addEventListener('click', handleGenerateDarkEnergy);
    }
}

function handleRunPrediction() {
    const simulationElement = document.getElementById('simulation-data');
    if (!simulationElement) return;
    
    const simulationId = simulationElement.getAttribute('data-simulation-id');
    if (!simulationId) {
        showAlert('Simulation ID not found', 'danger');
        return;
    }
    
    // Get market data from form
    const price = parseFloat(document.getElementById('market-price').value) || 100.0;
    const volume = parseFloat(document.getElementById('market-volume').value) || 1000.0;
    const sentiment = parseFloat(document.getElementById('market-sentiment').value) || 0.5;
    
    // Show loading indicator
    const predictionResults = document.getElementById('prediction-results');
    if (predictionResults) {
        predictionResults.innerHTML = '<div class="d-flex justify-content-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>';
    }
    
    // Call API to run prediction
    fetch('/api/run_prediction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            simulation_id: simulationId,
            price: price,
            volume: volume,
            sentiment: sentiment
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Display prediction results
            displayPredictionResults(data.results);
            
            // Show success message
            showAlert('Quantum prediction completed successfully!', 'success');
            
            // Refresh visualizations
            if (typeof setupQuantumStateVisualization === 'function') {
                setupQuantumStateVisualization();
            }
        } else {
            showAlert('Error: ' + data.message, 'danger');
            
            if (predictionResults) {
                predictionResults.innerHTML = '<div class="alert alert-danger">Failed to run quantum prediction</div>';
            }
        }
    })
    .catch(error => {
        console.error('Error running prediction:', error);
        showAlert('Error running quantum prediction. Please try again.', 'danger');
        
        if (predictionResults) {
            predictionResults.innerHTML = '<div class="alert alert-danger">Failed to run quantum prediction</div>';
        }
    });
}

function handleManipulateOrderBook() {
    const simulationElement = document.getElementById('simulation-data');
    if (!simulationElement) return;
    
    const simulationId = simulationElement.getAttribute('data-simulation-id');
    if (!simulationId) {
        showAlert('Simulation ID not found', 'danger');
        return;
    }
    
    // Get symbol from form
    const symbol = document.getElementById('market-symbol').value || 'DET/USD';
    
    // Show loading indicator
    const manipulationResults = document.getElementById('manipulation-results');
    if (manipulationResults) {
        manipulationResults.innerHTML = '<div class="d-flex justify-content-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>';
    }
    
    // Call API to manipulate order book
    fetch('/api/manipulate_order_book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            simulation_id: simulationId,
            symbol: symbol
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Display manipulation results
            displayManipulationResults(data.results);
            
            // Show success message
            showAlert('Order book successfully manipulated with quantum plasma nanobots!', 'success');
            
            // Refresh market geometry visualization if available
            if (typeof setupMarketGeometryVisualization === 'function') {
                setupMarketGeometryVisualization();
            }
        } else {
            showAlert('Error: ' + data.message, 'danger');
            
            if (manipulationResults) {
                manipulationResults.innerHTML = '<div class="alert alert-danger">Failed to manipulate order book</div>';
            }
        }
    })
    .catch(error => {
        console.error('Error manipulating order book:', error);
        showAlert('Error manipulating order book. Please try again.', 'danger');
        
        if (manipulationResults) {
            manipulationResults.innerHTML = '<div class="alert alert-danger">Failed to manipulate order book</div>';
        }
    });
}

function handleGenerateDarkEnergy() {
    const simulationElement = document.getElementById('simulation-data');
    if (!simulationElement) return;
    
    // Get address and amount from form
    const address = document.getElementById('wallet-address').value || '0x0000000000000000000000000000000000000000';
    const amount = parseFloat(document.getElementById('token-amount').value) || 1.0;
    
    // Show loading indicator
    const darkEnergyResults = document.getElementById('dark-energy-results');
    if (darkEnergyResults) {
        darkEnergyResults.innerHTML = '<div class="d-flex justify-content-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>';
    }
    
    // Call API to generate dark energy tokens
    fetch('/api/generate_dark_energy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            address: address,
            amount: amount
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Display dark energy token results
            displayDarkEnergyResults(data.token_data);
            
            // Show success message
            showAlert('Dark Energy Tokens generated successfully!', 'success');
        } else {
            showAlert('Error: ' + data.message, 'danger');
            
            if (darkEnergyResults) {
                darkEnergyResults.innerHTML = '<div class="alert alert-danger">Failed to generate Dark Energy Tokens</div>';
            }
        }
    })
    .catch(error => {
        console.error('Error generating dark energy:', error);
        showAlert('Error generating Dark Energy Tokens. Please try again.', 'danger');
        
        if (darkEnergyResults) {
            darkEnergyResults.innerHTML = '<div class="alert alert-danger">Failed to generate Dark Energy Tokens</div>';
        }
    });
}

function displayPredictionResults(results) {
    const predictionResults = document.getElementById('prediction-results');
    if (!predictionResults) return;
    
    // Format probability landscape
    let probHtml = '<h5>Probability Landscape</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    probHtml += '<thead><tr><th>Timeline</th><th>Probability</th></tr></thead><tbody>';
    
    let count = 0;
    if (results.probability_landscape) {
        for (const [timeline, probability] of Object.entries(results.probability_landscape)) {
            probHtml += `<tr><td>${timeline}</td><td>${probability.toFixed(4)}</td></tr>`;
            count++;
            if (count >= 10) break; // Limit to 10 entries
        }
    }
    
    probHtml += '</tbody></table></div>';
    
    // Format optimal strategy
    let strategyHtml = '<h5>Optimal Strategy</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    strategyHtml += '<thead><tr><th>Asset</th><th>Weight</th></tr></thead><tbody>';
    
    if (results.optimal_strategy) {
        for (let i = 0; i < results.optimal_strategy.length; i++) {
            strategyHtml += `<tr><td>Asset ${i+1}</td><td>${results.optimal_strategy[i].toFixed(4)}</td></tr>`;
        }
    }
    
    strategyHtml += '</tbody></table></div>';
    
    // Format volatility
    const volatilityHtml = `
        <h5>Quantum Metrics</h5>
        <div class="quantum-metric-card">
            <div class="card bg-dark text-light mb-3">
                <div class="card-body">
                    <h6 class="card-title">Quantum Volatility</h6>
                    <p class="card-text display-6">${results.quantum_volatility ? results.quantum_volatility.toFixed(4) : 'N/A'} Ψ</p>
                </div>
            </div>
        </div>
    `;
    
    // Combine all results
    predictionResults.innerHTML = `
        <div class="row">
            <div class="col-md-6">
                ${probHtml}
            </div>
            <div class="col-md-6">
                ${strategyHtml}
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-6">
                ${volatilityHtml}
            </div>
        </div>
    `;
}

function displayManipulationResults(results) {
    const manipulationResults = document.getElementById('manipulation-results');
    if (!manipulationResults) return;
    
    // Format quark states
    let quarkHtml = '<h5>Quark States</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    quarkHtml += '<thead><tr><th>Property</th><th>Value</th></tr></thead><tbody>';
    
    if (results.quark_states) {
        quarkHtml += `<tr><td>Gluon Pressure</td><td>${results.quark_states.gluon_pressure.toFixed(4)}</td></tr>`;
        quarkHtml += `<tr><td>Color Confinement</td><td>${results.quark_states.color_confinement.toFixed(4)}</td></tr>`;
        quarkHtml += `<tr><td>Asymptotic Freedom</td><td>${results.quark_states.asymptotic_freedom.toFixed(4)}</td></tr>`;
    }
    
    quarkHtml += '</tbody></table></div>';
    
    // Format geometry metrics
    let geometryHtml = '<h5>Distorted Geometry</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    geometryHtml += '<thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>';
    
    if (results.distorted_geometry) {
        geometryHtml += `<tr><td>Ricci Scalar</td><td>${results.distorted_geometry.ricci_scalar.toFixed(4)}</td></tr>`;
        geometryHtml += `<tr><td>Curvature</td><td>${results.distorted_geometry.curvature.toFixed(4)}</td></tr>`;
        geometryHtml += `<tr><td>Torsion Field</td><td>${results.distorted_geometry.torsion_field.toFixed(4)}</td></tr>`;
    }
    
    geometryHtml += '</tbody></table></div>';
    
    // Format energy output
    const energyHtml = `
        <h5>Manipulation Results</h5>
        <div class="quantum-metric-card">
            <div class="card bg-dark text-light mb-3">
                <div class="card-body">
                    <h6 class="card-title">Energy Output</h6>
                    <p class="card-text display-6">${results.energy_output ? results.energy_output.toExponential(4) : 'N/A'} GeV/fm³</p>
                </div>
            </div>
            <div class="card bg-dark text-light mb-3">
                <div class="card-body">
                    <h6 class="card-title">Manipulation Efficiency</h6>
                    <p class="card-text display-6">${results.manipulation_efficiency ? (results.manipulation_efficiency * 100).toFixed(2) : 'N/A'}%</p>
                </div>
            </div>
        </div>
    `;
    
    // Combine all results
    manipulationResults.innerHTML = `
        <div class="row">
            <div class="col-md-6">
                ${quarkHtml}
            </div>
            <div class="col-md-6">
                ${geometryHtml}
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-12">
                ${energyHtml}
            </div>
        </div>
    `;
}

function displayDarkEnergyResults(tokenData) {
    const darkEnergyResults = document.getElementById('dark-energy-results');
    if (!darkEnergyResults) return;
    
    // Format token info
    let tokenHtml = '<h5>Token Information</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    tokenHtml += '<thead><tr><th>Property</th><th>Value</th></tr></thead><tbody>';
    
    if (tokenData) {
        tokenHtml += `<tr><td>Address</td><td>${tokenData.address}</td></tr>`;
        tokenHtml += `<tr><td>Balance</td><td>${tokenData.balance} DET</td></tr>`;
        tokenHtml += `<tr><td>Energy Available</td><td>${tokenData.energy_available ? 'Yes' : 'No'}</td></tr>`;
    }
    
    tokenHtml += '</tbody></table></div>';
    
    // Format vacuum state parameters
    let vacuumHtml = '<h5>Quantum Vacuum State</h5><div class="table-responsive"><table class="table table-sm table-dark">';
    vacuumHtml += '<thead><tr><th>Parameter</th><th>Value</th></tr></thead><tbody>';
    
    if (tokenData && tokenData.vacuum_state) {
        vacuumHtml += `<tr><td>Fluctuation Rate</td><td>${tokenData.vacuum_state.fluctuation_rate.toExponential(4)}</td></tr>`;
        vacuumHtml += `<tr><td>Casimir Effect</td><td>${tokenData.vacuum_state.casimir_effect.toExponential(4)}</td></tr>`;
        vacuumHtml += `<tr><td>Hawking Radiation</td><td>${tokenData.vacuum_state.hawking_radiation.toExponential(4)}</td></tr>`;
    }
    
    vacuumHtml += '</tbody></table></div>';
    
    // Format energy metrics
    const energyHtml = `
        <h5>Vacuum Energy</h5>
        <div class="quantum-metric-card">
            <div class="card bg-dark text-light mb-3">
                <div class="card-body">
                    <h6 class="card-title">Total Vacuum Energy</h6>
                    <p class="card-text display-6">${tokenData.vacuum_energy ? tokenData.vacuum_energy.toExponential(4) : 'N/A'} GeV/fm³</p>
                </div>
            </div>
        </div>
    `;
    
    // Combine all results
    darkEnergyResults.innerHTML = `
        <div class="row">
            <div class="col-md-6">
                ${tokenHtml}
            </div>
            <div class="col-md-6">
                ${vacuumHtml}
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-12">
                ${energyHtml}
            </div>
        </div>
    `;
}

function updateSimulationInfo(simulationId) {
    // This would normally fetch the latest simulation data from the server
    // For now, we'll just update the UI based on existing data
    
    // Update simulation status indicators if they exist
    updateStatusIndicators();
}

function updateStatusIndicators() {
    // Update timeline count
    const timelineIndicator = document.getElementById('timeline-count');
    if (timelineIndicator) {
        const simulationElement = document.getElementById('simulation-data');
        if (simulationElement) {
            const numTimelines = simulationElement.getAttribute('data-timelines');
            if (numTimelines) {
                timelineIndicator.textContent = numTimelines;
            }
        }
    }
}

function showAlert(message, type) {
    const alertsContainer = document.getElementById('alerts-container');
    if (!alertsContainer) return;
    
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    alertsContainer.appendChild(alertDiv);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => alertDiv.remove(), 150);
    }, 5000);
}
