<p align="center">
    <picture>
        <source srcset="./.assets/logo.png" media="(prefers-color-scheme: dark)">
        <img src="./.assets/logo.png" width="30%">
    </picture>
    
</p>

<p align="center">
    <a href="https://heartmula.github.io/">Demo 🎶</a> &nbsp;|&nbsp; 📑 <a href="">Paper (Coming Soon)</a>
    <br>
    <a href="https://huggingface.co/HeartMuLa/HeartMuLa-oss-7B">HeartMuLa-oss-7B 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B">HeartMuLa-oss-3B 🤗</a>
    <br>
    <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-oss-7B">HeartMuLa-oss-7B <picture>
        <source srcset="./.assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./.assets/badge.svg" width="20px">
    </picture></a> &nbsp;|&nbsp; <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-oss-3B">HeartMuLa-oss-3B <picture>
        <source srcset="./.assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./.assets/badge.svg" width="20px">
    </picture></a>
    
</p>

---
# HeartMuLa: A Family of Open Sourced Music Foundation Models

HeartMuLa is a family of open sourced music foundation models including: 
1. HeartMuLa: a music language model that generates music conditioned on lyrics and tags with multilingual support including but not limited to English, Chinese, Japanese, Korean and Spanish.
2. HeartCodec: a 12.5 hz music codec with high reconstruction fidelity;
3. HeartTranscriptor: a whisper-based model specifically tuned for lyrics transcription;
4. HeartCLAP: an audio–text alignment model that establishes a unified embedding space for music descriptions and cross-modal retrieval.
---

Check [this page](./examples/README.md) for usage of HeartTranscriptor.

Below shows the experiment result of our oss-3B version compared with other baselines.
<p align="center">
    <picture>
        <source srcset="./.assets/exp.png" media="(prefers-color-scheme: dark)">
        <img src="./.assets/exp.png" width="90%">
    </picture>
    
</p>

## 📰 News

- 🚀 **14 Jan. 2026**  
  Our **oss-7B HeartMuLa** is released! Our latest internal version of HeartMuLa achieves **comparable performance with Suno** in terms of musicality, fidelity and controllability. If you are interested, welcome to reach us out via heartmula.ai@gmail.com


  The official release of **HeartTranscriptor**.


  We release the first **oss-3B version of HeartMuLa**.

---
## 🧭 TODOs

- ⏳ Release scripts for inference acceleration.
- ⏳ Release **HeartCLAP**.
- ⏳ Support **reference audio conditioning**.
- ✅ Release inference code and pretrained checkpoints of  
  **HeartCodec-oss, HeartMuLa-oss-3B, HeartMuLa-oss-7B, and HeartTranscriptor**.

---

## 🛠️ Local Deployment

### ⚙️ Environment Setup

We recommend using `python=3.10` for local deployment.

Clone this repo and install locally.

```
git clone xxx
cd heartlib
pip install -e .
```

Download our pretrained checkpoints from huggingface or modelscope using the following command:

```
# if you are using huggingface
hf download --model 'HeartMuLa/HeartMuLaGen' --local_dir 'YOUR-CKPT-CACHE-PATH'
hf download --model 'HeartMuLa/HeartMuLa-3B-oss' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-oss-3B'
hf download --model 'HeartMuLa/HeartMuLa-7B-oss' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-oss-7B'
hf download --model 'HeartMuLa/HeartCodec-oss' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartCodec-oss'

# if you are using modelscope
modelscope download --model 'HeartMuLa/HeartMuLaGen' --local_dir 'YOUR-CKPT-CACHE-PATH'
modelscope download --model 'HeartMuLa/HeartMuLa-oss-3B' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-oss-3B'
modelscope download --model 'HeartMuLa/HeartMuLa-oss-7B' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-oss-7B'
modelscope download --model 'HeartMuLa/HeartCodec-oss' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartCodec-oss'
```

After downloading, the folder where checkpoints are saved should structured like this:
```
YOUR-CKPT-CACHE-PATH/
├── HeartCodec-oss/
├── HeartMuLa-oss-3B/
├── HeartMuLa-oss-7B/
├── gen_config.json
└── tokenizer.json
```


### ▶️ Example Usage

To generate music, run:

```
python ./examples/run_music_generation.py --model_path=YOUR-CKPT-CACHE-PATH --version="3B"
```

By default this command will generate a piece of music conditioned on lyrics and tags provided in `./assets` folder. The output music will be saved at `./assets/output.wav`. The current generation speed is about RTF=1.0 (i.e. it takes around 90 seconds to generate a 90-seconds song), and the inference acceleration support will be released in the future.

All parameters:

- `--model_path` (required): Path to the pretrained model checkpoint
- `--lyrics`: Path to lyrics file (default: `./.assets/lyrics.txt`)
- `--tags`: Path to tags file (default: `./.assets/tags.txt`)
- `--save_path`: Output audio file path (default: `./.assets/output.wav`)
- `--max_audio_length_ms`: Maximum audio length in milliseconds (default: 240000)
- `--topk`: Top-k sampling parameter for generation (default: 50)
- `--temperature`: Sampling temperature for generation (default: 1.0)
- `--cfg_scale`: Classifier-free guidance scale (default: 1.5)
- `--version`: The version of HeartMuLa, choose between [`3B`, `7B`]. (default: `3B`)

Recommended format of lyrics and tags:
```txt
[Intro]

[Verse]
The sun creeps in across the floor
I hear the traffic outside the door
The coffee pot begins to hiss
It is another morning just like this

[Prechorus]
The world keeps spinning round and round
Feet are planted on the ground
I find my rhythm in the sound

[Chorus]
Every day the light returns
Every day the fire burns
We keep on walking down this street
Moving to the same steady beat
It is the ordinary magic that we meet

[Verse]
The hours tick deeply into noon
Chasing shadows,chasing the moon
Work is done and the lights go low
Watching the city start to glow

[Bridge]
It is not always easy,not always bright
Sometimes we wrestle with the night
But we make it to the morning light

[Chorus]
Every day the light returns
Every day the fire burns
We keep on walking down this street
Moving to the same steady beat

[Outro]
Just another day
Every single day
```

Our different tags are comma-separated without spaces as illustrated below:
```txt
piano,happy,wedding,synthesizer,romantic
```

## 🙏 Acknowledgements

This repository is developed on the basis of [ConversationTTS](https://github.com/Audio-Foundation-Models/ConversationTTS). We thank the authors for their open source contributions.

## ⚖️ License & Ethics Statement

This repository is licensed under the
Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0).

🔒 For non-commercial research and educational use only

🚫 Any commercial use is strictly prohibited

⚠️ Users are solely responsible for ensuring that generated content does not infringe any third-party copyrights


## 📚 Citation

```
@article{heartmula2026,
  author    = {HeartMuLa Teams},
  title     = {HeartMuLa: A Family of Open Sourced Music Foundation Models},
  journal   = {arXiv preprint},
  year      = {2026},
}
```

## 📬 Contact
If you are interested in HeartMuLa, feel free to reach us at heartmula.ai@gmail.com