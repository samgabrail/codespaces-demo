"""
Demo Application - Simple Dashboard
Demonstrates a typical Python development workflow in GitHub Codespaces
"""

from flask import Flask, jsonify, render_template
from datetime import datetime, timedelta
import random
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

class DataAnalyzer:
    """Sample data analysis class for demonstration"""
    
    def __init__(self):
        self.data = self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate sample development metrics data"""
        data = []
        start_date = datetime.now() - timedelta(days=30)
        
        for i in range(30):
            date = start_date + timedelta(days=i)
            data.append({
                'date': date.isoformat(),
                'commits': random.randint(2, 8),
                'pull_requests': random.randint(0, 4),
                'code_reviews': random.randint(1, 5),
                'active_developers': random.randint(10, 25),
                'codespace_hours': round(random.uniform(20, 100), 2)
            })
        
        return data
    
    def get_summary_stats(self):
        """Calculate summary statistics"""
        total_commits = sum(d['commits'] for d in self.data)
        total_prs = sum(d['pull_requests'] for d in self.data)
        total_hours = sum(d['codespace_hours'] for d in self.data)
        avg_developers = sum(d['active_developers'] for d in self.data) / len(self.data)
        
        return {
            'total_commits': total_commits,
            'avg_daily_commits': round(total_commits / len(self.data), 2),
            'total_prs': total_prs,
            'avg_developers': round(avg_developers, 1),
            'total_codespace_hours': round(total_hours, 2),
            'cost_estimate': round(total_hours * 0.18, 2)  # $0.18/hour
        }
    
    def get_weekly_trends(self):
        """Get weekly aggregated trends"""
        # Simple weekly aggregation
        weeks = []
        for i in range(0, len(self.data), 7):
            week_data = self.data[i:i+7]
            week = {
                'week_start': week_data[0]['date'],
                'commits': sum(d['commits'] for d in week_data),
                'pull_requests': sum(d['pull_requests'] for d in week_data),
                'code_reviews': sum(d['code_reviews'] for d in week_data),
                'active_developers': round(sum(d['active_developers'] for d in week_data) / len(week_data), 1),
                'codespace_hours': round(sum(d['codespace_hours'] for d in week_data), 2)
            }
            weeks.append(week)
        return weeks

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