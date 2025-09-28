# MCP Feedback Enhanced

**🌐 Language / 語言切換:** **English** | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

**Original Author:** [Fábio Ferreira](https://x.com/fabiomlferreira) | [Original Project](https://github.com/noopstudios/interactive-feedback-mcp) ⭐
**Enhanced Fork:** [Minidoracat](https://github.com/Minidoracat)
**UI Design Reference:** [sanshao85/mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

## 🎯 Core Concept

This [MCP server](https://modelcontextprotocol.io/) establishes **feedback-driven development workflows** through a **pure Web UI architecture**, seamlessly supporting local development, **SSH Remote environments** (Cursor SSH Remote, VS Code Remote SSH), and **WSL (Windows Subsystem for Linux) environments**. By guiding AI to confirm with users instead of making speculative operations, it consolidates multiple tool calls into a single feedback-driven request, dramatically reducing platform costs while improving development efficiency.

**🌐 Web-Only Architecture Benefits:**
- 🚀 **Streamlined Deployment**: Eliminates GUI dependencies for lighter installation
- 🌍 **Universal Compatibility**: Works across all operating systems and environments
- 🔧 **Simplified Maintenance**: Unified Web interface reduces complexity
- 📦 **Minimal Footprint**: Heavy GUI libraries removed for significantly smaller package size

**Supported Platforms:** [Cursor](https://www.cursor.com) | [Cline](https://cline.bot) | [Windsurf](https://windsurf.com) | [Augment](https://www.augmentcode.com) | [Trae](https://www.trae.ai)

### 🔄 Workflow
1. **AI Invocation** → Calls `mcp-feedback-enhanced` tool
2. **Web UI Launch** → Automatically opens browser interface (pure Web architecture)
3. **Intelligent Interaction** → Enables prompt selection, text input, image upload, and auto-submit
4. **Real-time Feedback** → WebSocket connection instantly delivers information to AI
5. **Session Tracking** → Automatically records session history and statistics
6. **Process Continuation** → AI adjusts behavior or concludes task based on user feedback

## 🌟 Key Features

### 🌐 Pure Web UI Architecture System
- **Web-Only Design**: Complete elimination of desktop GUI dependencies with pure Web interface
- **Universal Compatibility**: Full support for local, SSH Remote, and WSL environments
- **Intelligent Adaptation**: Automatic environment detection with optimal configuration
- **Effortless Deployment**: No complex GUI environment setup required

### 📝 Intelligent Prompt Management System (v2.4.0 New Feature)
- **Full CRUD Operations**: Create, edit, delete, and utilize frequently used prompts
- **Usage Analytics**: Track usage frequency with intelligent sorting algorithms
- **Instant Application**: One-click prompt selection and application
- **Auto-Submit Integration**: Seamless auto-submit marking with priority display

### ⏰ Auto-Timed Submit Feature (v2.4.0 New Feature)
- **Flexible Timing**: Configurable countdown timer ranging from 1 to 86,400 seconds
- **Visual Feedback**: Real-time countdown display with comprehensive status indicators
- **Deep Integration**: Seamless coordination with the prompt management system
- **Full Control**: Complete pause, resume, and cancel operation support

### 📊 Session Management & Tracking (v2.4.0 New Feature)
- **Live Status Monitoring**: Real-time display of current session status
- **Comprehensive History**: Complete session records with detailed statistical analysis
- **Data Insights**: Daily session counts and average duration analytics
- **Advanced Management**: Detailed session viewing and comprehensive management tools

### 🔗 Connection Monitoring System (v2.4.0 New Feature)
- **Live Connection Monitoring**: Real-time WebSocket connection status tracking
- **Quality Metrics**: Comprehensive latency measurement and connection quality indicators
- **Intelligent Reconnection**: Smart reconnection mechanisms with robust error handling
- **Comprehensive Analytics**: Complete connection statistics and performance metrics

### 🎨 Modern Interface Design
- **Modular Architecture**: Complete JavaScript modularization with clean code structure
- **Responsive Design**: Seamless adaptation to various screen sizes and window dimensions
- **Unified Aesthetics**: Consistent design language ensuring cohesive visual experience
- **Enhanced Session Panel**: Feature-rich left sidebar with collapsible session management

### 🖼️ Comprehensive Image Support
- **Broad Format Compatibility**: Full support for PNG, JPG, JPEG, GIF, BMP, and WebP formats
- **Flexible Upload Options**: Intuitive drag & drop functionality plus clipboard paste (Ctrl+V)
- **Unrestricted File Handling**: Support for images of any size with intelligent automatic processing

### 🌏 Multi-language Support
- **Triple Language Support**: Complete English, Traditional Chinese, and Simplified Chinese localization
- **Intelligent Detection**: Automatic language selection based on system preferences
- **Dynamic Switching**: Real-time language changes directly within the interface

### ✨ WSL Environment Support (v2.2.5)
- **Intelligent Detection**: Automatic identification of WSL (Windows Subsystem for Linux) environments
- **Seamless Browser Integration**: Automatic Windows browser launching within WSL environments
- **Multiple Launch Strategies**: Support for `cmd.exe`, `powershell.exe`, `wslview`, and additional browser launch methods
- **Zero-Configuration Experience**: Direct Web UI access for WSL users without additional setup

### 🌐 SSH Remote Environment Support (v2.3.0 New Feature)
- **Intelligent Detection**: Automatic identification of SSH Remote environments (Cursor SSH Remote, VS Code Remote SSH, etc.)
- **Browser Launch Assistance**: Clear guidance and solutions when automatic browser launching fails
- **Complete Port Forwarding Support**: Comprehensive setup guidance and troubleshooting documentation
- **Enhanced MCP Integration**: Optimized integration with MCP systems for improved connection stability
- **Comprehensive Documentation**: [SSH Remote Environment Usage Guide](docs/en/ssh-remote/browser-launch-issues.md)
- 🎯 **Smart Input Focus**: Automatic focus on feedback input box upon window opening for enhanced UX (Thanks @penn201500)

## 🌐 Interface Preview

### Web UI Interface (v2.4.0 - Web-Only Architecture)

<div align="center">
  <img src="docs/en/images/web1.jpeg" width="400" alt="Web UI Main Interface - Prompt Management & Auto-Submit" />
</div>

<details>
<summary>📱 Click to view complete interface screenshots</summary>

<div align="center">
  <img src="docs/en/images/web2.jpeg" width="800" alt="Web UI Complete Interface - Session Management & Settings" />
</div>

</details>

*Web UI Interface - Pure Web architecture supporting intelligent features including prompt management, auto-submit, session tracking, and more*

**Keyboard Shortcuts**
- `Ctrl+Enter` (Windows/Linux) / `Cmd+Enter` (macOS): Submit feedback (supports both main and numeric keypad)
- `Ctrl+V` (Windows/Linux) / `Cmd+V` (macOS): Paste clipboard images directly
- `Ctrl+I` (Windows/Linux) / `Cmd+I` (macOS): Quick input box focus (Thanks @penn201500)

## 🚀 Quick Start

### 1. Installation & Testing
```bash
# Install uv (if not already installed)
pip install uv

# Quick functionality test
uvx mcp-feedback-enhanced@latest test
```

### 2. MCP Configuration
**Standard Configuration** (recommended for most users):
```json
{
  "mcpServers": {
    "mcp-feedback-enhanced": {
      "command": "uvx",
      "args": ["mcp-feedback-enhanced@latest"],
      "timeout": 600,
      "autoApprove": ["interactive_feedback"]
    }
  }
}
```

**Advanced Configuration** (for custom environment requirements):
```json
{
  "mcpServers": {
    "mcp-feedback-enhanced": {
      "command": "uvx",
      "args": ["mcp-feedback-enhanced@latest"],
      "timeout": 600,
      "env": {
        "MCP_DEBUG": "false",
        "MCP_WEB_PORT": "8765"
      },
      "autoApprove": ["interactive_feedback"]
    }
  }
}
```

### 3. Prompt Engineering Setup
For optimal results, configure your AI assistant with these guidelines:

```
# MCP Interactive Feedback Rules

1. During any process, task, or conversation phase—whether inquiring, responding, or completing tasks—always invoke MCP mcp-feedback-enhanced.
2. Upon receiving user feedback, if content is non-empty, invoke MCP mcp-feedback-enhanced again and adjust behavior accordingly.
3. Only cease calling MCP mcp-feedback-enhanced when users explicitly indicate "end" or "no further interaction needed"—this marks process completion.
4. Unless explicitly instructed to end, all workflow steps must repeatedly invoke MCP mcp-feedback-enhanced.
5. Before task completion, use MCP mcp-feedback-enhanced to solicit user feedback.
```

## ⚙️ Advanced Settings

### Environment Variables
| Variable | Purpose | Accepted Values | Default |
|----------|---------|----------------|----------|
| `MCP_DEBUG` | Debug mode | `true`/`false` | `false` |
| `MCP_WEB_PORT` | Web UI port | `1024-65535` | `8765` |

### Testing Options
```bash
# Version information
uvx mcp-feedback-enhanced@latest version       # Check current version

# Interface testing
uvx mcp-feedback-enhanced@latest test --web    # Test Web UI (continuous auto-running mode)
uvx mcp-feedback-enhanced@latest test --enhanced # Comprehensive enhanced test suite

# Debug mode
MCP_DEBUG=true uvx mcp-feedback-enhanced@latest test
```

### Developer Installation
```bash
git clone https://github.com/Minidoracat/mcp-feedback-enhanced.git
cd mcp-feedback-enhanced
uv sync
```

**Local Testing Methods**
```bash
# Functional Testing
uv run python -m mcp_feedback_enhanced test              # Standard functional testing
uvx --with-editable . mcp-feedback-enhanced test --web   # Web UI testing (continuous running mode)

# Unit Testing
make test                                                # Execute all unit tests
make test-fast                                          # Fast testing (excludes slow tests)
make test-cov                                           # Testing with coverage report generation

# Code Quality Assurance
make check                                              # Comprehensive code quality validation
make quick-check                                        # Quick validation with automatic fixes
```

**Testing Descriptions**
- **Functional Testing**: Validates complete MCP tool functionality workflows
- **Unit Testing**: Tests individual module functionality in isolation
- **Coverage Testing**: Generates comprehensive HTML coverage reports in `htmlcov/` directory
- **Quality Assurance**: Includes comprehensive linting, formatting, and type checking

## 🆕 Version History

📋 **Complete Version History:** [RELEASE_NOTES/CHANGELOG.en.md](RELEASE_NOTES/CHANGELOG.en.md)

### Latest Version Highlights (v2.4.0)
- 🏗️ **Web-Only Architecture Refactoring**: Complete elimination of PyQt6 GUI dependencies with transition to pure Web UI architecture, dramatically simplifying deployment
- 📝 **Intelligent Prompt Management**: Comprehensive prompt CRUD system featuring usage analytics and intelligent sorting algorithms
- ⏰ **Auto-Timed Submit**: Configurable countdown timer with seamless prompt management system integration
- 📊 **Advanced Session Management**: Real-time session monitoring, comprehensive history tracking, and detailed statistical analysis
- 🔗 **Enhanced Connection Monitoring**: Sophisticated WebSocket connection monitoring with latency measurement and intelligent auto-reconnection
- 🎨 **Comprehensive UI/UX Enhancement**: Modern session panel, responsive design principles, and unified visual aesthetics
- 🌐 **Improved Multi-language System**: Optimized language switching mechanisms with enhanced localization coverage
- 🛠️ **Technical Architecture Modernization**: Complete JavaScript modularization adopting contemporary development patterns

## 🐛 Common Issues

### 🌐 SSH Remote Environment Issues
**Q: Browser cannot launch in SSH Remote environment**
A: This is expected behavior. SSH Remote environments lack graphical interfaces, requiring manual browser access via local machine. For comprehensive solutions, see: [SSH Remote Environment Usage Guide](docs/en/ssh-remote/browser-launch-issues.md)

**Q: Why am I not receiving new MCP feedback?**
A: This typically indicates a WebSocket connection issue. **Solution**: Simply refresh the browser page to re-establish connection.

**Q: Why isn't MCP being invoked?**
A: Please verify the MCP tool status displays a green indicator. **Solution**: Toggle the MCP tool on/off repeatedly, allowing a few seconds for system reconnection.

**Q: Augment cannot start MCP**
A: **Solution**: Completely close and restart VS Code or Cursor, then reopen the project to reset the MCP connection.

### 🔧 General Issues
**Q: How to access the legacy GUI interface?**
A: v2.4.0 has completely eliminated PyQt6 GUI dependencies in favor of pure Web UI architecture. To access legacy GUI functionality, specify v2.3.0 or earlier versions:
```bash
# Use v2.3.0 (final version supporting GUI)
uvx mcp-feedback-enhanced@2.3.0

# Or specify version in MCP configuration
{
  "mcpServers": {
    "mcp-feedback-enhanced": {
      "command": "uvx",
      "args": ["mcp-feedback-enhanced@2.3.0"],
      "timeout": 600,
      "autoApprove": ["interactive_feedback"]
    }
  }
}
```
**Important**: Legacy versions lack v2.4.0 features (prompt management, auto-submit, session management, etc.).

**Q: Encountering "Unexpected token 'D'" error**
A: This stems from debug output interference. Set `MCP_DEBUG=false` or remove the environment variable entirely.

**Q: Chinese character encoding issues**
A: Resolved in v2.0.3. Update to latest version: `uvx mcp-feedback-enhanced@latest`

**Q: Multi-screen window positioning problems**
A: Fixed in v2.1.1. Navigate to "⚙️ Settings" tab and enable "Always show window at primary screen center" for resolution. Particularly effective for T-shaped screen arrangements and complex multi-monitor setups.

**Q: Image upload failures**
A: Verify file format compatibility (PNG/JPG/JPEG/GIF/BMP/WebP). The system supports images of any size with intelligent processing.

**Q: Web UI startup failures**
A: Check firewall configurations or attempt using an alternative port.

**Q: UV Cache consuming excessive disk space**
A: Frequent `uvx` command usage can accumulate cache to tens of GB. Regular maintenance is recommended:
```bash
# Analyze cache size and detailed information
python scripts/cleanup_cache.py --size

# Preview cleanup operations (without executing)
python scripts/cleanup_cache.py --dry-run

# Execute standard cleanup
python scripts/cleanup_cache.py --clean

# Force cleanup (attempts process termination, resolves Windows file lock issues)
python scripts/cleanup_cache.py --force

# Direct uv command alternative
uv cache clean
```
For comprehensive instructions, see: [Cache Management Guide](docs/en/cache-management.md)

**Q: AI models struggle with image parsing**
A: Various AI models (including Gemini Pro 2.5, Claude, etc.) exhibit inconsistent image parsing performance, sometimes successfully identifying content while other times failing completely. This represents a known limitation in AI visual understanding technology. Recommendations:
1. Ensure optimal image quality (high contrast, clear text)
2. Attempt multiple uploads; repeated attempts typically succeed
3. If parsing consistently fails, experiment with different image sizes or formats

## 🙏 Acknowledgments

### 🌟 Support Original Author
**Fábio Ferreira** - [X @fabiomlferreira](https://x.com/fabiomlferreira)
**Original Project:** [noopstudios/interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)

If you find this useful, please:
- ⭐ [Star the original project](https://github.com/noopstudios/interactive-feedback-mcp)
- 📱 [Follow the original author](https://x.com/fabiomlferreira)

### Design Inspiration
**sanshao85** - [mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

### Contributors
**penn201500** - [GitHub @penn201500](https://github.com/penn201500)
- 🎯 Auto-focus input box feature ([PR #39](https://github.com/Minidoracat/mcp-feedback-enhanced/pull/39))

### Community Support
- **Discord:** [https://discord.gg/Gur2V67](https://discord.gg/Gur2V67)
- **Issues:** [GitHub Issues](https://github.com/Minidoracat/mcp-feedback-enhanced/issues)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---
**🌟 Welcome to Star and share with more developers!**
