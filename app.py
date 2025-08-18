"""
Demo Application - Data Analysis Dashboard
Demonstrates a typical Python development workflow in GitHub Codespaces
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

class DataAnalyzer:
    """Sample data analysis class for demonstration"""
    
    def __init__(self):
        self.data = self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate sample development metrics data"""
        dates = pd.date_range(
            start=datetime.now() - timedelta(days=30),
            end=datetime.now(),
            freq='D'
        )
        
        data = {
            'date': dates,
            'commits': np.random.poisson(5, len(dates)),
            'pull_requests': np.random.poisson(2, len(dates)),
            'code_reviews': np.random.poisson(3, len(dates)),
            'active_developers': np.random.randint(10, 25, len(dates)),
            'codespace_hours': np.random.uniform(20, 100, len(dates))
        }
        
        return pd.DataFrame(data)
    
    def get_summary_stats(self):
        """Calculate summary statistics"""
        return {
            'total_commits': int(self.data['commits'].sum()),
            'avg_daily_commits': round(self.data['commits'].mean(), 2),
            'total_prs': int(self.data['pull_requests'].sum()),
            'avg_developers': round(self.data['active_developers'].mean(), 1),
            'total_codespace_hours': round(self.data['codespace_hours'].sum(), 2),
            'cost_estimate': round(self.data['codespace_hours'].sum() * 0.18, 2)  # $0.18/hour
        }
    
    def get_weekly_trends(self):
        """Get weekly aggregated trends"""
        weekly = self.data.resample('W', on='date').agg({
            'commits': 'sum',
            'pull_requests': 'sum',
            'code_reviews': 'sum',
            'active_developers': 'mean',
            'codespace_hours': 'sum'
        }).round(2)
        
        weekly.reset_index(inplace=True)
        return weekly.to_dict('records')

analyzer = DataAnalyzer()

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    """API endpoint for summary statistics"""
    return jsonify(analyzer.get_summary_stats())

@app.route('/api/trends')
def get_trends():
    """API endpoint for weekly trends"""
    return jsonify(analyzer.get_weekly_trends())

@app.route('/api/governance')
def get_governance():
    """API endpoint demonstrating governance data"""
    governance_data = {
        'policies': {
            'machine_types': ['2-core', '4-core', '8-core'],
            'idle_timeout_minutes': 30,
            'max_retention_days': 7,
            'require_sso': True,
            'allowed_extensions': [
                'ms-python.python',
                'ms-python.vscode-pylance',
                'github.copilot'
            ]
        },
        'compliance': {
            'total_codespaces': 15,
            'active_codespaces': 8,
            'compliant_codespaces': 15,
            'policy_violations': 0,
            'last_audit': datetime.now().isoformat()
        },
        'cost_controls': {
            'monthly_budget': 5000,
            'current_spend': 1234.56,
            'projected_spend': 2890.45,
            'per_user_limit': 500
        }
    }
    return jsonify(governance_data)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'environment': 'GitHub Codespaces',
        'organization': 'Demo Organization'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)