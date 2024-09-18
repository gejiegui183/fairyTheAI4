## 搭建Fairy人工智能
> 前期准备：
> 你需要拥有Kimi人工智能的API和GPT-SoVits的Token
> Kimi API获取方法：https://platform.moonshot.cn/console/info
> 获取到Kimi API后请在 ```GPT/GPTPlayGround.py```文件中替换(已标明替换位置)
> GPT-SoVits令牌获取：https://getkey.acgnai.top/ 
> 获取到GPT-SoVits令牌后在 ```TTSService/TTSAudioService.py```文件中替换(已标明替换位置)


> 环境准备：
> 确保你的电脑安装python，且版本>=3.8 若没有请点击[此处](https://www.python.org/downloads/release/python-396/)下载，下载时点击```Windows installer (64-bit)```
> 安装python请查看本篇[博客](https://blog.csdn.net/qq_53280175/article/details/121107748)
> 若觉得不方便调试可以下载[Visual Studio Code代码编辑器](https://visualstudio.microsoft.com/zh-hans/downloads/) 注意是```Visual Studio Code```，不是```Visual Studio```

> Paraformer语音识别模型下载链接: https://pan.baidu.com/s/1cNa8LuYRcAquI4-udnyGog?pwd=3365 提取码: 3365

> 提示：
> 本项目为online版本，使用云端计算资源，对本地设备没有太多需求，按下述步骤执行即可运行该项目


<br>

## 环境搭建
- 创建虚拟环境
在```fairyTheAI4```目录下使用命令行执行以下代码
```bash
python -m venv venv
```

- 安装项目依赖
在```fairyTheAI4```目录下使用命令行执行以下代码
```bash
pip install -r requirements_out_of_pytorch.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 项目运行
```bash
python launch.py
```
在控制台中看到```*```后就可以开始说话，你可以说8秒钟的话。语音输入结束后请耐心等待Fairy的回应。在看到```----------------------```后表示录音结束，Fairy正在回应你，请耐心等待。
