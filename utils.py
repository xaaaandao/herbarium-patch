import math
import numpy as np

from PIL import Image

def crop_horizontal(image_path, output_path=None, white_threshold=250):
    # Carregar a imagem
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Garantir que é uma imagem colorida (RGB ou RGBA)
    if len(img_array.shape) != 3:
        raise ValueError("A imagem deve ser colorida (RGB ou RGBA)")
    
    altura, largura, canais = img_array.shape
    
    # Encontrar primeira linha não-branca do topo (começando em 0,0)
    primeira_linha_colorida = 0
    for i in range(altura):
        linha = img_array[i, :, :]
        
        # Verificar se há pelo menos um pixel colorido (não-branco) na linha
        # Um pixel é considerado branco se todos os seus canais RGB >= white_threshold
        if canais == 4:  # RGBA
            pixels_brancos = np.all(linha[:, :3] >= white_threshold, axis=1)
        else:  # RGB
            pixels_brancos = np.all(linha >= white_threshold, axis=1)
        
        # Se existe pelo menos um pixel não-branco, paramos
        if not np.all(pixels_brancos):
            primeira_linha_colorida = i
            break
    else:
        # Toda a imagem é branca
        primeira_linha_colorida = altura
    
    # Encontrar primeira linha não-branca de baixo para cima
    ultima_linha_colorida = altura - 1
    for i in range(altura - 1, -1, -1):
        linha = img_array[i, :, :]
        
        # Verificar se há pelo menos um pixel colorido (não-branco) na linha
        if canais == 4:  # RGBA
            pixels_brancos = np.all(linha[:, :3] >= white_threshold, axis=1)
        else:  # RGB
            pixels_brancos = np.all(linha >= white_threshold, axis=1)
        
        # Se existe pelo menos um pixel não-branco, paramos
        if not np.all(pixels_brancos):
            ultima_linha_colorida = i
            break
    else:
        # Toda a imagem é branca
        ultima_linha_colorida = -1
    
    # Recortar a imagem
    if primeira_linha_colorida <= ultima_linha_colorida:
        img_processada = img_array[primeira_linha_colorida:ultima_linha_colorida + 1, :, :]
    else:
        # Imagem completamente branca
        img_processada = np.array([])
    
    # Salvar se um caminho de saída foi fornecido
    if output_path and img_processada.size > 0:
        img_final = Image.fromarray(img_processada)
        img_final.save(output_path)
        print(f"Imagem salva em: {output_path}")
        print(f"Linhas removidas do topo: {primeira_linha_colorida}")
        print(f"Linhas removidas da base: {altura - ultima_linha_colorida - 1}")
        print(f"Dimensões original: {altura}x{largura}")
        print(f"Dimensões final: {img_processada.shape[0]}x{img_processada.shape[1]}")
    
    return img_processada


def criar_patches_verticais(img_path, orig_size, num_patches_y):
    """
    Cria patches verticais de uma imagem colorida.

    Parâmetros:
        img_path (str): caminho da imagem.
        orig_size (tuple): (orig_width, orig_height) esperado.
        num_patches_y (int): número de patches verticais desejados.

    Regras:
        - Calcula o tamanho do patch baseado na altura original.
        - Se patch < altura original, retorna quantos patches cabem na imagem real.
        - Se não dividir perfeitamente → criar patches sobrepostos.
    """

    # Carregar imagem
    img = Image.open(img_path).convert("RGB")
    img_width, img_height = img.size
    orig_width, orig_height = orig_size

    # Tamanho do patch baseado na altura original
    patch_height = orig_height // num_patches_y
    patch_width = orig_width  # largura é sempre a total

    # Regra: se patch menor que a imagem original, retornar QTD possível
    if patch_height <= 0 or patch_height > img_height:
        return [img] * num_patches_y

    # Se não divide exatamente → sobrepor
    total_height = img_height

    if patch_height * num_patches_y != total_height:
        # stride com sobreposição
        stride = (total_height - patch_height) / (num_patches_y - 1)
    else:
        stride = patch_height

    patches = []

    for i in range(num_patches_y):
        y0 = int(i * stride)
        y1 = y0 + patch_height

        # Garantir que não extrapole a imagem
        if y1 > total_height:
            y1 = total_height
            y0 = y1 - patch_height

        patch = img.crop((0, y0, img_width, y1))
        patches.append(np.array(patch))

    return patches