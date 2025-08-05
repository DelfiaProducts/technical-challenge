# Desafio de Desenvolvimento - Sistema de Categorização

## 📋 Contexto

Você está desenvolvendo um sistema de categorização de despesas que suporta dois tipos de categorias:

- **Categorização Global**: Categoria principal sem dependência de outras
- **Categorização Local**: Categoria que deve sempre ter uma categoria pai (global ou local)

## 🎯 Objetivo

Implementar a funcionalidade de criação de categorizações seguindo os cenários de teste definidos em BDD (Behavior Driven Development).

## 📁 Estrutura do Projeto

```
candidato/
├── create_categorization.py          
├── features/
│   ├── create_categorization.feature  
│   └── steps/
│       └── create_categorization_test.py  
└── README.md                         
```

## 🚀 Como Executar os Testes

```bash
# Instalar dependências
pip install behave pydantic

# Executar os testes BDD
behave features/
```

## 📋 Requisitos Técnicos

### Obrigatórios:
1. **Python** como linguagem principal
2. **Uso de Design Patterns** na solução
3. **Padrões Táticos do DDD** (Domain-Driven Design)
4. **Fazer os testes BDD passarem**

### Regras de Negócio:
- Categorização local **sempre** deve ter uma categoria pai
- Soma dos orçamentos dos filhos **não pode exceder** o orçamento do pai
- Cada categorização deve ter um ID único
- Categorização local deve ter campos específicos: `integration_data_id` e `groups`

## 🧪 Cenários de Teste

Os cenários estão definidos em `features/create_categorization.feature`:

1. **Criar categorização global** - Caso de sucesso básico
2. **Criar categorização local** - Deve ser filha de uma existente
3. **Falha por orçamento excedido** - Validação de regra de negócio

## 🎯 O que Avaliaremos

### Decisões Arquiteturais:
- Como você organiza as responsabilidades?
- Onde coloca as validações de negócio?
- Como trata a criação de diferentes tipos?
- Como abstrai a persistência?

## 🎯 Foco do Exercício

### ✅ O que queremos ver:
- **Persistência FALSA/MOCK** - use dicionários, listas, qualquer coisa simples
- **Lógica de domínio** bem estruturada e organizada

### ❌ O que NÃO precisamos:
- **Banco de dados real** ou conexões
- **APIs/Endpoints** REST ou GraphQL
- **Frameworks web** como Flask/FastAPI
- **Persistência real** em arquivos ou externos
- **Infraestrutura complexa**

## ⏰ Tempo Estimado

**30 minutos** para demonstrar suas decisões arquiteturais e implementar a estrutura principal.

## 💡 Dicas

- Foque nas **decisões arquiteturais** primeiro
- **Não é necessário** implementar tudo perfeitamente
- **Demonstre conhecimento** dos patterns e conceitos
- Alterações no **arquivo de teste** são nescessárias
- Pode criar **novos arquivos**

---

**Boa sorte! 🚀**

*Lembre-se: Queremos ver como você pensa e organiza código, não perfeição nos detalhes.*
