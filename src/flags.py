from .utils.configrw import getConfig
from aqt import mw
from collections import namedtuple

FlagDef = namedtuple("FlagDef", [
    "configKey",
    "defaultColor",
    "defaultLabel"
])

flagDefs = {
    1: FlagDef("redText", "rgb(255, 102, 102)", "Hard problem"),
    2: FlagDef("orangeText", "rgb(255, 153, 0)", ""),
    3: FlagDef("greenText", "rgb(119, 255, 119)", "Controversial"),
    4: FlagDef("blueText", "rgb(119, 170, 255)", "Maybe check later?"),
    5: FlagDef("pinkText", "rgb(240, 151, 228)", ""),
    6: FlagDef("turquoiseText", "rgb(92, 207, 202)", ""),
    7: FlagDef("purpleText", "rgb(159, 99, 211)", ""),
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
        defaultLabel = flag.label or flagDefs[flag_index].defaultLabel
    except (ImportError, AttributeError):
        defaultLabel = flagDefs[flag_index].defaultLabel

    # Return defaultLabel in case flagLabel = ""
    # Note: we can't use getConfig's default key, cause
    # there are valid defined values on config.json ("")
    flagLabel = getConfig(flagDefs[flag_index].configKey)
    return flagLabel or defaultLabel
