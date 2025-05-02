document.addEventListener('DOMContentLoaded', function() {
    // Initialize dashboard components
    initializeDashboard();
    
    // Set up event listeners for interactive elements
    setupEventListeners();
});

function initializeDashboard() {
    // Fetch quantum metrics for dashboard visualizations
    fetchQuantumMetrics();
    
    // Initialize any dashboard widgets
    initializeWidgets();
}

function setupEventListeners() {
    // Create simulation button
    const createSimButton = document.getElementById('create-simulation-btn');
    if (createSimButton) {
        createSimButton.addEventListener('click', showCreateSimulationModal);
    }
    
    // Form submission for creating simulations
    const simForm = document.getElementById('simulation-form');
    if (simForm) {
        simForm.addEventListener('submit', handleSimulationFormSubmit);
    }
}

function showCreateSimulationModal() {
    const modal = new bootstrap.Modal(document.getElementById('create-simulation-modal'));
    modal.show();
}

function handleSimulationFormSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const formData = {
        name: document.getElementById('simulation-name').value,
        description: document.getElementById('simulation-description').value,
        num_timelines: parseInt(document.getElementById('simulation-timelines').value) || 1024
    };
    
    // Create simulation
    createSimulation(formData);
}

function createSimulation(data) {
    fetch('/api/create_simulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Hide modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('create-simulation-modal'));
            modal.hide();
            
            // Show success message
            showAlert('Simulation created successfully!', 'success');
            
            // Reload page after short delay
            setTimeout(() => {
                window.location.reload();
            }, 1500);
        } else {
            showAlert('Error: ' + data.message, 'danger');
        }
    })
    .catch(error => {
        console.error('Error creating simulation:', error);
        showAlert('Error creating simulation. Please try again.', 'danger');
    });
}

function fetchQuantumMetrics() {
    fetch('/api/quantum_metrics')
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Render timeline visualization
            renderTimelineVisualization(data.timeline_data);
            
            // Render volatility chart
            renderVolatilityChart(data.volatility_data);
            
            // Render energy consumption chart
            renderEnergyChart(data.energy_data);
        } else {
            console.error('Error fetching quantum metrics:', data.message);
        }
    })
    .catch(error => {
        console.error('Error fetching quantum metrics:', error);
    });
}

function renderTimelineVisualization(timelineData) {
    const container = document.getElementById('timeline-visualization');
    if (!container || !timelineData || timelineData.length === 0) return;
    
    // Clear previous content
    container.innerHTML = '';
    
    // Set up D3 visualization
    const margin = {top: 20, right: 30, bottom: 40, left: 50};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;
    
    const svg = d3.select(container)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
    
    // X scale for timelines
    const x = d3.scaleBand()
        .domain(timelineData.map(d => d.timeline))
        .range([0, width])
        .padding(0.1);
    
    // Y scale for probabilities
    const y = d3.scaleLinear()
        .domain([0, d3.max(timelineData, d => d.probability)])
        .nice()
        .range([height, 0]);
    
    // Add X axis
    svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .selectAll('text')
        .attr('transform', 'rotate(-45)')
        .style('text-anchor', 'end');
    
    // Add Y axis
    svg.append('g')
        .call(d3.axisLeft(y));
    
    // Add a title
    svg.append('text')
        .attr('x', width / 2)
        .attr('y', 0)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .text('Timeline Probability Distribution');
    
    // Add bars
    svg.selectAll('.bar')
        .data(timelineData)
        .enter()
        .append('rect')
        .attr('class', 'bar')
        .attr('x', d => x(d.timeline))
        .attr('y', d => y(d.probability))
        .attr('width', x.bandwidth())
        .attr('height', d => height - y(d.probability))
        .attr('fill', '#8a2be2') // Blueviolet color for quantum theme
        .on('mouseover', function(event, d) {
            d3.select(this).attr('fill', '#b768ff');
            
            // Show tooltip
            const tooltip = d3.select('body').append('div')
                .attr('class', 'tooltip')
                .style('position', 'absolute')
                .style('background-color', 'rgba(0, 0, 0, 0.7)')
                .style('color', 'white')
                .style('padding', '5px')
                .style('border-radius', '5px')
                .style('pointer-events', 'none')
                .style('opacity', 0);
            
            tooltip.transition()
                .duration(200)
                .style('opacity', 0.9);
            
            tooltip.html(`Timeline: ${d.timeline}<br>Probability: ${d.probability.toFixed(4)}`)
                .style('left', (event.pageX + 10) + 'px')
                .style('top', (event.pageY - 28) + 'px');
        })
        .on('mouseout', function() {
            d3.select(this).attr('fill', '#8a2be2');
            d3.select('.tooltip').remove();
        });
}

function renderVolatilityChart(volatilityData) {
    const container = document.getElementById('volatility-chart');
    if (!container || !volatilityData || volatilityData.length === 0) return;
    
    // Parse timestamps
    const data = volatilityData.map(d => ({
        timestamp: new Date(d.timestamp),
        value: d.value
    }));
    
    // Clear previous content
    container.innerHTML = '';
    
    // Set up chart dimensions
    const margin = {top: 20, right: 30, bottom: 50, left: 50};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 250 - margin.top - margin.bottom;
    
    const svg = d3.select(container)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
    
    // X scale for time
    const x = d3.scaleTime()
        .domain(d3.extent(data, d => d.timestamp))
        .range([0, width]);
    
    // Y scale for volatility
    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.value)])
        .nice()
        .range([height, 0]);
    
    // Define line generator
    const line = d3.line()
        .x(d => x(d.timestamp))
        .y(d => y(d.value))
        .curve(d3.curveMonotoneX);
    
    // Add X axis
    svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .selectAll('text')
        .attr('transform', 'rotate(-45)')
        .style('text-anchor', 'end');
    
    // Add Y axis
    svg.append('g')
        .call(d3.axisLeft(y));
    
    // Add title
    svg.append('text')
        .attr('x', width / 2)
        .attr('y', 0)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .text('Quantum Volatility');
    
    // Add path
    svg.append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', '#6a0dad') // Purple color
        .attr('stroke-width', 2)
        .attr('d', line);
    
    // Add dots
    svg.selectAll('.dot')
        .data(data)
        .enter()
        .append('circle')
        .attr('class', 'dot')
        .attr('cx', d => x(d.timestamp))
        .attr('cy', d => y(d.value))
        .attr('r', 4)
        .attr('fill', '#6a0dad');
}

function renderEnergyChart(energyData) {
    const container = document.getElementById('energy-chart');
    if (!container || !energyData || energyData.length === 0) return;
    
    // Parse timestamps
    const data = energyData.map(d => ({
        timestamp: new Date(d.timestamp),
        value: d.value
    }));
    
    // Clear previous content
    container.innerHTML = '';
    
    // Set up chart dimensions
    const margin = {top: 20, right: 30, bottom: 50, left: 50};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 250 - margin.top - margin.bottom;
    
    const svg = d3.select(container)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
    
    // X scale for time
    const x = d3.scaleTime()
        .domain(d3.extent(data, d => d.timestamp))
        .range([0, width]);
    
    // Y scale for energy
    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.value)])
        .nice()
        .range([height, 0]);
    
    // Add X axis
    svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .selectAll('text')
        .attr('transform', 'rotate(-45)')
        .style('text-anchor', 'end');
    
    // Add Y axis
    svg.append('g')
        .call(d3.axisLeft(y));
    
    // Add title
    svg.append('text')
        .attr('x', width / 2)
        .attr('y', 0)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .text('Dark Energy Consumption');
    
    // Create area generator
    const area = d3.area()
        .x(d => x(d.timestamp))
        .y0(height)
        .y1(d => y(d.value))
        .curve(d3.curveMonotoneX);
    
    // Add area
    svg.append('path')
        .datum(data)
        .attr('fill', 'rgba(138, 43, 226, 0.3)') // Blueviolet with opacity
        .attr('stroke', '#8a2be2')
        .attr('stroke-width', 1.5)
        .attr('d', area);
}

function initializeWidgets() {
    // Initialize any additional dashboard widgets
    // This could be additional charts, status indicators, etc.
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
