<div align="center">

**PT-PT** | [EN](./README.md)

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=36&duration=3200&pause=1200&color=8A00C4&background=00000000&center=true&vCenter=true&width=850&height=80&lines=THE+BROKEN+GATE;LAB+DE+AN%C3%81LISE+PE;SEGUE+A+DECIS%C3%83O;L%C3%AA+O+FLUXO+DE+CONTROLO;PROVA+A+FRAQUEZA" alt="The Broken Gate — laboratório de análise PE">

<br>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=24&duration=2600&pause=1000&color=E4BCFF&background=00000000&center=true&vCenter=true&width=850&height=40&lines=%3E+observar+%2F+formular+%2F+validar;%3E+strings+%2F+imports+%2F+branches;%3E+hip%C3%B3tese+%E2%86%92+evid%C3%AAncia+%E2%86%92+conclus%C3%A3o;Um+laborat%C3%B3rio+de+reverse+engineering+feito+de+raiz." alt="Observar, formular, validar — strings, imports, branches — hipótese, evidência, conclusão">

[![Âmbito](https://img.shields.io/badge/%C3%A2mbito-labs%20locais-8a00c4?style=flat-square)](./SCOPE.pt-PT.md)
[![Foco](https://img.shields.io/badge/foco-reverse%20engineering-111111?style=flat-square)](./labs/01-broken-gate/WRITEUP.pt-PT.md)
[![Linguagens](https://img.shields.io/badge/linguagens-C%20%7C%20Python-5c2d91?style=flat-square)](./tooling/inspect_sample.py)

</div>

# NE0SYNC RE Labs

Laboratórios pequenos e reproduzíveis de segurança ofensiva, criados para
documentar como um operador e um reverse engineer passam de um sample
desconhecido a uma conclusão técnica sustentada.

O primeiro laboratório é **The Broken Gate**: um sample PE Windows, criado de
raiz, com um fluxo local de validação intencionalmente fraco. O alvo é seguro,
determinístico e está incluído no repositório para análise. Não envolve
software de terceiros, credenciais ou alvos reais.

## Demo de 60 segundos

```text
clonar → compilar o sample → inspeccionar strings/imports → seguir a validação → ler o write-up
```

```powershell
git clone https://github.com/jeremiasamado/redteam-examples.git
cd redteam-examples
.\scripts\build.ps1
python .\tooling\inspect_sample.py .\samples\broken-gate.exe
```

O sample apresenta um training token determinístico quando o fluxo de validação
esperado é atingido. O exercício é recuperar e compreender esse fluxo, não
contornar software comercial.

## Mapa do repositório

```text
labs/01-broken-gate/
├─ README.md                 # briefing e objetivos — versão inglesa
├─ README.pt-PT.md           # briefing e objetivos — PT-PT
├─ WRITEUP.md                # operator notebook — versão inglesa
└─ WRITEUP.pt-PT.md          # operator notebook — PT-PT
scripts/build.ps1            # build reproduzível em Windows
tooling/inspect_sample.py    # análise de hash, strings e headers PE
samples/.gitkeep             # os binários gerados ficam fora do Git
SCOPE.md                     # âmbito e segurança — versão inglesa
SCOPE.pt-PT.md               # âmbito e segurança — PT-PT
```

## Lab 01 — The Broken Gate

**Objetivo:** recuperar o fluxo de validação de um pequeno sample PE através de
análise estática, explicar a fraqueza de desenho e indicar a correcção de
engenharia adequada.

**Competências:** inspecção PE, strings, imports, raciocínio sobre fluxo de
controlo, validação assistida por debugger e reporting técnico conciso.

O laboratório está dividido em quatro momentos:

1. **Observar** — identificar o ficheiro, o hash e a superfície visível.
2. **Formular** — ligar strings e APIs importadas aos possíveis caminhos de código.
3. **Validar** — confirmar o fluxo contra um binário compilado a partir do source incluído.
4. **Explicar** — registar evidência, impacto e remediação no write-up.

Começa pelo [briefing do laboratório](./labs/01-broken-gate/README.pt-PT.md) e
depois lê o [operator notebook](./labs/01-broken-gate/WRITEUP.pt-PT.md).

## Porque existe

Este repositório é um portefólio público de tradecraft ofensivo e pensamento
de reverse engineering. Cada sample é criado para este projecto, corre
localmente e usa dados sintéticos. O valor está na cadeia de raciocínio:
**hipótese → evidência → conclusão**.

## Identidade do projecto

```text
Autor           NE0SYNC
Voz técnica     BadBoy17
Foco            offensive security · reverse engineering
```

`BadBoy17` é a identidade técnica usada nos labs e nos write-ups. A autoria no
GitHub mantém-se ligada ao dono verificado do repositório; não é usada nenhuma
conta de contributor sintética.

## Licença

O código é distribuído sob a licença MIT. Os samples e a documentação destinam-se
a investigação e treino autorizado em ambiente local; consulta o
[âmbito de utilização](./SCOPE.pt-PT.md).
