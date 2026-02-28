#!/bin/bash
# Git 初始化和提交脚本

echo "=========================================="
echo "LangChain 项目 Git 初始化脚本"
echo "=========================================="
echo ""

# 检查是否在项目目录
if [ ! -f "requirements.txt" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 1. 初始化 Git 仓库
echo "📦 步骤 1: 初始化 Git 仓库..."
if [ -d ".git" ]; then
    echo "✅ Git 仓库已存在"
else
    git init
    echo "✅ Git 仓库初始化完成"
fi
echo ""

# 2. 检查敏感文件是否被忽略
echo "🔒 步骤 2: 检查敏感文件..."
if git check-ignore -q config/.env; then
    echo "✅ config/.env 已被忽略"
else
    echo "⚠️  警告: config/.env 可能会被提交！"
fi

if git check-ignore -q .env; then
    echo "✅ .env 已被忽略"
else
    echo "⚠️  警告: .env 可能会被提交！"
fi
echo ""

# 3. 清理 config/.env 中的真实 API Key
echo "🧹 步骤 3: 清理配置文件..."
if [ -f "config/.env" ]; then
    echo "⚠️  检测到 config/.env 包含真实 API Key"
    echo "请确认是否已备份，然后我们将创建一个示例文件"
    # 不自动修改，只提醒
fi
echo ""

# 4. 添加文件
echo "➕ 步骤 4: 添加文件到暂存区..."
git add .gitignore
git add requirements.txt
git add README_NEW.md
git add MIGRATION.md
git add .env.example
git add src/
git add examples/
git add docs/
git add main_new.py

# 添加保留的旧文件（可选）
git add main.py
git add deepseek_example.py
git add custom_tools.py
git add multi_model_example.py
git add skills_tutorial.py
git add my_custom_skills.py
git add streaming_example.py

echo "✅ 文件已添加到暂存区"
echo ""

# 5. 显示将要提交的文件
echo "📋 步骤 5: 将要提交的文件:"
git status --short
echo ""

# 6. 检查是否有敏感信息
echo "🔍 步骤 6: 检查敏感信息..."
if git diff --cached | grep -i "api_key.*sk-" > /dev/null; then
    echo "❌ 警告: 检测到可能的 API Key！请检查！"
    echo "运行: git diff --cached | grep -i 'api_key'"
    exit 1
else
    echo "✅ 未检测到明显的 API Key"
fi
echo ""

# 7. 提交
echo "💾 步骤 7: 创建提交..."
git commit -m "Initial commit: LangChain agent framework

- 模块化项目结构
- 支持多种 AI 模型 (DeepSeek/Claude/GPT/Gemini)
- 可扩展的技能系统
- 完整的示例和文档
- 工厂模式创建代理
- 统一配置管理

Features:
- Basic skills: weather, calculator, search
- Advanced skills: time, reminders, file operations
- Agent factory for easy agent creation
- Comprehensive documentation and examples"

echo "✅ 提交完成"
echo ""

# 8. 显示当前状态
echo "📊 步骤 8: 当前状态"
git log --oneline -1
git status
echo ""

# 9. 提示添加远程仓库
echo "=========================================="
echo "✅ 本地 Git 初始化完成！"
echo "=========================================="
echo ""
echo "下一步操作："
echo ""
echo "1️⃣  添加远程仓库:"
echo "   git remote add origin <你的仓库地址>"
echo ""
echo "2️⃣  推送到远程:"
echo "   git push -u origin main"
echo ""
echo "   或者（如果是 master 分支）:"
echo "   git push -u origin master"
echo ""
echo "3️⃣  如果远程已有文件，可能需要先拉取:"
echo "   git pull origin main --allow-unrelated-histories"
echo ""
echo "=========================================="
echo "⚠️  重要提醒:"
echo "请确保 config/.env 文件不在仓库中！"
echo "运行: git status"
echo "如果看到 config/.env，说明它可能会被提交！"
echo "=========================================="
