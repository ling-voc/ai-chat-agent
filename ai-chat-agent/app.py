from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

MODEL_NAME = os.getenv("MODEL_NAME")

SYSTEM_PROMPT = '''
你是一个高级聊天分析 Agent。

你的任务：
1. 判断聊天氛围
2. 判断双方情绪
3. 分析聊天阶段
4. 判断是否冷场
5. 给出下一句高质量回复建议
6. 分析用户哪里做得不好

输出格式：

【聊天阶段】

【情绪分析】

【冷场风险】

【问题分析】

【推荐回复】

【进阶建议】
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        chat_content = request.form.get('chat')

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"以下是聊天记录：\n\n{chat_content}"
                }
            ],
            temperature=0.8
        )

        result = response.choices[0].message.content

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
