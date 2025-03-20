import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should print False if running on CPU
