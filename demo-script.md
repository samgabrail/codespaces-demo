# GitHub Codespaces Demo Script

## Pre-Demo Setup
- [ ] Ensure you're logged into GitHub with an account that has Codespaces access
- [ ] Have this repository ready to demo
- [ ] Clear browser cache/cookies if needed
- [ ] Have organization settings page ready (if you have admin access)

## Demo Flow

### 1. Introduction (2 minutes)
**Talking Points:**
- "Today I'll demonstrate how GitHub Codespaces solves shadow IT challenges while improving developer productivity"
- "We'll see governance controls, standardization, and the developer experience"
- "Everything runs in the cloud - no local setup required"

### 2. Creating a Codespace (3 minutes)

**Actions:**
1. Navigate to the repository
2. Click green "Code" button
3. Show Codespaces tab
4. Click "Create codespace on main"

**While it's loading, explain:**
- "Notice it takes about 60 seconds to spin up"
- "The `.devcontainer/devcontainer.json` file defines the entire environment"
- "Every developer gets the exact same setup - Python 3.11, all tools pre-installed"
- "This eliminates 'works on my machine' problems"

### 3. Environment Tour (5 minutes)

**Show `.devcontainer/devcontainer.json`:**
```bash
cat .devcontainer/devcontainer.json
```

**Highlight:**
- Standardized Python 3.11 image
- Pre-approved VS Code extensions
- Security settings (capability drops, no new privileges)
- Post-create commands for automatic setup

**Show installed extensions:**
- Open Extensions sidebar
- Point out Python, Jupyter, GitHub Copilot
- "Only approved extensions are available"

**Show terminal:**
```bash
# Show Python is installed
python --version

# Show pre-installed packages
pip list

# Show git is configured
git config --list | grep user
```

### 4. Governance Features (5 minutes)

**Show policy file:**
```bash
cat .github/codespaces-policy.yml
```

**Key points to highlight:**
- Machine type restrictions (no expensive instances)
- 30-minute idle timeout (cost control)
- SSO requirement
- IP allowlisting capability
- Per-user spending limits

**If you have org admin access:**
- Navigate to Organization Settings > Codespaces
- Show actual policy configuration
- Point out usage reports and cost tracking

### 5. Running the Demo App (5 minutes)

**Start the application:**
```bash
python app.py
```

**Actions:**
1. Open browser preview using Ports tab
2. Show the dashboard loads immediately
3. Point out the governance metrics
4. Highlight cost tracking features

**Explain:**
- "This dashboard represents what IT admins would see"
- "Real-time tracking of all development activity"
- "Complete visibility into costs and compliance"

### 6. Developer Workflow (5 minutes)

**Create a new feature:**
```bash
# Create a new branch
git checkout -b feature/demo-enhancement

# Edit a file
echo "# New feature code" >> feature.py

# Show pre-commit hooks
git add .
git commit -m "Add demo feature"
```

**Show pre-commit in action:**
- "Notice automatic code formatting with Black"
- "Linting checks run automatically"
- "Security scanning with Bandit"
- "This ensures code quality without manual review"

### 7. Shadow IT Prevention (3 minutes)

**Key talking points:**
- "Centralized development provides complete visibility"
- "IT has complete visibility of all development activity"
- "Audit logs track every action"
- "Organizations can monitor and control development patterns"

**Show audit capability:**
```bash
# Show that all actions are logged
echo "All commands and file changes are audited"
echo "Export to SIEM systems is possible"
```

### 8. Cost Management (2 minutes)

**Show cost calculations:**
- Open browser to GitHub pricing calculator
- "2-core instance: $0.18/hour"
- "Automatic shutdown after 30 minutes idle"
- "Monthly budget of $500/developer is typically sufficient"
- "That's ~2,700 hours of development time per month"

### 9. Collaboration Features (2 minutes)

**If time permits:**
- Show port forwarding for sharing
- Mention Live Share capabilities
- Explain how multiple developers can work together

### 10. Q&A and Specific Scenarios (5 minutes)

**Be prepared to answer:**

**Q: "What about our existing tools?"**
A: Show how to add them to devcontainer.json

**Q: "Can developers still work offline?"**
A: "Yes, developers can still clone repos locally, but Codespaces provides the governance visibility and standardized environment that IT needs"

**Q: "What about data scientists with large datasets?"**
A: Discuss volume mounts and data persistence options

**Q: "How do we migrate existing projects?"**
A: Walk through adding .devcontainer to existing repo

## Key Messages to Reinforce

Throughout the demo, repeatedly emphasize:

1. **Security**: "Centralized development with audit visibility"
2. **Standardization**: "Everyone gets the same environment"
3. **Cost Control**: "Pay only for what you use"
4. **Productivity**: "Developers can start coding in 60 seconds"
5. **Governance**: "Complete visibility and control for IT"

## Troubleshooting

If something doesn't work:

**Codespace won't start:**
- "This might be a quota issue - let me show you the backup"
- Have screenshots ready

**App doesn't run:**
- "Let me quickly check the logs"
- Run `pip install -r requirements.txt` manually

**Network issues:**
- "This would typically be configured for your corporate network"
- Explain how IP restrictions work

## Post-Demo Follow-up

Provide:
1. Link to this repository
2. Link to GitHub Codespaces documentation
3. Offer to set up a pilot program
4. Schedule follow-up meeting for deeper dive

## Customization for Specific Audiences

### For Developers:
- Focus more on productivity features
- Show debugging capabilities
- Demonstrate extension ecosystem

### For IT/Security:
- Emphasize governance controls
- Deep dive into audit logs
- Show cost management dashboards

### For Management:
- Focus on cost savings
- Highlight productivity metrics
- Show compliance capabilities

## Success Metrics to Share

- "Typical setup time reduced from hours to 60 seconds"
- "0% shadow IT incidents after implementation"
- "30% reduction in environment-related issues"
- "Average $200/month per developer cost"