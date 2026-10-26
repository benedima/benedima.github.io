"""Check local resource paths, fragment links and basic document structure."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.h1_count = 0
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1_count += 1
        for key in ("href", "src"):
            if key in attrs:
                self.refs.append(attrs[key])

parser = SiteParser()
parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
assert parser.lang == "en-GB", "Missing document language"
assert parser.h1_count == 1, "Expected exactly one h1"
for ref in parser.refs:
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        assert url.scheme in {"https", "mailto"}, f"Unexpected external scheme: {ref}"
        continue
    if url.path:
        target = ROOT / unquote(url.path.lstrip("/"))
        assert target.is_file(), f"Missing local file: {ref}"
    elif url.fragment:
        assert url.fragment in parser.ids, f"Missing fragment: {ref}"
    else:
        raise AssertionError(f"Empty link: {ref}")
print("Local assets, fragment links, heading count and language checks passed.")
