

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
        return {"ui": {"text": [formatted_text]}, "result": (formatted_text,)}

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
            return {"ui": {"text": [formatted_text]}, "result": (formatted_text,)}
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
            print(f"Errors in reading file: {str(e)}")
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
            print(f"Errors in reading file: {str(e)}")
            return {"ui": {"text": "Errors"}, "result": ([],)}

    @classmethod
    def IS_CHANGED(cls, file_path, **kwargs):
        if os.path.exists(file_path):
            m = hashlib.sha256()
            with open(file_path, 'rb') as f:
                m.update(f.read())
            return m.digest().hex()
        return float("NaN")