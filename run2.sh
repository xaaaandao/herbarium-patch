#!/usr/bin/env bash

INPUT_DIR="/mnt/eec07521-c36a-4d2b-9047-0110e7749eae/Nextcloud/Dropbox import/datasets/2025/images/uem/data_aug+dcgan/patch=1/pr_dataset+20"
OUTPUT_DIR="/mnt/eec07521-c36a-4d2b-9047-0110e7749eae/Nextcloud/Dropbox import/datasets/2025/images/uem/data_aug+dcgan/patch=1/pr_dataset+20"

# pr_dataset+20
for label in "Peperomia+blanda" "Peperomia+catharinae" "Peperomia+corcovadensis" "Peperomia+glabella" "Peperomia+martiana" "Peperomia+rotundifolia" "Peperomia+tetraphylla" "Peperomia+urocarpa" "Piper+aduncum" "Piper+amalago" "Piper+arboreum" "Piper+caldense" "Piper+crassinervium" "Piper+dilatatum" "Piper+gaudichaudianum" "Piper+glabratum" "Piper+grazielae" "Piper+hispidum" "Piper+mikanianum" "Piper+miquelianum" "Piper+regnellii" "Piper+solmsianum" "Piper+xylosteoides" ; do
    for color in "RGB"; do
        for img_size in "256"; do
            python main2.py --input_dir "${INPUT_DIR}/pr_dataset+20+rotation+colorjitter/${color}/${img_size}/${label}" --output_dir "${OUTPUT_DIR}/pr_dataset+20+rotation+colorjitter+no-white/${color}/${img_size}/${label}"
        done
    done
done

# for label in "Peperomia+blanda" "Peperomia+catharinae" "Peperomia+corcovadensis" "Peperomia+glabella" "Peperomia+martiana" "Peperomia+rotundifolia" "Peperomia+tetraphylla" "Peperomia+urocarpa" "Piper+aduncum" "Piper+amalago" "Piper+arboreum" "Piper+caldense" "Piper+crassinervium" "Piper+dilatatum" "Piper+gaudichaudianum" "Piper+glabratum" "Piper+grazielae" "Piper+hispidum" "Piper+mikanianum" "Piper+miquelianum" "Piper+regnellii" "Piper+solmsianum" "Piper+xylosteoides" ; do
#     for data_aug in "Rotate+90" "Rotate+180" "Rotate+270" "HorizontalFlip" "VerticalFlip" "Transpose"; do
#         for color in "RGB"; do
#             for img_size in "256"; do
#                 python main2.py --input_dir "${INPUT_DIR}/pr_dataset+20+${data_aug}/${color}/${img_size}/${label}" --output_dir "${OUTPUT_DIR}/pr_dataset+20+${data_aug}+no-white/${color}/${img_size}/${label}"
#             done
#         done
#     done
# done