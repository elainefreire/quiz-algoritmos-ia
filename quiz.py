"""Montagem do prompt e validação da resposta do modelo."""
import json

PROMPT = """Você é um professor de Ciência da Computação.
Crie {n} questões de múltipla escolha sobre "{topico}" (nível: {nivel}).
Responda APENAS com JSON válido, sem texto extra, neste formato:
{{"questoes": [{{"enunciado": "...", "alternativas": ["...", "...", "...", "..."], "correta": 0, "explicacao": "..."}}]}}
"correta" é o índice (de 0 a 3) da alternativa correta. Escreva em português."""


def montar_prompt(topico, nivel, n=3):
    return PROMPT.format(n=n, topico=topico, nivel=nivel)


def extrair_json(texto):
    """Pega o trecho entre a primeira '{' e a última '}' (ignora ```json etc.)."""
    inicio, fim = texto.find("{"), texto.rfind("}")
    if inicio == -1 or fim == -1:
        raise ValueError("a resposta não contém JSON")
    return json.loads(texto[inicio : fim + 1])


def validar(dados):
    """Confere se o JSON tem o formato esperado e devolve a lista de questões."""
    questoes = dados.get("questoes") if isinstance(dados, dict) else None
    if not isinstance(questoes, list) or not questoes:
        raise ValueError("lista de questões ausente ou vazia")
    for q in questoes:
        alternativas = q.get("alternativas")
        if not isinstance(alternativas, list) or len(alternativas) != 4:
            raise ValueError("cada questão precisa de 4 alternativas")
        if q.get("correta") not in (0, 1, 2, 3):
            raise ValueError("campo 'correta' deve ser um índice de 0 a 3")
        if not q.get("enunciado") or not q.get("explicacao"):
            raise ValueError("enunciado e explicação são obrigatórios")
    return questoes
