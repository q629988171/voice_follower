# voice_follower
这是一个小小的Python脚本，可以和OBS通讯把现在麦克风音量作为信息传给我们的程序。我们的程序根据麦克风音量去动态调节人声音量。

## 开始之前

### OBS

你需要[OBS](https://obsproject.com/)。请确保在OBS中开启WebSocket服务器。

### Python requirements

建议大家在[虚拟环境](https://docs.python.org/zh-cn/3/library/venv.html)中工作

```
python -m venv venv
source venv/bin/activate
```

最简单的方式：

```
pip install -r requirements.txt
```

### 人声分离

这个脚本并不能帮你做人声分离，你需要用其他的软件或者库来完成这件事。

* [Ultimate Vocal Remover](https://ultimatevocalremover.com/) 是目前我用过效果最好的软件，免费
* [spleeter](https://github.com/deezer/spleeter) 是一个开源的人声分离库

## 使用

你需要准备两个文件

* 音乐文件（.mp3）
* 从音乐文件中分离出人声和伴奏两个部分（.mp3）

接下来我们打开OBS，在来源这里把人声和伴奏导进去。

[演示视频](https://www.bilibili.com/video/BV1ob4y1K7ei)

## 原理说明

那其实这个所谓拉麦或者递麦的效果原理非常简单，它本质就是用麦克风音量作为输入去控制人声的音量，最后我们输出的时候只输出伴奏和人声这两个音轨，不输出真正的麦克风，这样我们的麦克风实际上变成一个调节人声大小的开关。

## LICENSE

Copyright 2023 Tian Gao.

Distrubuted under the terms of the [Apache 2.0 license](https://github.com/q629988171/voice_follower/blob/master/LICENSE)
