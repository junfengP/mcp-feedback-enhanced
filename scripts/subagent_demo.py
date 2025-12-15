#!/usr/bin/env python3
"""
Subagent 功能演示腳本
==================

這個腳本展示了 subagent 如何執行 bash 命令並以結構化格式返回結果。

功能展示：
1. 執行簡單的 bash 命令
2. 列出目錄文件
3. 獲取系統信息
4. 返回結構化的執行結果
"""

import json
import subprocess
import sys
from typing import Dict, Any, List, Optional


class SubagentDemo:
    """Subagent 功能演示類"""
    
    def __init__(self):
        """初始化 subagent 演示實例"""
        self.history: List[Dict[str, Any]] = []
    
    def execute_bash_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """
        執行 bash 命令並返回結構化結果
        
        Args:
            command: 要執行的 bash 命令
            timeout: 命令超時時間（秒）
            
        Returns:
            包含執行結果的字典
        """
        result = {
            "command": command,
            "success": False,
            "stdout": "",
            "stderr": "",
            "return_code": None,
            "execution_time": None
        }
        
        try:
            import time
            start_time = time.time()
            
            # 執行命令
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=None  # 使用當前工作目錄
            )
            
            end_time = time.time()
            
            # 填充結果
            result.update({
                "success": process.returncode == 0,
                "stdout": process.stdout,
                "stderr": process.stderr,
                "return_code": process.returncode,
                "execution_time": round(end_time - start_time, 3)
            })
            
        except subprocess.TimeoutExpired:
            result["stderr"] = f"Command timed out after {timeout} seconds"
        except Exception as e:
            result["stderr"] = f"Error executing command: {str(e)}"
        
        # 記錄歷史
        self.history.append(result.copy())
        
        return result
    
    def list_files(self, directory: str = ".", pattern: Optional[str] = None) -> Dict[str, Any]:
        """
        列出目錄中的文件
        
        Args:
            directory: 目標目錄路徑
            pattern: 文件名模式過濾器
            
        Returns:
            包含文件列表的執行結果
        """
        if pattern:
            command = f"ls -la {directory} | grep '{pattern}'"
        else:
            command = f"ls -la {directory}"
            
        return self.execute_bash_command(command)
    
    def get_system_info(self) -> Dict[str, Any]:
        """
        獲取系統基本信息
        
        Returns:
            包含系統信息的執行結果
        """
        commands = [
            "uname -a",           # 系統內核信息
            "uptime",             # 系統運行時間
            "df -h",              # 磁盤使用情況
            "free -h",            # 內存使用情況
            "ps aux | head -10"   # 前10個進程
        ]
        
        results = {}
        for cmd in commands:
            key = cmd.split()[0].replace("-", "_")
            results[key] = self.execute_bash_command(cmd)
            
        return {
            "command": "get_system_info",
            "success": True,
            "data": results,
            "execution_time": sum(r.get("execution_time", 0) for r in results.values())
        }
    
    def run_demo(self) -> None:
        """運行完整的演示"""
        print("🚀 Subagent 功能演示開始\n")
        
        # 1. 執行簡單命令
        print("1. 執行簡單命令: pwd")
        result = self.execute_bash_command("pwd")
        self._print_result(result)
        
        # 2. 列出文件
        print("\n2. 列出當前目錄文件")
        result = self.list_files(".")
        self._print_result(result)
        
        # 3. 執行帶管道的複雜命令
        print("\n3. 查找 Python 文件")
        result = self.execute_bash_command("find . -name '*.py' | head -5")
        self._print_result(result)
        
        # 4. 獲取系統信息
        print("\n4. 獲取系統信息")
        result = self.get_system_info()
        self._print_system_info(result)
        
        # 5. 錯誤處理演示
        print("\n5. 錯誤處理演示")
        result = self.execute_bash_command("invalid_command_that_does_not_exist")
        self._print_result(result)
        
        print("\n✅ 演示完成!")
        print(f"📊 總共執行了 {len(self.history)} 個命令")
    
    def _print_result(self, result: Dict[str, Any]) -> None:
        """打印單個命令執行結果"""
        print(f"  命令: {result['command']}")
        print(f"  成功: {'✅' if result['success'] else '❌'}")
        print(f"  返回碼: {result['return_code']}")
        print(f"  執行時間: {result['execution_time']} 秒")
        
        if result['stdout']:
            print(f"  標準輸出:\n{result['stdout'][:200]}{'...' if len(result['stdout']) > 200 else ''}")
        
        if result['stderr']:
            print(f"  錯誤輸出:\n{result['stderr'][:200]}{'...' if len(result['stderr']) > 200 else ''}")
    
    def _print_system_info(self, result: Dict[str, Any]) -> None:
        """打印系統信息結果"""
        print(f"  命令: {result['command']}")
        print(f"  成功: {'✅' if result['success'] else '❌'}")
        print(f"  執行時間: {result['execution_time']} 秒")
        
        if 'data' in result:
            print("  系統信息:")
            for key, value in result['data'].items():
                status = "✅" if value['success'] else "❌"
                print(f"    {key}: {status} (返回碼: {value['return_code']})")


def main():
    """主函數"""
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        # JSON 輸出模式
        demo = SubagentDemo()
        results = []
        
        # 執行幾個示例命令
        commands = ["pwd", "ls -la", "date", "whoami"]
        for cmd in commands:
            results.append(demo.execute_bash_command(cmd))
        
        # 輸出 JSON 格式結果
        print(json.dumps({
            "results": results,
            "history": demo.history
        }, indent=2, ensure_ascii=False))
    else:
        # 交互式演示模式
        demo = SubagentDemo()
        demo.run_demo()


if __name__ == "__main__":
    main()