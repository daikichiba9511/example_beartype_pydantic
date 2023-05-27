import numpy as np
import torch
from beartype import beartype
from numpy.typing import NDArray


@beartype
def np_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a + b


@beartype
def np_diff(a: NDArray[np.float16], b: NDArray[np.float16]) -> np.ndarray:
    return b - a


@beartype
def torch_add(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return a + b


def main() -> None:
    print(" ###### np.ndarray Case ###### ")
    print(np_add(a=np.array([1, 2, 3]), b=np.array([4, 5, 6])))

    try:
        np_add(a=[1, 2, 3], b=np.array([4, 5, 6]))
    except Exception as e:
        print(e)

    # NDArray Case
    print(" ###### NDArray Case ###### \n")
    print(
        np_diff(
            a=np.array([1, 2, 3], dtype=np.float16),
            b=np.array([4, 5, 6], dtype=np.float16),
        )
    )
    # NDArray Error Case
    try:
        np_diff(
            a=np.array([1, 2, 3], dtype=np.float64),
            b=np.array([4, 5, 6], dtype=np.float16),
        )
    except Exception as e:
        print(e)

    print(" ###### torch.Tensor Case ###### \n")
    print(torch_add(a=torch.tensor([1, 2, 3]), b=torch.tensor([4, 5, 6])))


if __name__ == "__main__":
    main()
