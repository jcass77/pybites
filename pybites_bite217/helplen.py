from contextlib import redirect_stdout
from io import StringIO
from types import BuiltinFunctionType


def get_len_help_text(builtin: BuiltinFunctionType) -> int:
    if type(builtin) is not BuiltinFunctionType:
        raise ValueError("'builtin' must be of type 'BuiltinFunctionType'")

    f = StringIO()
    with redirect_stdout(f):
        help(builtin)
        return len(f.getvalue())
