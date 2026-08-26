# Build: d2e051670a30b0b89aaf2b9db87e1637

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
