"""
Checksum Algorithms

Pure-Python implementations of common checksum algorithms:
Luhn, CRC-32, Fletcher-16, and Adler-32.
"""

from typing import List

MOD_ADLER: int = 65521  # largest prime smaller than 2^16


# ---------------------------------------------------------------------------
# Luhn algorithm
# ---------------------------------------------------------------------------


def luhn_checksum(number_str: str) -> int:
    """Compute the Luhn check digit for a numeric string.

    The check digit is chosen so that appending it to *number_str* produces
    a string that passes the Luhn validation.

    Args:
        number_str: A non-empty string composed entirely of ASCII digits.

    Returns:
        The check digit (an integer in the range 0–9).

    Raises:
        TypeError: If *number_str* is not a string.
        ValueError: If *number_str* is empty or contains non-digit characters.
    """

    if not isinstance(number_str, str):
        raise TypeError(f"Expected a string, got {type(number_str).__name__}.")
    if len(number_str) == 0:
        raise ValueError("Input string must not be empty.")
    if not number_str.isdigit():
        raise ValueError(
            f"Input string must contain only digits, got '{number_str}'."
        )

    digits: List[int] = [int(ch) for ch in number_str]

    # Double every second digit from the right (the payload digits).
    # Since we are computing the check digit, every digit in the existing
    # string is processed starting from the rightmost one.
    total: int = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return (10 - (total % 10)) % 10


def luhn_validate(number_str: str) -> bool:
    """Validate a number string using the Luhn algorithm.

    The last digit of *number_str* is treated as the check digit.

    Args:
        number_str: A string of at least two digits.

    Returns:
        ``True`` if the string passes the Luhn check, ``False`` otherwise.

    Raises:
        TypeError: If *number_str* is not a string.
        ValueError: If *number_str* has fewer than two characters or contains
            non-digit characters.
    """

    if not isinstance(number_str, str):
        raise TypeError(f"Expected a string, got {type(number_str).__name__}.")
    if len(number_str) < 2:
        raise ValueError("Input string must have at least two digits.")
    if not number_str.isdigit():
        raise ValueError(
            f"Input string must contain only digits, got '{number_str}'."
        )

    digits: List[int] = [int(ch) for ch in number_str]

    total: int = 0
    # Process from the rightmost digit; the check digit (index 0 from right)
    # is NOT doubled, the next one IS doubled, alternating.
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return total % 10 == 0


# ---------------------------------------------------------------------------
# CRC-32
# ---------------------------------------------------------------------------


def crc32(data: bytes, polynomial: int = 0xEDB88320) -> int:
    """Compute the CRC-32 checksum for *data*.

    Uses the standard bit-by-bit algorithm with a reflected polynomial.

    Args:
        data: The bytes object to checksum.
        polynomial: The reflected CRC-32 polynomial.  The default value
            ``0xEDB88320`` corresponds to the standard CRC-32 used in
            Ethernet, gzip, PNG, etc.

    Returns:
        The CRC-32 value as an unsigned 32-bit integer.

    Raises:
        TypeError: If *data* is not a ``bytes`` object.
    """

    if not isinstance(data, bytes):
        raise TypeError(f"Expected bytes, got {type(data).__name__}.")

    # Build a 256-entry lookup table for speed.
    table: List[int] = []
    for byte in range(256):
        crc: int = byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table.append(crc)

    crc = 0xFFFFFFFF
    for byte in data:
        crc = table[(crc ^ byte) & 0xFF] ^ (crc >> 8)

    return crc ^ 0xFFFFFFFF


# ---------------------------------------------------------------------------
# Fletcher-16
# ---------------------------------------------------------------------------


def fletcher16(data: bytes) -> int:
    """Compute the Fletcher-16 checksum for *data*.

    Args:
        data: The bytes object to checksum.

    Returns:
        The Fletcher-16 value as a 16-bit unsigned integer.

    Raises:
        TypeError: If *data* is not a ``bytes`` object.
    """

    if not isinstance(data, bytes):
        raise TypeError(f"Expected bytes, got {type(data).__name__}.")

    sum1: int = 0
    sum2: int = 0

    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255

    return (sum2 << 8) | sum1


# ---------------------------------------------------------------------------
# Adler-32
# ---------------------------------------------------------------------------


def adler32(data: bytes) -> int:
    """Compute the Adler-32 checksum for *data*.

    Args:
        data: The bytes object to checksum.

    Returns:
        The Adler-32 value as an unsigned 32-bit integer.

    Raises:
        TypeError: If *data* is not a ``bytes`` object.
    """

    if not isinstance(data, bytes):
        raise TypeError(f"Expected bytes, got {type(data).__name__}.")

    a: int = 1
    b: int = 0

    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER

    return (b << 16) | a
