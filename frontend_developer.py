# frontend_developer.py

from backend import PromptGenerator

class Frontend:
    def __init__(self, backend):
        self.backend = backend
    
    def prompt_generation(self, input_text):
        generated_prompt = self.backend.generate_prompt(input_text)
        return generated_prompt

# Example usage
if __name__ == "__main__":
    model_path = "path/to/ai_model.h5"
    backend = PromptGenerator(model_path)
    frontend = Frontend(backend)

    input_text = "Hello, world!"
    generated_prompt = frontend.prompt_generation(input_text)
    print(generated_prompt)
