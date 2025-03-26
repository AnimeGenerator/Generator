import os
import shutil

def clean_outputs():
    output_dir = "examples/outputs"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print(f"Cleaned {output_dir}")
    os.makedirs(output_dir)
    print(f"Recreated empty {output_dir}")

if __name__ == "__main__":
    clean_outputs()
