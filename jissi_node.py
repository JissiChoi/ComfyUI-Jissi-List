import numpy as np

class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False

def IntField(defaultValue, minValue=0, maxValue=100, step=1, slider=False):

    field = { 
                     "default": defaultValue,
                     "min": minValue,
                     "max": maxValue,
                     "step": step,
                     "display": "number"
                 }
    if slider :
        field["display"] = "slider"
     
    result = ("INT", field)
    
    return result

def FloatField(defaultValue, minValue=0.0, maxValue=100.0, step=0.1, slider=False):
    field = { 
        "default": float(defaultValue),
        "min": float(minValue),
        "max": float(maxValue),
        "step": float(step),
        "display": "number"
    }
#     if slider:
#         field["display"] = "slider"
     
    result = ("FLOAT", field)
    return result

class JissiTest:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "slider" # Cosmetic only: display as "number" or "slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "slider"}),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Jissi World"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "execute"

    OUTPUT_NODE = True

    CATEGORY = "Jissi"

    def execute(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        #do some processing on the image, in this example I just invert it
        image = 1.0 - image * float_field
        return (image,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

#jissi
class JissiList:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Min": IntField(0,-100,100, 1, False),
                "Max": IntField(100,-100,100, 1, False),
                "Step": IntField(5,1,10, 1, False)
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
                "Min": FloatField(0.0, -100.0, 100.0, 0.1, False),
                "Max": FloatField(1.0, -100.0, 100.0, 0.1, False),
                "Step": FloatField(0.1, 0.0, 10.0, 0.0001, False)
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


any_type = AlwaysEqualProxy("*")

class JissiMatchingLists:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list1": (any_type,),
            },
            "optional": {
                "list2": (any_type, {"default": None}),
                "list3": (any_type, {"default": None}),
                "list4": (any_type, {"default": None}),
                "list5": (any_type, {"default": None}),
            }
        }
    
    INPUT_IS_LIST = (True, True, True, True, True)
    OUTPUT_IS_LIST = (True, True, True, True, True)
    RETURN_TYPES = ("LIST", "LIST", "LIST", "LIST", "LIST")
    FUNCTION = "process"
    CATEGORY = "Jissi"

    def process(self, list1, list2=None, list3=None, list4=None, list5=None):
        from itertools import product
        
        # None이 아닌 입력 리스트만 수집
        input_lists = []
        for lst in [list1, list2, list3, list4, list5]:
            if lst is not None:
                input_lists.append(lst)
        
        # 모든 가능한 조합 생성
        matching_lists = list(product(*input_lists))
        # 매칭된 리스트를 개별 리스트로 분리하고 튜플을 리스트로 변환
        result_lists = [list(x) for x in zip(*matching_lists)]
        
        # 사용하지 않는 출력은 빈 리스트로 채움
        while len(result_lists) < 5:
            result_lists.append([])
            
        return tuple(result_lists)


# jissi - text node
class JissiTextNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Steps"}),
                "number": ("INT", {"default": 30, "min": 0, "max": 999999}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "format_text"
    CATEGORY = "text"
    
    def format_text(self, text, number):
        # 텍스트 형식: "텍스트 [숫자]"
        formatted_text = f"{text} [{number}]"
        return (formatted_text,)

# jissi - text template node
class JissiTextTemplateNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {
                    "default": "my_text [{x}]",
                    "multiline": False
                }),
                "x": ("STRING", {"default": "30"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "format_text"
    CATEGORY = "text"
    
    def format_text(self, template, x):
        try:
            # 템플릿의 {x}를 입력값으로 대체
            formatted_text = template.replace("{x}", str(x))
            return (formatted_text,)
        except Exception as e:
            print(f"Error formatting text: {e}")
            return (template,)

# jissi - multiple prompts from files
class TextListFromFile:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,  # 여러 줄 입력 가능
                    "default": "텍스트를 입력하세요\n\n여러 줄로 입력하면\n\n자동으로 분리됩니다"
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "create_text_list"
    CATEGORY = "Jissi"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True, )

    def create_text_list(self, text, unique_id=None, extra_pnginfo=None):
        try:
            text_list = text.split('\n\n')
            text_list = [text.strip() for text in text_list]
            return {"ui": {"text": text_list}, "result": (text_list,)}
        except Exception as e:
            print(f"파일을 읽는 중 오류 발생: {str(e)}")
            return ([],)


# jissi - multi prompt text
import os
from pathlib import Path

class TextFileToListDisplay:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {
                    "default": '',
                    "multiline": False
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True, )
    FUNCTION = "process_text_file"
    CATEGORY = "Jissi"

    def process_text_file(self, file_path, unique_id=None, extra_pnginfo=None):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # 두 줄 공백을 기준으로 분할
                text_list = content.split('\n\n')
                # 각 텍스트의 앞뒤 공백 제거 및 빈 문자열 제거
                text_list = [text.strip() for text in text_list if text.strip()]
                return {"ui": {"text": text_list}, "result": (text_list,)}
        except Exception as e:
            print(f"파일을 읽는 중 오류 발생: {str(e)}")
            return {"ui": {"text": "오류 발생"}, "result": ([],)}

    @classmethod
    def IS_CHANGED(cls, file_path, **kwargs):
        if os.path.exists(file_path):
            m = hashlib.sha256()
            with open(file_path, 'rb') as f:
                m.update(f.read())
            return m.digest().hex()
        return float("NaN")

#jissi - show value - viewer
class JissiView:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "title":  ("STRING", 
                                        {
                                            "default": " --- Jissi Viewer ---",
                                        }),                
            },
            "optional": {
                "whatever": ("BOOLEAN,INT,FLOAT,STRING,LATENT,IMAGE,MODEL,CONDITIONING,CLIP,VAE,CLIP_VISION", ),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Jissi"
    OUTPUT_NODE = True

    def execute(self, title, whatever, unique_id=None, extra_pnginfo=None):
        result = str(title) + "\n"
        test = str(whatever)
        if test:
            result = result + test
        else:
            print("Failed to convert {whatever} to string")

        return {"ui": {"text": [result]}, "result": (result,)}




