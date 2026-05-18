# Mitosis

Juego desarrollado en Python con pygame, inspirado en [agar.io](https://agar.io). Arquitectura cliente-servidor: el servidor maneja toda la lógica del juego y el cliente se encarga exclusivamente del renderizado y la entrada del usuario.

## Instalación (desarrolladores)

**Linux / macOS:**
```bash
./setup.sh
source venv/bin/activate
```

**Windows:**
```bat
setup.bat
venv\Scripts\activate
```

Los scripts crean el entorno virtual e instalan las dependencias automáticamente.

## Cómo correr

El servidor y el cliente se corren por separado desde la raíz del proyecto.

**Servidor:**
```bash
python -m server.main
```

**Cliente:**
```bash
python -m client.main
```

El servidor escucha en `127.0.0.1:5000` por defecto.

## Ejecutable

Los ejecutables pre-compilados para Linux, Windows y macOS están disponibles en la sección [Releases](../../releases) del repositorio. No requieren tener Python instalado.

Para compilar el ejecutable localmente:

**Linux / macOS:**
```bash
source venv/bin/activate
pyinstaller client.spec --distpath dist --workpath build/pyinstaller
```

**Windows:**
```bat
venv\Scripts\activate
pyinstaller client.spec --distpath dist --workpath build\pyinstaller
```

## Controles

| Tecla | Acción |
|-------|--------|
| Mouse | Dirección de movimiento |
| `Espacio` | Split (dividir célula) |
| `W` | Eject (eyectar masa) |
| `Escape` | Salir de la partida |

## Mecánicas

- **Comer comida:** aumenta la masa de la célula.
- **Comer jugador:** una célula puede comer a otra si tiene al menos 1.3× su masa.
- **Split:** divide cada célula en dos. Máximo 16 células simultáneas.
- **Eject:** lanza una pequeña porción de masa hacia el cursor. Puede alimentar virus.
- **Virus:** al comerlo, la célula explota en múltiples fragmentos. Se alimentan con masa ejectada y se replican al alcanzar cierta masa. Máximo 20 virus simultáneos en el mapa.
- **Fusión:** las células divididas se fusionan automáticamente después de un tiempo.
- **Zoom:** la cámara se aleja progresivamente al ganar masa y al dividirse. Se adapta automáticamente a cualquier resolución de pantalla.

## Estructura del proyecto

```
agario/
├── client/
│   ├── camera/         # Lógica de cámara y zoom
│   ├── config/         # Configuración del cliente (UI, cámara, mapa)
│   │   └── ui/         # Configuración por estado de UI (leaderboard, playing, etc.)
│   ├── core/           # Game loop principal
│   ├── managers/       # SnapshotManager
│   ├── network/        # Conexión TCP y mensajes al servidor
│   ├── states/         # Estados del juego (menú, jugando, respawn, error)
│   ├── ui/             # Componentes de interfaz reutilizables
│   └── main.py
│
├── server/
│   ├── config/         # Configuración del servidor (jugador, comida, virus, match)
│   ├── entities/       # Cell, Player, Food, Virus
│   ├── managers/       # PlayerManager, FoodManager, VirusManager, CollisionManager
│   ├── match/          # Lógica de partida y tick
│   ├── matchmaking/    # Asignación de jugadores a partidas
│   ├── network/        # Servidor TCP y manejo de mensajes entrantes
│   └── main.py
│
├── shared/
│   ├── config/         # Configuración compartida (mapa, red)
│   └── protocol/       # Tipos de mensajes y campos del protocolo
│
├── .github/
│   └── workflows/
│       └── build-client.yml  # Build automático de ejecutables por plataforma
│
├── docs/
│   ├── README.md
│   └── PROTOCOL.md
│
├── client.spec         # Configuración de PyInstaller
├── requirements.txt    # Dependencias del cliente
├── setup.sh            # Setup para Linux / macOS
└── setup.bat           # Setup para Windows
```

## Arquitectura

```
Cliente                          Servidor
  │                                  │
  │──── CONNECT (username) ─────────>│
  │<─── MATCH_FOUND (player_id) ─────│
  │                                  │
  │──── PLAYER_INPUT (dx, dy) ──────>│  ← cada frame
  │<─── GAME_STATE (snapshot) ───────│  ← 30 veces por segundo
  │                                  │
  │      ... jugando ...             │
  │                                  │
  │<─── PLAYER_DEAD (stats) ─────────│
  │──── RESPAWN ────────────────────>│
  │                                  │
  │──── DISCONNECT ─────────────────>│
```

**Flujo del servidor (por tick):**
1. Procesar inputs recibidos de los clientes
2. Actualizar posiciones y velocidades (`PlayerManager`, `FoodManager`, `VirusManager`)
3. Detectar colisiones (`CollisionManager`)
4. Enviar snapshot del estado del mundo a todos los clientes

**Flujo del cliente (por frame):**
1. Enviar dirección del mouse al servidor
2. Recibir y almacenar el último snapshot
3. Renderizar el snapshot con interpolación de cámara y zoom
