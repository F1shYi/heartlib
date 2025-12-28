python demo.py \
    --model_path ./checkpoint \
    --lyrics ./heartmula_gen/samples/lyrics.txt \
    --tags ./heartmula_gen/samples/tags.txt \
    --save_path ./heartmula_gen/samples/result.wav \
    --topk 50 \
    --temperature 1.0 \
    --cfg_scale 1.5 \
    --max_audio_length_ms 120_000