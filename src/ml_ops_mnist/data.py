import glob
import pathlib
from pathlib import Path

import torch
import typer


def Corrupt_mnist():
    train_paths = zip(
        sorted(glob.glob("data/processed/corruptmnist_v1/train_images_*.pt")),
        sorted(glob.glob("data/raw/corruptmnist_v1/train_target_*.pt")),
    )
    train = ((torch.load(x), torch.load(y)) for x, y in train_paths)

    test_paths = zip(
        sorted(glob.glob("data/processed/corruptmnist_v1/test_images.pt")),
        sorted(glob.glob("data/raw/corruptmnist_v1/test_target.pt")),
    )
    test = ((torch.load(x), torch.load(y)) for x, y in test_paths)

    return train, test


def preprocess_data():
    train_images = list(sorted(glob.glob("data/raw/corruptmnist_v1/train_images_*.pt")))
    tensors = set()
    for image in train_images:
        dir = Path("data/processed/corruptmnist_v1/normalized")
        dir.mkdir(exist_ok=True, parents=True)

        tensor = torch.load(image)
        # Normalize images
        tensor = (tensor - torch.mean(tensor)) / torch.std(tensor)
        tensors.add(tensor)

    torch.save(tensors, dir / "train_images.pt")

    test_image = Path("data/raw/corruptmnist_v1/test_images.pt")
    tensor = torch.load(image)
    # Normalize image
    tensor = (tensor - torch.mean(tensor)) / torch.std(tensor)
    torch.save(tensor, dir / "test_images.pt")


if __name__ == "__main__":
    typer.run(preprocess_data)
