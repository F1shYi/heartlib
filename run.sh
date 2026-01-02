python demo.py \
    --model_path /turing_music_fs/music_data/ckpts/heartmula-gen/ \
    --lyrics ./samples/lyrics.txt \
    --tags ./samples/tags.txt \
    --save_path ./samples/result.wav \
    --topk 50 \
    --temperature 1.0 \
    --cfg_scale 1.0 \
    --max_audio_length_ms 30_000