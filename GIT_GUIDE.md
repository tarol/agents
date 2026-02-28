# Git 提交指南

## ⚠️ 重要：Xcode 许可协议

你需要先同意 Xcode 许可协议才能使用 Git。请运行：

```bash
sudo xcodebuild -license
```

然后按 `q` 退出，输入 `agree` 同意协议。

## 🚀 快速提交（推荐）

### 方式1：使用自动化脚本

```bash
# 1. 初始化并提交
./git_init.sh

# 2. 添加远程仓库
git remote add origin <你的仓库地址>

# 3. 推送
./git_push.sh
```

### 方式2：手动操作

```bash
# 1. 同意 Xcode 许可（如果需要）
sudo xcodebuild -license

# 2. 初始化 Git
git init

# 3. 添加文件
git add .

# 4. 提交
git commit -m "Initial commit: LangChain agent framework"

# 5. 添加远程仓库
git remote add origin <你的仓库地址>

# 6. 推送
git push -u origin main
```

## 🔒 安全检查清单

在提交前，请确认：

- [ ] `.gitignore` 已正确配置
- [ ] `config/.env` 不在暂存区（包含真实 API Key）
- [ ] `.env` 文件被忽略
- [ ] 运行 `git status` 检查没有敏感文件

### 检查命令

```bash
# 查看将要提交的文件
git status

# 检查 .env 是否被忽略
git check-ignore config/.env .env

# 查看暂存区的差异（确保没有 API Key）
git diff --cached | grep -i "api_key"
```

如果看到真实的 API Key，**立即运行**：
```bash
git reset HEAD <包含API Key的文件>
```

## 📝 提交信息建议

```bash
git commit -m "Initial commit: LangChain agent framework

- 模块化项目结构 (src/agents, src/skills, src/utils)
- 支持多种 AI 模型 (DeepSeek/Claude/GPT/Gemini)
- 可扩展的技能系统
- 完整的示例和文档
- 工厂模式创建代理
- 统一配置管理"
```

## 🌐 常见 Git 仓库地址格式

### GitHub
```bash
# HTTPS
git remote add origin https://github.com/username/repo-name.git

# SSH
git remote add origin git@github.com:username/repo-name.git
```

### GitLab
```bash
git remote add origin https://gitlab.com/username/repo-name.git
```

### Gitee (码云)
```bash
git remote add origin https://gitee.com/username/repo-name.git
```

## 🔄 推送到远程

### 首次推送
```bash
git push -u origin main
```

### 如果远程分支是 master
```bash
git push -u origin master
```

### 如果远程已有内容
```bash
# 先拉取
git pull origin main --allow-unrelated-histories

# 解决冲突后推送
git push -u origin main
```

## 📋 已忽略的文件

以下文件/目录已通过 `.gitignore` 忽略：

- ✅ `.env` - 环境变量（包含 API Key）
- ✅ `config/.env` - 配置文件
- ✅ `__pycache__/` - Python 缓存
- ✅ `*.pyc` - 编译的 Python 文件
- ✅ `.vscode/`, `.idea/` - IDE 配置
- ✅ `.DS_Store` - macOS 系统文件
- ✅ `*.key`, `*.secret` - 敏感文件

## ✅ 将要提交的文件

核心代码：
- `src/` - 所有源代码模块
- `examples/` - 示例代码
- `docs/` - 文档

配置和说明：
- `requirements.txt` - 依赖列表
- `README_NEW.md` - 项目说明
- `MIGRATION.md` - 迁移指南
- `.env.example` - 环境变量示例（不含真实 Key）
- `.gitignore` - Git 忽略规则

入口文件：
- `main_new.py` - 新版主程序

旧文件（可选）：
- `main.py`, `deepseek_example.py` 等

## ❌ 绝对不要提交

- ❌ `config/.env` - 包含真实 API Key
- ❌ `.env` - 任何环境变量文件
- ❌ 任何包含 `sk-` 开头的 API Key 的文件

## 🆘 紧急情况：如果不小心提交了 API Key

### 如果还未推送到远程
```bash
# 撤销最后一次提交（保留更改）
git reset --soft HEAD~1

# 移除敏感文件
git reset HEAD config/.env

# 重新提交
git commit -m "你的提交信息"
```

### 如果已推送到远程
```bash
# 1. 立即更改你的 API Key（最重要！）

# 2. 从历史记录中删除敏感文件
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch config/.env" \
  --prune-empty --tag-name-filter cat -- --all

# 3. 强制推送（谨慎！）
git push origin --force --all
```

## 📞 获取仓库地址

### 在 GitHub 上创建新仓库

1. 访问 https://github.com/new
2. 输入仓库名称（如 `langchain-agent`）
3. 选择 Public 或 Private
4. 不要初始化 README（因为本地已有）
5. 创建后，GitHub 会显示仓库地址

### 在 Gitee 上创建新仓库

1. 访问 https://gitee.com/projects/new
2. 输入仓库名称
3. 选择开源或私有
4. 创建后复制仓库地址

## 💡 提示

1. **首次提交**：确保没有敏感信息
2. **API Key 管理**：使用 `.env.example` 作为模板
3. **定期备份**：重要代码及时推送
4. **分支管理**：考虑使用 `develop` 分支开发

## 🎉 完成后

提交成功后，你的仓库应该包含：
- ✅ 完整的项目代码
- ✅ 模块化的目录结构
- ✅ 详细的文档
- ✅ 实用的示例
- ❌ 没有任何敏感信息

现在可以分享你的仓库链接了！🚀
