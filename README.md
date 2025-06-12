Integrantes : João vitor Vilas Boas & Taila Camargo.

# 🔐 Gerenciador de Senhas com Autenticação

## 🧠 1. Definição da Aplicação Web

Essa aplicação é um **gerenciador de senhas** pessoal, com autenticação simples. Foi criada para fins de prática em desenvolvimento web e testes automatizados com Selenium + Pytest.

### 🎯 Funcionalidades:

- Página de login com usuário/senha fixos (`admin / 1234`);
- Geração de senhas fortes usando critérios de segurança;
- Associação de senhas com redes sociais (Instagram, Gmail, etc.);
- Exibição de lista com as senhas associadas;
- Validações de erro para campos vazios, login incorreto, etc.

> **Tecnologias utilizadas:**  
> - Backend: Python (Flask)  
> - Frontend: HTML, CSS, JS  
> - Testes: Selenium WebDriver + Pytest  

---

## ✅ 2. Principais Fluxos de Interação a Serem Validados

| Fluxo                        | Descrição                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| **Login**                   | Usuário acessa com login fixo (`admin/1234`).                             |
| **Geração de Senha**        | Após login, usuário clica em "Gerar Senha". Backend gera uma senha forte. |
| **Associação à Rede Social**| Usuário insere nome da rede e vincula à senha.                            |
| **Exibição de Senhas**      | Lista atualizada com todas as senhas associadas.                          |
| **Erros/Validações**        | Testar login inválido, campos em branco, cliques sem preencher, etc.      |

---

## 🧮 3. Tabela de Decisão

| Regra Nº | Login correto | Gerar senha clicado | Nome de rede inserido | Campos vazios | Ação esperada                                           |
|----------|----------------|---------------------|------------------------|----------------|----------------------------------------------------------|
| 1        | Sim            | Sim                 | Sim                    | Não            | Senha gerada e associada à rede. Exibir na lista.       |
| 2        | Sim            | Sim                 | Não                    | Não            | Exibir erro: "Informe o nome da rede social."           |
| 3        | Sim            | Não                 | -                      | -              | Nenhuma ação. Aguardar clique no botão.                 |
| 4        | Sim            | Sim                 | Sim                    | Sim            | Exibir erro: "Preencha todos os campos obrigatórios."   |
| 5        | Não            | -                   | -                      | -              | Exibir erro de login. Não permite acesso.               |
| 6        | Sim            | -                   | -                      | Sim            | Exibir erro: "Campos de entrada não podem estar vazios."|
| 7        | Sim            | Sim                 | Sim                    | Não            | Associar senha com rede. Exibir lista atualizada.       |
| 8        | Sim            | Sim                 | Sim                    | Não            | Verificar se a senha atende critérios fortes.           |

---

## 🧪 4. Testes Automatizados

Foram criados testes automatizados usando:

- **Selenium WebDriver** para interação com o navegador
- **Pytest** como framework de testes
- Execução dos testes feita com `pytest` no terminal

### 📂 Estrutura dos testes:
/projeto  
├── app.py  
├── static/  
├── templates/  
├── tests/  
│ └── test_app.py  
├── venv/  
└── requirements.txt  





📦 6. Como Rodar o Projeto:

1-Clone o repositório:

git clone https://github.com/seu-user/mega_gerator.git  
cd mega_gerator

2-Ative o ambiente virtual:
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

3-Instale as dependências:
pip install -r requirements.txt


4-Rode a aplicação:  
```python app.py```  
Acesse em: http://127.0.0.1:5000  

🧪 Rodando os Testes  
```pytest```


📸 Evidências dos Testes
As evidências de execução estão disponíveis na pasta evidencias/:

-Prints de execução do Selenium

-Logs dos testes com Pytest






