from fastapi import FastAPI
import requests
import json

app = FastAPI()

OLLAMA_MODEL = "llama3.2"  # Change to your preferred model (e.g., "llama2")

@app.post("/generate_blog")
async def generate_blog(topic: str):
    """
    Generate a blog post using Ollama based on the given topic.
    """
    prompt = f"Write a detailed blog post about {topic}."
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": OLLAMA_MODEL, "prompt": prompt}
    )

    data = response.json()
    blog_text = data.get("response", "Failed to generate text.")
    
    return {"topic": topic, "blog": blog_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
