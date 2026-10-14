import torch
import torch_directml

dml = torch_directml.device()
print("Kullanılan Aygıt:", dml)

x = torch.randn(1000, 1000, device=dml)
print("İşlem Başarılı, Matris Boyutu:", (x @ x).shape)
