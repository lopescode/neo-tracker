from boa3.sc import storage
from boa3.sc.compiletime import NeoMetadata, public
from boa3.sc.runtime import notify

@public
def create_task() -> bool:
    storage.put(b'hello', b'world')

    notify(["Task created", b'hello'])
    
    return True

@public
def get_task() -> bytes:
    task = storage.get(b'hello') 

    if task is None or task == b'':
        notify(["Task not found", b'hello'])
        return b''

    notify(["Task found", b'hello'])

    return task

@public
def complete_task() -> bool:
    task = storage.get(b'hello')

    if task is None or task == b'':
        notify(["Task not found", b'hello'])
        return False

    # Adding a marker to indicate the task is completed
    completed_task = task + b'_completed'

    storage.put(b'hello', completed_task)

    notify(["Task completed", b'hello'])
    
    return True

@public
def delete_task() -> bool:
    task = storage.get(b'hello')

    if task is None or task == b'':
        notify(["Task not found", b'hello'])    
        return False
    
    storage.delete(b'hello')
    
    notify(["Task deleted", b'hello'])
    
    return True

def manifest() -> NeoMetadata:
    meta = NeoMetadata()

    meta.author = "Lopes"
    meta.email = "lopes@example.com"
    meta.description = 'NeoTasker: manage tasks on the blockchain'
    
    return meta