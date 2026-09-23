
class Text:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return self.content

class BoldDecorator:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicDecorator:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return f"<i>{self.text.render()}</i>"

# Build formatted text step by step
message = Text("Hello World")
message = BoldDecorator(message)
message = ItalicDecorator(message)

print(message.render())