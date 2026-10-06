"""Private terminal styling for local research tooling."""

from __future__ import annotations

import os
import sys
import time
from typing import TextIO

PURPLE = "\033[38;5;141m"
LIGHT_PURPLE = "\033[38;5;183m"
RESET = "\033[0m"


def enabled(stream: TextIO | None = None) -> bool:
    stream = stream or sys.stderr
    return bool(stream.isatty() and os.environ.get("NO_COLOR") is None and os.environ.get("TERM") != "dumb")


def paint(value: str, colour: str, stream: TextIO | None = None) -> str:
    return f"{colour}{value}{RESET}" if enabled(stream) else value


def trace_sequence(stream: TextIO | None = None) -> None:
    stream = stream or sys.stderr
    if not enabled(stream):
        return
    for frame in (
        "[•    ] LINKING BADBOY17 NODE",
        "[ •   ] TRACE CHANNEL OPEN",
        "[  •  ] EVIDENCE PATH READY",
    ):
        print(paint(frame, LIGHT_PURPLE, stream), file=stream, flush=True)
        time.sleep(0.12)
