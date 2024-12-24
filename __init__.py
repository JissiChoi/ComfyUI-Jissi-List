
from .jissi_node import *


# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
WEB_DIRECTORY = "./web"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "JissiList": JissiList,
    "JissiFloatList": JissiFList,
    "JissiView": JissiView,
    "JissiMatching": JissiMatchingLists,
    "JissiText": JissiTextNode,
    "JissiTextTemplate": JissiTextTemplateNode,
    "JissiMultiplePrompts": TextListFromFile,
    "JissiTextFileToListDisplay": TextFileToListDisplay,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "JissiList": "Jissi List",
    "JissiFloatList": "Jissi Float List",
    "JissiView": "Jissi View",
    "JissiMatching": "Jissi Matching Lists",
    "JissiText": "Jissi Text",
    "JissiTextTemplate": "Jissi Text Template",
    "JissiMultiplePrompts": "Jissi Multiple Prompts",
    "JissiTextFileToListDisplay": "Jissi TextFileToList Display",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']