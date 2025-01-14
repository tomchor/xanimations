from .core import Movie
from .presets import basic

try:
    from ._version import __version__

except ModuleNotFoundError:
    __version__ = "unknown"


__all__ = ("Movie",)
