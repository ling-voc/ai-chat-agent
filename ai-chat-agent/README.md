# AI Chat Analyzer Agent

一个基于 AI Agent Workflow 的聊天分析系统。

## 功能

- 情绪识别
- 聊天阶段判断
- 冷场检测
- AI 回复建议
- 多模型兼容

## 技术栈

- Flask
- OpenAI SDK
- Claude / Gemini API
- Prompt Workflow

## 启动项目

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

打开：

```txt
http://127.0.0.1:5000
```

---

## Agent Workflow

1. 用户上传聊天记录
2. Agent 进行情绪分析
3. Agent 判断聊天阶段
4. Agent 检测冷场风险
5. Agent 自动生成回复策略

---

## 项目亮点

- 多轮上下文分析
- Prompt Routing
- 自动回复生成
- AI Workflow 自动化
- 支持 OpenAI Compatible API
