class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None
    
    def visit(self, url: str) -> None:
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack = []  # Limpiar historial hacia adelante
    
    def back(self) -> str:
        if not self.back_stack:
            return self.current
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current
    
    def forward(self) -> str:
        if not self.forward_stack:
            return self.current
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current

# Ejemplo de uso
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
print(browser.back())

