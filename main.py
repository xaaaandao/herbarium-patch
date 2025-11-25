import argparse
import logging
import math
import os
import pathlib
import tensorflow as tf

logging.basicConfig(format="\033[32m [%(asctime)s] (%(levelname)s) {%(filename)s %(lineno)d}  %(message)s \033[0m", datefmt="%d/%m/%Y %H:%M:%S", level=logging.INFO)

def next_patch_horizontal(spec: int, n: int):
    """
    Retorna a posição do próximo corte na imagem.
    :param spec: é a altura da imagem.
    :param n: é o número de divisões que serão feitas na imagem.
    """
    step = math.floor(spec.shape[0] / n)
    for i in range(n):
        yield spec[i * step:(i + 1) * step, :, :]


def next_patch_vertical(spec: int, n: int):
    """
    Retorna a posição do próximo corte na imagem.
    :param spec: é a altura da imagem.
    :param n: é o número de divisões que serão feitas na imagem.
    """
    step = math.floor(spec.shape[1] / n)
    for i in range(n):
        yield spec[:, i * step:(i + 1) * step, :]


def next_patch(spec: int, n: int, orientation: str):
    """
    Chama a função baseado na orientação em que serão feito a divisão da imagem.
    :param spec: é a altura da imagem.
    :param n: é o número de divisões que serão feitas na imagem.
    :param orientation: é a orientação do corte da imagem.
    """
    match orientation:
        case "horizontal":
            return next_patch_horizontal(spec, n)
        case "vertical":
            return next_patch_vertical(spec, n)

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--input_dir", type=str, required=True)
    argparser.add_argument("--num_patches", type=int, default=3)
    argparser.add_argument("--orientation", type=str, default="horizontal", choices=["horizontal", "vertical", "block"])
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
            image = tf.keras.preprocessing.image.load_img(f)
            spec = tf.keras.preprocessing.image.img_to_array(image)
            for idx, p in enumerate(next_patch(spec, args.num_patches, args.orientation), start=1):
                filename = f"{idx:03}+{f.name}"
                filename = os.path.join(args.output_dir, filename)
                print("saving %s" % filename)
                tf.keras.preprocessing.image.save_img(filename, p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
