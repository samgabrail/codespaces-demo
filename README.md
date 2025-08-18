# GitHub Codespaces Enterprise Demo

This repository demonstrates enterprise-grade GitHub Codespaces configuration with governance, security, and standardization features for Python development teams.

## 🎯 Purpose

This demo showcases how GitHub Codespaces can:
- Eliminate shadow IT through centralized cloud development
- Enforce organizational standards via `.devcontainer` configurations
- Provide governance and cost controls
- Maintain security and compliance requirements

## 🚀 Quick Start

### Using GitHub Codespaces (Recommended)

1. Click the green **Code** button above
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. Wait ~60 seconds for environment setup
5. The development environment will open with VSCode in your browser

### Local Development

```bash
# Clone the repository
git clone https://github.com/[your-org]/codespaces-demo.git
cd codespaces-demo

# Install dependencies
pip install -r requirements.txt

# Run the demo application
python app.py
```

## 📁 Repository Structure

```
.
├── .devcontainer/
│   └── devcontainer.json      # Codespaces configuration
├── .github/
│   └── codespaces-policy.yml  # Example governance policies
├── app.py                     # Demo Flask application
├── templates/                 # HTML templates
├── static/                    # CSS and JavaScript
├── requirements.txt           # Python dependencies
└── .pre-commit-config.yaml   # Code quality hooks
```

## 🔧 Features Demonstrated

### 1. Standardized Development Environment
- Pre-configured Python 3.11 environment
- VSCode with curated extensions
- Automated dependency installation
- Security-hardened containers

### 2. Governance Controls
- Machine type restrictions
- Idle timeout policies
- Cost management limits
- Audit logging capabilities

### 3. Developer Experience
- 60-second environment setup
- Full VSCode in browser
- GitHub integration
- Jupyter notebook support

### 4. Security Features
- SSO enforcement
- Network restrictions
- Secrets management
- Centralized development with audit visibility

## 📊 Demo Application

The included Flask application demonstrates a development metrics dashboard with:
- Real-time usage statistics
- Governance policy visualization
- Cost tracking and estimates
- Compliance monitoring

### Running the Demo

Once your Codespace is running:

```bash
# The application starts automatically, or run:
python app.py
```

Access the dashboard at:
- `http://localhost:5000` (local)
- Use the **Ports** tab in Codespaces to open the forwarded URL

## 🛡️ Governance Configuration

**Note**: The `.github/codespaces-policy.yml` file is a demonstration example only. Actual GitHub Codespaces policies are configured through your organization's web interface at Settings → Codespaces → Policies.

The example policy file shows potential governance controls including:

- **Machine Types**: Control available compute resources
- **Timeouts**: Automatic resource cleanup
- **Security**: SSO, 2FA, IP restrictions
- **Cost Controls**: Budget limits and alerts
- **Compliance**: Audit logging and monitoring

## 💰 Cost Management

GitHub Codespaces pricing (2025):
- **2-core**: $0.18/hour
- **4-core**: $0.36/hour
- **8-core**: $0.72/hour
- **Storage**: $0.07/GB per month

Cost controls demonstrated:
- Per-user spending limits
- Team budget allocation
- Automatic idle shutdown
- Usage monitoring dashboards

## 🔄 Pre-commit Hooks

This repository includes pre-commit hooks for:
- Code formatting (Black)
- Linting (Flake8, Pylint)
- Type checking (MyPy)
- Security scanning (Bandit)
- File integrity checks

## 📈 Benefits for Organizations

### Eliminate Shadow IT
- Centralized development with governance visibility
- Complete audit trails of all development activity
- Policy enforcement and workflow controls
- Discourage local development through streamlined cloud workflow

### Standardization
- Consistent development environments
- Enforced coding standards
- Approved tools and extensions
- Reproducible setups

### Cost Optimization
- Pay only for active usage
- Automatic resource cleanup
- Budget controls
- Usage analytics

### Developer Productivity
- Instant environment setup
- No "works on my machine" issues
- Powerful cloud resources
- Seamless collaboration

## 🚦 Demo Scenarios

### Scenario 1: New Developer Onboarding
1. Developer receives repository access
2. Creates Codespace with one click
3. Environment ready in 60 seconds
4. Starts coding immediately

### Scenario 2: Governance Enforcement
1. Organization sets machine type limits
2. Configures idle timeout to 30 minutes
3. Sets $500/month per-user budget
4. Monitors compliance dashboard

### Scenario 3: Security Compliance
1. Enforce SSO authentication
2. Restrict to corporate IP ranges
3. Manage secrets centrally
4. Audit all activities

## 📚 Additional Resources

- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Pricing Calculator](https://github.com/pricing/calculator?feature=codespaces)
- [Dev Container Specification](https://containers.dev/)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)

## 📝 License

This demo repository is provided under the MIT License. See LICENSE file for details.

---

**Important**: This is a demonstration repository. The `.github/codespaces-policy.yml` file is an example only - actual GitHub Codespaces policies are configured through your GitHub organization's web interface (Settings → Codespaces → Policies), not through YAML files in repositories.

**Real Policy Configuration**: [Managing Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization)