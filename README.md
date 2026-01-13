<p align="center">
    <picture>
        <source srcset="./.assets/logo.png" media="(prefers-color-scheme: dark)">
        <img src="./.assets/logo.png" width="40%">
    </picture>
</p>

<p align="center">
    <a href="https://map-yue.github.io/">Demo 🎶</a> &nbsp;|&nbsp; 📑 <a href="https://arxiv.org/abs/2503.08638">Paper</a>
    <br>
    <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot">YuE-s1-7B-anneal-en-cot 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-icl">YuE-s1-7B-anneal-en-icl 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-jp-kr-cot">YuE-s1-7B-anneal-jp-kr-cot 🤗</a>
    <br>
    <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-jp-kr-icl">YuE-s1-7B-anneal-jp-kr-icl 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-zh-cot">YuE-s1-7B-anneal-zh-cot 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/m-a-p/YuE-s1-7B-anneal-zh-icl">YuE-s1-7B-anneal-zh-icl 🤗</a>
    <br>
    <a href="https://huggingface.co/m-a-p/YuE-s2-1B-general">YuE-s2-1B-general 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/m-a-p/YuE-upsampler">YuE-upsampler 🤗</a>
</p>

---
# HeartMuLa: A Family of Open Sourced Music Foundation Models

HeartMuLa is a family of open sourced music foundation models including: 
1. HeartCodec: a 12.5 hz music codec with high reconstruction fidelity;
2. HeartMuLa: a 3B music language model that generates music conditioned on lyrics and tags;
3. HeartTranscriptor: a whisper-based model specifically tuned for lyrics transcription;
4. HeartCLAP: 

This repo accompanies our technical report (url here).

## News & TODOs

Jan. 2026: We are happy to release our first version of HeartMuLa. Happy New Year!

TODOs:

[ ] Release HeartCLAP.

[ ] Support reference audio conditioning.

[√] Release inference code and pretrained checkpoints of HeartCodec, HeartMuLa and HeartTranscriptor.


## Local Deployment

### Environment Setup

Clone this repo and install locally.

```
git clone https://github.com/F1shYi/heartlib.git
cd heartlib
pip install -e .
```

Download our pretrained checkpoints from huggingface or modelscope using the following command:

```
# if you are using huggingface
hf download f1shy1/HeartMuLa --local-dir YOUR-CKPT-CACHE-PATH

# if you are using modelscope
modelscope download --model 'iStardust/heartmula-gen-tmp' --local_dir 'YOUR-CKPT-CACHE-PATH'
```

### Example Usage

To generate music, run:

```
python ./examples/run_music_generation.py --model_path=YOUR-CKPT-CACHE-PATH
```

By default this command will generate a 30-seconds music clip conditioned on lyrics and tags provided in `./assets` folder. The output music will be saved at `./assets/output.wav`. 

All parameters:

- `--model_path` (required): Path to the pretrained model checkpoint
- `--lyrics`: Path to lyrics file (default: `./.assets/lyrics.txt`)
- `--tags`: Path to tags file (default: `./.assets/tags.txt`)
- `--save_path`: Output audio file path (default: `./.assets/output.wav`)
- `--max_audio_length_ms`: Maximum audio length in milliseconds (default: 40000)
- `--topk`: Top-k sampling parameter for generation (default: 50)
- `--temperature`: Sampling temperature for generation (default: 1.0)
- `--cfg_scale`: Classifier-free guidance scale (default: 1.5)

To transcribe lyrics given music file, run:

```
python ./examples/run_lyrics_transcription.py --model_path=YOUR-CKPT-CACHE-PATH
```

By default this command will load the generated music file at `./assets/output.wav` and print the  transcribed lyrics. Use `--music_path` to specify the path to the music file.

Note that our HeartTranscriptor is trained on separated vocal tracks. In this example usage part, we directly demonstrate on unseparated music tracks, which is purely for simplicity of illustration. We recommend using source separation tools like demucs to separate the tracks before transcribing lyrics to achieve better results.

## Acknowledgement

This repository is developed on the basis of [ConversationTTS](https://github.com/Audio-Foundation-Models/ConversationTTS), [SongGeneration](https://github.com/tencent-ailab/SongGeneration), and [Transformers](https://github.com/huggingface/transformers/tree/main). We thank the authors for their open source contributions.


## License & Ethics Statement

This repository is licensed under the **Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0)**.


The music generation model and all associated assets are provided for non-commercial research and educational purposes only. **Any commercial use is strictly prohibited.**

Users are solely responsible for ensuring that the generated content does not infringe upon any third-party copyrights or other intellectual property rights.

## Citation