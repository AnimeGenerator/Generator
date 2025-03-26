class PromptProcessor:
    def __init__(self):
        self.style_templates = {
            "shonen": "dynamic, action-packed, bold outlines",
            "shoujo": "soft colors, romantic, detailed backgrounds",
            "mecha": "futuristic, mechanical, sharp edges"
        }
    
    def process(self, prompt, style):
        """Enhance user prompt with style-specific details"""
        if style in self.style_templates:
            enhanced_prompt = f"{prompt}, {self.style_templates[style]}, anime style"
        else:
            enhanced_prompt = f"{prompt}, anime style"
        return enhanced_prompt
