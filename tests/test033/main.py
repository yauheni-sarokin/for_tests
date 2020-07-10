def greet(name, question):
    return ('Hello, ' + name + 'How is it' + question + '?')

import dis

print(dis.dis(greet('1', '2')))
