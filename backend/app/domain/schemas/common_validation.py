import re
from typing import Optional


def validate_url(url: Optional[str]) -> Optional[str]:
    if url is None:
        return ''
    if re.fullmatch(r"https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+", url) is None:
        raise ValueError('malformed url: %s' % url)
    return url