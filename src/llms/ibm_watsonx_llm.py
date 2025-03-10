import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM

load_dotenv()

class IBMWatsonxLLM:
    def __init__(self):
        parameters = {
            GenParams.DECODING_METHOD: 'greedy',
            GenParams.TEMPERATURE: 1,
            GenParams.TOP_P: 1,
            GenParams.TOP_K: 1,
            GenParams.MIN_NEW_TOKENS: 10,
            GenParams.MAX_NEW_TOKENS: 2000,
            GenParams.REPETITION_PENALTY:1,
            GenParams.STOP_SEQUENCES:[],
            GenParams.RETURN_OPTIONS: {
                'input_tokens': True,
                'generated_tokens': True,
                'token_logprobs': True,
                'token_ranks': True,
            }
        }

        self.llm = WatsonxLLM(
            model_id="ibm/granite-13b-chat-v2",
            url=os.getenv('WATSONX_URL'),
            apikey=os.getenv('WATSONX_API_KEY'),
            project_id=os.getenv('WATSONX_PROJECT_ID'),
            params=parameters
        )

    def get_llm(self):
        return self.llm