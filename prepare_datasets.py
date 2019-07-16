import os
import tarfile
from tqdm.autonotebook import tqdm


for idx in tqdm(range(1000)):
    base_path = '/content/gdrive/My Drive/imagenet-tars'
    filenames = [f'{idx:04d}-train.tar', f'{idx:04d}-val.tar']
    filenames = [os.path.join(base_path, f) for f in filenames]
    for fn in filenames:
        with tarfile.open(fn) as tar:
            tar.extractall()

