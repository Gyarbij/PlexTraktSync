#!/usr/bin/env python3 -m pytest
from tests.conftest import get_plex_api

plex = get_plex_api()


def test_plex_search():
    search = plex.search("The Addams Family (1964)", libtype="show")
    results = [m for m in search]

    assert len(results) == 1

    m = results[0]
    assert m.type == "show"
    assert m.item.title == "The Addams Family (1964)"
    assert m.provider == "tvdb"
    assert m.id == "77137"
