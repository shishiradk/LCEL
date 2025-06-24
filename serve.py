# from fastapi import FastAPI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq
# import os
# from langserve import add_routes
# from dotenv import load_dotenv
# load_dotenv()

# groq_api_key=os.getenv("GROQ_API_KEY")
# model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# # 1. Create prompt template
# system_template = "Translate the following into {language}:"
# prompt_template = ChatPromptTemplate.from_messages([
#     ('system', system_template),
#     ('user', '{text}')
# ])

# parser=StrOutputParser()

# ##create chain
# chain=prompt_template|model|parser



# ## App definition
# app=FastAPI(title="Langchain Server",
#             version="1.0",
#             description="A simple API server using Langchain runnable interfaces")

# ## Adding chain routes
# add_routes(
#     app,
#     chain,
#     path="/chain"
# )


# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run(app,host="127.0.0.1",port=8000)


from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
import os

# Load .env and GROQ key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Create model
model = ChatGroq(model="Gemma-7b-it", groq_api_key=groq_api_key)  # or "Gemma2-9b-It" if available

# Pydantic input model
class TranslationInput(BaseModel):
    language: str
    text: str

# Define the chain logic as a Python function
def translate_fn(inputs: TranslationInput) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ('system', "Translate the following into {language}:"),
        ('user', '{text}')
    ])
    chain = prompt | model | StrOutputParser()
    output = chain.invoke({"language": inputs.language, "text": inputs.text})
    return str(output)  # ensure it's JSON-serializable

# Wrap the function with RunnableLambda
translation_chain = RunnableLambda(translate_fn)

# Initialize FastAPI app
app = FastAPI(title="LangChain Translation API")

# Add LangServe route with input type
add_routes(app, translation_chain, path="/chain", input_type=TranslationInput)

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

