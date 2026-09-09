import numpy as np


temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
                         6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
                         8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
                         10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
                         7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
                         6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
                         5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
                         6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
                         9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
                         10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

print(temperaturas)
print("--- Análise Estatística das Temperaturas ---")
print(f"Média = ≈ {np.mean(temperaturas):.4f}")
print(f"Mediana = ≈ {np.median(temperaturas):.4f}")
print(f"Desvio Padrão = ≈ {np.std(temperaturas):.4f}")

diasFrios= temperaturas[temperaturas < 5]
diasModerados = temperaturas[(temperaturas >= 5) & (temperaturas <= 15)]
diasQuente = temperaturas[temperaturas > 15]

print("--- Classificação de Temperaturas ---")
print(f"Quantidade de dias frios (<5°C): {len(diasFrios)}")
print(f"Quantidade de dias moderados (5°C - 15°C): {len(diasModerados)}")
print(f"Quantidade de dias quentes (>15°C): {len(diasQuente)}\n")


diasMaisFrios = np.sort(temperaturas)[:5]
diasMaisQuentes = np.sort(temperaturas)[-5:][::-1] 

print("--- Dias Extremos ---")
print(f"O dia mais frio do ano fez: {np.min(temperaturas)}°C")
print(f"O dia mais quente do ano fez: {np.max(temperaturas)}°C")
print(f"Top 5 dias mais frios: {diasMaisFrios}")
print(f"Top 5 dias mais quentes: {diasMaisQuentes}")





