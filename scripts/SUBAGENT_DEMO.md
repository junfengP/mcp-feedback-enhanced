# Subagent 功能演示

這個演示展示了 subagent 如何執行 bash 命令並以結構化格式返回結果。

## 功能特性

1. **Bash 命令執行**: 安全地執行任意 bash 命令
2. **結構化結果**: 所有命令執行結果都以統一的 JSON 格式返回
3. **錯誤處理**: 完善的錯誤處理機制
4. **超時控制**: 可設置命令執行超時時間
5. **歷史記錄**: 自動記錄所有執行過的命令和結果

## 使用方法

### 互動式演示

```bash
python3 scripts/subagent_demo.py
```

這將運行一個完整的演示，展示各種功能：

1. 執行簡單命令 (如 `pwd`)
2. 列出目錄文件
3. 執行複雜命令 (帶管道)
4. 獲取系統信息
5. 錯誤處理演示

### JSON 輸出模式

```bash
python3 scripts/subagent_demo.py --json
```

這會以 JSON 格式輸出結果，便於程序解析。

## API 說明

### 主要方法

- `execute_bash_command(command, timeout=30)`: 執行 bash 命令
- `list_files(directory=".", pattern=None)`: 列出目錄文件
- `get_system_info()`: 獲取系統基本信息

### 返回格式

所有方法都返回統一格式的字典：

```json
{
  "command": "執行的命令",
  "success": true/false,
  "stdout": "標準輸出內容",
  "stderr": "錯誤輸出內容",
  "return_code": 0,
  "execution_time": 0.123
}
```

### 結構化數據

對於複合操作（如獲取系統信息），會返回嵌套的結構化數據：

```json
{
  "command": "get_system_info",
  "success": true,
  "data": {
    "uname": {...},
    "uptime": {...},
    // 更多系統信息
  }
}
```