import torch
import numpy as np

def iou(y_true, y_pred, class_label):
    y_true = y_true == class_label
    y_pred = y_pred == class_label
    inter = (y_true & y_pred).sum()
    union = (y_true | y_pred).sum()
    return inter / (union + 1e-8)

# final_iou = (iou(y_true, y_pred, class_label=1)+iou(y_true, y_pred, class_label=0))/2

# 1 пример
y_true = np.array([[0,0,0],
                   [0,0,0],
                   [0,0,0]])

# y_pred = segmentation_algorithm.predict(rgb_image)
y_pred = np.array([[0,0,0],
                   [0,0,0],
                   [0,0,0]])


metric = iou(y_true, y_pred, class_label=1)
print(y_true.shape,y_pred.shape) # (3, 3) (3, 3)
print(metric) # 1.0

# 2 пример
y_true = torch.tensor([[[0,0,0],
                        [1,1,1],
                        [0,0,0]]])

# y_pred = segmentation_algorithm.predict(rgb_image)
y_pred = torch.tensor([[[0,0,0],
                        [1,1,1],
                        [1,1,1]]])

metric = iou(y_true, y_pred, class_label=1)
print(y_true.shape,y_pred.shape) # torch.Size([1, 3, 3]) torch.Size([1, 3, 3])
print(metric) # tensor(0.5000)

# Дополнения/Пояснения
# функция работает и для numpy массивов (1 пример), и для torch тензоров (2 пример)
# функция работает и для отдельных масок (1 пример), и батчей с масками (2 пример)
