"""
Tests for checksum algorithms — Luhn, CRC-32, Fletcher-16, and Adler-32.
"""

import pytest

from ..implementation.checksum import (
    luhn_checksum,
    luhn_validate,
    crc32,
    fletcher16,
    adler32,
)


# ---------------------------------------------------------------------------
# luhn_checksum tests
# ---------------------------------------------------------------------------


def test_luhn_checksum_single_digit():
    # Check digit for "0" should be 0 (0 + 0 = 0 mod 10).
    assert luhn_checksum("0") == 0


def test_luhn_checksum_known_card_number():
    # Visa test number: 4539578763621486
    # The payload is "453957876362148"; check digit should be 6.
    assert luhn_checksum("453957876362148") == 6


def test_luhn_checksum_another_card_number():
    # MasterCard test number: 5500000000000004
    # Payload "550000000000000"; check digit should be 4.
    assert luhn_checksum("550000000000000") == 4


def test_luhn_checksum_amex():
    # Amex test number: 378282246310005
    # Payload "37828224631000"; check digit should be 5.
    assert luhn_checksum("37828224631000") == 5


def test_luhn_checksum_type_error():
    with pytest.raises(TypeError, match="Expected a string"):
        luhn_checksum(12345)  # type: ignore[arg-type]


def test_luhn_checksum_empty_string():
    with pytest.raises(ValueError, match="must not be empty"):
        luhn_checksum("")


def test_luhn_checksum_non_digit():
    with pytest.raises(ValueError, match="only digits"):
        luhn_checksum("123a56")


# ---------------------------------------------------------------------------
# luhn_validate tests
# ---------------------------------------------------------------------------


def test_luhn_validate_valid_visa():
    assert luhn_validate("4539578763621486") is True


def test_luhn_validate_valid_mastercard():
    assert luhn_validate("5500000000000004") is True


def test_luhn_validate_valid_amex():
    assert luhn_validate("378282246310005") is True


def test_luhn_validate_invalid_number():
    assert luhn_validate("4539578763621480") is False


def test_luhn_validate_another_invalid():
    assert luhn_validate("1234567890") is False


def test_luhn_validate_roundtrip():
    payload = "7992739871"
    check = luhn_checksum(payload)
    assert luhn_validate(payload + str(check)) is True


def test_luhn_validate_type_error():
    with pytest.raises(TypeError, match="Expected a string"):
        luhn_validate(12345)  # type: ignore[arg-type]


def test_luhn_validate_too_short():
    with pytest.raises(ValueError, match="at least two digits"):
        luhn_validate("5")


def test_luhn_validate_non_digit():
    with pytest.raises(ValueError, match="only digits"):
        luhn_validate("12ab")


# ---------------------------------------------------------------------------
# crc32 tests
# ---------------------------------------------------------------------------


def test_crc32_standard_check_value():
    # The CRC-32 of the ASCII string "123456789" is 0xCBF43926.
    assert crc32(b"123456789") == 0xCBF43926


def test_crc32_empty():
    # CRC-32 of empty data is 0x00000000.
    assert crc32(b"") == 0x00000000


def test_crc32_single_byte():
    # CRC-32 of b"a" is a known value.
    result = crc32(b"a")
    assert isinstance(result, int)
    assert 0 <= result <= 0xFFFFFFFF


def test_crc32_hello_world():
    # Known CRC-32 of b"Hello, World!"
    assert crc32(b"Hello, World!") == 0xEC4AC3D0


def test_crc32_type_error():
    with pytest.raises(TypeError, match="Expected bytes"):
        crc32("not bytes")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# fletcher16 tests
# ---------------------------------------------------------------------------


def test_fletcher16_simple():
    # Fletcher-16 of [0x01, 0x02] computed manually:
    # sum1: 0 -> 1 -> 3   (mod 255)
    # sum2: 0 -> 1 -> 4   (mod 255)
    # result: (4 << 8) | 3 = 0x0403 = 1027
    assert fletcher16(b"\x01\x02") == 0x0403


def test_fletcher16_empty():
    assert fletcher16(b"") == 0x0000


def test_fletcher16_single_byte():
    # For byte 0x01: sum1 = 1, sum2 = 1 → (1 << 8) | 1 = 0x0101
    assert fletcher16(b"\x01") == 0x0101


def test_fletcher16_abc():
    # "abcde" (bytes 97, 98, 99, 100, 101)
    result = fletcher16(b"abcde")
    assert isinstance(result, int)
    assert 0 <= result <= 0xFFFF


def test_fletcher16_type_error():
    with pytest.raises(TypeError, match="Expected bytes"):
        fletcher16("string")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# adler32 tests
# ---------------------------------------------------------------------------


def test_adler32_wikipedia():
    # Well-known test vector: adler32(b"Wikipedia") == 0x11E60398
    assert adler32(b"Wikipedia") == 0x11E60398


def test_adler32_empty():
    # Adler-32 of empty data: a=1, b=0 → (0 << 16) | 1 = 1
    assert adler32(b"") == 0x00000001


def test_adler32_single_a():
    # b"a" = [97]: a = (1 + 97) % 65521 = 98, b = (0 + 98) % 65521 = 98
    # result = (98 << 16) | 98 = 0x00620062
    assert adler32(b"a") == 0x00620062


def test_adler32_abc():
    # Known: adler32(b"abc") = 0x024d0127
    assert adler32(b"abc") == 0x024D0127


def test_adler32_type_error():
    with pytest.raises(TypeError, match="Expected bytes"):
        adler32(123)  # type: ignore[arg-type]
