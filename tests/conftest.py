from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator

import pytest
from cryptography.fernet import Fernet

from diskcache_fernet import FernetCache, FernetDisk, FernetFanoutCache, SecretValue


@pytest.fixture()
def tempdir() -> Generator[Path, None, None]:
    with TemporaryDirectory() as temp:
        yield Path(temp)


@pytest.fixture()
def token() -> SecretValue[bytes]:
    return SecretValue(Fernet.generate_key())


@pytest.fixture()
def cache(token: SecretValue[bytes], tempdir: Path) -> FernetCache:
    return FernetCache(tempdir, disk_fernet=token)


@pytest.fixture()
def cache_disk(cache: FernetCache) -> FernetDisk:
    if not isinstance(cache.disk, FernetDisk):
        raise TypeError("cache disk is not fernet disk")
    return cache.disk


@pytest.fixture()
def fcache(token: SecretValue[bytes], tempdir: Path) -> FernetFanoutCache:
    return FernetFanoutCache(tempdir, disk_fernet=token)


@pytest.fixture()
def fcache_disk(fcache: FernetFanoutCache) -> FernetDisk:
    if not isinstance(fcache.disk, FernetDisk):
        raise TypeError("fcache disk is not fernet disk")
    return fcache.disk
