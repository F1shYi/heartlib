from heartlib.pipelines.lyrics_transcription import HeartTranscriptorPipeline
import torch

if __name__ == "__main__":
    pipe = HeartTranscriptorPipeline.from_pretrained(
        "/turing_music_fs/music_data/ckpts/heartmula-gen/",
        device=torch.device("cuda"),
        dtype=torch.float16,
    )
    result = pipe(
        "/root/code/heartmula_gen/separated/htdemucs/result/vocals.wav",
        **{
            "max_new_tokens": 256,
            "num_beams": 2,
            "task": "transcribe",
            "condition_on_prev_tokens": False,
            "compression_ratio_threshold": 1.8,
            "temperature": (0.0, 0.1, 0.2, 0.4),
            "logprob_threshold": -1.0,
            "no_speech_threshold": 0.4,
        },
    )
    print(result)

    print(result["text"])
