from src.pipelines.music_generation import HeartMuLaGenPipeline
import argparse
import torch


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--lyrics", type=str, required=True)
    parser.add_argument("--tags", type=str, required=True)
    parser.add_argument("--save_path", type=str, required=True)

    parser.add_argument("--max_audio_length_ms", type=int, default=120_000)
    parser.add_argument("--topk", type=int, default=50)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--cfg_scale", type=float, default=1.5)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    pipe = HeartMuLaGenPipeline.from_pretrained(
        args.model_path, torch.device("cuda"), torch.bfloat16
    )
    pipe(
        {
            "lyrics": args.lyrics,
            "tags": args.tags,
        },
        max_audio_length_ms=args.max_audio_length_ms,
        save_path=args.save_path,
        topk=args.topk,
        temperature=args.temperature,
        cfg_scale=args.cfg_scale,
    )
