import sys

from openai import OpenAI
# sys.path.append('../GPT/vits')
import GPT.tune as t

def ask_kimi(askQuestion):
    client = OpenAI(
        api_key="此处换成你自己的Kimi API",  # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
        base_url="https://api.moonshot.cn/v1",
    )

    character_tune = t.get_tune()

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": character_tune},
            {"role": "user", "content": askQuestion}
        ],
        temperature=0.3,
    )

    # 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
    return completion.choices[0].message.content
