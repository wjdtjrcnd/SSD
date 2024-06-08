# config.py
import os.path

# gets home dir cross platform
HOME = os.path.expanduser("~")

# for making bounding boxes pretty
COLORS = ((255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128),
          (0, 255, 255, 128), (255, 0, 255, 128), (255, 255, 0, 128))

MEANS = (104, 117, 123)

# # SSD300 CONFIGS
voc = {
    'num_classes': 2,
    'lr_steps': (80000, 100000, 120000),
    'max_iter': 2000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [30, 60, 111, 162, 213, 264],
    'max_sizes': [60, 111, 162, 213, 264, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}

# 150 * 150
# voc = {
#     'num_classes': 2,
#     'lr_steps': (80000, 100000, 120000),
#     'max_iter': 200000,
#     'feature_maps': [1],
#     'min_dim': 150,
#     'steps': [150],
#     'min_sizes': [120],
#     'max_sizes': [160],
#     'aspect_ratios': [],
#     'variance': [0.1, 0.2],
#     'clip': True,
#     'name': 'VOC',
# }
# voc = {
#     'num_classes': 21,
#     'lr_steps': (80000, 100000, 120000),
#     'max_iter': 200000,
#     'feature_maps': [13, 7, 4],
#     'min_dim': 100,
#     'steps': [8, 14, 25],
#     'min_sizes': [10, 25, 45],
#     'max_sizes': [25, 45, 65],
#     'aspect_ratios': [[2], [2, 3], [2, 3]],
#     'variance': [0.1, 0.2],
#     'clip': True,
#     'name': 'VOC_lite',
# }
coco = {
    'num_classes': 201,
    'lr_steps': (280000, 360000, 400000),
    'max_iter': 400000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [21, 45, 99, 153, 207, 261],
    'max_sizes': [45, 99, 153, 207, 261, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'COCO',
}
