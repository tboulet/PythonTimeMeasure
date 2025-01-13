import time
from tmeasure import RuntimeMeter

def foo():
    time.sleep(0.1)

def bar():
    time.sleep(0.2)

for _ in range(3):
    with RuntimeMeter("foo"):
        foo()
    with RuntimeMeter("bar"):
        bar()

print(RuntimeMeter.get_stage_runtime("foo"))
print(RuntimeMeter.get_stage_runtime("bar"))
print(RuntimeMeter.get_stage_runtime("total"))