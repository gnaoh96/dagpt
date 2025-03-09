from langchain_ollama import ChatOllama

def load_llm(model_name):
    """Load Large Language Model
    """

    if model_name == "llama3.1:8b":
        return ChatOllama(
            model= model_name,
            temperature= 0.0,
            max_tokens= 1000,
        )
    # elif model_name == "gpt-4":
    #     return ChatOpenAI(
    #         model= model_name,
    #         temperature= 0.0,
    #         max_tokens= 1000,
    #     )
    else:
        raise ValueError(
            "Unknown model. \
                Please choose from ['llama3.1:8b']"
        )