# Etapa 1:
banda = []
print("etapa 1:", banda)

# Etapa 2:
banda.append("John Lenon")
banda.append("Paul McCartney")
banda.append("George Harrison")
print("etaoa 2:", banda)

# Etapa 3:
for members in range(2):
    banda.append(input("Novo membro: "))
print("etapa 3:", banda)

# Etapa 4:
del banda[-1]
del banda[-1]
print("etapa 4:", banda)

# Etapa 5:
banda.insert(0, "RingoStarr")
print("etapa 5:", banda)
print("The Fab:", len(banda))