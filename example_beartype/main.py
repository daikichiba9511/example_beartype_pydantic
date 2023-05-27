from typing import Union

from beartype import beartype


@beartype
def hello(name: str) -> str:
    return f"Hello {name}!"


@beartype
def hello_names(names: list[str]) -> str:
    return f"Hello {', '.join(names)}!"


@beartype
def hello_union(name: Union[str, int]) -> str:
    return f"Hello {name}!"


def main() -> None:
    # Normal Case
    print(hello(name="world"))

    # Error Case
    # 行儀良くないけどエラーを握りつぶす
    try:
        hello(name=1)
    except Exception as e:
        print(e)

    # list[str] Case
    print(hello_names(names=["world", "python", "nnc_5522"]))

    # union case
    print(hello_union(name="world"))
    print(hello_union(name=100))

    # union Error Case
    try:
        hello_union(name=1.0)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
