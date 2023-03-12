from aqt import mw
from aqt.flags import FlagManager

import os


def getCurrentAddonName():
    fPath = os.path.dirname(os.path.abspath(__file__))
    fPath = fPath.replace(os.sep, '/')
    fPathParts = fPath.split('/')
    addons21Index = fPathParts.index('addons21')
    return fPathParts[addons21Index + 1]

def getDefaultLabel(flag_index: int) -> str:
    """
    :param flag_index: The integer by which the flag is represented internally (1-7).
    :return: label: The default label
    """
    try:
        flag = FlagManager.get_flag(flag_index)
        label = flag.label
    finally:
        return label or ''


def getConfig(key, flag_index: int):
    addonName = getCurrentAddonName()
    config = mw.addonManager.getConfig(addonName)
    defaultLabel = getDefaultLabel(flag_index)

    if not config:
        return defaultLabel

    return config.get(key, defaultLabel)


def setConfig(key, value):
    addonName = getCurrentAddonName()
    config = mw.addonManager.getConfig(addonName)
    if config is None:
        config = {}
    config[key] = value
    mw.addonManager.writeConfig(addonName, config)
