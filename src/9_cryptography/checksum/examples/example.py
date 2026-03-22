"""
Checksum Algorithms — Example

Demonstrates the Luhn, CRC-32, Fletcher-16, and Adler-32 checksum
algorithms provided by the checksum module.
"""

from ..implementation.checksum import (
    luhn_checksum,
    luhn_validate,
    crc32,
    fletcher16,
    adler32,
)


def main() -> None:
    # --- Luhn algorithm ---
    payload = "453957876362148"
    check_digit = luhn_checksum(payload)
    full_number = payload + str(check_digit)
    print(f"Luhn check digit for {payload}: {check_digit}")
    print(f"Full number: {full_number}")
    print(f"Valid: {luhn_validate(full_number)}")
    print()

    # --- CRC-32 ---
    data = b"123456789"
    checksum = crc32(data)
    print(f"CRC-32 of {data!r}: 0x{checksum:08X}")
    print()

    # --- Fletcher-16 ---
    data = b"Hello, World!"
    checksum = fletcher16(data)
    print(f"Fletcher-16 of {data!r}: 0x{checksum:04X}")
    print()

    # --- Adler-32 ---
    data = b"Wikipedia"
    checksum = adler32(data)
    print(f"Adler-32 of {data!r}: 0x{checksum:08X}")


if __name__ == "__main__":
    main()
