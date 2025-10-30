import os
import shutil
import subprocess
import time

def _resolve_neo_express_path() -> str:
    neo_express_env = os.environ.get("NEO_EXPRESS_PATH")
    if neo_express_env:
        return neo_express_env

    found = shutil.which("neo-express")
    if found:
        return found

    fallback = os.path.expandvars(r"%USERPROFILE%\.dotnet\tools\neo-express.exe")
    if os.path.exists(fallback):
        return fallback

    raise FileNotFoundError(
        "neo-express not found. Specify NEO_EXPRESS_PATH, "
        "add %USERPROFILE%\\.dotnet\\tools to PATH, or provide the full path."
    )

def invoke(method_path: str, *args) -> bool:
    exe = _resolve_neo_express_path()

    cmd = [exe, "contract", "invoke", ".\\samples\\" + method_path + ".json", "genesis"] + [str(a) for a in args]
    print("> " + " ".join(cmd))
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    
    if result.returncode != 0:
        print(result.stderr)
    
    return result.returncode == 0

if __name__ == "__main__":
    invoke("invoke_create_task")

    time.sleep(15)
    invoke("invoke_get_task", "--results")

    invoke("invoke_complete_task")
    
    time.sleep(15)
    invoke("invoke_get_task", "--results")

    invoke("invoke_delete_task")
    
    time.sleep(15)
    invoke("invoke_get_task", "--results")
