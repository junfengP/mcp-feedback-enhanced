# MCP Feedback Enhanced（交互反馈 MCP）

**🌐 语言切换 / Language:** [English](README.md) | [繁體中文](README.zh-TW.md) | **简体中文**

**原作者：** [Fábio Ferreira](https://x.com/fabiomlferreira) | [原始项目](https://github.com/noopstudios/interactive-feedback-mcp) ⭐
**分支版本：** [Minidoracat](https://github.com/Minidoracat)
**UI 设计参考：** [sanshao85/mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

## 🎯 核心理念

这是一个 [MCP 服务器](https://modelcontextprotocol.io/)，旨在建立**反馈驱动的开发工作流程**，采用**纯 Web UI 架构**，完美兼容本地开发、**SSH 远程环境**（Cursor SSH Remote、VS Code Remote SSH）与 **WSL (Windows Subsystem for Linux) 环境**。通过引导 AI 与用户确认而非进行推测性操作，能够将多次工具调用整合为单次反馈驱动请求，显著降低平台成本并提升开发效率。

**🌐 Web-Only 架构优势：**
- 🚀 **部署简化**：无需 GUI 依赖，安装更加轻量
- 🌍 **通用兼容**：支持所有操作系统和环境
- 🔧 **维护简化**：统一的 Web 界面，降低复杂度
- 📦 **体积精简**：移除重型 GUI 库，安装包大幅缩小

**支持平台：** [Cursor](https://www.cursor.com) | [Cline](https://cline.bot) | [Windsurf](https://windsurf.com) | [Augment](https://www.augmentcode.com) | [Trae](https://www.trae.ai)

### 🔄 工作流程
1. **AI 调用** → 调用 `mcp-feedback-enhanced` 工具
2. **Web UI 启动** → 自动打开浏览器界面（纯 Web 架构）
3. **智能交互** → 实现提示词选择、文本输入、图片上传和自动提交
4. **实时反馈** → WebSocket 连接即时传递信息给 AI
5. **会话追踪** → 自动记录会话历史与统计数据
6. **流程继续** → AI 根据用户反馈调整行为或结束任务

## 🌟 主要功能

### 🌐 纯 Web UI 架构系统
- **Web-Only 设计**：彻底移除桌面 GUI 依赖，采用纯 Web 界面
- **通用兼容性**：全面支持本地、SSH Remote 和 WSL 环境
- **智能适配**：自动环境检测与最优配置
- **轻量部署**：无需复杂的 GUI 环境配置

### 📝 智能提示词管理系统（v2.4.0 新功能）
- **全功能 CRUD 操作**：新增、编辑、删除和使用常用提示词
- **使用数据分析**：追踪使用频率并智能排序
- **快速应用**：一键选择和应用提示词
- **自动提交集成**：支持自动提交标记和优先显示

### ⏰ 自动定时提交功能（v2.4.0 新功能）
- **灵活计时**：可设定 1-86400 秒的倒数计时器
- **可视化显示**：实时倒数显示和状态指示
- **深度集成**：与提示词管理系统无缝配合
- **全面控制**：支持暂停、恢复、取消操作

### 📊 会话管理与追踪（v2.4.0 新功能）
- **实时状态监控**：实时显示当前会话状态
- **全面历史记录**：完整的会话历史和统计分析
- **数据洞察**：今日会话数量和平均时长统计
- **高级管理**：会话详情查看和管理功能

### 🔗 连接监控系统（v2.4.0 新功能）
- **实时连接监控**：实时追踪 WebSocket 连接状态
- **质量指标**：全面的延迟测量和连接质量指示
- **智能重连**：智能重连机制和错误处理
- **全面统计**：完整的连接统计信息

### 🎨 现代化界面设计
- **模块化架构**：JavaScript 完全模块化重构，代码结构简洁
- **响应式设计**：完美适配不同屏幕尺寸和窗口大小
- **统一美学**：一致的设计语言和视觉体验
- **增强会话面板**：功能丰富的左侧会话管理面板，支持收合/展开

### 🖼️ 全面图片支持
- **广泛格式兼容**：全面支持 PNG、JPG、JPEG、GIF、BMP、WebP 格式
- **灵活上传方式**：直观的拖放功能 + 剪贴板粘贴（Ctrl+V）
- **无限制文件处理**：支持任意大小的图片文件，智能自动处理

### 🌏 多语言支持
- **三语支持**：完整的简体中文、英文、繁体中文本地化
- **智能检测**：根据系统语言自动选择
- **动态切换**：界面内可实时切换语言

### ✨ WSL 环境支持（v2.2.5）
- **智能检测**：自动识别 WSL (Windows Subsystem for Linux) 环境
- **无缝浏览器集成**：WSL 环境下自动启动 Windows 浏览器
- **多種启动策略**：支持 `cmd.exe`、`powershell.exe`、`wslview` 等多种浏览器启动方法
- **零配置体验**：WSL 用户可直接使用 Web UI，无需额外配置

### 🌐 SSH Remote 环境支持（v2.3.0 新功能）
- **智能检测**：自动识别 SSH Remote 环境（Cursor SSH Remote、VS Code Remote SSH 等）
- **浏览器启动指导**：当无法自动启动浏览器时，提供清晰的解决方案
- **全面端口转发支持**：完整的端口转发设置指导和故障排除
- **MCP 集成优化**：改善与 MCP 系统的集成，提供更稳定的连接体验
- **详细文档**：[SSH Remote 环境使用指南](docs/zh-CN/ssh-remote/browser-launch-issues.md)

## 🌐 界面预览

### Web UI 界面（v2.4.0 - Web-Only 架构）

<div align="center">
  <img src="docs/zh-CN/images/web1.jpeg" width="400" alt="Web UI 主界面 - 提示词管理与自动提交" />
</div>

<details>
<summary>📱 点击查看完整界面截图</summary>

<div align="center">
  <img src="docs/zh-CN/images/web2.jpeg" width="800" alt="Web UI 完整界面 - 会话管理与设置" />
</div>

</details>

*Web UI 界面 - 纯 Web 架构，支持提示词管理、自动提交、会话追踪等智能功能*

**快捷键支持**
- `Ctrl+Enter`（Windows/Linux）/ `Cmd+Enter`（macOS）：提交反馈（主键盘与数字键盘均可用）
- `Ctrl+V`（Windows/Linux）/ `Cmd+V`（macOS）：直接粘贴剪贴板图片
- `Ctrl+I`（Windows/Linux）/ `Cmd+I`（macOS）：快速聚焦输入框 (感谢 @penn201500)

## 🚀 快速开始

### 1. 安装与测试
```bash
# 安装 uv（如果尚未安装）
pip install uv

# 快速功能测试
uvx mcp-feedback-enhanced@latest test
```

### 2. 配置 MCP
**标准配置**（推荐大多数用户使用）：
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

**进阶配置**（需要自定义环境要求）：
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

### 3. 设定提示工程
为了获得最佳效果，请在 AI 助手中配置以下指导原则：

```
# MCP Interactive Feedback 规则

1. 在任何流程、任务、对话阶段中——无论是询问、响应还是完成任务——始终调用 MCP mcp-feedback-enhanced。
2. 收到用户反馈后，如果内容非空，再次调用 MCP mcp-feedback-enhanced 并相应调整行为。
3. 仅当用户明确表示“结束”或“不再需要交互”时，才可停止调用 MCP mcp-feedback-enhanced——这标志着流程完成。
4. 除非明确指示结束，否则所有工作流步骤必须重复调用 MCP mcp-feedback-enhanced。
5. 任务完成前，使用 MCP mcp-feedback-enhanced 征求用户反馈。
```

## ⚙️ 进阶设定

### 环境变量
| 变量 | 用途 | 可接受值 | 默认值 |
|------|------|-----------|------|
| `MCP_DEBUG` | 调试模式 | `true`/`false` | `false` |
| `MCP_WEB_PORT` | Web UI 端口 | `1024-65535` | `8765` |

### 测试选项
```bash
# 版本信息
uvx mcp-feedback-enhanced@latest version       # 检查当前版本

# 界面测试
uvx mcp-feedback-enhanced@latest test --web    # 测试 Web UI（持续自动运行模式）
uvx mcp-feedback-enhanced@latest test --enhanced # 全面增强测试套件

# 调试模式
MCP_DEBUG=true uvx mcp-feedback-enhanced@latest test
```

### 开发者安装
```bash
git clone https://github.com/Minidoracat/mcp-feedback-enhanced.git
cd mcp-feedback-enhanced
uv sync
```

**本地测试方式**
```bash
# 功能测试
uv run python -m mcp_feedback_enhanced test              # 标准功能测试
uvx --with-editable . mcp-feedback-enhanced test --web   # Web UI 测试（持续运行模式）

# 单元测试
make test                                                # 执行所有单元测试
make test-fast                                          # 快速测试（排除慢速测试）
make test-cov                                           # 测试并生成覆盖率报告

# 代码质量保证
make check                                              # 全面代码质量验证
make quick-check                                        # 快速验证并自动修复
```

**测试说明**
- **功能测试**：验证 MCP 工具的完整功能工作流程
- **单元测试**：测试各个模块的独立功能
- **覆盖率测试**：生成全面的 HTML 覆盖率报告到 `htmlcov/` 目录
- **质量保证**：包含全面的 linting、格式化和类型检查

## 🆕 版本更新记录

📋 **完整版本更新记录：** [RELEASE_NOTES/CHANGELOG.zh-CN.md](RELEASE_NOTES/CHANGELOG.zh-CN.md)

### 最新版本亮点（v2.4.0）
- 🏗️ **Web-Only 架构重构**: 彻底移除 PyQt6 GUI 依赖，迁移至纯 Web UI 架构，大幅简化部署流程
- 📝 **智能提示词管理**: 新增完整的提示词 CRUD 系统，支持使用统计和智能排序
- ⏰ **自动定时提交**: 可配置倒数计时器，与提示词管理深度集成
- 📊 **高级会话管理**: 实时会话监控、全面历史追踪和详细统计分析
- 🔗 **增强连接监控**: 高级 WebSocket 连接监控，包含延迟测量和智能自动重连
- 🎨 **全面 UI/UX 增强**: 现代化会话面板、响应式设计原则和统一视觉美学
- 🌐 **多语言系统改进**: 优化语言切换机制，增强本地化覆盖率
- 🛠️ **技术架构现代化**: 完整 JavaScript 模块化，采用当代开发模式

## 🐛 常见问题

### 🌐 SSH Remote 环境问题
**Q: SSH Remote 环境下浏览器无法启动**
A: 这是预期行为。SSH Remote 环境缺乏图形界面，需要手动通过本地机器访问浏览器。详细解决方案请参考：[SSH Remote 环境使用指南](docs/zh-CN/ssh-remote/browser-launch-issues.md)

**Q: 为什么没有接收到 MCP 新的反馈？**
A: 这通常表示 WebSocket 连接问题。**解决方法**：直接刷新浏览器页面以重新建立连接。

**Q: 为什么没有调用出 MCP？**
A: 请验证 MCP 工具状态显示为绿色指示器。**解决方法**：反复开关 MCP 工具，等待几秒让系统重新连接。

**Q: Augment 无法启动 MCP**
A: **解决方法**：完全关闭并重新启动 VS Code 或 Cursor，重新打开项目以重置 MCP 连接。

### 🔧 一般问题
**Q: 如何使用旧版 GUI 界面？**
A: v2.4.0 版本已完全移除 PyQt6 GUI 依赖，转为纯 Web UI 架构。如需使用旧版 GUI，请指定 v2.3.0 或更早版本：
```bash
# 使用 v2.3.0（最后支持 GUI 的版本）
uvx mcp-feedback-enhanced@2.3.0

# 或在 MCP 配置中指定版本
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
**注意**：旧版本不包含 v2.4.0 的新功能（提示词管理、自动提交、会话管理等）。

**Q: 出现 "Unexpected token 'D'" 错误**
A: 这源于调试输出干扰。设置 `MCP_DEBUG=false` 或完全移除该环境变量。

**Q: 中文字符编码问题**
A: 已在 v2.0.3 解决。更新到最新版本：`uvx mcp-feedback-enhanced@latest`

**Q: 多屏幕环境下窗口定位问题**
A: 已在 v2.1.1 修复。进入「⚙️ 设置」标签页，启用「总是在主屏幕中心显示窗口」即可解决。特别适用于 T 字型屏幕排列等复杂多屏幕配置。

**Q: 图片上传失败**
A: 验证文件格式兼容性（PNG/JPG/JPEG/GIF/BMP/WebP）。系统支持任意大小的图片文件并智能处理。

**Q: Web UI 启动失败**
A: 检查防火墙配置或尝试使用不同的端口。

**Q: UV Cache 占用过多磁盘空间**
A: 由于频繁使用 `uvx` 命令，cache 可能会累积到数十 GB。建议定期维护：
```bash
# 分析 cache 大小和详细信息
python scripts/cleanup_cache.py --size

# 预览清理操作（不实际执行）
python scripts/cleanup_cache.py --dry-run

# 执行标准清理
python scripts/cleanup_cache.py --clean

# 强制清理（尝试终止进程，解决 Windows 文件锁定问题）
python scripts/cleanup_cache.py --force

# 直接 uv 命令替代方案
uv cache clean
```
全面说明请参考：[Cache 管理指南](docs/zh-CN/cache-management.md)

**Q: AI 模型无法解析图片**
A: 各种 AI 模型（包括 Gemini Pro 2.5、Claude 等）在图片解析上呈现不一致的性能，有时成功识别内容，有时完全失败。这代表 AI 视觉理解技术的已知限制。建议：
1. 确保最优图片质量（高对比度、清晰文字）
2. 尝试多次上传；重复尝试通常能成功
3. 如果解析一直失败，尝试不同的图片尺寸或格式

## 🙏 致谢

### 🌟 支持原作者
**Fábio Ferreira** - [X @fabiomlferreira](https://x.com/fabiomlferreira)
**原始项目：** [noopstudios/interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)

如果您觉得有用，请：
- ⭐ [为原项目按星星](https://github.com/noopstudios/interactive-feedback-mcp)
- 📱 [关注原作者](https://x.com/fabiomlferreira)

### 设计灵感
**sanshao85** - [mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

### 贡献者
**penn201500** - [GitHub @penn201500](https://github.com/penn201500)
- 🎯 自动聚焦输入框功能 ([PR #39](https://github.com/Minidoracat/mcp-feedback-enhanced/pull/39))

### 社群支援
- **Discord：** [https://discord.gg/Gur2V67](https://discord.gg/Gur2V67)
- **Issues：** [GitHub Issues](https://github.com/Minidoracat/mcp-feedback-enhanced/issues)

## 📄 授权

MIT 授权条款 - 详见 [LICENSE](LICENSE) 档案

---
**🌟 欢迎 Star 并分享给更多开发者！**
