from boa3.sc import storage
from boa3.sc.compiletime import NeoMetadata, public

@public
def create_task() -> bool:
    storage.put(b'hello', b'world')
    
    return True

@public
def get_task() -> bytes:
    task = storage.get(b'hello') 

    print(task)   
   
    return task

@public
def complete_task() -> bool:
    task = storage.get(b'hello')

    if task is None or task == b'':
        return False

    # Adding a marker to indicate the task is completed
    completed_task = task + b'_completed'

    storage.put(b'hello', completed_task)
    
    return True

@public
def delete_task() -> bool:
    task = storage.get(b'hello')

    if task is None or task == b'':
        return False
    
    storage.delete(b'hello')
    
    return True

def manifest() -> NeoMetadata:
    meta = NeoMetadata()

    meta.author = "Lopes"
    meta.email = "lopes@example.com"
    meta.description = 'NeoTasker: manage tasks on the blockchain'
    
    return meta