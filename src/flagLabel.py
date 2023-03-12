from .utils.configrw import getConfig
from aqt import mw

_flagKeys = {
    1: "redText",
    2: "orangeText",
    3: "greenText",
    4: "blueText",
    5: "pinkText",
    6: "turquoiseText",
    7: "purpleText",
}


def getFlagLabel(flag_index: int):
    """
    :param configKey: config.json key string
    :param flag_index: The integer by which the flag is represented internally (1-7).
    :return: label: The default label
    """
    try:
        # FlagManager is for anki 2.1.45+ only
        flag = mw.flags.get_flag(flag_index)
        defaultLabel = flag.label
    except (ImportError, AttributeError):
        defaultLabel = ""

    # Return defaultLabel in case flagLabel = ""
    # Note: we can't use getConfig's default key, cause
    # there are valid defined values on config.json ("")
    flagLabel = getConfig(_flagKeys[flag_index])
    return flagLabel or defaultLabel
