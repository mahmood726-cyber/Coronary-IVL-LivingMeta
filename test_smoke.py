"""Minimal smoke test for the Coronary-IVL living meta-analysis dashboard.

This repo ships a single-file HTML dashboard (CORONARY_IVL_REVIEW.html) plus an
index.html redirect. There is no build step and the statistics engine lives
inline. This smoke test asserts the deployable invariants that have bitten this
class of single-file dashboard before: BOM, unbalanced static-HTML divs,
unbalanced <script> tags, unfilled placeholder tokens, and external CDN
references that lack Subresource Integrity.

Run: python -m pytest -q   (or)   python test_smoke.py
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(ROOT, "CORONARY_IVL_REVIEW.html")
INDEX = os.path.join(ROOT, "index.html")


def _read(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    assert raw[:3] != b"\xef\xbb\xbf", f"{os.path.basename(path)} has a UTF-8 BOM"
    return raw.decode("utf-8", errors="replace")


def test_files_exist():
    assert os.path.exists(MAIN), "main dashboard file missing"
    assert os.path.exists(INDEX), "index.html redirect missing"


def test_no_bom_and_decodes():
    _read(MAIN)
    _read(INDEX)


def test_script_tags_balanced():
    s = _read(MAIN)
    opens = len(re.findall(r"<script\b", s))
    closes = len(re.findall(r"</script>", s))
    assert opens == closes, f"<script> tags unbalanced: {opens} open vs {closes} close"


def test_static_html_divs_balanced():
    # Divs emitted inside JS template strings need not balance statically, so
    # strip <script> blocks before counting.
    s = _read(MAIN)
    no_js = re.sub(r"<script\b[^>]*>.*?</script>", "", s, flags=re.S | re.I)
    opens = len(re.findall(r"<div[\s>]", no_js))
    closes = len(re.findall(r"</div>", no_js))
    assert opens == closes, f"static-HTML divs unbalanced: {opens} open vs {closes} close"


def test_no_unfilled_placeholder_tokens():
    s = _read(MAIN)
    # Tokens assembled at runtime so this negative-test fixture does not itself
    # contain the literal placeholder strings it scans for.
    tokens = ("REPLACE" + "_ME", "__PLACE" + "HOLDER__", "{{" + "REPLACE", "TODO" + "_FILL")
    for token in tokens:
        assert token not in s, f"unfilled placeholder token present: {token}"


def test_external_cdn_links_have_sri():
    # Any cdnjs/jsdelivr/unpkg <link>/<script> in a deployable offline-first
    # dashboard must carry an integrity attribute.
    s = _read(MAIN)
    pattern = re.compile(
        r"<(?:link|script)\b[^>]*\b(?:href|src)=\"https://"
        r"(?:cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|unpkg\.com)[^>]*>",
        re.I,
    )
    for tag in pattern.findall(s):
        assert "integrity=" in tag, f"external CDN tag lacks SRI: {tag[:120]}"


def test_stat_engine_functions_present():
    # Guard against an accidental deletion of the pooling engine.
    s = _read(MAIN)
    for fn in ("function poolWith", "function pauleMandelTau2", "function binaryEffect"):
        assert fn in s, f"expected stat function missing: {fn}"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
    print(f"\n{len(fns) - failed} passed, {failed} failed")
    raise SystemExit(1 if failed else 0)
