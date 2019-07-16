import random

import numpy as np
import torch


def set_all_rng_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)

    # see PyTorch Notes
    # https://pytorch.org/docs/stable/notes/randomness.html
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.manual_seed(seed)


def get_all_rng_states():
    r = {
        'pytorch': torch.get_rng_state(),
        'pytorch_cuda': torch.cuda.get_rng_state_all(),
        'numpy': np.random.get_state(),
        'python': random.getstate()
    }
    return r

def set_all_rng_states(state: dict):
    random.setstate(state['python'])
    np.random.set_state(state['numpy'])
    torch.set_rng_state(state['pytorch'])
    if 'pytorch_cuda' in state:
        torch.cuda.set_rng_state_all(state['pytorch_cuda'])
