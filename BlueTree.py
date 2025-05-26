#you need to install colorama
# 💙
#pip install colorama or apt install python3-colorama
import os
import sys
import re
import stat
import json
import time
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init
print(
    """\x1b[0;5;37;47m                        .;t:...                   \x1b[0m
\x1b[0;5;37;47m  .  . .  .  . . .%\x1b[0;1;37;47m8\x1b[0;5;37;47mt%\x1b[0;1;37;47m8\x1b[0;5;37;47m;%\x1b[0;1;37;47mS\x1b[0;1;36;47m8\x1b[0;1;30;47m@\x1b[0;36;47m8\x1b[0;1;37;47mt8\x1b[0;5;37;47mt. . . .  . .  . .  \x1b[0m
\x1b[0;5;37;47m   .  :;.. .;\x1b[0;1;37;47m8X\x1b[0;1;30;47m \x1b[0;1;37;47m88\x1b[0;1;30;46m8@88;@\x1b[0;34;46mX8888@%\x1b[0;36;47m8\x1b[0;1;37;47mX\x1b[0;36;47m88\x1b[0;1;37;47m;\x1b[0;1;36;47mX\x1b[0;1;37;47m;\x1b[0;5;37;47mS.     .    \x1b[0m
\x1b[0;5;37;47m     :\x1b[0;1;37;47m8\x1b[0;1;30;47m \x1b[0;1;37;47m:t8S\x1b[0;36;47mX\x1b[0;1;30;46m8X;8\x1b[0;36;47m8\x1b[0;1;30;46m8%%\x1b[0;36;44mX\x1b[0;1;30;44m8\x1b[0;36;44m@8\x1b[0;32;40m8\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;34;46m8888\x1b[0;36;44m88\x1b[0;1;30;46m8\x1b[0;1;37;47m:\x1b[0;5;37;47mXS;  .    .  \x1b[0m
\x1b[0;5;37;47m .  .:@\x1b[0;1;37;47m:\x1b[0;1;30;46m8888\x1b[0;5;36;40mt88\x1b[0;30;44m8\x1b[0;1;30;46m%\x1b[0;36;44m8\x1b[0;1;30;44m8\x1b[0;34;40m8\x1b[0;1;30;46m.\x1b[0;34;40mX\x1b[0;30;44m8\x1b[0;36;42m8\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;1;30;46m \x1b[0;34;40m@\x1b[0;34;46m8\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;30;44mX\x1b[0;36;44m@\x1b[0;30;44m8\x1b[0;36;44m88\x1b[0;34;46m8\x1b[0;1;34;46m8\x1b[0;36;47m8\x1b[0;5;37;47m8:..  .   \x1b[0m
\x1b[0;5;37;47m   ;@\x1b[0;1;37;47m;\x1b[0;1;30;47mX\x1b[0;1;30;46m8\x1b[0;5;36;40m:88\x1b[0;36;44m@\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;1;30;46m.\x1b[0;34;40m@\x1b[0;5;32;40mX\x1b[0;34;40m8\x1b[0;32;46m8\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;1;30;46m \x1b[0;34;40m8\x1b[0;30;44mX\x1b[0;36;44m8\x1b[0;32;40m@\x1b[0;36;44mX\x1b[0;34;40m@\x1b[0;30;44m88\x1b[0;1;30;46m \x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;32;40m@\x1b[0;36;44m@\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;1;30;44m8\x1b[0;36;44m88\x1b[0;1;30;46m8\x1b[0;1;36;47m@\x1b[0;1;30;46m8\x1b[0;1;37;47m.\x1b[0;5;37;47m8:    \x1b[0m
\x1b[0;5;37;47m  .:\x1b[0;1;37;47mX\x1b[0;1;30;47mX\x1b[0;5;36;40m888\x1b[0;34;40m@8\x1b[0;36;42m8\x1b[0;30;44m8\x1b[0;5;34;40mS\x1b[0;32;40m8\x1b[0;34;46m8\x1b[0;30;44m8\x1b[0;32;46m8\x1b[0;30;44m@\x1b[0;34;46m@\x1b[0;32;40m8\x1b[0;30;44mS\x1b[0;34;46m8\x1b[0;32;40m@\x1b[0;36;44mS\x1b[0;30;44m88\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;30;44m88\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m@\x1b[0;30;44m88\x1b[0;34;46m8\x1b[0;1;30;44m8\x1b[0;36;44m%8\x1b[0;37;46mX\x1b[0;1;37;47mS\x1b[0;5;37;47mt. .  \x1b[0m
\x1b[0;5;37;47m .@\x1b[0;1;37;47m:\x1b[0;5;37;40m8\x1b[0;5;36;40mXX\x1b[0;1;30;40m8\x1b[0;5;32;40mX\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;5;34;40mS\x1b[0;30;44m8\x1b[0;32;46m8\x1b[0;30;44m@\x1b[0;36;42m8\x1b[0;30;44m@X\x1b[0;34;46m8\x1b[0;34;40m@\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;30;44m88\x1b[0;34;46m8\x1b[0;34;40m@\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m@\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;30;44m@\x1b[0;36;44m@X8\x1b[0;37;46mX\x1b[0;1;36;47m%\x1b[0;5;37;47mS   \x1b[0m
\x1b[0;5;37;47m.\x1b[0;1;37;47m8\x1b[0;1;30;47m%\x1b[0;5;33;40m:\x1b[0;5;32;40m@S\x1b[0;1;30;40m8\x1b[0;34;46m8\x1b[0;32;40mX\x1b[0;34;46m8\x1b[0;1;30;42m8\x1b[0;36;44m8\x1b[0;30;42m8\x1b[0;36;44m@\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;30;42m8\x1b[0;36;44m@\x1b[0;34;40mX\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m@\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40mS\x1b[0;36;44m8\x1b[0;32;40mX\x1b[0;30;44mX88\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m@8\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;34;46m8\x1b[0;36;47mX\x1b[0;1;37;47m;\x1b[0;5;37;47mS.  \x1b[0m
\x1b[0;5;37;47m.S\x1b[0;1;30;47mX\x1b[0;5;33;40m%\x1b[0;5;32;40mX\x1b[0;5;34;40m@\x1b[0;5;32;40m8\x1b[0;34;40m8\x1b[0;5;36;40m8\x1b[0;34;40m@8\x1b[0;1;30;42m8\x1b[0;36;44mX\x1b[0;32;40m8\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m@\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;32;40mX\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;34;40m@\x1b[0;36;44m8\x1b[0;34;40m88\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;30;44mS@\x1b[0;34;46m8\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;1;30;44mX\x1b[0;34;46m8\x1b[0;37;46m@\x1b[0;5;37;47m8%.\x1b[0m
\x1b[0;5;37;47m;\x1b[0;1;37;47mt\x1b[0;5;37;40mX\x1b[0;5;33;40m@\x1b[0;5;32;40m8\x1b[0;1;30;40m8\x1b[0;1;30;44m8\x1b[0;30;42m8\x1b[0;36;44mX\x1b[0;30;42m8\x1b[0;36;44m8\x1b[0;30;44m8\x1b[0;5;36;40m8\x1b[0;30;44m8\x1b[0;36;42m8\x1b[0;30;44m8\x1b[0;36;42m8\x1b[0;30;44m@\x1b[0;34;46m8\x1b[0;34;40m@8\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;36;44m@\x1b[0;34;40m@\x1b[0;34;46m8\x1b[0;34;40m@\x1b[0;36;44m8\x1b[0;32;40m@\x1b[0;36;44mX\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;34;40mS\x1b[0;30;44m@\x1b[0;36;44m8\x1b[0;34;40m@8\x1b[0;34;46m8\x1b[0;34;40mS\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;36;44m@\x1b[0;30;44m8\x1b[0;36;44m8\x1b[0;1;30;46m8\x1b[0;1;37;47m \x1b[0;5;37;47mS.\x1b[0m
\x1b[0;5;37;47m @\x1b[0;1;30;47m8\x1b[0;5;33;40mt\x1b[0;5;34;40mS\x1b[0;5;32;40m8\x1b[0;34;40m8\x1b[0;5;36;40m8\x1b[0;34;40m8\x1b[0;36;44m@\x1b[0;34;40m@\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;1;30;46m:\x1b[0;34;40m8\x1b[0;5;34;40mS\x1b[0;30;44m88\x1b[0;34;40m8\x1b[0;34;46m8\x1b[0;34;40m@8\x1b[0;34;46m8\x1b[0;34;40mX\x1b[0;30;44m88\x1b[0;1;30;46m.\x1b[0;30;44m8\x1b[0;36;44mX\x1b[0;1;30;44m8\x1b[0;36;44m8\x1b[0;34;40mX\x1b[0;36;44m@\x1b[0;34;40m@8\x1b[0;34;46m8\x1b[0;34;40m@8\x1b[0;36;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;34;40mS\x1b[0;30;44m8\x1b[0;34;40m8\x1b[0;36;44m8\x1b[0;1;30;44m8\x1b[0;34;46m@\x1b[0;1;36;47m8\x1b[0;1;37;47m;\x1b[0;5;37;47m;\x1b[0m
\x1b[0;5;37;47m;\x1b[0;1;37;47mS\x1b[0;5;37;40m8\x1b[0;5;33;40m:S\x1b[0;5;30;40m@\x1b[0;5;32;40mX\x1b[0;34;40m8\x1b[0;5;30;40mS\x1b[0;34;40m8\x1b[0;32;46m8\x1b[0;30;44m8\x1b[0;1;30;44m8\x1b[0;34;40m8\x1b[0;36;44m@\x1b[0;34;40m8\x1b[0;32;46m@\x1b[0;36;44m8\x1b[0;32;40m8\x1b[0;36;44m@\x1b[0;36;42m8\x1b[0;30;44m88\x1b[0;34;46m8\x1b[0;30;44m8\x1b[0;5;34;40mS\x1b[0;30;44m@\x1b[0;1;30;46m8\x1b[0;5;37;40m8\x1b[0;34;46m8\x1b[0;1;30;44m8\x1b[0;34;40m8\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;34;40m@8\x1b[0;36;44m8\x1b[0;34;40m@8\x1b[0;36;44m8\x1b[0;34;40mS\x1b[0;30;44m@\x1b[0;36;44m8\x1b[0;34;40m@8\x1b[0;36;44m8\x1b[0;1;30;44m8\x1b[0;36;47m8\x1b[0;5;37;47m8t\x1b[0m
\x1b[0;5;37;47m%\x1b[0;1;37;47m \x1b[0;1;30;47m:8\x1b[0;5;33;40m;\x1b[0;5;30;40mX\x1b[0;5;34;40m8\x1b[0;32;40m8\x1b[0;36;44m@\x1b[0;1;30;44m88\x1b[0;36;44m8\x1b[0;30;44m8\x1b[0;5;36;40m888\x1b[0;5;34;40m8X\x1b[0;36;44m8\x1b[0;30;44m8\x1b[0;5;34;40m8\x1b[0;1;30;46mS\x1b[0;1;30;44m8\x1b[0;5;34;40mS\x1b[0;1;30;46m@\x1b[0;36;44m8\x1b[0;5;36;40m;\x1b[0;1;37;47m:\x1b[0;1;30;46m8\x1b[0;5;36;40mS\x1b[0;36;44mS\x1b[0;30;44m8\x1b[0;1;30;46m:\x1b[0;34;40m8\x1b[0;1;30;44m8\x1b[0;30;44m88\x1b[0;1;30;46m.\x1b[0;30;44m88\x1b[0;36;44m8\x1b[0;34;40m@8\x1b[0;34;46m8\x1b[0;34;40m@\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;36;47m8\x1b[0;5;37;47mS \x1b[0m
\x1b[0;5;37;47m.@\x1b[0;1;37;47m.\x1b[0;5;37;40mX\x1b[0;5;33;40mt\x1b[0;5;32;40mS\x1b[0;5;34;40m8\x1b[0;1;30;44m8\x1b[0;1;30;40m8\x1b[0;5;36;40m88; %\x1b[0;5;34;40m@\x1b[0;5;36;40mt;t\x1b[0;1;30;47m8\x1b[0;5;36;40m8\x1b[0;1;30;47m8%\x1b[0;5;36;40m:\x1b[0;1;30;46m8\x1b[0;1;30;47m%\x1b[0;5;36;40m \x1b[0;1;30;46m8\x1b[0;1;30;47m88\x1b[0;5;34;40mX\x1b[0;5;36;40m8\x1b[0;1;30;44m8\x1b[0;5;36;40m8@\x1b[0;1;30;46m8\x1b[0;1;30;47m;\x1b[0;1;30;46m8\x1b[0;1;30;44m8\x1b[0;1;30;46mS\x1b[0;1;30;44m@\x1b[0;30;44m8\x1b[0;34;46m8\x1b[0;34;40m@8\x1b[0;1;30;46m \x1b[0;34;40m8\x1b[0;1;30;46m8\x1b[0;1;37;47m;\x1b[0;5;37;47mt \x1b[0m
\x1b[0;5;37;47m :S\x1b[0;1;37;47m;\x1b[0;1;30;47mXX\x1b[0;5;36;40m ::\x1b[0;5;37;40mX\x1b[0;1;30;47m8\x1b[0;1;37;47m:.\x1b[0;1;30;47m@\x1b[0;1;37;47m \x1b[0;5;37;47m8\x1b[0;1;37;47m \x1b[0;1;30;47m8\x1b[0;1;30;46m8\x1b[0;1;37;47m \x1b[0;5;36;40mt\x1b[0;1;30;47m8\x1b[0;1;37;47m \x1b[0;5;36;40m.\x1b[0;5;37;47m8\x1b[0;1;30;47mX\x1b[0;1;34;44m@\x1b[0;1;30;47mt\x1b[0;36;47m8\x1b[0;35;44mX\x1b[0;1;30;47m8%\x1b[0;1;37;47m  \x1b[0;1;30;47m8\x1b[0;37;46m8\x1b[0;1;30;47m88@\x1b[0;1;37;47m \x1b[0;1;30;46m8\x1b[0;5;36;40m@\x1b[0;36;44m8\x1b[0;30;44m8\x1b[0;5;34;40mS\x1b[0;34;46m@\x1b[0;1;30;47mS\x1b[0;5;37;47m8.  \x1b[0m
\x1b[0;5;37;47m   :.%\x1b[0;1;37;47m .888\x1b[0;5;37;47m8\x1b[0;1;37;47m8\x1b[0;5;37;47m8tX888\x1b[0;1;30;47m8\x1b[0;5;36;44mS\x1b[0;1;37;47m \x1b[0;36;47m8\x1b[0;1;37;47m \x1b[0;5;37;47m8\x1b[0;5;36;40m \x1b[0;1;30;46m8\x1b[0;35;47m8\x1b[0;36;44m8\x1b[0;5;37;47m8@88\x1b[0;1;30;47m8\x1b[0;36;47mX\x1b[0;1;37;47m ;t\x1b[0;5;37;47m8\x1b[0;1;37;47mS\x1b[0;1;30;47mt8\x1b[0;1;30;46mt\x1b[0;5;36;40m8\x1b[0;1;30;47m@\x1b[0;5;37;47m@.  \x1b[0m
\x1b[0;5;37;47m  . .S@t:;XSt: ..;t8\x1b[0;1;30;47m8\x1b[0;5;36;40m%\x1b[0;1;30;45m8\x1b[0;5;37;47m8\x1b[0;1;36;47mS\x1b[0;35;47m@\x1b[0;1;30;46m8\x1b[0;1;30;44m8\x1b[0;1;37;47m;\x1b[0;5;37;47m8\x1b[0;1;37;47m. \x1b[0;5;37;47m88@88888XX8\x1b[0;1;37;47m  \x1b[0;5;37;47mX  . \x1b[0m
\x1b[0;5;37;47m      .         .  .%\x1b[0;1;30;47mX\x1b[0;36;44m8\x1b[0;5;37;47m8\x1b[0;1;30;47m8\x1b[0;36;47mS\x1b[0;1;34;44m@\x1b[0;1;30;47m8\x1b[0;1;37;47m:\x1b[0;5;37;47m@..;::;%;;.. .:. .   \x1b[0m
\x1b[0;5;37;47m  .    .      .   . .t\x1b[0;1;30;46m8\x1b[0;1;30;45m8\x1b[0;36;47m@\x1b[0;1;34;44mt\x1b[0;5;36;40m \x1b[0;5;37;47m%      .  .     .    . \x1b[0m
\x1b[0;5;37;47m    .   .        .    8\x1b[0;36;44m8\x1b[0;1;30;44m8S\x1b[0;1;37;47mX\x1b[0;5;37;47m  .  .     .  .   .    \x1b[0m
\x1b[0;5;37;47m      .      . .    .:.8\x1b[0;36;44m@\x1b[0;5;36;40m8\x1b[0;5;37;47m8.  .   . .      .   .  \x1b[0m
\x1b[0;5;37;47m .  .   .         .   :\x1b[0;1;37;47m%\x1b[0;5;34;40m@\x1b[0;1;30;44mS\x1b[0;1;37;47m.\x1b[0;5;37;47m .         . .    .   .\x1b[0m"""
)
# Initialize colorama
init(autoreset=True)


def get_dir_size(path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except:
                continue
    return total


def is_hidden(path):
    name = os.path.basename(path)
    if name.startswith('.'):
        return True
    try:
        attrs = os.stat(path).st_file_attributes
        return bool(attrs & stat.FILE_ATTRIBUTE_HIDDEN)
    except AttributeError:
        return False


def clean_ansi_codes(text):
    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)


def get_yes_no(prompt):
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'")


def convert_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"


def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_symlink_target(path):
    try:
        return os.readlink(path)
    except OSError as e:
        return f"[Error: {str(e)}]"
    except AttributeError:
        return "[Unsupported]"


def export_json(tree_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(tree_data, f, indent=2)
    print(f"{Fore.GREEN}JSON structure saved to: {Fore.CYAN}{output_path}{Style.RESET_ALL}")


def export_html(tree_data, output_path):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Directory Tree: {tree_data['name']}</title>
        <style>
            .tree {{ font-family: monospace; padding: 20px; }}
            .dir {{ color: #2196F3; cursor: pointer; }}
            .file {{ color: #4CAF50; }}
            .symlink {{ color: #9C27B0; }}
            .collapsed {{ display: none; }}
        </style>
    </head>
    <body>
        <div class="tree" id="tree">{build_html_nodes(tree_data)}</div>
        <script>
            function toggle(e) {{
                const parent = e.parentElement;
                const children = parent.querySelector('.children');
                if(children) children.classList.toggle('collapsed');
                e.textContent = children?.classList.contains('collapsed') ? '▶' : '▼';
            }}
        </script>
    </body>
    </html>
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"{Fore.GREEN}HTML structure saved to: {Fore.CYAN}{output_path}{Style.RESET_ALL}")


def build_html_nodes(node):
    html = []
    if node['type'] == 'directory':
        html.append(f'<div class="dir" onclick="toggle(this)">▼ {node["name"]}</div>')
        html.append('<div class="children">')
        for child in node['children']:
            html.append(build_html_nodes(child))
        html.append('</div>')
    elif node['type'] == 'symlink':
        html.append(f'<div class="symlink">{node["name"]} → {node["target"]}</div>')
    else:
        size = f" ({convert_size(node['size'])})" if 'size' in node else ''
        html.append(f'<div class="file">{node["name"]}{size}</div>')
    return '\n'.join(html)


def get_tree_structure(root_dir, exclude_dirs=None, max_depth=None,
                       include_size=False, include_counts=False,
                       include_date=False, use_color=False,
                       include_hidden=False, sort_method='alphabetical',
                       sort_order='ascending', export_format='text'):
    tree = []
    exclude_dirs = set(exclude_dirs or [])
    dir_count = 0
    file_count = 0
    total_size = 0

    colors = {
        'dir': Fore.BLUE if use_color else '',
        'file': Fore.YELLOW if use_color else '',
        'link': Fore.MAGENTA if use_color else '',
        'meta': Fore.LIGHTBLACK_EX if use_color else '',
        'reset': Style.RESET_ALL if use_color else ''
    }

    def add_line(entry, depth, is_last, is_dir, last_in_level, meta=None):
        indent = ""
        for i in range(depth):
            if i == depth - 1:
                indent += "└── " if is_last else "├── "
            else:
                indent += "    " if last_in_level.get(i, False) else "│   "

        if is_dir:
            line = f"{colors['dir']}{indent}{entry}/{colors['reset']}"
        else:
            meta_str = f"{colors['meta']}({', '.join(meta)}){colors['reset']}" if meta else ""
            line = f"{colors['file']}{indent}{entry}{colors['reset']} {meta_str}"
        tree.append(line)

    def process_entry(entry, path, depth, last_in_level, is_last):
        nonlocal dir_count, file_count, total_size
        entry_path = os.path.join(path, entry)
        is_link = os.path.islink(entry_path)
        is_dir = os.path.isdir(entry_path) and not is_link

        if is_link:
            file_count += 1
            target = get_symlink_target(entry_path)
            meta = [f"link → {colors['link']}{target}{colors['reset']}"]
            if include_size:
                try:
                    file_size = os.path.getsize(entry_path)
                    total_size += file_size
                    meta.append(f"size: {convert_size(file_size)}")
                except:
                    pass
            add_line(entry, depth, is_last, False, last_in_level, meta)
        elif is_dir:
            dir_count += 1
            add_line(entry, depth, is_last, True, last_in_level)
            walk_directory(entry_path, depth + 1, last_in_level.copy())
        else:
            file_count += 1
            meta = []
            try:
                stat = os.stat(entry_path)
                if include_size:
                    file_size = stat.st_size
                    total_size += file_size
                    meta.append(f"size: {convert_size(file_size)}")
                if include_date:
                    meta.append(f"modified: {format_timestamp(stat.st_mtime)}")
            except Exception as e:
                meta.append(f"error: {str(e)}")
            add_line(entry, depth, is_last, False, last_in_level, meta)

    def walk_directory(path, depth=0, last_in_level=None):
        nonlocal dir_count, file_count, total_size
        last_in_level = last_in_level or {}

        if max_depth and depth > max_depth:
            return

        try:
            entries = []
            dirs = []
            files = []
            for entry in os.listdir(path):
                entry_path = os.path.join(path, entry)
                if entry in exclude_dirs:
                    continue
                if os.path.isdir(entry_path) and not os.path.islink(entry_path):
                    dirs.append(entry)
                else:
                    files.append(entry)

            if not include_hidden:
                dirs = [d for d in dirs if not is_hidden(os.path.join(path, d))]
                files = [f for f in files if not is_hidden(os.path.join(path, f))]

            if sort_method == 'size':
                dirs = sorted(dirs, key=lambda x: get_dir_size(os.path.join(path, x)),
                              reverse=(sort_order == 'descending'))
                files = sorted(files, key=lambda x: os.path.getsize(os.path.join(path, x)),
                               reverse=(sort_order == 'descending'))
            else:
                dirs.sort(key=lambda x: x.lower())
                files.sort(key=lambda x: x.lower())

            entries = dirs + files
            total_entries = len(entries)

            for index, entry in enumerate(entries):
                is_last = index == total_entries - 1
                current_last = last_in_level.copy()
                current_last[depth] = is_last
                process_entry(entry, path, depth, current_last, is_last)

        except PermissionError as e:
            tree.append(f"{colors['meta']} [Permission denied: {path}]{colors['reset']}")
        except Exception as e:
            tree.append(f"{colors['meta']} [Error: {str(e)}]{colors['reset']}")

    def build_export_structure(path):
        name = os.path.basename(path)
        if os.path.islink(path):
            return {
                'name': name,
                'type': 'symlink',
                'target': get_symlink_target(path)
            }
        if os.path.isdir(path):
            children = []
            try:
                for entry in sorted(os.listdir(path), key=lambda x: x.lower()):
                    children.append(build_export_structure(os.path.join(path, entry)))
            except Exception as e:
                children.append({'name': f"[Error: {str(e)}]", 'type': 'error'})
            return {
                'name': name,
                'type': 'directory',
                'children': children
            }
        return {
            'name': name,
            'type': 'file',
            'size': os.path.getsize(path)
        }

    # Start processing
    if export_format != 'text':
        return build_export_structure(root_dir)

    tree.append(f"{colors['dir']}{os.path.basename(root_dir)}/{colors['reset']}")
    walk_directory(root_dir)

    if include_counts:
        summary = [
            f"\n{colors['dir']}SUMMARY:{colors['reset']}",
            f"{colors['meta']}• Directories 🗃 : {dir_count}",
            f"{colors['meta']}• Files 📁 : {file_count}"
        ]
        if include_size:
            summary.append(f"{colors['meta']}• Total size: {convert_size(total_size)}")
        tree.append('\n'.join(summary))

    return '\n'.join(tree)


def get_valid_directory():
    while True:
        path_str = input("Enter directory 🗃 path to scan 🔍️ : ").strip()
        if not path_str:
            print(f"{Fore.RED}Error ❌ : Path cannot be empty{Style.RESET_ALL}")
            continue
        path = Path(path_str)
        if path.is_dir():
            return path
        print(f"{Fore.RED}Error ❌ : '{path_str}' is not a valid directory{Style.RESET_ALL}")


def get_output_method():
    print(f"\n{Fore.YELLOW}Output Options:{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX}1. Save to file📄")
    print(f"{Fore.LIGHTGREEN_EX}2. Print to terminal as text format📜")
    print(f"{Fore.LIGHTMAGENTA_EX}3. Both save and print📝")

    while True:
        choice = input(f"{Fore.CYAN}Choose destination (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print(f"{Fore.RED}Invalid choice ❌ . Please enter 1-3{Style.RESET_ALL}")


def main():
    print(f"{Fore.BLUE} 💙 Welcome to BlueTree, Directory 🌳 Generator 💙{Style.RESET_ALL}")

    path = get_valid_directory()
    output_choice = get_output_method()
    save_to_file = output_choice in [1, 3]
    print_to_terminal = output_choice in [2, 3]

    output_file = "bluetree"
    if save_to_file:
        output_file = input("Enter output file path (default: bluetree): ").strip() or "bluetree"

    exclude = input("Enter directories to exclude (comma-separated): ").strip()
    exclude_dirs = [x.strip() for x in exclude.split(',')] if exclude else []

    max_depth = input("Enter maximum depth (Enter for unlimited): ").strip()
    max_depth = int(max_depth) if max_depth.isdigit() else None

    print(f"\n{Fore.YELLOW}Sorting Options🔃:{Style.RESET_ALL}")
    sort_method = input("Sort by (a)lphabetical🔠 or (s)ize🚼️ [a/s]: ").strip().lower()
    sort_method = 'size' if sort_method == 's' else 'alphabetical'

    sort_order = 'ascending'
    if sort_method == 'size':
        sort_order = input("Sort order (a)scending↗️/(d)escending↘️ [a/d]: ").strip().lower()
        sort_order = 'descending' if sort_order == 'd' else 'ascending'

    print(f"\n{Fore.YELLOW}Export Format:{Style.RESET_ALL}")
    fmt_choice = input("Choose format [1]Text [2]JSON [3]HTML (default 1): ").strip() or '1'
    export_format = {'1': 'text', '2': 'json', '3': 'html'}.get(fmt_choice, 'text')

    print(f"\n{Fore.YELLOW}Additional Options:{Style.RESET_ALL}")
    include_hidden = get_yes_no("Include hidden files/directories🥸?")
    include_size = get_yes_no("Include file sizes🚼️?")
    include_date = get_yes_no("Include modification dates📅?")
    include_counts = get_yes_no("Include summary counts⌛?")
    use_color = get_yes_no("Use colored output?, works only with text file.\n🟢🔵🟣🟤⚫️⚪️") if print_to_terminal else False

    start_time = time.time()
    print(f"{Fore.BLUE}Irrigating the seed\n🚿\n🌱\n🌳{Style.RESET_ALL}")

    try:
        tree_data = get_tree_structure(
            root_dir=str(path),
            exclude_dirs=exclude_dirs,
            max_depth=max_depth,
            include_size=include_size,
            include_counts=include_counts,
            include_date=include_date,
            use_color=use_color,
            include_hidden=include_hidden,
            sort_method=sort_method,
            sort_order=sort_order,
            export_format=export_format
        )

        if save_to_file:
            if export_format == 'json':
                export_json(tree_data, output_file)
            elif export_format == 'html':
                export_html(tree_data, output_file)
            else:
                clean_tree = clean_ansi_codes(tree_data)
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with output_path.open('w', encoding='utf-8') as f:
                    f.write(clean_tree)
                print(f"{Fore.GREEN}Tree 🌳 saved to: {Fore.CYAN}{output_path.resolve()}{Style.RESET_ALL}")

        if print_to_terminal:
            print(f"\n{Fore.LIGHTMAGENTA_EX}🟣your 🌳 tree🟣{Style.RESET_ALL}")
            print(tree_data if export_format == 'text' else "Preview not available for JSON/HTML")

        print(f"\n{Fore.RED}=== 📚️Statistics📚️ ==={Style.RESET_ALL}")
        print(f"Elapsed time⌛️: {time.time() - start_time:.2f} seconds")
        print(Fore.BLUE + """                                        
██████╗ ██╗     ██╗   ██╗███████╗
██╔══██╗██║     ██║   ██║██╔════╝
██████╔╝██║     ██║   ██║█████╗  
██╔══██╗██║     ██║   ██║██╔══╝  
██████╔╝███████╗╚██████╔╝███████╗
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝                                    
████████╗██████╗ ███████╗███████╗
╚══██╔══╝██╔══██╗██╔════╝██╔════╝
   ██║   ██████╔╝█████╗  █████╗  
   ██║   ██╔══██╗██╔══╝  ██╔══╝  
   ██║   ██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
""")

    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
