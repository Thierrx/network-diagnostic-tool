# NetDiag — Network Diagnostic Tool

Uma ferramenta de diagnóstico de rede desenvolvida em Python, com interface web, que permite consultar endereços IP, testar conectividade e analisar a latência de um domínio.

## 🖥️ Interface

O NetDiag possui uma interface web desenvolvida com HTML e CSS, conectada a um backend Python utilizando Flask.

## 🚀 Funcionalidades

- Consulta DNS para obter o endereço IPv4 de um domínio.
- Teste de conectividade utilizando Ping.
- Cálculo da latência média.
- Exibição do resultado dos testes na interface.
- Comunicação entre frontend e backend por requisições HTTP e JSON.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Lógica e diagnóstico de rede |
| Flask | Servidor web e endpoint da API |
| HTML | Estrutura da interface |
| CSS | Estilização da interface |
| JavaScript | Interação e comunicação com o backend |
| Socket | Consulta DNS |
| Subprocess | Execução do comando Ping |
| Regex | Extração dos tempos de resposta |

## 📁 Estrutura do projeto

```text
network-diagnostic-tool/
│
├── main.py
├── interface.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
└── requirements.txt
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd network-diagnostic-tool
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python interface.py
```

### 5. Acesse no navegador

```text
http://127.0.0.1:5000
```

Digite um domínio, como `google.com`, e inicie o diagnóstico.

## 📚 Aprendizados

Este projeto foi desenvolvido com o objetivo de praticar programação em Python, conceitos de redes, desenvolvimento web, integração entre frontend e backend e utilização de APIs.

## 👨‍💻 Autor

Desenvolvido como projeto de estudo e prática em desenvolvimento de software.