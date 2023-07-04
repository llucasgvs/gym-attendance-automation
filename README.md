# gym-attendance-automation
Project Name: Gym Attendance Automation Automate gym attendance tracking using iPhone location. Mark days as paid when spending 30+ minutes near the gym. Streamline monitoring without manual effort. Efficiently track fitness progress.

This project aims to automate the process of tracking your visits to the gym based on your iPhone's location. By using the iCloud API and Python, this script will check if your iPhone's location matches the gym's location and mark the day as paid if you stay there for more than 30 minutes. The goal is to provide an automated way to keep track of your gym attendances without manual intervention.

## Setup and Usage

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Open the `localizacao_academia.py` file and replace `<your_email>` and `<your_password>` with your iCloud credentials.
4. Modify the latitude and longitude values in the `marca_dia_pago()` function with the coordinates of your gym.
5. Run the script either manually or schedule it to run automatically using task schedulers or cloud services.

## Dependencies

This project relies on the following dependencies:

- pyicloud (for interfacing with the iCloud API)
- datetime (for dealing with dates and times)

Please refer to the `requirements.txt` file for the specific versions of the dependencies.

## Contributing

Contributions to this project are welcome. If you have any suggestions or would like to add new features, please create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

**README.md (Versão em português do Brasil):**
```
# Automacao-academia

Este projeto tem como objetivo automatizar o processo de registro de suas visitas à academia com base na localização do seu iPhone. Utilizando a API do iCloud e Python, este script irá verificar se a localização do seu iPhone corresponde à localização da academia e marcar o dia como pago se você permanecer lá por mais de 30 minutos. O objetivo é fornecer uma maneira automatizada de acompanhar suas idas à academia sem intervenção manual.

## Configuração e Uso

Para utilizar este script, siga os seguintes passos:

1. Clone este repositório em sua máquina local.
2. Instale as dependências Python necessárias executando `pip install -r requirements.txt`.
3. Abra o arquivo `localizacao_academia.py` e substitua `<seu_email>` e `<sua_senha>` pelas suas credenciais do iCloud.
4. Modifique os valores de latitude e longitude na função `marca_dia_pago()` com as coordenadas da sua academia.
5. Execute o script manualmente ou agende sua execução automaticamente usando agendadores de tarefas ou serviços em nuvem.

## Dependências

Este projeto depende das seguintes bibliotecas:

- pyicloud (para interagir com a API do iCloud)
- datetime (para lidar com datas e horas)

Por favor, consulte o arquivo `requirements.txt` para verificar as versões específicas das dependências.

## Contribuição

Contribuições para este projeto são bem-vindas. Se você tiver sugestões ou desejar adicionar novos recursos, por favor, crie uma pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
