# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://Rayan-Config.github.io/ALL",
    "https://url.medicaltreatment.ir/Ainita",
    "https://url.medicaltreatment.ir/GAFN-Hysteria",
    "https://raw.githubusercontent.com/gransa/Temp-Sub/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/Rayan-Config/HUB/refs/heads/main/H-I",
    "https://raw.githubusercontent.com/Rayan-Config/HUB/refs/heads/main/H-II",
    "https://raw.githubusercontent.com/Rayan-Config/HUB/refs/heads/main/H-III",
    "https://raw.githubusercontent.com/Rayan-Config/HUB/refs/heads/main/H-IV",
    "https://raw.githubusercontent.com/Rayan-Config/HUB/refs/heads/main/H-V",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 700

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": False,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 365
