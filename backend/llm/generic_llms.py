import os
import importlib
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GenericLLM:
    def __init__(self, llm_name, model_name):
        # Load LLM configuration from JSON file
        config_path = os.path.join(os.path.dirname(__file__), 'llm_config.json')
        print(config_path)
        with open(config_path, 'r') as config_file:
            llm_map = json.load(config_file)

        if llm_name not in llm_map:
            raise ValueError(f"Unsupported LLM: {llm_name}")

        module_name, class_name = llm_map[llm_name].rsplit('.', 1)
        module = importlib.import_module(f'backend.llm.llms.{module_name}')
        llm_class = getattr(module, class_name)
        self.llm_instance = llm_class(model_name)

    def get_llm(self):
        return self.llm_instance.get_llm()