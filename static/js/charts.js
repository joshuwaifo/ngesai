// SGEIB - Charts JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Function to create a line chart
    function createLineChart(canvasId, labels, data, label, borderColor, backgroundColor) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return;
        
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: data,
                    borderColor: borderColor,
                    backgroundColor: backgroundColor,
                    tension: 0.1,
                    borderWidth: 2,
                    pointRadius: 3,
                    pointBackgroundColor: borderColor,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.7)',
                        titleColor: '#fff',
                        bodyColor: '#fff',
                        bodySpacing: 5,
                        padding: 10,
                        boxWidth: 10,
                        usePointStyle: true,
                        callbacks: {
                            label: function(context) {
                                return `${context.dataset.label}: ${context.parsed.y}`;
                            }
                        }
                    }
                }
            }
        });
    }

    // Function to create a bar chart
    function createBarChart(canvasId, labels, data, label, backgroundColor) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return;
        
        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: data,
                    backgroundColor: backgroundColor,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                }
            }
        });
    }

    // Function to create a doughnut chart
    function createDoughnutChart(canvasId, labels, data, backgroundColors) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return;
        
        return new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: backgroundColors,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                }
            }
        });
    }

    // Function to create a radar chart
    function createRadarChart(canvasId, labels, datasets) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return;
        
        return new Chart(ctx, {
            type: 'radar',
            data: {
                labels: labels,
                datasets: datasets
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        pointLabels: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        },
                        ticks: {
                            backdropColor: 'transparent',
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                }
            }
        });
    }

    // Function to create a horizontal bar chart for trend confidence
    function createTrendConfidenceChart(canvasId, labels, data, colors) {
        const ctx = document.getElementById(canvasId);
        if (!ctx) return;
        
        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    axis: 'y',
                    label: 'Confidence Score (%)',
                    data: data,
                    backgroundColor: colors,
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true,
                        max: 100,
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },
                    y: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `Confidence: ${context.parsed.x}%`;
                            }
                        }
                    }
                }
            }
        });
    }

    // Dashboard charts
    const revenueTrendChart = document.getElementById('revenueTrendChart');
    if (revenueTrendChart) {
        createLineChart(
            'revenueTrendChart',
            ['2018', '2019', '2020', '2021', '2022', '2023'],
            [152, 189, 245, 350, 480, 650],
            'Gaming Revenue (Million SAR)',
            'rgba(75, 192, 192, 1)',
            'rgba(75, 192, 192, 0.2)'
        );
    }

    const userDemographicsChart = document.getElementById('userDemographicsChart');
    if (userDemographicsChart) {
        createDoughnutChart(
            'userDemographicsChart',
            ['13-17', '18-24', '25-34', '35-44', '45+'],
            [15, 35, 30, 15, 5],
            [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)',
                'rgba(153, 102, 255, 0.7)'
            ]
        );
    }

    const gamePreferencesChart = document.getElementById('gamePreferencesChart');
    if (gamePreferencesChart) {
        createBarChart(
            'gamePreferencesChart',
            ['Mobile', 'Console', 'PC', 'VR/AR'],
            [65, 40, 35, 10],
            'Gaming Platform Preference (%)',
            [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)'
            ]
        );
    }

    // Trend Forecaster chart
    const trendConfidenceChart = document.getElementById('trendConfidenceChart');
    if (trendConfidenceChart) {
        // Trend data should be loaded from the server
        // This is a fallback in case it's not available
        const trends = window.trendData || [
            {name: 'Mobile Esports Growth', confidence: 87},
            {name: 'Local Content Development', confidence: 78},
            {name: 'Educational Gaming', confidence: 72},
            {name: 'Cloud Gaming Adoption', confidence: 65},
            {name: 'Female Gamer Growth', confidence: 80}
        ];
        
        const labels = trends.map(trend => trend.name);
        const data = trends.map(trend => trend.confidence);
        const colors = [
            'rgba(255, 99, 132, 0.7)',
            'rgba(54, 162, 235, 0.7)',
            'rgba(255, 206, 86, 0.7)',
            'rgba(75, 192, 192, 0.7)',
            'rgba(153, 102, 255, 0.7)'
        ];
        
        createTrendConfidenceChart('trendConfidenceChart', labels, data, colors);
    }

    // Market Analysis chart
    const marketSegmentationChart = document.getElementById('marketSegmentationChart');
    if (marketSegmentationChart) {
        createDoughnutChart(
            'marketSegmentationChart',
            ['Mobile Gaming', 'Console Gaming', 'PC Gaming', 'Esports', 'Game Development'],
            [45, 20, 15, 12, 8],
            [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)',
                'rgba(153, 102, 255, 0.7)'
            ]
        );
    }

    // Function to fetch market data from API and update chart
    window.fetchMarketDataAndUpdateChart = function(category, chartId, label, color) {
        fetch(`/api/market-data/${category}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    const labels = data.map(item => item.date);
                    const values = data.map(item => item.value);
                    
                    createLineChart(
                        chartId,
                        labels,
                        values,
                        label,
                        color,
                        color.replace('1)', '0.2)')
                    );
                } else {
                    document.getElementById(chartId).parentElement.innerHTML = 
                        '<div class="alert alert-info">No data available for this category</div>';
                }
            })
            .catch(error => {
                console.error('Error fetching market data:', error);
                document.getElementById(chartId).parentElement.innerHTML = 
                    '<div class="alert alert-danger">Error loading data</div>';
            });
    };

    // Attach event handlers to market data category selectors
    const marketDataCategorySelect = document.getElementById('marketDataCategorySelect');
    if (marketDataCategorySelect) {
        marketDataCategorySelect.addEventListener('change', function() {
            const category = this.value;
            const chartColors = {
                'revenue': 'rgba(75, 192, 192, 1)',
                'users': 'rgba(54, 162, 235, 1)',
                'demographics': 'rgba(153, 102, 255, 1)',
                'game_preferences': 'rgba(255, 159, 64, 1)'
            };
            
            const chartLabels = {
                'revenue': 'Gaming Revenue (Million SAR)',
                'users': 'Active Users (Millions)',
                'demographics': 'Age Demographics (%)',
                'game_preferences': 'Game Genre Preference (%)'
            };
            
            fetchMarketDataAndUpdateChart(
                category, 
                'marketDataChart', 
                chartLabels[category] || 'Market Data',
                chartColors[category] || 'rgba(75, 192, 192, 1)'
            );
        });
        
        // Trigger the change event to load initial data
        if (marketDataCategorySelect.value) {
            marketDataCategorySelect.dispatchEvent(new Event('change'));
        }
    }
});
