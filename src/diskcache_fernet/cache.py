from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, overload

from diskcache import Cache as _Cache
from diskcache import Disk
from typing_extensions import override

from diskcache_fernet.disk import FernetDisk

if TYPE_CHECKING:
    from pathlib import Path

__all__ = ["Cache"]


class Cache(_Cache):  # noqa: D101
    @override
    def __init__(
        self,
        directory: str | Path | None = None,
        timeout: float = 60,
        disk: type[Disk] = FernetDisk,
        **settings: Any,
    ) -> None:
        if directory is not None and not isinstance(directory, str):
            directory = directory.as_posix()
        super().__init__(directory, timeout, disk, **settings)  # type: ignore

    if TYPE_CHECKING:

        @override
        def set(
            self,
            key: Any,
            value: Any,
            expire: float | None = None,
            read: bool = False,  # noqa: FBT001
            tag: str | None = None,
            retry: bool = False,  # noqa: FBT001
        ) -> bool:
            ...

        @override
        def __setitem__(self, key: Any, value: Any) -> None:
            ...

        @override
        def add(
            self,
            key: Any,
            value: Any,
            expire: float | None = None,
            read: bool = False,  # noqa: FBT001
            tag: str | None = None,
            retry: bool = False,  # noqa: FBT001
        ) -> bool:
            ...

        @overload
        def get(
            self,
            key: Any,
            default: Any = ...,
            read: bool = ...,  # noqa: FBT001
            expire_time: Literal[False] = ...,
            tag: Literal[False] = ...,
            retry: bool = ...,  # noqa: FBT001
        ) -> Any:
            ...

        @overload
        def get(
            self,
            key: Any,
            default: Any = ...,
            read: bool = ...,  # noqa: FBT001
            expire_time: Literal[True] = ...,
            tag: Literal[False] = ...,
            retry: bool = ...,  # noqa: FBT001
        ) -> tuple[Any, float | None]:
            ...

        @overload
        def get(
            self,
            key: Any,
            default: Any = ...,
            read: bool = ...,  # noqa: FBT001
            expire_time: Literal[False] = ...,
            tag: Literal[True] = ...,
            retry: bool = ...,  # noqa: FBT001
        ) -> tuple[Any, str | None]:
            ...

        @overload
        def get(
            self,
            key: Any,
            default: Any = ...,
            read: bool = ...,  # noqa: FBT001
            expire_time: Literal[True] = ...,
            tag: Literal[True] = ...,
            retry: bool = ...,  # noqa: FBT001
        ) -> tuple[Any, float | None, str | None]:
            ...

        @overload
        def get(
            self,
            key: Any,
            default: Any = ...,
            read: bool = ...,  # noqa: FBT001
            expire_time: bool = ...,  # noqa: FBT001
            tag: bool = ...,  # noqa: FBT001
            retry: bool = ...,  # noqa: FBT001
        ) -> Any:
            ...

        @override
        def get(
            self,
            key: Any,
            default: Any = None,
            read: bool = False,  # noqa: FBT001
            expire_time: bool = False,  # noqa: FBT001
            tag: bool = False,  # noqa: FBT001
            retry: bool = False,  # noqa: FBT001
        ) -> Any:
            ...

        @override
        def __getitem__(self, key: Any) -> Any:
            ...


Cache.__doc__ = _Cache.__doc__
