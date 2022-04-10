# ERC20-Token
Proyecto de brownie para la creación y deployment de un token con el estandar ERC20 a blockchain ethereum.

## Instrucciones

Crear un fichero .env con tus credenciales de Infura que usaremos como endpoint para acceder a la cadena de bloques, tu clave privada, y un etherscan token en caso de que quieras verificar tus contratos en etherscan.

### Example 

export PRIVATE_KEY=<your_wallet_private_key>
export WEB3_INFURA_PROJECT_ID=<your_infura_project_id>
export ETHERSCAN_TOKEN=<your_etherscan_token>

## Comandos
"brownie compile"
"brownie run ./scripts/deploy_token.py"