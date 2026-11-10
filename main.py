"""Quiz de Algoritmos com IA: gera questões com um LLM e corrige localmente."""
from llm import gerar_texto
from quiz import extrair_json, montar_prompt, validar


def gerar_questoes(topico, nivel, tentativas=2):
    for _ in range(tentativas):
        try:
            return validar(extrair_json(gerar_texto(montar_prompt(topico, nivel))))
        except ValueError as erro:  # inclui JSON inválido
            print(f"Resposta fora do formato ({erro}). Tentando de novo...")
    raise SystemExit("Não foi possível gerar o quiz. Tente outro tópico.")


def jogar(questoes):
    acertos = 0
    for i, q in enumerate(questoes, 1):
        print(f"\n{i}. {q['enunciado']}")
        for letra, alternativa in zip("ABCD", q["alternativas"]):
            print(f"   {letra}) {alternativa}")
        resposta = input("Sua resposta (A-D): ").strip().upper()
        if resposta and "ABCD".find(resposta[0]) == q["correta"]:
            acertos += 1
            print("Correto!")
        else:
            print(f"Errado. Resposta certa: {'ABCD'[q['correta']]}")
        print(f"Explicação: {q['explicacao']}")
    print(f"\nVocê acertou {acertos} de {len(questoes)}.")


def main():
    topico = input("Tópico (ex.: busca binária): ").strip()
    nivel = input("Nível (iniciante/intermediário/avançado): ").strip() or "iniciante"
    if not topico:
        raise SystemExit("Informe um tópico.")
    jogar(gerar_questoes(topico, nivel))


if __name__ == "__main__":
    main()
