# The Broken Gate — operator notebook

[EN](./WRITEUP.md)

## Hipótese

O sample parece implementar uma barreira local de funcionalidade. Os primeiros
indicadores são as strings `license`, `premium`, `accepted` e `rejected`, em
conjunto com a API Windows de identidade importada pelo executável.

## Observação

O programa recebe um valor semelhante a uma licença, calcula uma decisão local e
apresenta um training token quando a validação é aceite. O token é
propositadamente sintético. Não existe qualquer pedido de rede nem dependência
de um serviço externo.

A observação importante é arquitectural: a decisão é tomada integralmente no
processo cliente. Um booleano local é tratado como prova de autorização.

## Fluxo de validação

```text
input
  ↓
normalização
  ↓
comparação local da licença
  ├─ diferente → rejected
  └─ igual     → accepted → training token sintético
```

O branch relevante é fácil de localizar porque o sample contém strings distintas
para sucesso e falha. Num assessment real, strings são apenas âncoras: a
conclusão tem de ser sustentada pelas instruções que produzem o branch e por
observação em runtime num ambiente autorizado.

## Finding

**A validação local não é uma fronteira de autorização.**

O cliente pode ser inspeccionado e modificado pela mesma entidade que controla
o processo. O resultado local pode servir para UX, mas não deve proteger uma
funcionalidade premium nem um recurso sensível.

## Correcção de engenharia

Mover a decisão de confiança para um verificador do lado do servidor:

1. enviar um pedido curto e associado ao serviço;
2. verificar a entitlement no servidor;
3. devolver apenas a capacidade necessária para a operação actual;
4. associar operações sensíveis a um token emitido pelo servidor e com expiração;
5. tratar todas as verificações no cliente como meramente indicativas.

## Padrão de evidência

Este laboratório regista o raciocínio em vez de publicar um patch contra
software de terceiros. A conclusão é reproduzível a partir do source, do
sample gerado e da tooling de inspecção incluída neste repositório.

## Conclusão do operador

O resultado mais forte não é mudar uma string ou forçar um branch. É identificar
a falha na fronteira de confiança, prová-la com o mínimo de evidência necessária
e explicar o desenho que elimina a fraqueza.
