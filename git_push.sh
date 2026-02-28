#!/bin/bash
# 快速推送到远程仓库脚本

echo "=========================================="
echo "Git 推送脚本"
echo "=========================================="
echo ""

# 检查是否已有远程仓库
if git remote | grep -q "origin"; then
    echo "✅ 检测到远程仓库 origin"
    git remote -v
    echo ""
    
    echo "📤 推送到远程仓库..."
    git push -u origin main || git push -u origin master
    
    if [ $? -eq 0 ]; then
        echo "✅ 推送成功！"
    else
        echo "❌ 推送失败，可能需要先拉取远程更改"
        echo "尝试运行: git pull origin main --rebase"
    fi
else
    echo "❌ 错误: 未找到远程仓库"
    echo ""
    echo "请先添加远程仓库："
    echo "  git remote add origin <你的仓库地址>"
    echo ""
    echo "例如："
    echo "  git remote add origin https://github.com/username/repo.git"
    echo "  或"
    echo "  git remote add origin git@github.com:username/repo.git"
    exit 1
fi
