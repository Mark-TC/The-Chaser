# 笑话生成器 - Joke Generator

这是我在 **The Chaser** 学习之旅中的第一个编程项目！

## 📖 项目介绍

这是一个简单的 Python 程序，使用外部 API 获取随机笑话并展示给用户。

**学到的知识：**
- ✅ 如何调用外部 API
- ✅ 如何处理 JSON 数据
- ✅ 基本的 Python 编程概念
- ✅ 如何使用条件判断和循环

## 🚀 快速开始

### 前提条件
- 安装了 Python 3.6 或更高版本
- 安装了 `requests` 库

### 安装依赖

```bash
pip install requests
```

### 运行程序

```bash
python joke_generator.py
```

## 📝 使用说明

1. 运行程序后，你会看到欢迎信息
2. 按 **Enter** 键获取一个随机笑话
3. 输入 **q** 然后按 Enter 退出程序

## 🔍 代码讲解

### 关键概念：

**1. 导入库**
```python
import requests  # 用来发送网络请求
import json      # 用来处理 JSON 数据
```

**2. 函数 (Function)**
- `get_random_joke()` - 获取笑话的函数
- `main()` - ��程序函数

**3. API 调用**
```python
response = requests.get(url)  # 从网络获取数据
```

**4. 错误处理**
使用 `try-except` 来处理可能出现的错误

**5. 循环 (Loop)**
```python
while True:  # 不断循环，直到用户输入 'q'
```

## 🎨 API 信息

使用的是 **JokeAPI** - 一个完全免费的笑话 API
- 网址: https://official-joke-api.appspot.com/
- 无需密钥
- 支持多种类型的笑话

## 💡 学习收获

通过这个项目，我学会了：
1. 如何使用 Python 的 `requests` 库
2. 如何调用 REST API
3. 如何解析 JSON 数据
4. 如何处理网络错误
5. 如何编写清晰、有注释的代码

## 🎯 下一步改进

- [ ] 添加笑话类型过滤
- [ ] 保存喜欢的笑话
- [ ] 翻译笑话成中文
- [ ] 创建图形界面 (GUI)
- [ ] 添加更多 API 来源

## 📚 推荐学习资源

- [Python 官方文档](https://docs.python.org/3/)
- [Requests 库文档](https://requests.readthedocs.io/)
- [REST API 概念](https://restfulapi.net/)

---

**项目开始日期：** 2026-05-11  
**难度等��：** ⭐ 初级  
**完成度：** ✅ 100%

*这是我编程之旅的第一步。感谢你的支持！* 🚀
