import re
from pathlib import Path


README_PATH = Path(__file__).resolve().parents[2] / "README.md"
REPO_LINK_PREFIX = "https://github.com/djeada/Numerical-Methods/"


def test_readme_has_no_empty_href_attributes():
    hrefs = re.findall(r'href="([^"]*)"', README_PATH.read_text())

    assert all(href for href in hrefs)


def test_readme_repo_links_point_to_existing_paths():
    readme_text = README_PATH.read_text()
    hrefs = re.findall(r'href="([^"]*)"', readme_text)

    missing_paths = []

    for href in hrefs:
        if not href.startswith(REPO_LINK_PREFIX):
            continue

        relative_path = re.sub(
            r"^https://github\.com/djeada/Numerical-Methods/(?:blob|tree)/master/",
            "",
            href,
        )

        if relative_path and not (README_PATH.parent / relative_path).exists():
            missing_paths.append(relative_path)

    assert not missing_paths
