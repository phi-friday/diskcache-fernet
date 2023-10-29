from __future__ import annotations

from typing import Any

from cryptography.fernet import Fernet
from diskcache import Cache, FanoutCache

from diskcache_fernet import FernetDisk, SecretValue


def test_set_and_get(cache: Cache) -> None:
    cache.set("key", "value")
    value = cache.get("key")
    assert value == "value"


def test_set_and_get_decrypt(cache: Cache, cache_disk: FernetDisk) -> None:
    cache.set("key", b"value")
    new_cache = Cache(cache.directory)
    value: Any = new_cache.get("key")
    assert value != b"value"
    decrypt = cache_disk._decrypt(value)  # noqa: SLF001
    assert decrypt == b"value"


def test_set_and_get_fanout(fcache: FanoutCache) -> None:
    fcache.set("key", "value")
    value = fcache.get("key")
    assert value == "value"


def test_set_and_get_decrypt_fanout(
    fcache: FanoutCache, fcache_disk: FernetDisk
) -> None:
    fcache.set("key", b"value")
    new_cache = FanoutCache(fcache.directory)
    value: Any = new_cache.get("key")
    assert value != b"value"
    decrypt = fcache_disk._decrypt(value)  # noqa: SLF001
    assert decrypt == b"value"


def test_set_and_get_decrypt_outside(cache: Cache, token: SecretValue[bytes]) -> None:
    cache.set("key", b"value")
    fernet = Fernet(token.get_value())
    new_cache = Cache(cache.directory)
    value: Any = new_cache.get("key")
    assert value != b"value"
    decrypt = fernet.decrypt(value)
    assert decrypt == b"value"


def test_set_and_get_decrypt_outside_fanout(
    fcache: FanoutCache, token: SecretValue[bytes]
) -> None:
    fcache.set("key", b"value")
    fernet = Fernet(token.get_value())
    new_cache = FanoutCache(fcache.directory)
    value: Any = new_cache.get("key")
    assert value != b"value"
    decrypt = fernet.decrypt(value)
    assert decrypt == b"value"
