#for preprocessing json file

import re
import sys
import json

CPP_PATTERN = re.compile(
    r"""
          (?P<comments>
                /\*[^*]*\*+(?:[^/*][^*]*\*+)*/  # multi-line comments
              | \s*//(?:[^\r\n])*               # single line comments
          )
        | (?P<code>
                "(?:\\.|[^"\\])*"               # double quotes
              | '(?:\\.|[^'\\])*'               # single quotes
              | .[^/"']*                        # everything else
          )
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL
)
        
def main():
    regex = CPP_PATTERN
        
    if(len(sys.argv) == 2):
        f = open(sys.argv[1], "r")
        text_with_comments = f.read()
        f.close()
    else:
        text_with_comments = ""
        for line in sys.stdin:
            text_with_comments = text_with_comments + line
        
    it = regex.finditer(text_with_comments)
    code_blocks = [m.groupdict()["code"] for m in it]
    
    print ''.join(str(cb) for cb in code_blocks if str(cb) != 'None')
    
main()