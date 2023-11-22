# config file
import json
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION") or "davinci"

class Config:
    """Config class for GPT Researcher."""

    def __init__(self, config_file: str = None):
        """Initialize the config class."""
        os.environ["OPENAI_API_TYPE"] = "azure"
        os.environ["azure_endpoint"] = AZURE_OPENAI_ENDPOINT
        os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
        os.environ["OPENAI_API_KEY"] = AZURE_OPENAI_KEY
        os.environ["OPENAI_API_VERSION"] = OPENAI_API_VERSION
        os.environ["AZURE_OPENAI_KEY"] = AZURE_OPENAI_KEY

        self.config_file = config_file
        self.retriever = "tavily"
        self.llm_provider = "AzureChatOpenAI"
        self.fast_llm_model = "gpt-35-turbo-16k"
        self.smart_llm_model = "gpt-4"
        self.fast_token_limit = 2000
        self.smart_token_limit = 4000
        self.browse_chunk_max_length = 8192
        self.summary_token_limit = 700
        self.temperature = 0.55
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
                          " Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        self.max_search_results_per_query = 5
        self.memory_backend = "local"
        self.total_words = 1000
        self.report_format = "apa"
        self.max_iterations = 3

        self.load_config_file()

    def load_config_file(self) -> None:
        """Load the config file."""
        if self.config_file is None:
            return None
        with open(self.config_file, "r") as f:
            config = json.load(f)
        for key, value in config.items():
            self.__dict__[key] = value

