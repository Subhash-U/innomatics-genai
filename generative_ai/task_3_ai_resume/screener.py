import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from prompts.templates import screening_prompt_template

def build_screening_chain():
    # 1. Initialize Groq (Updated to the active Llama 3.1 model)
    llm = ChatGroq(
        model="llama-3.1-8b-instant", 
        temperature=0.1
    ).bind(response_format={"type": "json_object"})
    
    # 2. Initialize JSON parser
    parser = JsonOutputParser()
    
    # 3. Build LCEL Chain
    chain = screening_prompt_template | llm | parser
    
    # 4. Add tags for LangSmith tracking
    return chain.with_config({"tags": ["resume_screening_groq"]})