from urllib.parse import quote
from .exceptions import InvalidArgumentError

def to_matrix_properties(properties: dict[str, str | list[str]] | None) -> str:
    """
    Convert a dict of properties to Artifactory matrix parameter format.

    Returns a string like: ;key1=value1;key2=value2
    For multi-value properties: ;key=val1;key=val2

    Args:
        properties: Dictionary of property key-value pairs.
            Values can be strings or lists of strings.

    Returns:
        Matrix parameter string or empty string if no properties.
    """
    if not properties:
        return ""

    parts: list[str] = []
    for key, value in properties.items():
        encoded_key = quote(str(key), safe="")
        if isinstance(value, list):
            for item in value:
                encoded_value = quote(str(item), safe="")
                parts.append(f"{encoded_key}={encoded_value}")
        else:
            encoded_value = quote(str(value), safe="")
            parts.append(f"{encoded_key}={encoded_value}")

    return ";" + ";".join(parts)

def to_query_properties(properties: dict[str, str]) -> str:
    """
    Convert a dict of properties to URL query parameter format.

    Returns a string like: ?key1=value1&key2=value2

    Args:
        properties: Dictionary of property key-value pairs.

    Returns:
        Query string or empty string if no properties.
    """
    if not properties:
        return ""

    parts: list[str] = []
    for key, value in properties.items():
        encoded_key = quote(str(key), safe="")
        encoded_value = quote(str(value), safe="")
        parts.append(f"{encoded_key}={encoded_value}")

    return "?" + "&".join(parts)

def ensure_trailing_slash(url: str) -> str:
    """Ensure the URL ends with a trailing slash.

    Args:
        url: The URL to normalize.

    Returns:
        The URL with a trailing slash.
    """
    if not url.endswith("/"):
        return url + "/"
    return url

def validate_non_empty_string(value: str, name: str) -> None:
    """
    Validate that a string is not empty or None.

    Args:
        value: The string to validate.
        name: The name of the parameter (for error messages).
    Raises:
        InvalidArgumentError: If the string is empty or None.
    """
    if not value or value.isspace():
        raise InvalidArgumentError(f"{name} is required and cannot be empty or whitespace")
