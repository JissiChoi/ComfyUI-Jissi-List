import numpy as np

def IntField(defaultValue, minValue=0, maxValue=100, step=1):

    field = { 
                    "default": defaultValue,
                    "min": minValue,
                    "max": maxValue,
                    "step": step,
                    "display": "number"
    }
     
    result = ("INT", field)
    return result

def FloatField(defaultValue, minValue=0.0, maxValue=100.0, step=0.1):
    field = { 
                    "default": float(defaultValue),
                    "min": float(minValue),
                    "max": float(maxValue),
                    "step": float(step),
                    "display": "number"
    }
     
    result = ("FLOAT", field)
    return result

class JissiList:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Min": IntField(0,-100,100, 1),
                "Max": IntField(100,-100,100, 1),
                "Step": IntField(5,1,10, 1)
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "execute"
    CATEGORY = "Jissi"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True, )

    def execute(self, Min, Max, Step):
        result = list(range(int(Min), int(Max+1), int(Step)))
        print(str(result))
        return (result,)

class JissiFList:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Min": FloatField(0.0, -100.0, 100.0, 0.1),
                "Max": FloatField(1.0, -100.0, 100.0, 0.1),
                "Step": FloatField(0.1, 0.0, 10.0, 0.0001)
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    CATEGORY = "Jissi"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    def execute(self, Min, Max, Step):
        # numpy.arange()를 사용하여 float range 생성
        result = list(np.arange(float(Min), float(Max + Step), float(Step)))
        print(str(result))
        return (result,)