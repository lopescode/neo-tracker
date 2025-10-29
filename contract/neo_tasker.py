from boa3.sc import storage
from boa3.sc.compiletime import NeoMetadata, public

@public
def create_task() -> bool:
    storage.put(b'hello', b'world')
    
    return True

@public
def get_task() -> bytes:
    value = storage.get(b'hello')    
   
    return value

def manifest() -> NeoMetadata:
    meta = NeoMetadata()

    meta.author = "Lopes"
    meta.email = "lopes@example.com"
    meta.description = 'NeoTasker: manage tasks on the blockchain'
    
    return meta