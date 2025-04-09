# Testes Automatizados - Contact Store

Este projeto contém testes automatizados para o formulário de contato da loja fictícia [Demoblaze](https://www.demoblaze.com/).  
Os testes foram desenvolvidos em **Python**, utilizando as bibliotecas **Selenium**, **pytest** e **pytest-xdist** (para execução em paralelo).
**Sobre o site**  
O site utilizado neste projeto, [https://www.demoblaze.com/](https://www.demoblaze.com/), é um ambiente **fictício e público**, criado exclusivamente para fins educacionais e de teste de software.  
Nenhuma informação real é enviada ou processada.

## Objetivo

Verificar o comportamento do formulário de contato, incluindo:

- Identificar a falha que permite o envio de mensagens mesmo com campos vazios.
- Verificar o alerta exibido ao enviar mensagem com dados preenchidos.

## Estrutura dos Testes

- `test_enviar_mensagem_com_dados.py`: Verifica se é possível enviar uma mensagem com todos os campos preenchidos corretamente.
- `test_enviar_mensagem_vazia.py`: Verifica uma falha na aplicação, onde é possível enviar uma mensagem **sem preencher os campos obrigatórios** e ainda assim receber confirmação de envio.

## Tecnologias utilizadas

- Python
- Selenium
- pytest
- pytest-xdist
- webdriver-manager

## Estrutura dos arquivos

```
Contact Store/
├── py/
│   ├── conftest.py
│   ├── test_enviar_mensagem_com_dados.py
│   ├── test_enviar_mensagem_vazia.py
│   ├── requirements.txt
│   └── README.md
```

## Como executar os testes

1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/seu-usuario/testes-loja-automacao.git
cd testes-loja-automacao/py
```

2. Crie e ative um ambiente virtual:

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os testes em paralelo:

```bash
pytest -n 3
```

## Observações

Os testes utilizam `webdriver-manager` para baixar e gerenciar os drivers automaticamente. Durante a execução, os navegadores Chrome, Firefox e Edge são utilizados em paralelo para validar o comportamento da aplicação.

## Autora

Ingrid Santos  
Projeto desenvolvido como prática simples.
