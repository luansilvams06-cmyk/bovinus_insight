# DOCUMENTAÇÃO TÉCNICA — BOVINUS INSIGHT

**Projeto:** BOVINUS Insight  
**Evento:** Hackathon FMU & Bovinu'S  
**Área:** Tecnologia da Informação e Gestão de Alimentação  
**Instituição:** FMU  
**Local:** São Paulo — SP  
**Ano:** 2026

---

## 1. INTRODUÇÃO

O BOVINUS Insight é um sistema desenvolvido no contexto do Hackathon FMU & Bovinu'S, com a proposta de apoiar o acompanhamento e a gestão de operações relacionadas à alimentação.

A aplicação apresenta um painel de controle com indicadores e módulos destinados ao registro e acompanhamento de informações sobre pratos, filas, mesas e qualidade dos alimentos.

A solução busca centralizar informações operacionais em um único ambiente, facilitando a visualização dos dados e contribuindo para a tomada de decisões.

## 2. OBJETIVO DO PROJETO

O objetivo principal do BOVINUS Insight é desenvolver uma aplicação web capaz de organizar informações da operação de alimentação e apresentar indicadores de acompanhamento.

Entre os objetivos específicos estão:

- Registrar informações sobre pratos e alimentos.
- Acompanhar informações relacionadas às filas.
- Organizar o controle de mesas e limpeza.
- Registrar avaliações de qualidade dos alimentos.
- Acompanhar sobras e comentários sobre os pratos.
- Apresentar indicadores em um painel central.

## 3. TECNOLOGIAS UTILIZADAS

O desenvolvimento utiliza as seguintes tecnologias:

**Python:** linguagem utilizada na lógica e no funcionamento da aplicação.

**Flask:** framework responsável pela criação da aplicação web e pelo gerenciamento das rotas.

**HTML:** estruturação das páginas e dos formulários.

**CSS:** estilização e organização visual da interface.

**JavaScript:** implementação de comportamentos e interações no navegador.

**SQLite:** banco de dados utilizado para armazenar informações e manter os registros mesmo após o encerramento da aplicação.

**Chart.js:** biblioteca utilizada para a apresentação de gráficos e visualizações de dados.

## 4. ARQUITETURA DO SISTEMA

O BOVINUS Insight utiliza uma arquitetura web baseada em Flask.

O funcionamento geral ocorre em três partes:

1. **Interface:** páginas HTML responsáveis pela interação com o usuário.
2. **Aplicação:** código Python e Flask responsável pelo processamento das solicitações e pelo funcionamento das funcionalidades.
3. **Persistência:** banco de dados SQLite responsável pelo armazenamento dos registros.

O usuário acessa a aplicação pelo navegador. As informações inseridas nos formulários são processadas pela aplicação e armazenadas no banco de dados quando a funcionalidade correspondente está implementada.

## 5. MÓDULOS DO SISTEMA

### 5.1 Dashboard

O dashboard é a tela principal da aplicação.

Apresenta indicadores gerais relacionados à operação, permitindo acompanhar informações como:

- Quantidade de pratos registrados.
- Peso total registrado.
- Informações sobre filas.
- Avaliações de qualidade.

### 5.2 Módulo de pratos

Responsável pelo registro e acompanhamento de informações sobre os pratos e alimentos.

Permite organizar os dados relacionados aos alimentos cadastrados no sistema.

### 5.3 Módulo de filas

Destinado ao acompanhamento das informações relacionadas às filas da operação de alimentação.

Seu propósito é facilitar a visualização e o controle dos registros referentes ao atendimento.

### 5.4 Módulo de mesas

Responsável pelo acompanhamento das informações relacionadas às mesas e à limpeza do ambiente.

O módulo contribui para a organização das informações operacionais.

### 5.5 Módulo de qualidade

Destinado ao registro de avaliações dos alimentos.

Entre as informações trabalhadas estão:

- Nome do prato.
- Nota de qualidade.
- Quantidade de sobras.
- Comentários e observações.

Esses registros ajudam a acompanhar a percepção sobre a qualidade dos alimentos.

## 6. ROTAS DA APLICAÇÃO

A navegação do sistema é organizada por rotas gerenciadas pelo Flask.

Entre as rotas dos módulos estão:

| Rota | Funcionalidade |
|---|---|
| `/` | Página principal da aplicação |
| `/modulo/pratos` | Acesso ao módulo de pratos |
| `/modulo/filas` | Acesso ao módulo de filas |
| `/modulo/mesas` | Acesso ao módulo de mesas |
| `/modulo/qualidade` | Acesso ao módulo de qualidade |

## 7. BANCO DE DADOS

O projeto utiliza SQLite para a persistência das informações.

A utilização desse banco permite armazenar registros localmente, sem a necessidade de instalar um servidor de banco de dados separado.

Os dados persistidos podem continuar disponíveis após o encerramento e a reinicialização da aplicação.

O banco de dados é utilizado como suporte às funcionalidades de registro e consulta do sistema.

## 8. REQUISITOS FUNCIONAIS

Os requisitos funcionais representam as operações que o sistema deve oferecer.

- **RF01:** disponibilizar um painel principal com indicadores.
- **RF02:** permitir o acesso ao módulo de pratos.
- **RF03:** disponibilizar o módulo de filas.
- **RF04:** disponibilizar o módulo de mesas.
- **RF05:** disponibilizar o módulo de qualidade dos alimentos.
- **RF06:** permitir o registro de avaliações dos pratos.
- **RF07:** armazenar informações utilizando o banco de dados SQLite.
- **RF08:** apresentar informações de acompanhamento na interface.

## 9. REQUISITOS NÃO FUNCIONAIS

- **RNF01:** possuir interface acessível por navegador.
- **RNF02:** utilizar tecnologias de desenvolvimento web.
- **RNF03:** manter organização entre páginas, estilos e lógica da aplicação.
- **RNF04:** permitir persistência local dos registros.
- **RNF05:** apresentar navegação simples e intuitiva.
- **RNF06:** manter estrutura que permita futuras melhorias e expansões.

## 10. EXECUÇÃO DO SISTEMA

Para executar o projeto em ambiente local, são necessários:

- Python instalado.
- VS Code ou outro editor de código.
- Dependências descritas no arquivo `requirements.txt`.

Com o terminal aberto na pasta do projeto, execute:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Inicie a aplicação:

```powershell
python app.py
```

Após iniciar o servidor Flask, acesse o endereço local indicado no terminal pelo navegador.

## 11. TESTES E VALIDAÇÃO

Durante o desenvolvimento, foram realizados testes de execução e navegação da aplicação.

As verificações envolveram:

- Inicialização do servidor Flask.
- Acesso ao painel principal.
- Navegação entre os módulos.
- Visualização das páginas.
- Utilização dos formulários disponíveis.
- Verificação da persistência de registros no SQLite.

Os testes tiveram como objetivo identificar problemas de funcionamento e verificar o comportamento da aplicação durante sua utilização local.

## 12. LIMITAÇÕES DO PROJETO

O BOVINUS Insight foi desenvolvido como uma solução de prototipação no contexto de um hackathon.

A aplicação depende da inserção de informações pelos usuários e não deve ser considerada um sistema integrado a sensores ou equipamentos físicos de monitoramento.

Na versão desenvolvida, a execução ocorre em ambiente local, sem publicação confirmada em um servidor de produção.

## 13. MELHORIAS FUTURAS

Como possibilidades de evolução, o projeto poderá receber:

- Relatórios gerenciais mais completos.
- Gráficos e indicadores adicionais.
- Filtros por período.
- Controle de usuários e permissões.
- Melhorias na experiência de navegação.
- Integração com sensores e dispositivos de monitoramento.
- Hospedagem em ambiente online.
- Recursos adicionais para análise de desperdício e qualidade.

## 14. CONSIDERAÇÕES FINAIS

O BOVINUS Insight representa uma proposta de aplicação tecnológica voltada à organização e ao acompanhamento de informações da operação de alimentação.

Por meio de uma interface web, módulos específicos e armazenamento em banco de dados, o projeto busca facilitar o acesso aos registros e oferecer uma visão centralizada dos indicadores.

O desenvolvimento também proporcionou a aplicação prática de conhecimentos de programação, desenvolvimento web, banco de dados e organização de sistemas.

**BOVINUS INSIGHT — Tecnologia e informação para uma gestão mais inteligente.**