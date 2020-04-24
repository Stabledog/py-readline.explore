
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
              f'begin={begin}' +
              f'end={end}' +
              f'being_completed={being_completed}' +
              f'words={words}')
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

                except:
                    #

