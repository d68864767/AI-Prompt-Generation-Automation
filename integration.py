name:$integration.py

name:$integration.py

from backend import PromptGenerator
from frontend import Frontend

class Integration:
    def __init__(self, model_path):
        self.backend = PromptGenerator(model_path)
        self.frontend = Frontend(self.backend)
    
    def run_integration(self, input_text):
        generated_prompt = self.frontend.prompt_generation(input_text)
        return generated_prompt

# Example usage
model_path = "path/to/ai_model.h5"
integration = Integration(model_path)
input_text = "Hello, world!"
generated_prompt = integration.run_integration(input_text)
print(generated_prompt)

