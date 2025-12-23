from langchain_openai import OpenAI
from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

set_llm_cache(SQLiteCache(database_path="llm_cache.db"))

llm = OpenAI(model_name="gpt-4o-mini", temperature=0)

# print(llm.invoke("Explain about cricket"))
# print(llm.invoke("Explain about cricket"))
# print(llm.invoke("Explain about football"))

print(llm.invoke("Explain about football"))