
## TODO List
1. 支持MuQ-Mulan
2. 支持Transcriptor


## 环境配置

0. 克隆仓库

`git clone https://github.com/Music-Foundation-Models/release-test.git`
`cd release-test`

1. 安装依赖

一些依赖包，我还没整理，不过大火的开发机器上应该都能跑起来的，我用的是uniaudio_ydc_llm这个镜像里面的uniaudio2环境。
`conda activate uniaudio2`

2. 下载模型参数

`modelscope download --model 'iStardust/heartmula-gen-tmp' --local_dir './checkpoint'`

## 本地推理

`bash run.sh`

参数：

`--model_path` 下载的模型文件夹路径，默认`./checkpoint`

`--lyrics` 歌词txt文件路径，默认`./samples/lyrics.txt`

`--tags` 标签txt文件路径，默认`./samples/tags.txt`

`--save_path` 输出wav文件路径，默认`./samples/result.wav`

`--topk` 采样时的topk

`--temperature` 采样时的temperature

`--cfg_scale` 采样时的cfg_scale

`--max_audio_length_ms` 最大音频长度（毫秒）



