from os import environ
from typing import Dict, Optional

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

class TokenParser:
    def __init__(self, config_file: Optional[str] = None):
        self.tokens = {}
        self.config_file = config_file

    def parse_from_env(self) -> Dict[int, str]:
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(
                    lambda n: n[0].startswith("MULTI_TOKEN"), sorted(environ.items())
                )
            )
        )
        return self.tokens

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2
