import wikipedia

busca = input(">> ")
wiki = wikipedia.set_lang("pt")
resposta = wikipedia.summary(busca,2)
print(resposta)