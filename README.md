# Lighter
> A humble Deep Learning framework based on Pytorch.
>
### **Coal + Stick + Lighter = Torch on Fire**

- Lighter: Almost invisible, but it lets you see what you want to see.
- CoalTrainer: The source of fire, refining the scepter.
- StickModel: Stick of flame.

## Getting started

## Lighter
> Visualization
>
- It's an EventListener can handle multiple Events.

**For example:**
```python
from lighter import lighters
from lighter.events import on
from lighter.coal_and_stick.trainer_events import *

class DemoLighter(lighters.Lighter): 
    def __init__(self):
        self.info_stored = None

    @on(BeforeEpoch)
    def _show_epoch(self, event: BeforeEpoch):
        print(event.epoch)
        self.info_stored = event

    @on(AfterEpoch)
    def _after_epoch(self, event: AfterEpoch):
        print(self.info_stored)
```

## CoalTrainer
> Training

## StickModel
> Model

## Easy Customization