#!/usr/bin/env python3.7

import readline
import quiklog

logger = quiklog.Quiklog()

class SimpleCompleter:
    def __init__(self,options):
        self.options=sorted(options)
        self.matches=None

    def complete(self, text, state):
        response = None
        logger.debug(f"complete:{text}" )
        if state == 0:
            # this is the first time for this text,
            # so build a match list:
            if text:
                self.matches = [ s for s in self.options if s and s.startswith(text) ]

                logger.debug(f'{text} matches: {self.matches}')
            else:
                self.matches = self.options[:]
                logger.debug(f'(empty input) matches: {self.matches}')

        # Return the state'th item from the match list, if
        # we have that many.
        try:
            response = self.matches[ state ]
        except IndexError:
            response = None
        logger.debug(f'complete({text}, {state}) => {response}')
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print(f'Dispatch {line}')

logger.debug("Initializing...")
# Register the completer function
OPTIONS = ['start','stop','list','print']
readline.set_completer(SimpleCompleter(OPTIONS).complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

# Prompt the user for text:
input_loop()
