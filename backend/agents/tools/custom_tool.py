from langchain.tools import Tool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class CustomClass:
    @staticmethod
    def printMessage():
        return "Ja be"

class CustomTool:
    def __init__(self):
        self.cust_tool = Tool(
            name="Custom Function",
            func=CustomClass.printMessage,  # Pass the method as a callable
            description="Useful for Custom functions."
        )

    def get_tool(self):
        return self.cust_tool

# Example usage
if __name__ == "__main__":
    wiki_tool_instance = CustomTool()
    tool = wiki_tool_instance.get_tool()
    print(tool.name)
    print(tool.description)
    # Example call to the tool
    print(tool.func())