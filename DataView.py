

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
