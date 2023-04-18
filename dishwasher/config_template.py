import hashlib
import datetime
import discord
import json

# Basic bot config, insert your token here, update description if you want, put owner IDs, and log channel ID.
prefixes = ["pws ", "dish "]
token = "token-goes-here"
bot_description = "Dishwasher, a spaghetti bot."
bot_managers = [120698901236809728]
bot_logchannel = 1006820351134683186

# If you forked Dishwasher, put your repo here
source_url = "https://github.com/vrnavi/dishwasher"
rules_url = "<#989959323771895880>"

# The bot description to be used in the about command.
embed_desc = (
    "Dishwasher is maintained by `renavi`, as a Dishwasher in her kitchen."
    " I am presently washing her dishes. I am also a fork of "
    "[robocop-ng](https://github.com/reswitched/robocop-ng)."
)

# The cogs the bot will load on startup.
initial_cogs = [
    "cogs.common",
    "cogs.admin",
    "cogs.appeal",
    "cogs.cotd",
    "cogs.explains",
    "cogs.mod",
    "cogs.mod_antiraid",
    "cogs.mod_archive",
    "cogs.mod_locks",
    "cogs.mod_oneshot",
    "cogs.mod_observation",
    "cogs.mod_note",
    "cogs.mod_userlog",
    "cogs.mod_timed",
    "cogs.mod_watch",
    "cogs.basic",
    "cogs.basic_oneshot",
    "cogs.logs",
    "cogs.remind",
    "cogs.reply",
    "cogs.dishtimer",
    "cogs.meme",
    "cogs.invites",
    "cogs.usertime",
    "cogs.prefixes",
    "cogs.burstreacts",
]

# == cogs.prefixes maximum prefixes. ==
maxprefixes = 6  # !max of 24!

# A mapping of role IDs to names.
named_roles = {
    "journal": 303555716109565955,
}

# Staff role.
staff_role_ids = [
    259199371361517569,
]
# Ex-Staff role.
exstaff_role_ids = [
    491431570251579412,
]
# Tossed/Rolebanned role.
toss_role_id = 257050851611377666
# Bot role.
bot_role = 257036973187923968

# Specific server configuration. Some cogs will default to the first in the list.
guild_configs = {
    # OneShot Discord
    256926147827335170: {
        "logs": {
            # Main Log Channel
            "logs_channel": 1095153813079457823,
            # Thread for moderation logs.
            "mlog_thread": 1095159750674624583,
            # Thread for server logs.
            "slog_thread": 1095159988814626966,
            # Thread for user logs.
            "ulog_thread": 1095160504470736987,
            # Channel for tracking watched users.
            "tracker_channel": 1095559009152536626,
        },
        "staff": {
            # Staff role.
            "staff_role": 259199371361517569,
            # Staff channel.
            "staff_channel": 256964111626141706,
            # [cogs.appeal] Ban appeal channel.
            "ban_appeal_channel": 402019542345449472,
            # [cogs.appeal] Ban appeal webhook ID.
            "ban_appeal_webhook_id": 402016472878284801,
        },
        "toss": {
            "toss_role": 257050851611377666,
            "toss_channels": [
                "basement",
                "abyss",
                "recycle-bin",
                "out-of-bounds",
            ],
        },
        "archive": {
            "drive_folder": "folder_goes_here",
            "unroleban_expiry": 180,
        },
        "lockdown": {
            # [cogs.lockdown]
        },
        "misc": {
            # [cogs.cotd] CoTD role.
            "cotd_role": 534976600454725632,
            # [cogs.cotd] CoTD name.
            "cotd_name": "Fluctuating Phosphor",
        },
    }
}

# Staff channel.
staff_channel = 256964111626141706

# These channel entries are used to determine which roles will be given
# access when we unlock them
general_channels = [
    256926147827335170,
    256970699581685761,
    257057492851228674,
    547150473363456020,
    270745381061525504,
    688183601233133650,
    350855217614553088,
    631612006826377226,
    256984616915828738,
    369934580465139712,
    256973430702866437,
    863599748622712872,
]  # Channels everyone can access

# Controls which roles are blocked during lockdown
lockdown_configs = {
    # Used as a default value for channels without a config, defaults to main guild's everyone role.
    "default": {"channels": general_channels, "roles": [guild_whitelist[0]]},
}

# Channels that will be cleaned every minute/hour.
# This feature isn't very good rn.
# See https://github.com/reswitched/robocop-ng/issues/23
minutely_clean_channels = []
hourly_clean_channels = []

# List of words that will be ignored if they match one of the
# suspect_words (This is used to remove false positives)
suspect_ignored_words = []
# == Only if you want to use cogs.pin ==
# Used for the pinboard. Leave empty if you don't wish for a gist pinboard.
github_oauth_token = ""

# Channels and roles where users can pin messages
allowed_pin_channels = []
allowed_pin_roles = []

# Channel to upload text files while editing list items. (They are cleaned up.)
list_files_channel = 0

# == Only if you want to use cogs.lists ==
# Channels that are lists that are controlled by the lists cog.
list_channels = []

# == Only if you want to use cogs.sar ==
self_assignable_roles = {}

# == Only if you want to use cogs.reply ==
noreply_role = 1059460475588448416

# == Only if you want to use cogs.mod_oneshot ==
pingmods_allow = [named_roles["journal"]] + staff_role_ids

# == Only if you want to use cogs.appeal ==
ban_appeal_channel = 402019542345449472
ban_appeal_webhook_id = 402016472878284801

# == Only if you want to use cogs.mod_antiraid ==
# Auto-mention threshold (Minimum to fire, inclusive) (set to 0 to disable)
mention_threshold = 5
# Recent join threshold - When reporting auto lockdowns, will also print a list of members who joined in the last n seconds. (set to 0 to disable)
recent_join_threshold = 20
# Announcement messages for lockdown/unlockdown. Set to `null` if unused.
lockdown_annoncement = "All public channels are temporarily restricted."
unlockdown_annoncement = "All public channels are no longer restricted."


# == Only if you want to use cogs.mod_toss and cogs.mod_archive ==
# Example for Toss role.
#    {
#        "role": 0,
#        "channel": 0
#    }
toss_role = 257050851611377666
# Names for the bot to use.
toss_channels = [
    "basement",
    "abyss",
    "recycle-bin",
    "out-of-bounds",
]
# Where the bot should place overflow channels.
# If it is a channel id, it will be placed under this channel.
# If it is a category id, it will be placed at the last spot.
toss_placement = 263715783782301696

# == Only if you want to use cogs.mod_archive ==
# == cogs.mod_toss must be configured for this to work!
# == Make sure to supply service_account.json!
# The Google Drive folder.
drive_folder = "folder_goes_here"
# The toss/roleban expiry timeout.


# Used for the bot's random options.
# No touch!
placeholders = json.load(open("assets/placeholders.json", "r"))
# Change this to set the playing type.
game_type = discord.ActivityType.listening
# This is a list of all the "games" to play.
game_names = placeholders["games"]
# These appear when doing pws quit.
death_messages = placeholders["deaths"]
# These appear when the bot tells you not to do a command to itself.
target_bot_messages = placeholders["if_target_bot"]
# These appear when the bot tells you not to do a command to yourself.
target_self_messages = placeholders["if_target_self"]
# Currently unused.
tarot_cards = placeholders["tarot"]
