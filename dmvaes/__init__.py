# -*- coding: utf-8 -*-

"""Top-level package."""
import torch

def get_device()-> str:
    DEVICE = 'cpu'
    if torch.cuda.is_available():
      DEVICE = 'cuda'
    return DEVICE