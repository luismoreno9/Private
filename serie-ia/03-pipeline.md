# Pipeline de producción: cómo se hace un capítulo

El problema número uno de una serie hecha con IA es que **los personajes cambien de cara de un plano a otro**. Todo este documento está pensado para evitarlo.

## Flujo por capítulo

```
Guion → Lista de planos → Voces → Imagen inicial de cada bloque → Seedance → Selección → Montaje → Publicación
```

### 1. Guion
- Plantilla: [plantillas/guion-episodio.md](plantillas/guion-episodio.md).
- Como máximo **unas 150 palabras de diálogo** para 60–90 s. El castellano hablado va a unas 2,5 palabras por segundo y hay que dejar sitio a las pausas y a los gags visuales (probable).
- Un solo conflicto por capítulo.

### 2. Lista de planos
- Plantilla: [plantillas/shot-list.md](plantillas/shot-list.md).
- El capítulo se divide en **bloques de 10 a 15 s**, aunque Seedance 2.5 permita 30 s. Los bloques cortos dan más control, y cuando un bloque sale mal se repite solo ese trozo.
- Cada bloque lleva el plano, la acción, el diálogo, los personajes, el decorado y las referencias que se adjuntan.

### 3. Voces
Hay dos opciones. **El día 1 se prueban las dos y se elige una para toda la temporada.**

| Opción | Ventaja | Riesgo |
|---|---|---|
| A. Audio nativo de Seedance | Más rápido; la boca y la voz salen sincronizadas | La voz puede cambiar entre clips (probable) |
| B. ElevenLabs con una voz fija por personaje, y el audio como referencia en Seedance o montado encima | La voz es idéntica en todos los capítulos | Un paso más; la sincronización labial depende de cómo Seedance siga el audio |

En esta sesión de Claude Code hay acceso a ElevenLabs, así que puedo generar los diálogos con voces fijas si se elige la opción B.

### 4. Imagen inicial
- Para cada bloque se genera primero una imagen fija con los personajes y el decorado de referencia. Después se anima con Seedance a partir de esa imagen.
- Partir de una imagen mantiene a los personajes más parecidos que generar el vídeo solo con texto (probable).

### 5. Generación en Seedance
- Se lanzan **2 a 4 variantes por bloque** y se elige la mejor.
- El prompt siempre lleva la **descripción canónica** del personaje, copiada palabra por palabra de su ficha. No se reescribe nunca.
- Se apunta en la lista de planos qué variante se ha elegido.

### 6. Montaje
- Con CapCut, Premiere o DaVinci (el que domines).
- **Subtítulos grandes y quemados en el vídeo.** Mucha gente ve los vídeos sin sonido (probable).
- Se exporta a 1080×1920. Si el original es de 720p, se reescala al exportar.
- Se usa la plantilla fija: rótulo "Capítulo N", el estilo de subtítulos y el cierre.

### 7. Publicación
Ver [04-interaccion.md](04-interaccion.md).

## Reglas de consistencia

1. **Una sola hoja de referencia por personaje**, guardada en `personajes/<nombre>/`. No se regenera nunca. Si hay que cambiar algo, se hace una versión nueva y se marca la antigua como obsoleta.
2. **Una descripción canónica** por personaje, en su ficha, que se pega igual en todos los prompts.
3. **Vestuario fijo.** Si en un capítulo hace falta otra ropa, se crea una hoja de referencia nueva para ese vestuario.
4. **Decorados fijos** con su imagen de referencia. Así la casa no cambia de distribución de un capítulo a otro.
5. **Iluminación y estilo fijos:** un bloque de estilo común para todos los prompts, por ejemplo "estilo cinematográfico, luz cálida de tarde, cámara al hombro ligera" (a definir).

## Nombres de archivo y almacenamiento

```
T1E01_B03_v2.mp4   → temporada 1, episodio 01, bloque 03, variante 2
T1E01_FINAL.mp4    → capítulo montado
COMODIN_salon_entrada_01.mp4  → plano reutilizable
```

- **Vídeos e imágenes van a Google Drive**, en una carpeta `SERIE IA/` con la misma estructura. En el repo solo se guardan textos: guiones, prompts y fichas.
- Las hojas de referencia, que son imágenes pequeñas, pueden ir al repo, en `personajes/`.

## Checklist por capítulo

- [ ] Guion de 150 palabras o menos, con gancho y cierre.
- [ ] Lista de planos con todos los prompts escritos.
- [ ] Voces generadas, si se usa la opción B.
- [ ] Imagen inicial de cada bloque.
- [ ] Bloques generados y elegidos.
- [ ] Montaje con la plantilla.
- [ ] Subtítulos revisados, sin faltas.
- [ ] Revisión de 10 s: ¿alguien que no conoce la serie entiende el gancho?
- [ ] Etiqueta de contenido generado con IA activada en cada plataforma.
- [ ] Música sacada solo de la biblioteca de cada plataforma, nunca canciones con derechos subidas a mano.
- [ ] Vídeo subido a Drive y fila actualizada en [episodios/README.md](episodios/README.md).
