SOFT311-LAB2-LuisSoto
Proyecto de automatización de pruebas E2E utilizando Python, Pytest y Playwright. Incluye Page Objects para las principales páginas de la aplicación y casos de prueba automatizados para registro, login, carrito y favoritos.

📂 Estructura del proyecto
SOFT311-LAB2-LuisSoto/
├── pages/                  # Page Objects
│   ├── home_page.py
│   ├── signup_page.py
│   ├── login_page.py
│   ├── addproduct_page.py
│   └── addfavorite_page.py
├── tests/                  # Casos de prueba
│   ├── test_1_signup.py
│   ├── test_2_login.py
│   ├── test_3_home.py
│   ├── test_4_product.py
│   └── test_5_favorite.py
├── pyproject.toml          # Configuración de dependencias
└── README.md               # Documentación del proyecto

⚙️ Instalación
Clonar el repositorio:
git clone https://github.com/TU-USUARIO/SOFT311-LAB2-LuisSoto.git (github.com in Bing)  
cd SOFT311-LAB2-LuisSoto

Crear y activar entorno virtual:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instalar Playwright browsers:
playwright install

Ejecución de pruebas
Ejecutar todas las pruebas en terminal:
pytest --headed --browser=chromium --slowmo 500

Ejecutar un test específico:
pytest tests/test_4_product.py --headed --browser=chromium --slowmo 500

NOTA:
***CASO DE PRUEBA SIGNUP***
usar un correo diferente antes de ejecutar el test, esto porque el correo usado en el codigo ya contiene una cuenta creada en el sistema y si se usa el mismo correo va a indicar que el test fallo porque la cuenta
ya existe 
 ***CASO DE PRUEBA LOGIN***
 actualizar el correo por el mismo correo usado en el test de sign up, esto para validar el logueo de la cuenta que se creo con el test anterior
 

Casos de prueba automatizados
Home Page → Validar que la página principal carga correctamente.

Registro → Completar formulario de registro y crear cuenta.

Login → Iniciar sesión con credenciales válidas.

Carrito → Agregar producto al carrito y validar que aparece.

Favoritos → Agregar producto a favoritos y validar que aparece en la lista.

Requisitos:
Python 3.11+
Playwright
Pytest

Evidencia
Se recomienda correr con --headed --slowmo para observar el flujo paso a paso.
