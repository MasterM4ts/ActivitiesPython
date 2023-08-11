import openai

openai.api_key = "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"
def get_compilation(prompt, model = "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,
    )
    return response.choices[0].message["content"]


prompt = input("Pergunta: ")
response = get_compilation(prompt)
print(response)