from langchain_openai import OpenAI
import redis
from langchain_community.cache import SQLiteCache,RedisCache
from langchain_core.globals import set_llm_cache
from langchain_community.callbacks.manager import get_openai_callback
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

set_llm_cache(RedisCache(redis_client))

llm = OpenAI(model_name="gpt-4o-mini", temperature=0)

propmt = "Explain about Kabaddi"
with get_openai_callback() as cb:
    response = llm.invoke(propmt)
    print(f"Response: {response}")
    print("-----------------------")
    print(f"Tokens used: {cb.total_tokens}")
    print("-----------------------")
    print(f"Total Cost: ${cb.total_cost}")