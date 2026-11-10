# Quiz de Algoritmos com IA

Programa de terminal que usa um modelo de linguagem (LLM) para gerar questões de múltipla escolha sobre um tópico de Ciência da Computação, valida a resposta do modelo e corrige o quiz localmente.

Projeto de estudo para praticar integração com LLMs: prompts, saída estruturada em JSON, validação, provedores intercambiáveis e testes.

## Como funciona

1. Você informa um tópico (ex.: "busca binária") e um nível.
2. O programa monta um prompt pedindo questões em JSON (`quiz.py`).
3. O modelo é chamado (`llm.py`), localmente via Ollama ou pela API da Anthropic.
4. A resposta é extraída e validada: formato, 4 alternativas, índice da correta (`quiz.py`).
5. Se vier fora do formato, o programa tenta de novo (`main.py`).
6. A correção é feita no código, não pelo modelo.

## Como rodar (gratuito, com modelo local)

Requer Python 3.10+ e o [Ollama](https://ollama.com) instalado e rodando.

```bash
git clone https://github.com/elainefreire/quiz-algoritmos-ia.git
cd quiz-algoritmos-ia
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2
python main.py
```

### Usando a API da Anthropic (opcional)

```bash
pip install anthropic
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY="sua-chave"
python main.py
```

Variáveis opcionais: `OLLAMA_MODEL` (padrão `llama3.2`) e `OLLAMA_URL`.

## Testes

```bash
pytest
```

Os testes cobrem a extração e a validação do JSON e não precisam de modelo nem de internet.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `main.py` | Interface de terminal e repetição em caso de erro |
| `quiz.py` | Prompt, extração e validação do JSON |
| `llm.py` | Chamada ao modelo (único ponto de contato com o provedor) |
| `test_quiz.py` | Testes automatizados |

## Decisões de projeto

- **Validação da saída:** modelos podem responder fora do formato, então nada é usado antes de ser validado.
- **Correção no código:** o modelo gera as questões, mas a nota é calculada localmente.
- **Provedor isolado:** trocar de modelo ou de provedor exige mudar só o `llm.py`.
- **Modelo local por padrão:** permite rodar sem custo e sem enviar dados para fora.

## Limitações observadas

- Modelos pequenos às vezes criam alternativas erradas pouco convincentes e explicações imprecisas.
- O modelo pode errar o gabarito; ainda não há checagem da correção das questões.

## Próximos passos

- Salvar histórico de notas e permitir escolher o número de questões.
- Comparar a qualidade das questões entre modelos.
- Pedir ao modelo uma segunda passada para revisar o gabarito.
