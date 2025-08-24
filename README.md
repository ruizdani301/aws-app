# aws-app
## API con AWS Lambda, API Gateway y DynamoDB
Una aplicación serverless completa que implementa operaciones CRUD usando servicios de AWS.

📋 Características
✅ CREATE - Crear nuevos items

✅ READ - Leer items individuales y listar todos

✅ UPDATE - Actualizar items existentes

✅ DELETE - Eliminar items

🚀 Serverless - Sin servidores que administrar

🔒 Escalable - Automáticamente escala con la demanda

💰 Pago por uso - Solo pagas por lo que usas


🏗️ Arquitectura
```
[Frontend] → [API Gateway] → [Lambda Functions] → [DynamoDB]
```
```
crud-app/
├── functions/                 # Código de las funciones Lambda
│   ├── create_item.py        # Crear nuevos items
│   ├── get_item.py           # Obtener item por ID
│   ├── get_all_items.py      # Obtener todos los items
│   ├── update_item.py        # Actualizar item
│   └── delete_item.py        # Eliminar item
├── template.yaml             # Configuración de infraestructura (SAM)
├── requirements.txt          # Dependencias de Python
├── test-events/              # Eventos de prueba para testing
│   ├── test-get.json         # Evento para GET
│   └── test-post.json        # Evento para POST
└── README.md                 # Este archivo
```

🛠️ Prerrequisitos
Cuenta de AWS con permisos adecuados

AWS CLI configurado con credenciales

AWS SAM CLI instalado

Docker (para testing local)

Python 3.9+

## Ejemplo
![alt text](/img/image.png)
