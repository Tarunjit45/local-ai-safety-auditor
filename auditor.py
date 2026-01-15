from langchain_ollama import ChatOllama

# Switching to the 'Mini' version for speed
worker_llm = ChatOllama(model="phi3:mini", temperature=0)
auditor_llm = ChatOllama(model="tinydolphin", temperature=0)

def run_fast_agent(user_query):
    print(f"🚀 [Worker Thinking...]")
    
    # We use .stream() so you see the output instantly
    full_response = ""
    for chunk in worker_llm.stream(f"Explain {user_query} in 2 sentences."):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content
    
    print(f"\n\n🛡️ [Auditor Verifying...]")
    
    # Fast verification
    for chunk in auditor_llm.stream(f"Is this text about {user_query} accurate? answer 'YES' or 'NO' and explain why: {full_response}"):
        print(chunk.content, end="", flush=True)

if __name__ == "__main__":
    run_fast_agent("Neural Networks")