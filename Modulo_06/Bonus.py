import shutil
import os

# Criar pastas de exemplo
os.makedirs("origem", exist_ok=True)
os.makedirs("backup", exist_ok=True)

# Criar um arquivo de teste
with open("origem/arquivo_importante.txt", "w") as f:
    f.write("Este é um arquivo importante!")

# Copiar para pasta de backup
shutil.copy("origem/arquivo_importante.txt", "backup/arquivo_importante.txt")

print("Backup realizado com sucesso!")
