"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of pybites_bite8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum
from functools import singledispatch
from typing import Union, Any


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}


# complete :
def check_bt(donor: Union[int, str, Bloodtype], recipient: Union[int, str, Bloodtype]):
    """Checks red blood cell compatibility based on pybites_bite8 blood types
    Args:
    donor (int | str | Bloodtype): red blood cell type of the donor
    recipient (int | str | Bloodtype): red blood cell type of the recipient
    Returns:
    bool: True for compatability, False otherwise.
    """
    compatibility = _particular_antigen_comp(
        get_blood_type_as_int(donor), get_blood_type_as_int(recipient)
    )
    return all(a >= 0 for a in compatibility)


@singledispatch
def get_blood_type_as_int(blood_type: Any):
    # No suitable handler found for this type.
    raise TypeError


@get_blood_type_as_int.register
def _(blood_type: Bloodtype):
    return blood_type.value


@get_blood_type_as_int.register
def _(blood_type: int):
    try:
        return Bloodtype(blood_type).value
    except KeyError:
        raise ValueError


@get_blood_type_as_int.register
def _(blood_type: str):
    try:
        return blood_type_text[blood_type].value
    except KeyError:
        raise ValueError


# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (pybites_bite1, pybites_bite1, pybites_bite1)    0- can donate to AB+
    _particular_antigen_comp(pybites_bite1, 3) -> (0, pybites_bite1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, pybites_bite5) -> (pybites_bite1, -pybites_bite1, pybites_bite1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-pybites_bite1, -pybites_bite1, -pybites_bite1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )
