#!/usr/bin/env bash

NUM_PATCHES=3
INPUT_DIR="/mnt/eec07521-c36a-4d2b-9047-0110e7749eae/Nextcloud/Dropbox import/datasets/2025/images/uem/data_aug+traditional/patch=1/pr_dataset+20"
OUTPUT_DIR="/mnt/eec07521-c36a-4d2b-9047-0110e7749eae/Nextcloud/Dropbox import/datasets/2025/images/uem/data_aug+traditional/patch=${NUM_PATCHES}/pr_dataset+20"

# pr_dataset+5
# for label in "Peperomia+alata" "Peperomia+arifolia" "Peperomia+barbarana" "Peperomia+blanda" "Peperomia+catharinae" "Peperomia+circinnata" "Peperomia+corcovadensis" "Peperomia+emarginella" "Peperomia+galioides" "Peperomia+glabella" "Peperomia+hilariana" "Peperomia+hispidula" "Peperomia+hydrocotyloides" "Peperomia+martiana" "Peperomia+nitida" "Peperomia+pereirae" "Peperomia+pereskiaefolia" "Peperomia+pereskiifolia" "Peperomia+pseudoestrellensis" "Peperomia+rhombea" "Peperomia+rotundifolia" "Peperomia+rupestris" "Peperomia+subretusa" "Peperomia+tetraphylla" "Peperomia+trineura" "Peperomia+trineuroides" "Peperomia+urocarpa" "Piper+aduncum" "Piper+amalago" "Piper+amplum" "Piper+arboreum" "Piper+caldasianum" "Piper+caldense" "Piper+cernuum" "Piper+crassinervium" "Piper+dilatatum" "Piper+diospyrifolium" "Piper+gaudichaudianum" "Piper+glabratum" "Piper+grazielae" "Piper+hayneanum" "Piper+hispidum" "Piper+lhotzkianum" "Piper+macedoi" "Piper+malacophyllum" "Piper+mikanianum" "Piper+miquelianum" "Piper+mollicomum" "Piper+mosenii" "Piper+regnellii" "Piper+reitzii" "Piper+solmsianum" "Piper+umbellatum" "Piper+viminifolium" "Piper+xylosteoides"; do
#     for data_aug in "Rotate+90" "Rotate+180" "Rotate+270" "HorizontalFlip" "VerticalFlip" "Transpose"; do
#         for color in "RGB"; do
#             for size in "256"; do
#                 python main.py --input_dir "${INPUT_DIR}/pr_dataset+5+${data_aug}/${color}/${size}/${label}" --num_patches ${NUM_PATCHES} --orientation horizontal --output_dir "${OUTPUT_DIR}/pr_dataset+5+${data_aug}/${color}/${size}/${label}"
#             done
#         done
#     done
# done

# pr_dataset+20
for label in "Peperomia+blanda" "Peperomia+catharinae" "Peperomia+corcovadensis" "Peperomia+glabella" "Peperomia+martiana" "Peperomia+rotundifolia" "Peperomia+tetraphylla" "Peperomia+urocarpa" "Piper+aduncum" "Piper+amalago" "Piper+arboreum" "Piper+caldense" "Piper+crassinervium" "Piper+dilatatum" "Piper+gaudichaudianum" "Piper+glabratum" "Piper+grazielae" "Piper+hispidum" "Piper+mikanianum" "Piper+miquelianum" "Piper+regnellii" "Piper+solmsianum" "Piper+xylosteoides" ; do
    for data_aug in "Rotate+90" "Rotate+180" "Rotate+270" "HorizontalFlip" "VerticalFlip" "Transpose"; do
        for color in "RGB"; do
            for size in "256"; do
                python main.py --input_dir "${INPUT_DIR}/pr_dataset+20+${data_aug}/${color}/${size}/${label}" --num_patches ${NUM_PATCHES} --orientation horizontal --output_dir "${OUTPUT_DIR}/pr_dataset+20+${data_aug}/${color}/${size}/${label}"
            done
        done
    done
done

