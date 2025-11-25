import argparse
import logging
import math
import os
import pathlib
import tensorflow as tf

from utils import criar_patches_verticais

logging.basicConfig(format="\033[32m [%(asctime)s] (%(levelname)s) {%(filename)s %(lineno)d}  %(message)s \033[0m", datefmt="%d/%m/%Y %H:%M:%S", level=logging.INFO)

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--input_dir", type=str, required=True)
    argparser.add_argument("--img_size", type=int, default=256, choices=[256, 400, 512])
    argparser.add_argument("--num_patches", type=int, default=3)
    argparser.add_argument("--output_dir", type=str, default="./output")
    
    args = argparser.parse_args()

    logging.info("Loading images from %s" % args.input_dir)
    logging.info("Output directory is %s" % args.output_dir)

    if not os.path.exists(args.input_dir):
        raise SystemExit("Input directory does not exist")

    extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

    os.makedirs(args.output_dir, exist_ok=True)

    for f in pathlib.Path(args.input_dir).rglob("*"):
        if f.suffix.lower() in extensions:
            patches = criar_patches_verticais(f,  orig_size=(args.img_size, args.img_size), num_patches_y=args.num_patches)
            for idx, p in enumerate(patches, start=1):
                filename = f"{idx:03}+{f.name}"
                filename = os.path.join(args.output_dir, filename)
                print("saving %s" % filename)
                tf.keras.preprocessing.image.save_img(filename, p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
