from langchain_openai import OpenAI
from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache
from langchain_community.callbacks.manager import get_openai_callback
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

set_llm_cache(SQLiteCache(database_path="llm_cache.db"))

llm = OpenAI(model_name="gpt-4o-mini", temperature=0)

propmt = "Explain about Kabaddi"
with get_openai_callback() as cb:
    response = llm.invoke(propmt)
    print(f"Response: {response}")
    print("-----------------------")
    print(f"Tokens used: {cb.total_tokens}")
    print("-----------------------")
    print(f"Total Cost: ${cb.total_cost}")