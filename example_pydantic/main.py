from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import TypeAlias


class User(BaseModel):
    name: str = Field(..., description="名前")
    age: int = Field(..., description="年齢")


Users: TypeAlias = list[User]


class Request(BaseModel):
    id: int = Field(..., description="ID")
    image_name: str = Field(..., description="画像名")
    model_path: Path = Field(..., description="モデルパス")
    additional_config: Optional[dict[str, Union[str, float, bool]]] = Field(
        default_factory=lambda: {"tta": False}, description="追加設定"
    )


class EstimatedResult(BaseModel):
    value: list[int] = Field(..., description="推論結果")
    shape: tuple[int, int] = Field(..., description="推論結果のshape")


class Response(BaseModel):
    ids: list[int] = Field(..., description="ID")
    estimated_result: EstimatedResult = Field(..., description="推論結果")
    model_path: Path = Field(..., description="モデルパス")


class ImmutableResponse(BaseModel):
    ids: list[int] = Field(..., description="ID")
    estimated_result: EstimatedResult = Field(..., description="推論結果")
    model_path: Path = Field(..., description="モデルパス")

    class Config:
        frozen = True  # 全Fieldをimmutableにする


class ResponseConainsImmutableField(BaseModel):
    """
    Ref:
    [1] https://docs.pydantic.dev/latest/usage/schema/#field-customization
    """

    # allow_mutation=FalseでこのFieldのみimmutable
    ids: list[int] = Field(..., allow_mutation=False, description="ID")
    estimated_result: EstimatedResult = Field(..., description="推論結果")
    model_path: Path = Field(..., description="モデルパス")

    class Config:
        # to check to be performed
        validate_assignment = True


def main() -> None:
    user = User(name="nnc_5522", age=27)
    print(user)

    users: Users = [
        User(name="nnc_5522", age=27),
        User(name="nnc_5523", age=27),
        User(name="nnc_5524", age=27),
    ]
    print(users)

    request1 = Request(
        id="1111",
        image_name="image1.jpg",
        model_path=Path("weights/model1.pth"),
    )
    print(request1)
    # serializeも楽にできる
    print(request1.dict())
    print(request1.json())

    estimated = EstimatedResult(value=[1, 2, 3], shape=(3, 1))
    response = Response(
        ids=[1, 2, 3],
        estimated_result=estimated,
        model_path=Path("weights/model1.pth"),
    )
    print(response.dict())

    # immutable version
    immutable_response = ImmutableResponse(
        ids=[1, 2, 3],
        estimated_result=estimated,
        model_path=Path("weights/model1.pth"),
    )

    try:
        immutable_response.estimated_result = [1000000, 100000, 1000000]
    except Exception as e:
        print(e)

    # ids Fieldのみimmutable
    response_contains_immutable_field = ResponseConainsImmutableField(
        ids=[1, 2, 3],
        estimated_result=estimated,
        model_path=Path("weighs/model1.pth"),
    )
    # OK
    response_contains_immutable_field.model_path = Path("weights/model2.pth")
    # Fail
    try:
        response_contains_immutable_field.ids = [1111, 1111, 1111]
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
