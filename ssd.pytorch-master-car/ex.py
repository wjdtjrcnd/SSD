import torch

# 초기 텐서: 3x4 크기의 모든 값이 0인 텐서
tensor = torch.zeros(3, 4)
print("초기 텐서:")
print(tensor)

# index 설정
index = torch.tensor([1, 2, 0])

# index를 사용하여 특정 위치에 값을 채움
tensor.index_fill_(0, index, 2)

print("\nindex를 사용하여 특정 위치에 값을 채운 후의 텐서:")
print(tensor)
