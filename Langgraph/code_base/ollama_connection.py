from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama



# https://python.langchain.com/docs/concepts/chat_models/
# https://python.langchain.com/docs/how_to/local_llms/

MODEL_NAME = "deepseek-custom"

def get_ollama_model(MODEL_NAME : str = MODEL_NAME):
    model = OllamaLLM(model=MODEL_NAME)
    return model

def get_ollama_chat_model(MODEL_NAME : str = MODEL_NAME):
    model = ChatOllama(model=MODEL_NAME)
    return model

def test_model_connection():
    from langchain_core.prompts import ChatPromptTemplate
    template = """Question: {question}
    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    model = get_ollama_model()
    chain = prompt | model
    chain.invoke({"question": "What is LangChain?"})
    