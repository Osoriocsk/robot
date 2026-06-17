# SKILL.md - Robot Car Controller

## Descripción
Controla el robot Freenove ESP32 4WD por WiFi enviando comandos 
TCP al puerto 4000 del carro.

## Cuándo usarla
Cuando el usuario mande cualquier comando de movimiento como:
- "mueve el robot hacia adelante"
- "avanza 3 segundos"
- "gira a la derecha"
- "para el robot"

## Cómo funciona
1. Identifica la dirección del mensaje del usuario:
   - adelante, atras, izquierda, derecha, parar
2. Identifica la duración en segundos (default: 1 si no se menciona)
3. Ejecuta el script:
   python C:\Users\Juan Pablo\.openclaw\plugin-skills\robot-car\mover_robot.py <direccion> <duracion>
4. Espera a que el script termine
5. Reporta al usuario en español confirmando la acción

## Comandos disponibles
- adelante: avanza hacia adelante
- atras: retrocede
- izquierda: gira a la izquierda
- derecha: gira a la derecha
- parar: detiene el robot inmediatamente

## Ejemplos

| Mensaje usuario | Comando a ejecutar |
|---|---|
| "mueve hacia adelante 1 segundo" | python mover_robot.py adelante 1 |
| "ve hacia atrás 3 segundos" | python mover_robot.py atras 3 |
| "gira a la derecha" | python mover_robot.py derecha 1 |
| "avanza" | python mover_robot.py adelante 1 |
| "para el robot" | python mover_robot.py parar 0 |

## Respuesta al usuario
Siempre responder en español confirmando la acción. Ejemplo:
"✅ Robot moviéndose hacia adelante por 1 segundo."