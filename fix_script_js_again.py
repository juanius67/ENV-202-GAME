with open('script.js', 'r') as f:
    script = f.read()

import re
script = re.sub(r'\}, 1000\);\n\}', r'    };\n    updateTimer();\n    setInterval(updateTimer, 1000);\n}', script)

with open('script.js', 'w') as f:
    f.write(script)
