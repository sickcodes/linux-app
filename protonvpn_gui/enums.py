from enum import Enum, auto


class IndicatorActionEnum(Enum):
    QUICK_CONNECT = 0
    DISCONNECT = 1
    SHOW_GUI = 2


class GLibEventSourceEnum(Enum):
    ON_MONITOR_VPN = "on_monitor_vpn"
    ON_MONITOR_NETWORK_SPEED = "on_monitor_network_speed"
    ON_SERVER_LOAD = "on_server_load"
    ON_EVENT = "on_event"


class DashboardFeaturesEnum(Enum):
    KILLSWITCH = 0
    NETSHIELD = 1
    SECURE_CORE = 2


class DashboardKillSwitchIconEnum(Enum):
    OFF = auto()

    ON_DEFAULT = auto()
    ALWAYS_ON_DEFAULT = auto()

    ON_DISABLE = auto()
    ALWAYS_ON_DISABLE = auto()

    ON_ACTIVE = auto()
    ALWAYS_ON_ACTIVE = auto()


class DashboardNetshieldIconEnum(Enum):
    OFF = auto()
    MALWARE_DEFAULT = auto()
    MALWARE_ADS_DEFAULT = auto()

    MALWARE_DISABLE = auto()
    MALWARE_ADS_DISABLE = auto()

    MALWARE_ACTIVE = auto()
    MALWARE_ADS_ACTIVE = auto()


class DashboardSecureCoreIconEnum(Enum):
    OFF = auto()
    ON_DEFAULT = auto()
    ON_DISABLE = auto()
    ON_ACTIVE = auto()
    CHEVRON = auto()


class GTKPriorityEnum(Enum):
    """GTK Constants

    https://developer.gnome.org/glib/stable/glib-The-Main-Event-Loop.html#G-PRIORITY-HIGH:CAPS
    """
    PRIORITY_HIGH = -100
    PRIORITY_DEFAULT = 0
    PRIORITY_HIGH_IDLE = 100
    PRIORITY_DEFAULT_IDLE = 200
    PRIORITY_LOW = 300
