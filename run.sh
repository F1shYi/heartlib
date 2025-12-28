python demo.py \
    --model_path ./checkpoint \
    --lyrics ./samples/lyrics.txt \
    --tags ./samples/tags.txt \
    --save_path ./samples/result.wav \
    --topk 50 \
    --temperature 1.0 \
    --cfg_scale 1.5 \
    --max_audio_length_ms 120_000