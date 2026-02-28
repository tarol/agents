#!/bin/bash

# 交互式 Agent 选择器启动脚本

echo "🚀 启动交互式 Agent 选择器..."
echo ""

# 优先使用 Anaconda Python
if [ -f "/opt/anaconda3/bin/python" ]; then
    PYTHON_CMD="/opt/anaconda3/bin/python"
    echo "✅ 使用 Anaconda Python: $PYTHON_CMD"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✅ 使用系统 Python: $PYTHON_CMD"
else
    echo "❌ 错误: 未找到 Python"
    exit 1
fi

# 检查 .env 文件
if [ ! -f .env ]; then
    echo "⚠️  警告: 未找到 .env 文件，请先配置环境变量"
    echo "   可以复制 .env.example 为 .env 并填入 API 密钥"
    exit 1
fi

echo ""
# 运行程序
$PYTHON_CMD main.py
