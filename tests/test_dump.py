from __future__ import annotations

from array import array
from decimal import Decimal
from typing import Any

import pytest
from diskcache import Cache, FanoutCache

VALUES = [
    1,
    1.1,
    1 + 1j,
    "value",
    b"value",
    True,
    False,
    None,
    bytearray(b"value"),
    ["value"],
    ("value",),
    {"key": "value"},
    {"key": {"key": "value"}},
    Decimal("123.123"),
    array("l", [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize("value", VALUES)
def test_dtypes(cache: Cache, value: Any) -> None:
    cache["key"] = value
    value_from_cache = cache["key"]
    assert isinstance(value, type(value))
    assert value_from_cache == value


@pytest.mark.parametrize("value", VALUES)
def test_dtypes_fanout(fcache: FanoutCache, value: Any) -> None:
    fcache["key"] = value
    value_from_cache = fcache["key"]
    assert isinstance(value, type(value))
    assert value_from_cache == value
