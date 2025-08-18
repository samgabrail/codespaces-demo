document.addEventListener('DOMContentLoaded', function() {
    // Load summary statistics
    loadStats();
    // Load governance data
    loadGovernance();
    
    // Refresh data every 30 seconds
    setInterval(() => {
        loadStats();
        loadGovernance();
    }, 30000);
});

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        document.getElementById('total-commits').textContent = data.total_commits;
        document.getElementById('avg-developers').textContent = data.avg_developers;
        document.getElementById('codespace-hours').textContent = `${data.total_codespace_hours.toFixed(1)}h`;
        document.getElementById('cost-estimate').textContent = `$${data.cost_estimate.toFixed(2)}`;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

async function loadGovernance() {
    try {
        const response = await fetch('/api/governance');
        const data = await response.json();
        
        // Update policies
        const policiesList = document.getElementById('policies-list');
        policiesList.innerHTML = `
            <li>✓ Machine Types: ${data.policies.machine_types.join(', ')}</li>
            <li>✓ Idle Timeout: ${data.policies.idle_timeout_minutes} minutes</li>
            <li>✓ Max Retention: ${data.policies.max_retention_days} days</li>
            <li>✓ SSO Required: ${data.policies.require_sso ? 'Yes' : 'No'}</li>
            <li>✓ Allowed Extensions: ${data.policies.allowed_extensions.length} approved</li>
        `;
        
        // Update compliance status
        const complianceStatus = document.getElementById('compliance-status');
        const complianceRate = (data.compliance.compliant_codespaces / data.compliance.total_codespaces * 100).toFixed(1);
        complianceStatus.innerHTML = `
            <p><strong>Total Codespaces:</strong> ${data.compliance.total_codespaces}</p>
            <p><strong>Active:</strong> ${data.compliance.active_codespaces}</p>
            <p><strong>Compliance Rate:</strong> ${complianceRate}%</p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${complianceRate}%"></div>
            </div>
            <p><strong>Policy Violations:</strong> ${data.compliance.policy_violations}</p>
            <p style="font-size: 0.875rem; color: #656d76; margin-top: 8px;">
                Last audit: ${new Date(data.compliance.last_audit).toLocaleString()}
            </p>
        `;
        
        // Update cost controls
        const costControls = document.getElementById('cost-controls');
        const budgetUsed = (data.cost_controls.current_spend / data.cost_controls.monthly_budget * 100).toFixed(1);
        costControls.innerHTML = `
            <p><strong>Monthly Budget:</strong> $${data.cost_controls.monthly_budget}</p>
            <p><strong>Current Spend:</strong> $${data.cost_controls.current_spend}</p>
            <p><strong>Projected:</strong> $${data.cost_controls.projected_spend}</p>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${budgetUsed}%; background: ${budgetUsed > 80 ? '#cf222e' : '#1a7f37'}"></div>
            </div>
            <p><strong>Per User Limit:</strong> $${data.cost_controls.per_user_limit}</p>
        `;
    } catch (error) {
        console.error('Error loading governance data:', error);
    }
}