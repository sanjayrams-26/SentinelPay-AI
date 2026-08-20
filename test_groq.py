from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("GROQ_API_KEY", "")
print(f"Key: {key[:20]}...")
from groq import Groq
client = Groq(api_key=key)
try:
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Say: OK"}],
        max_tokens=10,
    )
    print("SUCCESS:", r.choices[0].message.content.strip())
except Exception as e:
    print("FAIL:", type(e).__name__, str(e)[:300])
