"""Único arquivo que conversa com a API. Para trocar de provedor, mude só aqui."""
import os

from anthropic import Anthropic

MODELO = "claude-haiku-5-5"


def gerar_texto(prompt):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("Defina a variável de ambiente ANTHROPIC_API_KEY.")
    cliente = Anthropic()
    resposta = cliente.messages.create(
        model=MODELO,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta.content[0].text
