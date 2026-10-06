# Lab 01 — The Broken Gate

[EN](./README.md)

## Briefing

Recebeste `broken-gate.exe`, um pequeno sample PE Windows produzido a partir do
source nesta pasta. O objectivo é recuperar o fluxo de validação local e
explicar porque não deve ser tratado como uma fronteira de autorização.

## Objectivos

- estabelecer uma identidade reproduzível para o ficheiro;
- extrair strings e imports relevantes;
- identificar a função de validação e o ponto de decisão;
- registar evidência sem alterar o sample;
- propor um desenho de verificação no lado do servidor.

## Arranque

A partir da raiz do repositório:

```powershell
.\scripts\build.ps1
python .\tooling\inspect_sample.py .\samples\broken-gate.exe
```

Usa um visualizador PE ou debugger à tua escolha para confirmar as observações.
O source incluído fica disponível para comparação depois da análise.

## Perguntas orientadoras

1. Que strings revelam a finalidade do sample?
2. Que API importada é usada para obter a identidade local?
3. Onde acontece a decisão entre sucesso e falha?
4. Porque pode uma decisão local ser alterada por quem controla o processo?
5. O que muda quando a confiança passa para um verificador do lado do servidor?

A resposta está no [write-up PT-PT](./WRITEUP.pt-PT.md), mas lê-o só depois
de formares a tua própria hipótese.
