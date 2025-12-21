from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def __init__(self, priority: int):
        self.priority = priority
        
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def execute(self, data: str) -> str:
        pass
    
    @abstractmethod
    def priority(self) -> int:
        pass

class LoggerPlugin(Plugin):
    def __init__(self, priority: int):
        self.priority = priority
        
    def name(self) -> str:
        return "Logger"
    
    def execute(self, data) -> str:
        print(f"[Logger] Procesando: {data}")
        return data
    
    def priority(self) -> int:
        return self.priority
    
class ValidatorPlugin(Plugin):
    def __init__(self, priority: int):
        self.priority = priority
    
    def name(self) -> str:
        return "Validator"
    
    def execute(self, data) -> str:
        for char in data:
            if char.isdigit():
                raise ValueError("Datos invalidos.")
            
        return data
    
    def priority(self):
        return self.priority
    
class TransformerPlugin(Plugin):
    def __init__(self, priority: int):
        self.priority = priority
    
    def name(self) -> str:
        return "Transformer"
    
    def execute(self, data) -> str:
        return data.upper()
    
    def priority(self):
        return self.priority
    
    
class PluginManager:
    plugins: list[Plugin] = []
    
    def register(self, plugin: Plugin) -> None:
        self.plugins.append(plugin)
    
    def run(self, initial_data: str) -> str:
        current_data = initial_data
        
        self.plugins = sorted(self.plugins, key=lambda p: p.priority, reverse=True)
        for plugin in self.plugins:
            print(f"Ejecutando [{plugin.name()}] (Prioridad: {plugin.priority})")
            current_data = plugin.execute(current_data)
            
        return current_data
        

if __name__ == "__main__":
    manager = PluginManager()
    manager.register(LoggerPlugin(100))
    manager.register(ValidatorPlugin(50))
    manager.register(TransformerPlugin(0))
    manager.register(LoggerPlugin(-100))  # otro logger al final

    resultado = manager.run("hola mundo cruel")
    print("Resultado final:", resultado)