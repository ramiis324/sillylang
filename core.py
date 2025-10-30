import inspect, runpy, sys, io

def run_translated(lang_map):
    frame = inspect.stack()[1]
    filename = frame.filename

    with open(filename, encoding="utf8") as f:
        code = f.read()

    code = "\n".join(line for line in code.splitlines() if not line.strip().startswith("import "))

    for fake, real in lang_map.items():
        code = code.replace(fake, real)

    sys.stdin = io.StringIO()
    exec(compile(code, filename, "exec"), globals())
