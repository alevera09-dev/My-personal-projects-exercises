def logger_token(token_type: str, value: str, line: int, col: int) -> None:
    print(f"[TOKEN] {token_type} '{value}' at ({line}, {col})")

def logger_error(msg: str, line: int, col: int) -> None:
    print(f"{msg} at ({line}, {col})")
    
def logger_nodo(node: str) -> None:
    print(f"[NODE] Contruido {node}")

class CountToken:
    def __init__(self) -> None:
        self.count = 0
        
    def __call__(self, token_type: str, value: str, line: int, col: int) -> None:
        self.count += 1
        
        if self.count < 2:
            print(f"Contador: 1 token visto.")
        else:
            print(f"Contador: {self.count} tokens vistos.")
            
class CountError:
    def __init__(self) -> None:
        self.count = 0
        
    def __call__(self, msg: str, line: int, col: int) -> None:
        self.count += 1
        print(f"Contador: {self.count}")
        
class CollectorAst:
    def __init__(self) -> None:
        self.nodes: list[str] = []
        
    def __call__(self, node: str) -> None:
        self.nodes.append(node)
    
class EventManager:
    ON_TOKEN = "on_token"
    ON_ERROR = "on_error"
    ON_NODE_BUILT = "on_node_built"
    
    def __init__(self):
        self.handlers: dict[str, list[callable]] = {}
    
    def subscribe(self, event_name: str, callback: callable):
        if event_name not in self.handlers.keys():
            list_callbacks = [callback]
            self.handlers[event_name] = list_callbacks
        else:
            self.handlers[event_name].append(callback)
    
    def emit(self,event_name: str, *args, **kargs):
            for func in self.handlers[event_name]:
                if event_name == self.ON_TOKEN:
                    func(token_type=token_type, value=value, line=line, column=column)
                elif event_name == self.ON_ERROR:
                    func(msg=msg, line=line, col=col)
                elif event_name == self.ON_NODE_BUILT:
                    func(node=node)
                else:
                    print("Error, este evento no existe.")
                    break
                
if __name__ == "__main__":
    # Crear el manager
    manager = EventManager()
    
    #Crear counts, etc
    contador_tokens = CountToken()
    contador_errores = CountError()
    colector_ast = CollectorAst()
    
    ON_TOKEN = "on_token"
    ON_ERROR = "on_error"
    ON_NODE_BUILT = "on_node_built"

    # Registrar varios handlers
    manager.subscribe(ON_TOKEN, logger_token)
    manager.subscribe(ON_TOKEN, contador_tokens)
    manager.subscribe(ON_ERROR, logger_error)
    manager.subscribe(ON_ERROR, contador_errores)
    manager.subscribe(ON_NODE_BUILT, logger_nodo)
    manager.subscribe(ON_NODE_BUILT, colector_ast)

    # Simular el flujo de un lexer/parser emitiendo eventos
    print("=== Iniciando prueba del motor de eventos ===\n")

    manager.emit(ON_TOKEN, token_type="IDENTIFIER", value="mi_variable", line=1, col=1)
    manager.emit(ON_TOKEN, token_type="EQUALS", value="=", line=1, col=12)
    manager.emit(ON_TOKEN, token_type="NUMBER", value="42", line=1, col=14)

    manager.emit(ON_NODE_BUILT, node_type="Assign", node_data={"target": "mi_variable", "value": 42})

    manager.emit(ON_TOKEN, token_type="IDENTIFIER", value="print", line=2, col=1)
    manager.emit(ON_TOKEN, token_type="LPAREN", value="(", line=2, col=6)

    manager.emit(ON_ERROR, message="Nombre no definido: 'x'", line=3, col=5)

    manager.emit(ON_NODE_BUILT, node_type="Call", node_data={"func": "print", "args": ["hola"]})

    # Al final, mostrar estadísticas
    print("\n=== Estadísticas finales ===")
    print(f"Tokens procesados: {contador_tokens.count}")
    print(f"Errores encontrados: {contador_errores.count}")
    print(f"Nodos AST construidos: {len(colector_ast.nodos)}")
                