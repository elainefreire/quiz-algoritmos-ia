"""Único arquivo que conversa com o modelo. Para trocar de provedor, mude só aqui.

Provedores (variável LLM_PROVIDER): "ollama" (padrão, local e gratuito) ou "anthropic".
"""
import json
import os
import urllib.error
import urllib.request

PROVEDOR = os.environ.get("LLM_PROVIDER", "ollama")
MODELO_OLLAMA = os.environ.get("OLLAMA_MODEL", "llama3.2")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODELO_ANTHROPIC = "claude-haiku-5-5"


def _ollama(prompt):
    corpo = json.dumps(
        {
            "model": MODELO_OLLAMA,
            "messages": [{"role": "user", "content": prompt}],
            "format": "json",
            "stream": False,
        }
    ).encode()
    pedido = urllib.request.Request(
        OLLAMA_URL, data=corpo, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(pedido, timeout=300) as resposta:
            return json.loads(resposta.read())["message"]["content"]
    except urllib.error.HTTPError as erro:
        raise RuntimeError(
            f"O Ollama respondeu com erro {erro.code}. "
            f"O modelo '{MODELO_OLLAMA}' foi baixado? (ollama pull {MODELO_OLLAMA})"
        ) from erro
    except urllib.error.URLError as erro:
        raise RuntimeError(
            "Não consegui falar com o Ollama. Ele está rodando? (ollama serve)"
        ) from erro


def _anthropic(prompt):
    from anthropic import Anthropic  # importado só se esse provedor for usado

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("Defina a variável de ambiente ANTHROPIC_API_KEY.")
    resposta = Anthropic().messages.create(
        model=MODELO_ANTHROPIC,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta.content[0].text


def gerar_texto(prompt):
    if PROVEDOR == "ollama":
        return _ollama(prompt)
    if PROVEDOR == "anthropic":
        return _anthropic(prompt)
    raise RuntimeError("LLM_PROVIDER deve ser 'ollama' ou 'anthropic'.")
