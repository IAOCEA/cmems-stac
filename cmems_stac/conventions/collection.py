import re

mfc_id = re.compile(
    r"""
    (?P<geographical_area>[A-Z]+)
    _(?P<product_type>[A-Z]+)
    _(?P<thematic>[A-Z]+)
    (?:_(?P<complementary_info>[A-Z]+))?
    _(?P<center_ranking>[0-9]{3})
    _(?P<center_id>[0-9]{3})
    """,
    flags=re.VERBOSE,
)
tac_id = re.compile(
    r"""
    (?P<observation_type>[A-Z]+)
    _(?P<geographical_area>[A-Z]+)
    _(?P<thematic>[A-Z]+)
    (?:_(?P<complementary_info>[A-Z]+))??
    _(?P<kind_product>[A-Z0-9]+)
    _(?P<product_type>[A-Z]+)
    _(?P<center_ranking>[0-9]{3})
    _(?P<center_id>[0-9]{3})
    """,
    flags=re.VERBOSE,
)
old_tac_id = re.compile(
    r"""
    (?P<observation_type>[A-Z]+)
    _(?P<geographical_area>[A-Z]+)
    _(?P=observation_type)
    _(?P<kind_product>[A-Z0-9]+)
    _(?P<product_type>[A-Z]+)
    _(?P<complementary_info>[A-Z]+)
    _(?P<center_ranking>[0-9]{3})
    _(?P<center_id>[0-9]{3})
    """,
    flags=re.VERBOSE,
)
