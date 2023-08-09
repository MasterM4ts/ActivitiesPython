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