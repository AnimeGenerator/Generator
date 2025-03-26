
#### `src/main.py`
```python
import argparse
from generator import AnimeGenerator
from utils.logger import setup_logger
from utils.config import load_config

def parse_args():
    parser = argparse.ArgumentParser(description="Generate anime-style images from prompts")
    parser.add_argument("--prompt", required=True, help="Description of the anime character")
    parser.add_argument("--style", default="shonen", help="Anime style (shonen, shoujo, etc.)")
    parser.add_argument("--resolution", default="512x512", help="Output resolution")
    parser.add_argument("--output", default="output.png", help="Output file name")
    return parser.parse_args()

def main():
    logger = setup_logger()
    config = load_config()
    
    args = parse_args()
    logger.info(f"Starting generation with prompt: {args.prompt}")
    
    try:
        generator = AnimeGenerator(config)
        generator.generate(
            prompt=args.prompt,
            style=args.style,
            resolution=args.resolution,
            output_path=args.output
        )
        logger.info(f"Image generated successfully at {args.output}")
    except Exception as e:
        logger.error(f"Generation failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
