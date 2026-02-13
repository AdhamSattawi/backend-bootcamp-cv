
def pid_find(log: str) -> str: 
    log = log.lower()
    start = log.index("pid") + 4
    end = start + 4
    pid = log[start : end]
    return pid

