# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2020/3/25 3:27 PM
@Author: Qinyang Lu
"""

import os

train_csv = r"tables/BUSI_anno_test.csv"
test_csv = r"tables/BUSI_anno_test.csv"
class_list = r"tables/class_list.csv"
model_path = r"cps/"
if os.path.exists(model_path) == 0:
    os.mkdir(model_path)

os.system("python train.py --dataset csv --csv_train {} --csv_classes {}"
          " --csv_val {} --model_path {}". \
          format(train_csv, class_list, test_csv, model_path))