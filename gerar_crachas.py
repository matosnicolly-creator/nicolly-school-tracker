import json
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

ARQUIVO_JSON = 'data/alunos.json'
PASTA_SAIDA = 'crachas_impressao'

if not os.path.exists(PASTA_SAIDA):
  os.makedirs(PASTA_SAIDA)

def gerar_crachas():
  try:
    with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
      alunos = json.load(f)
  except FileNotFoundError:
    print("Erro: Arquivo alunos.json não encontrado!")
    return

for aluno in alunos:
  nome = aluno['nome']
  turma = aluno['turma']
  tag = aluno['tag']

print(f"Gerando crachá para: {nome}...")

qr = qrcode.QRCode(version=1, box_size=10,border
