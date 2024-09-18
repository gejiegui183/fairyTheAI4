from numba import char
import ASR.ASRService as asr
import GPT.GPTPlayGround as gpt
import TTSService.TTSAudioService as tts
import requests
import pygame
from io import BytesIO
import logging
import REC.Recorder as audio_rec
import os

class fairy:

    def __init__(self):
        self.name = None

    def record(self):
        rec = audio_rec.Recorder()
        rec.start_recorder()
        self.audio_to_text()

    def audio_to_text(self):
        config_path = 'ASR/resources/config.yaml'
        service = asr.ASRService(config_path)
        wav_path = 'ASR/test_wavs/test2.wav'
        logging.info('audio to text finished')
        self.gpt_asking(service.infer(wav_path))

    def gpt_asking(self , audio_text):
        os.remove('ASR/test_wavs/test2.wav')
        gpt_ans = gpt.ask_kimi(askQuestion=audio_text)
        logging.info('gpt ans is getted' % char)
        self.speak(gpt_ans)

    def speak(self , ans):
        tts.get_char_list(ans)
        logging.info('tts audio url is getted')
        self.get_audio_back(tts.get_char_list(ans)["audio"] , ans)

    def get_audio_back(self , audio_url , ans):
        pygame.init()
        audio_path = f"{audio_url}"  # 获取音频地址
        resp = requests.get(audio_path)  # 获取二进制数据
        audio_data = BytesIO(resp.content)  # 转化为音频流
        pygame.mixer.music.load(audio_data)  # 加载音频流
        print('fairy say:' , ans)
        pygame.mixer.music.play()  # 播放音频
        while pygame.mixer.music.get_busy():  # 确保完全读完，不间断
            continue


    def lunc_func(self):
        self.record()


if __name__ == '__main__':
    launch = fairy()
    launch.lunc_func()
