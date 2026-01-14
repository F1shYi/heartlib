<p align="center">
    <picture>
        <source srcset="./.assets/logo.png" media="(prefers-color-scheme: dark)">
        <img src="./.assets/logo.png" width="80%">
    </picture>
    
</p>

<p align="center">
    <a href="https://heartmula.github.io/">Demo 🎶</a> &nbsp;|&nbsp; 📑 <a href="">Paper</a>
    <br>
    <a href="">HeartMuLa-7B 🤗</a> &nbsp;|&nbsp; <a href="">HeartMuLa-3B 🤗</a>
    <br>
    <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-7B">HeartMuLa-7B <picture>
        <source srcset="./.assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./.assets/badge.svg" width="20px">
    </picture></a> &nbsp;|&nbsp; <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-3B">HeartMuLa-3B <picture>
        <source srcset="./.assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./.assets/badge.svg" width="20px">
    </picture></a>
    
</p>

---
# HeartMuLa: A Family of Open Sourced Music Foundation Models

HeartMuLa is a family of open sourced music foundation models including: 
1. HeartCodec: a 12.5 hz music codec with high reconstruction fidelity;
2. HeartMuLa: a music language model that generates music conditioned on lyrics and tags with multilingual support including but not limited to English, Chinese, Japanese, Korean and Spanish.
3. HeartTranscriptor: a whisper-based model specifically tuned for lyrics transcription;
4. HeartCLAP: an audio–text alignment model that establishes a unified embedding space for music descriptions and cross-modal retrieval.


---

Check [this page](./examples/README.md) for usage of HeartTranscriptor.

## 📰 News

- 🚀 **14 Jan. 2026**  
  Our **7B HeartMuLa** achieves performance **comparable to Suno**.  

- 🎉 **14 Jan. 2026**  
  The official release of **HeartTranscriptor**.

- 🎄 **14 Jan. 2026**  
  We release the first **3B version of HeartMuLa**.

---
## 🧭 TODOs

- ⏳ Release **HeartCLAP**
- ⏳ Support **reference audio conditioning**
- ✅ Release inference code and pretrained checkpoints of  
  **HeartCodec, HeartMuLa-3B, HeartMuLa-7B, and HeartTranscriptor**

---

## 🛠️ Local Deployment

### ⚙️ Environment Setup

Clone this repo and install locally.

```
git clone xxx
cd heartlib
pip install -e .
```

Download our pretrained checkpoints from huggingface or modelscope using the following command:

```
# if you are using huggingface
hf download f1shy1/HeartMuLa --local-dir YOUR-CKPT-CACHE-PATH

# if you are using modelscope
modelscope download --model 'HeartMuLa/HeartMuLaGen' --local_dir 'YOUR-CKPT-CACHE-PATH'
modelscope download --model 'HeartMuLa/HeartMuLa-3B' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-3B'
modelscope download --model 'HeartMuLa/HeartMuLa-7B' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartMuLa-7B'
modelscope download --model 'HeartMuLa/HeartCodec' --local_dir 'YOUR-CKPT-CACHE-PATH/HeartCodec'
```

### ▶️ Example Usage

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

```txt
Heartbreak,Strings,Ballad,synthesizer,Piano,Alone
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