# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> SEVEREM

- AUTHOR:     Doramas García Jorge
- EMAIL:      doramas.dev@pm.me
- GITHUB:     https://github.com/doramasgarciajorge
- REPOSITORY: https://github.com/doramasgarciajorge/saverem
------------------------------------------------------------
"""

# Saverem imports
from saverem import Saverem


if __name__ == '__main__':
    saverem = Saverem(
        "Remember to save the game", 300, 150, 0.5)
    saverem.start_reminder()
