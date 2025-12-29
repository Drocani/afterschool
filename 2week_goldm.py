print("Qual é o teu nome?")
nome = input()
print("Olá " ,nome,  ", vamos fazer um quiz sobre a Madeira!")
pontos = 0



print("Pergunta 1: Qual é a capital da Madeira?")
print("A) Porto Santo")
print("B) Funchal")
print("C) Machico")
resposta1 = input("A tua resposta (A/B/C): ")

if resposta1 == "B":
    print("Correto! Funchal é a capital da Madeira.")
    pontos = pontos + 1
else:
    print("Incorreto. A capital da Madeira é Funchal (B).")


print("Pergunta 2: Qual é o ponto mais alto da Madeira?")
print("A) Pico Ruivo")
print("B) Pico do Areeiro") 
print("C) Pico das Torres")
resposta2 = input("A tua resposta (A/B/C): ")

if resposta2 == "A":
    print("Correto! O Pico Ruivo tem 1862 metros de altitude.")
    pontos = pontos + 1
else:
    print("Incorreto. O ponto mais alto é o Pico Ruivo (A).")


print("Pergunta 3: Em que oceano se localiza a Madeira?")
print("A) Oceano Índico")
print("B) Oceano Pacífico")
print("C) Oceano Atlântico")
resposta3 = input("A tua resposta (A/B/C): ")

if resposta3 == "C":
    print("Correto! A Madeira fica no Oceano Atlântico.")
    pontos = pontos + 1
else:
    print("Incorreto. A Madeira fica no Oceano Atlântico (C).")


print("Pergunta 4: Qual é a bebida tradicional da Madeira?")
print("A) Poncha")
print("B) Vinho do Porto")
print("C) Ginjinha")
resposta4 = input("A tua resposta (A/B/C): ")

if resposta4 == "A":
    print("Correto! A Poncha é a bebida tradicional madeirense.")
    pontos = pontos + 1
else:
    print("Incorreto. A bebida tradicional é a Poncha (A).")


print("Pergunta 5: A Madeira é:")
print("A) Um país independente")
print("B) Uma região autónoma de Portugal")
print("C) Uma província de Espanha")
resposta5 = input("A tua resposta (A/B/C): ")

if resposta5 == "B":
    print("Correto! A Madeira é uma região autónoma portuguesa.")
    pontos = pontos + 1
else:
    print("Incorreto. A Madeira é uma região autónoma de Portugal (B).")



print("=== RESULTADO ===")
print(nome + ", acertaste " + str(pontos) + " perguntas em 5.")

if pontos == 5:
    print("PERFEITO! És um especialista da Madeira!")
elif pontos == 4:
    print("Muito bom! Conheces bem a Madeira!")
elif pontos == 3:
    print("Bom! Sabes coisas importantes sobre a Madeira.")
elif pontos == 2:
    print("Razoável. Sabes o básico sobre a Madeira.")
elif pontos == 1:
    print("Conheces pouco sobre a Madeira.")
else:
    print("Precisas aprender mais sobre a Madeira.")