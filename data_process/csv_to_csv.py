import csv
import os

import pandas as pd


def annotation_trans():
    anno_csv = r"../tables/BUSI.csv"
    dst_path = r"../tables/BUSI_anno_test.csv"
    train_root = r"../Pytorch-UNet-master/data/train"
    test_root = r"../Pytorch-UNet-master/data/test"

    train_path = r"/Users/qinyang.lu/PycharmProjects/Pytorch-UNet-master/data/train"
    test_path = r"/Users/qinyang.lu/PycharmProjects/Pytorch-UNet-master/data/test"

    train_list = os.listdir(train_path)
    test_list = os.listdir(test_path)

    df = pd.read_csv(anno_csv, dtype=str)
    with open(dst_path, "w", newline="") as f:
        writer = csv.writer(f)
        for i in range(len(df)):
            img_name = df.iloc[i]["image_name"]
            x = int(df.iloc[i]["x"])
            y = int(df.iloc[i]["y"])
            w = int(df.iloc[i]["w"])
            h = int(df.iloc[i]["h"])

            x2 = x + w
            y2 = y + h
            if img_name in train_list:
                img_path = train_root + "/" + img_name
            elif img_name in test_list:
                img_path = test_root + "/" + img_name
            else:
                print(img_name)
                exit()

            row = [img_path, str(x), str(y), str(x2), str(y2), "nodule"]
            writer.writerow(row)


if __name__ == '__main__':
    annotation_trans()