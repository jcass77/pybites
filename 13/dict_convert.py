from collections import namedtuple
from datetime import datetime
import json
from json import JSONEncoder, JSONDecoder
from json.decoder import WHITESPACE
from typing import MutableMapping, Any, Callable

blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here
Blog = namedtuple("blog", blog.keys())


class BlogEncoder(JSONEncoder):
    def encode(self, o: Any) -> str:
        dict_ = o._asdict()
        dict_["started"] = o.started.isoformat()

        return super().encode(dict_)


class BlogDecoder(JSONDecoder):
    def decode(self, s: str, _w: Callable[..., Any] = WHITESPACE.match) -> Any:
        o = super().decode(s, _w=_w)
        o["founders"] = tuple(o["founders"])
        o["started"] = datetime.fromisoformat(o["started"])

        return Blog._make(o.values())


def dict2nt(dict_: MutableMapping):
    return Blog._make(dict_.values())


def nt2json(nt: namedtuple):
    return json.dumps(nt, cls=BlogEncoder)
