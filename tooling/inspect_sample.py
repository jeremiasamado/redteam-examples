"""Small, dependency-free triage helper for the authored lab sample."""

from __future__ import annotations

import hashlib
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from terminal_theme import trace_sequence


def printable_strings(data: bytes) -> list[str]:
    return sorted(
        {
            match.decode("ascii", errors="ignore")
            for match in re.findall(rb"[\x20-\x7e]{5,}", data)
        }
    )


def pe_summary(data: bytes) -> str:
    if data[:2] != b"MZ" or len(data) < 0x40:
        return "format: not a PE file"
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    if data[pe_offset : pe_offset + 4] != b"PE\0\0":
        return "format: invalid PE signature"
    machine, sections = struct.unpack_from("<HH", data, pe_offset + 4)
    return f"format: PE | machine: 0x{machine:04x} | sections: {sections}"


def main() -> int:
    trace_sequence()
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} <sample>")
        return 2

    sample = Path(sys.argv[1])
    if not sample.is_file():
        print(f"error: sample does not exist: {sample}", file=sys.stderr)
        return 1

    data = sample.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(f"sample: {sample}")
    print(f"size: {len(data)} bytes")
    print(f"sha256: {digest}")
    print(pe_summary(data))
    print("strings:")
    for value in printable_strings(data):
        print(f"  {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
