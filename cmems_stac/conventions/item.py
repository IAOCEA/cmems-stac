import re

id_ = re.compile(
    r"""
    (?P<origin>[a-z0-9]+)
    _(?P<group>[a-z]+)
    (?:-(?P<pc>[a-z]+))?
    _(?P<area>[a-z]+)
    _(?P<thematic>[a-z]+)
    (?:-(?P<var>[a-z]+))?
    _(?P<type>[a-z]+)
    (?:_(?P<complementary_info>(?:
        -?[a-z]+(?#complementary info)
        |-?[0-9.]+km|0\.25deg|hr (?#spatial resolution)
        |-?[a-z0-9]+  (?#data level)
        |-?[a-zA-Z0-9]+(?#platform)
        |-?[a-z]+  (?#insitu data type)
        |-?[0-9]D  (?#number of spatial dimensions)
    )+))?
    _(?P<temporal_resolution>[A-Z0-9a-z.]{3,})
    (?:-(?P<typology>[im]))?
    """,
    flags=re.VERBOSE,
)
