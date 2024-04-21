# from .files_utilities import *
from .handler import facade_handler
from .functions import send_msg, input_value

LOGO = """
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@     @@@  @@@ @@@ @@@ 
@@@     @@@  @@@          @@@          @@@  @@@              @@@      @@@     @@@  @@@ @   @@@      @@@     
@@@ @@@ @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@ @@@ @@@  @@@ @@@ @@@      @@@     
@@@     @@@          @@@          @@@  @@@          @@@      @@@      @@@     @@@  @@@   @ @@@      @@@     
@@@     @@@  @@@ @@@ @@@  @@@ @@@ @@@  @@@  @@@ @@@ @@@      @@@      @@@     @@@  @@@     @@@      @@@     

                                                                                   by Syntax Conquerors
"""

def main():
    msg = LOGO
    send_msg(msg)
    msg = 'Type "help" to get a command list.'
    send_msg(msg)
    while True:
        msg = '\nEnter your command: '
        command = input_value(msg)
        function_to_execute = facade_handler.function_runner(command)
        try:
            if command == 'exit':
                function_to_execute()
                break
            else:
                function_to_execute()
        except:
            continue
            
if __name__ == '__main__':
    main()