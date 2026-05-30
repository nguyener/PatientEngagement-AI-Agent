print("Loading agent.py...")
import json
from openai import OpenAI

from config import SYSTEM_PROMPT, MODEL
from tool_schemas import tools
from tools import tool_functions

print("About to define PatientEngagementAgent")
class PatientEngagementAgent:

    def __init__(self):
        self.client = OpenAI()
        self.conversation = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def handle_message(self, user_input: str) -> str:
        self.conversation.append({
            "role": "user",
            "content": user_input
        })

        response = self.client.responses.create(
            model=MODEL,
            input=self.conversation,
            tools=tools
        )

        self.conversation += response.output

        for item in response.output:
            if item.type == "function_call":
                tool_name = item.name
                arguments = json.loads(item.arguments)

                tool_result = tool_functions[tool_name](**arguments)

                self.conversation.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(tool_result)
                })

                final_response = self.client.responses.create(
                    model=MODEL,
                    input=self.conversation,
                    tools=tools
                )

                self.conversation += final_response.output
                return final_response.output_text

        return response.output_text