def tools(tool = None):
    tools = 'pillow', 'silencer', 'bottle'
    while tool not in tools: tool = input("Type from list:"
                                           "'pillow', 'silencer', 'bottle'")
    def silenced(fn):
        def wrapper():
            return f'Silenced with {tool} no {fn()}'
        return wrapper
    return silenced

@tools('silencer')
def shotgun():
    return 'BOOOM'

@tools('sdfss')
def handgun():
    return 'boom'
