#!/usr/bin/env python3.7


import quiklog

logger = quiklog.Quiklog()

class SimpleCompleter:
    def __init__(self,options):
        self.options=sorted(options)
        self.matches=None

    def complete(self, text, state):
        response = None
        # this is the first time for this text,
        # so build a match list:
        if text:
            self.matches = [ s for s in self.options if s and s.startswith(text) ]

            logger.debug('%s matches: %s',repr(text),self.matches)
        else:
            self.matches = self.options[:]
            logger.debug('(empty input) matches: %s',self.matches)

if __name__ == "__main__":
    pass
