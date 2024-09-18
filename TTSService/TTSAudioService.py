import requests
from sympy import true


url = 'https://infer.acgnai.top/infer/gen'
token_info = '此处换成你的Token令牌'
headers = {'Content-type':'application/json'}


def get_char_list(char):
    data = {
    "access_token": token_info,
    "type": "tts",
    "brand": "gpt-sovits",
    "name": "anime",
    "method": "api",
    "prarm": {
        "speaker": "Fairy【绝区零】",
        "emotion": "中立_neutral",
        "text": f"{char}",
        "text_language":"中英混合",
        "text_split_method": "按标点符号切",
        "fragment_interval": 0.3,
        "batch_size": 1,
        "batch_threshold": 0.75,
        "parallel_infer": "true",
        "split_bucket": "true",
        "top_k": 10,
        "top_p": 1.0,
        "temperature": 1.0,
        "speed_factor": 1.0
        }
    }
    response = requests.post(url , json=data , headers=headers)
    return response.json()

#
# if __name__ == '__main__':
#     service = TTSService()
#     service.get_char_list('我是三型总序式集成泛用人工智能，开发代号:Fairy。')