import os
import tarfile
from tqdm.autonotebook import tqdm


for idx in tqdm(range(1000)):
    base_path = '/content/gdrive/My Drive/imagenet-tars'
    filenames = [f'{idx:04d}-train.tar', f'{idx:04d}-val.tar']
    filenames = [os.path.join(base_path, f) for f in filenames]
    for fn in filenames:
        with tarfile.open(fn) as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar)

