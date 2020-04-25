
import readline
import quiklog

logger = quiklog.Quiklog()

class BufferAwareCompleter:
    def __init__(self,options):
        self.options = options
        self.current_candidates = []

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text,
            # so build a match list.
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logger.debug(f'origline={origline}\n' +
              f'begin={begin}\n' +
              f'end={end}\n' +
              f'being_completed={being_completed}\n' +
              f'words={words}\n')
            if not words:
                self.current_candidates = sorted( self.options.keys() )
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.options.keys()
                    else:
                        # later word
                        first  = words[0]
                        candidates = self.options[first]
                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [
                            w for w in candidates if w.startswith(being_completed)
                        ]
                    else:
                        # matching empty string,
                        # use all candidates:
                        self.current_candidates = candidates

                    logger.debug(f'candidates={self.current_candidates}')

                except (KeyError,IndexError) as err:
                    logger.error(f'completion error: {err}')
                    self.current_candidates = []
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logger.debug(f'complete({text},{state}) => {response}')
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print(f'Dispatch {line}')

# Register our completer function
completer = BufferAwareCompleter({
    'list': ['files','directories'],
    'print': ['byname', 'bysize'],
    'stop': [] }
    )

readline.set_completer(completer.complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

# Prompt the user for text
input_loop()

