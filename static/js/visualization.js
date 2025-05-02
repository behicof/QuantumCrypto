document.addEventListener('DOMContentLoaded', function() {
    // Initialize any 3D visualizations
    initializeQuantumVisualizations();
});

function initializeQuantumVisualizations() {
    // If we're on the simulation page, set up the 3D visualizations
    if (document.getElementById('quantum-state-visualization')) {
        setupQuantumStateVisualization();
    }
    
    if (document.getElementById('market-geometry-visualization')) {
        setupMarketGeometryVisualization();
    }
}

function setupQuantumStateVisualization() {
    const container = document.getElementById('quantum-state-visualization');
    if (!container) return;
    
    // Get the quantum states from the data attribute if available
    const quantumStatesElement = document.getElementById('quantum-states-data');
    let quantumStates = [];
    
    if (quantumStatesElement) {
        try {
            quantumStates = JSON.parse(quantumStatesElement.getAttribute('data-states'));
        } catch (e) {
            console.error('Error parsing quantum states:', e);
            // Use sample data as fallback
            quantumStates = generateSampleQuantumStates();
        }
    } else {
        // Use sample data if no real data is available
        quantumStates = generateSampleQuantumStates();
    }
    
    // Set up Plotly.js 3D visualization
    const data = [{
        type: 'scatter3d',
        mode: 'markers',
        x: quantumStates.map(state => state.x),
        y: quantumStates.map(state => state.y),
        z: quantumStates.map(state => state.z),
        marker: {
            size: quantumStates.map(state => state.probability * 20),
            color: quantumStates.map(state => state.probability),
            colorscale: 'Viridis',
            opacity: 0.8
        },
        text: quantumStates.map(state => `State: ${state.state}<br>Probability: ${state.probability.toFixed(4)}`),
        hoverinfo: 'text'
    }];
    
    const layout = {
        title: 'Quantum State Visualization',
        margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 30
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        scene: {
            xaxis: { title: 'X Dimension' },
            yaxis: { title: 'Y Dimension' },
            zaxis: { title: 'Z Dimension' },
            camera: {
                eye: { x: 1.5, y: 1.5, z: 1.5 }
            }
        }
    };
    
    const config = {
        responsive: true
    };
    
    Plotly.newPlot(container, data, layout, config);
    
    // Add animation to rotate the visualization
    let angle = 0;
    setInterval(() => {
        angle += 0.01;
        const newCamera = {
            eye: {
                x: 1.5 * Math.cos(angle),
                y: 1.5 * Math.sin(angle),
                z: 1.5
            }
        };
        Plotly.relayout(container, { 'scene.camera': newCamera });
    }, 100);
}

function setupMarketGeometryVisualization() {
    const container = document.getElementById('market-geometry-visualization');
    if (!container) return;
    
    // Get geometry data if available
    const geometryElement = document.getElementById('geometry-data');
    let geometryData = null;
    
    if (geometryElement) {
        try {
            geometryData = JSON.parse(geometryElement.getAttribute('data-geometry'));
        } catch (e) {
            console.error('Error parsing geometry data:', e);
            geometryData = null;
        }
    }
    
    // Generate grid data for the curved space visualization
    const gridSize = 20;
    const x = [];
    const y = [];
    const z = [];
    
    // Apply distortion from geometry data if available
    const curvature = geometryData ? geometryData.curvature : 0.5;
    const torsion = geometryData ? geometryData.torsion_field : 0.3;
    
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            const xi = (i - gridSize/2) / (gridSize/4);
            const yi = (j - gridSize/2) / (gridSize/4);
            
            // Calculate z with distortion based on market geometry
            const zi = Math.sin(xi * curvature) * Math.cos(yi * torsion) * Math.exp(-(xi*xi + yi*yi)/8);
            
            x.push(xi);
            y.push(yi);
            z.push(zi);
        }
    }
    
    // Create the surface plot
    const data = [{
        type: 'mesh3d',
        x: x,
        y: y,
        z: z,
        intensity: z,
        colorscale: 'Viridis',
        opacity: 0.8
    }];
    
    const layout = {
        title: 'Market Geometry Visualization',
        margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 30
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        scene: {
            xaxis: { title: 'Price' },
            yaxis: { title: 'Volume' },
            zaxis: { title: 'Curvature' }
        }
    };
    
    const config = {
        responsive: true
    };
    
    Plotly.newPlot(container, data, layout, config);
}

function generateSampleQuantumStates() {
    // Generate sample data for visualization when no real data is available
    const numStates = 50;
    const states = [];
    
    for (let i = 0; i < numStates; i++) {
        // Convert to binary string for state representation
        const state = i.toString(2).padStart(4, '0');
        
        // Generate probability (higher for certain states to show patterns)
        let probability = Math.random();
        if (state.split('1').length > 2) {
            // Increase probability for states with more 1s
            probability *= 2;
        }
        if (probability > 1) probability = 1;
        
        // Map to 3D coordinates
        // Use binary state bits to influence position
        const x = (parseInt(state[0]) * 2 - 1) + (Math.random() - 0.5) * 0.5;
        const y = (parseInt(state[1]) * 2 - 1) + (Math.random() - 0.5) * 0.5;
        const z = (parseInt(state[2] + state[3], 2) / 3) + (Math.random() - 0.5) * 0.5;
        
        states.push({
            state: state,
            probability: probability,
            x: x,
            y: y,
            z: z
        });
    }
    
    return states;
}
