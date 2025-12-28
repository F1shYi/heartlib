
## 环境配置

1. 安装依赖

2. 下载模型参数

`modelscope download --model 'iStardust/heartmula-gen-tmp' --local_dir './checkpoint'`

## 推理

`bash run.sh`

参数：

`--lyrics` 歌词txt文件路径

`--tags` 标签txt文件路径

`--save_path` 输出wav文件路径

`--topk` 采样时的topk

`--temperature` 采样时的temperature

`--cfg_scale` 采样时的cfg_scale

`--max_audio_length_ms` 最大音频长度（毫秒）



