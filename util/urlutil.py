from urllib.parse import quote, unquote


def escape(s):
    return quote(s)


def unescape(s):
    return unquote(s)
