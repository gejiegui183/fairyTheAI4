import pyaudio , wave

class Recorder:
    # def __init__(self):
    #     self.text = None


    def start_recorder(self):
        p = pyaudio.PyAudio()
        # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、输入、采样点缓存数量为2048
        stream = p.open(format=pyaudio.paInt16, channels=2, rate=16000, input=True, frames_per_buffer=4096)
        rec_buf = []
        count = 0
        while count < 8 * 8:
            audio_data = stream.read(2048)  # 读出声卡缓冲区的音频数据
            rec_buf.append(audio_data)  # 将读出的音频数据追加到record_buf列表
            count += 1
            print('*')
        print('----------------------')
        wf = wave.open('ASR/test_wavs/test2.wav', 'wb')  # 创建一个音频文件，名字为“01.wav"
        wf.setnchannels(2)  # 设置声道数为2
        wf.setsampwidth(2)  # 设置采样深度为
        wf.setframerate(16000)  # 设置采样率为16000
        # 将数据写入创建的音频文件
        wf.writeframes("".encode().join(rec_buf))
        # 写完后将文件关闭
        wf.close()


# if __name__ == '__main__':
#     rec = Recorder()
#     rec.start_recorder()





