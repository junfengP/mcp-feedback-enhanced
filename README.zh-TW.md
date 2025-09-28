# MCP Feedback Enhanced（互動回饋 MCP）

**🌐 語言切換 / Language:** [English](README.md) | **繁體中文** | [简体中文](README.zh-CN.md)

**原作者：** [Fábio Ferreira](https://x.com/fabiomlferreira) | [原始專案](https://github.com/noopstudios/interactive-feedback-mcp) ⭐
**分支版本：** [Minidoracat](https://github.com/Minidoracat)
**UI 設計參考：** [sanshao85/mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

## 🎯 核心理念

這是一個 [MCP 伺服器](https://modelcontextprotocol.io/)，旨在建立**回饋驅動的開發工作流程**，採用**純 Web UI 架構**，完美相容本地開發、**SSH 遠端环境**與 **WSL (Windows Subsystem for Linux) 环境**。透過引導 AI 與使用者確認而非進行推測性操作，能夠將多次工具調用整合為單次回饋驅動請求，顯著降低平台成本並提升開發效率。

**🌐 Web-Only 架構優勢：**
- 🚀 **部署簡化**：無需 GUI 依賴，安裝更加輕量
- 🌍 **通用相容**：支援所有作業系統和環境
- 🔧 **維護簡化**：統一的 Web 介面，降低複雜度
- 📦 **體積精簡**：移除重型 GUI 庫，安裝包大幅縮小

**支援平台：** [Cursor](https://www.cursor.com) | [Cline](https://cline.bot) | [Windsurf](https://windsurf.com) | [Augment](https://www.augmentcode.com) | [Trae](https://www.trae.ai)

### 🔄 工作流程
1. **AI 調用** → 調用 `mcp-feedback-enhanced` 工具
2. **Web UI 啟動** → 自動開啟瀏覽器介面（純 Web 架構）
3. **智能互動** → 實現提示詞選擇、文字輸入、圖片上傳和自動提交
4. **即時回饋** → WebSocket 連線即時傳遞資訊給 AI
5. **會話追蹤** → 自動記錄會話歷史與統計數據
6. **流程繼續** → AI 根據使用者回饋調整行為或結束任務

## 🌟 主要功能

### 🌐 純 Web UI 架構系統
- **Web-Only 設計**：彻底移除桌面 GUI 依賴，採用純 Web 介面
- **通用相容性**：全面支援本地、SSH Remote 和 WSL 環境
- **智能適配**：自動環境檢測與最佳配置
- **輕量部署**：無需複雜的 GUI 環境配置

### 📝 智能提示詞管理系統（v2.4.0 新功能）
- **全功能 CRUD 操作**：新增、編輯、刪除和使用常用提示詞
- **使用數據分析**：追蹤使用頻率並智能排序
- **快速應用**：一鍵選擇和應用提示詞
- **自動提交整合**：支援自動提交標記和優先顯示

### ⏰ 自動定時提交功能（v2.4.0 新功能）
- **靈活計時**：可設定 1-86400 秒的倒數計時器
- **可視化顯示**：即時倒數顯示和狀態指示
- **深度整合**：與提示詞管理系統無縫配合
- **全面控制**：支援暫停、恢復、取消操作

### 📊 會話管理與追蹤（v2.4.0 新功能）
- **即時狀態監控**：即時顯示目前會話狀態
- **全面歷史記錄**：完整的會話歷史和統計分析
- **數據洞察**：今日會話數量和平均時長統計
- **高級管理**：會話詳情查看和管理功能

### 🔗 連線監控系統（v2.4.0 新功能）
- **即時連線監控**：即時追蹤 WebSocket 連線狀態
- **品質指標**：全面的延遲測量和連線品質指示
- **智能重連**：智能重連機制和錯誤處理
- **全面統計**：完整的連線統計資訊

### 🎨 現代化介面設計
- **模組化架構**：JavaScript 完全模組化重構，代碼結構簡潔
- **響應式設計**：完美適配不同螢幕尺寸和視窗大小
- **統一美學**：一致的設計語言和視覺體驗
- **增強會話面板**：功能豐富的左側會話管理面板，支援收合/展開

### 🖼️ 全面圖片支援
- **廣泛格式相容**：全面支援 PNG、JPG、JPEG、GIF、BMP、WebP 格式
- **靈活上傳方式**：直覺的拖放功能 + 剪貼板粘貼（Ctrl+V）
- **無限制檔案處理**：支援任意大小的圖片檔案，智能自動處理

### 🌏 多語言支援
- **三語支援**：完整的繁體中文、英文、簡體中文本地化
- **智能偵測**：根據系統語言自動選擇
- **動態切換**：介面內可即時切換語言

### ✨ WSL 環境支援（v2.2.5）
- **智能檢測**：自動識別 WSL (Windows Subsystem for Linux) 環境
- **無縫瀏覽器整合**：WSL 環境下自動啟動 Windows 瀏覽器
- **多種啟動策略**：支援 `cmd.exe`、`powershell.exe`、`wslview` 等多種瀏覽器啟動方法
- **零配置體驗**：WSL 使用者可直接使用 Web UI，無需額外配置

### 🌐 SSH Remote 環境支援（v2.3.0 新功能）
- **智能檢測**：自動識別 SSH Remote 環境（Cursor SSH Remote、VS Code Remote SSH 等）
- **瀏覽器啟動指導**：當無法自動啟動瀏覽器時，提供清晰的解決方案
- **全面埠埠轉發支援**：完整的埠埠轉發設定指導和故障排除
- **MCP 整合優化**：改善與 MCP 系統的整合，提供更穩定的連接體驗
- **詳細文檔**：[SSH Remote 環境使用指南](docs/zh-TW/ssh-remote/browser-launch-issues.md)

## 🌐 介面預覽

### Web UI 介面（v2.4.0 - Web-Only 架構）

<div align="center">
  <img src="docs/zh-TW/images/web1.jpeg" width="400" alt="Web UI 主介面 - 提示詞管理與自動提交" />
</div>

<details>
<summary>📱 點擊查看完整介面截圖</summary>

<div align="center">
  <img src="docs/zh-TW/images/web2.jpeg" width="800" alt="Web UI 完整介面 - 會話管理與設定" />
</div>

</details>

*Web UI 介面 - 純 Web 架構，支援提示詞管理、自動提交、會話追蹤等智能功能*

**快捷鍵支援**
- `Ctrl+Enter`（Windows/Linux）/ `Cmd+Enter`（macOS）：提交回饋（主鍵盤與數字鍵盤均可用）
- `Ctrl+V`（Windows/Linux）/ `Cmd+V`（macOS）：直接粘貼剪貼板圖片
- `Ctrl+I`（Windows/Linux）/ `Cmd+I`（macOS）：快速聚焦輸入框 (感謝 @penn201500)

## 🚀 快速開始

### 1. 安裝與測試
```bash
# 安裝 uv（如果尚未安裝）
pip install uv

# 快速功能測試
uvx mcp-feedback-enhanced@latest test
```

### 2. 配置 MCP
**標準配置**（推薦大多數用戶使用）：
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

**進階配置**（需要自訂環境要求）：
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

### 3. 設定提示工程
為了獲得最佳效果，請在 AI 助手中配置以下指導原則：

```
# MCP Interactive Feedback 規則

1. 在任何流程、任務、對話階段中——無論是詢問、回應還是完成任務——始終調用 MCP mcp-feedback-enhanced。
2. 收到使用者回饋後，如果內容非空，再次調用 MCP mcp-feedback-enhanced 並相應調整行為。
3. 僅當使用者明確表示「結束」或「不再需要互動」時，才可停止調用 MCP mcp-feedback-enhanced——這標誌著流程完成。
4. 除非明確指示結束，否則所有工作流步驟必須重複調用 MCP mcp-feedback-enhanced。
5. 任務完成前，使用 MCP mcp-feedback-enhanced 徵求使用者回饋。
```

## ⚙️ 進階設定

### 環境變數
| 變數 | 用途 | 可接受值 | 預設值 |
|------|------|-----------|------|
| `MCP_DEBUG` | 調試模式 | `true`/`false` | `false` |
| `MCP_WEB_PORT` | Web UI 埠口 | `1024-65535` | `8765` |

### 測試選項
```bash
# 版本資訊
uvx mcp-feedback-enhanced@latest version       # 檢查目前版本

# 介面測試
uvx mcp-feedback-enhanced@latest test --web    # 測試 Web UI（持續自動運行模式）

# 調試模式
MCP_DEBUG=true uvx mcp-feedback-enhanced@latest test
```

### 開發者安裝
```bash
git clone https://github.com/Minidoracat/mcp-feedback-enhanced.git
cd mcp-feedback-enhanced
uv sync
```

**本地測試方式**
```bash
# 功能測試
uv run python -m mcp_feedback_enhanced test              # 標準功能測試
uvx --with-editable . mcp-feedback-enhanced test --web   # Web UI 測試（持續運行模式）

# 單元測試
make test                                                # 執行所有單元測試
make test-fast                                          # 快速測試（排除慢速測試）
make test-cov                                           # 測試並生成覆蓋率報告

# 代碼品質保證
make check                                              # 全面代碼品質驗證
make quick-check                                        # 快速驗證並自動修復
```

**測試說明**
- **功能測試**：驗證 MCP 工具的完整功能工作流程
- **單元測試**：測試各個模組的獨立功能
- **覆蓋率測試**：生成全面的 HTML 覆蓋率報告到 `htmlcov/` 目錄
- **品質保證**：包含全面的 linting、格式化和類型檢查


## 🆕 版本更新記錄

📋 **完整版本更新記錄：** [RELEASE_NOTES/CHANGELOG.zh-TW.md](RELEASE_NOTES/CHANGELOG.zh-TW.md)

### 最新版本亮點（v2.4.0）
- 🏗️ **Web-Only 架構重構**: 彻底移除 PyQt6 GUI 依賴，迁移至純 Web UI 架構，大幅簡化部署流程
- 📝 **智能提示詞管理**: 新增完整的提示詞 CRUD 系統，支援使用統計和智能排序
- ⏰ **自動定時提交**: 可配置倒數計時器，與提示詞管理深度整合
- 📊 **高級會話管理**: 即時會話監控、全面歷史追蹤和詳細統計分析
- 🔗 **連線監控增強**: 高級 WebSocket 連線監控，包含延遲測量和智能自動重連
- 🎨 **全面 UI/UX 增強**: 現代化會話面板、響應式設計原則和統一視覺美學
- 🌐 **多語言系統改進**: 優化語言切換機制，增強本地化覆蓋率
- 🛠️ **技術架構現代化**: 完整 JavaScript 模組化，採用當代開發模式

## 🐛 常見問題

### 🌐 SSH Remote 環境問題
**Q: SSH Remote 環境下瀏覽器無法啟動**
A: 這是預期行為。SSH Remote 環境缺乏圖形界面，需要手動通過本地機器訪問瀏覽器。詳細解決方案請參考：[SSH Remote 環境使用指南](docs/zh-TW/ssh-remote/browser-launch-issues.md)

**Q: 為什麼沒有接收到 MCP 新的反饋？**
A: 這通常表示 WebSocket 連接問題。**解決方法**：直接刷新瀏覽器頁面以重新建立連接。

**Q: 為什麼沒有呼叫出 MCP？**
A: 請驗證 MCP 工具狀態顯示為綠色指示器。**解決方法**：反覆開關 MCP 工具，等待幾秒讓系統重新連接。

**Q: Augment 無法啟動 MCP**
A: **解決方法**：完全關闉並重新啟動 VS Code 或 Cursor，重新開啟專案以重置 MCP 連接。

### 🔧 一般問題
**Q: 如何使用舊版 GUI 介面？**
A: v2.4.0 版本已完全移除 PyQt6 GUI 依賴，轉為純 Web UI 架構。如需使用舊版 GUI，請指定 v2.3.0 或更早版本：
```bash
# 使用 v2.3.0（最後支援 GUI 的版本）
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
**注意**：舊版本不包含 v2.4.0 的新功能（提示詞管理、自動提交、會話管理等）。

**Q: 出現 "Unexpected token 'D'" 錯誤**
A: 這源於調試輸出干擾。設置 `MCP_DEBUG=false` 或完全移除該環境變數。

**Q: 中文字符編碼問題**
A: 已在 v2.0.3 解決。更新到最新版本：`uvx mcp-feedback-enhanced@latest`

**Q: 多螢幕環境下視窗定位問題**
A: 已在 v2.1.1 修復。進入「⚙️ 設定」分頁，啟用「總是在主螢幕中心顯示視窗」即可解決。特別適用於 T 字型螢幕排列等複雜多螢幕配置。

**Q: 圖片上傳失敗**
A: 驗證檔案格式相容性（PNG/JPG/JPEG/GIF/BMP/WebP）。系統支援任意大小的圖片檔案並智能處理。

**Q: Web UI 啟動失敗**
A: 檢查防火牆配置或嘗試使用不同的埠口。

**Q: UV Cache 佔用過多磁碟空間**
A: 由於頻繁使用 `uvx` 命令，cache 可能會累積到數十 GB。建議定期維護：
```bash
# 分析 cache 大小和詳細資訊
python scripts/cleanup_cache.py --size

# 預覽清理操作（不實際執行）
python scripts/cleanup_cache.py --dry-run

# 執行標準清理
python scripts/cleanup_cache.py --clean

# 強制清理（嘗試終止進程，解決 Windows 檔案鎖定問題）
python scripts/cleanup_cache.py --force

# 直接 uv 命令替代方案
uv cache clean
```
全面說明請參考：[Cache 管理指南](docs/zh-TW/cache-management.md)

**Q: AI 模型無法解析圖片**
A: 各種 AI 模型（包括 Gemini Pro 2.5、Claude 等）在圖片解析上呈現不一致的性能，有時成功識別內容，有時完全失敗。這代表 AI 視覺理解技術的已知限制。建議：
1. 確保最优圖片品質（高對比度、清晰文字）
2. 嘗試多次上傳；重複嘗試通常能成功
3. 如果解析一直失敗，嘗試不同的圖片尺寸或格式

## 🙏 致謝

### 🌟 支持原作者
**Fábio Ferreira** - [X @fabiomlferreira](https://x.com/fabiomlferreira)
**原始專案：** [noopstudios/interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)

如果您覺得有用，請：
- ⭐ [為原專案按星星](https://github.com/noopstudios/interactive-feedback-mcp)
- 📱 [關注原作者](https://x.com/fabiomlferreira)

### 設計靈感
**sanshao85** - [mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)

### 貢獻者
**penn201500** - [GitHub @penn201500](https://github.com/penn201500)
- 🎯 自動聚焦輸入框功能 ([PR #39](https://github.com/Minidoracat/mcp-feedback-enhanced/pull/39))

### 社群支援
- **Discord：** [https://discord.gg/Gur2V67](https://discord.gg/Gur2V67)
- **Issues：** [GitHub Issues](https://github.com/Minidoracat/mcp-feedback-enhanced/issues)

## 📄 授權

MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

---
**🌟 歡迎 Star 並分享給更多開發者！**
