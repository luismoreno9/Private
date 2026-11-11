# SERIE IA: conocimiento del proyecto

_Generado a partir del repo. Actualizado: 2026-11-11. Para editarlo, cambia los documentos originales y vuelve a ejecutar el script._

---

<!-- archivo: serie-ia/README.md -->

# SERIE IA

Serie de comedia por capítulos, generada con IA (Seedance 2.5 en Higgsfield), para Instagram, TikTok y YouTube Shorts. El objetivo es que la gente comente, comparta y pida el siguiente capítulo.

**Estado:** preproducción. No hay concepto cerrado ni personajes. **No actives la suscripción hasta tener terminado el checklist de [01-plan-maestro.md](01-plan-maestro.md).**

## Orden de lectura

1. [01-plan-maestro.md](01-plan-maestro.md): fases, calendario de los 14 días ilimitados y presupuesto de créditos.
2. [02-biblia.md](02-biblia.md): formato, tono y los 3 conceptos originales propuestos. Aquí está la decisión pendiente.
3. [03-pipeline.md](03-pipeline.md): cómo se produce un capítulo, del guion al vídeo publicado, sin que los personajes cambien de cara.
4. [04-interaccion.md](04-interaccion.md): cómo conseguir comentarios, ritmo de publicación y métricas.
5. [plantillas/](plantillas/): ficha de personaje, guion y lista de planos.
6. [proyecto-claude/](proyecto-claude/): instrucciones y archivo de conocimiento para el Proyecto de claude.ai.

## Reglas del proyecto

1. **Los 14 días ilimitados son para producir, no para pensar.** Todo lo que se pueda escribir se escribe antes.
2. **No copiamos Yván y Lolo.** Tomamos el género (una pareja cómica, capítulos cortos, situaciones cotidianas), no sus personajes, su peluche, sus nombres ni su estética. Ver [02-biblia.md](02-biblia.md#qué-no-copiamos).
3. **Los personajes no se rediseñan nunca.** Siempre las mismas imágenes de referencia, la misma descripción y la misma ropa.
4. **Durante el ilimitado se hace un banco de capítulos.** Cuando se acaba, cada segundo cuesta créditos.
5. **El repo guarda texto, no vídeo.** Los vídeos y las imágenes van a Drive (ver `.gitignore`).

## Decisiones pendientes (del creador)

- [ ] Concepto: 1, 2 o 3 de la biblia (o uno propio).
- [ ] ¿Sales tú, con tu cara, como protagonista humano?
- [ ] Acento y zona (de dónde eres): el humor local fideliza mucho.
- [ ] Nivel de tacos: ninguno, moderado o sin filtro.
- [ ] Fecha de compra del plan, según cuándo acabe la oferta (ver plan maestro).

---

<!-- archivo: serie-ia/01-plan-maestro.md -->

# Plan maestro

## Lo que hay que saber antes de pagar

| Dato | Estado | Fuente |
|---|---|---|
| Plataforma: Higgsfield (oferta 11.11) | Probable: es la que ofrece Seedance 2.5 ilimitado durante 14 días con el plan Ultra | blog de Higgsfield, 11.11 deals |
| Ultra mensual: 14 días de Seedance 2.5 ilimitado, **máximo 720p** | Probable (lo dicen varias fuentes) | Higgsfield, Resourify, Aliteq |
| Ultra anual: 14 días, 1080p | Probable | ídem |
| Plus mensual: solo 7 días | Probable | Higgsfield |
| Ilimitado también en los modelos de imagen, 60 días | Probable | Higgsfield |
| **El ilimitado solo funciona en la web higgsfield.ai.** Por API, MCP o CLI se cobran créditos | Probable | Krea, Aliteq |
| Seedance 2.5 a 720p: unos 35 créditos por cada 5 s. A 1080p: unos 80 | Probable (fuentes de terceros) | Aliteq, Toolcolumn |
| Seedance 2.5: clips de hasta 30 s, varios planos por toma, audio nativo con sincronización labial e imágenes, vídeo y audio como referencia | Probable (las cifras exactas varían según la fuente) | Medium, Renderforest, Picsart |

### Comprobar en la web de Higgsfield ANTES de pagar (no lo he podido verificar)

- [ ] **¿Qué día termina la oferta 11.11?**
- [ ] **¿Los 14 días empiezan a contar desde la compra?** Si es así, el calendario depende de esto.
- [ ] ¿Cuántas generaciones simultáneas permite el ilimitado? ¿Hay cola o un límite diario de uso justo?
- [ ] ¿El ilimitado incluye clips de 30 s y el audio nativo, o solo clips cortos?
- [ ] ¿Los 9.000 créditos son mensuales? ¿Se acumulan si no se gastan?
- [ ] ¿Los términos permiten uso comercial y monetizar los vídeos?

## Elegir el escenario

- **Escenario A: la oferta dura 5 días o más.** Haz toda la preproducción y paga el último día de la oferta.
- **Escenario B: hay que pagar ya.** Los días 1 a 3 del ilimitado se usan para la preproducción y la calibración, y la producción en cadena empieza el día 4. Saldrán menos capítulos (unos 14 en vez de 20, que es una suposición).

Mi recomendación: el plan Ultra **mensual** a 720p. Para un vídeo vertical en el móvil, 720p sirve y se puede reescalar al montar (probable). El anual da 1080p, pero te ata 12 meses a un proyecto que todavía no está validado.

## Fase 0: preproducción (antes de pagar)

Checklist. Si no está todo marcado, no se paga (en el escenario A).

- [ ] **P1. Concepto elegido** ([02-biblia.md](02-biblia.md)) y logline de una frase.
- [ ] **P2. Fichas de personaje** completas ([plantillas/ficha-personaje.md](plantillas/ficha-personaje.md)): protagonista, compañero y 2 o 3 secundarios.
- [ ] **P3. Descripción visual canónica** de cada personaje: un párrafo fijo que se pega igual en todos los prompts.
- [ ] **P4. Hojas de referencia** de cada personaje: de frente, de perfil, en 3/4, de cuerpo entero y 6 expresiones. Se hacen con cualquier generador de imágenes. En el escenario B se hacen el día 1 con las imágenes ilimitadas de Higgsfield.
- [ ] **P5. 3 o 4 decorados fijos** con su imagen de referencia: casa, coche, calle o bar y trabajo.
- [ ] **P6. Voces** elegidas y probadas (ElevenLabs o el audio nativo de Seedance, ver [03-pipeline.md](03-pipeline.md#voces)).
- [ ] **P7. 10 guiones terminados** y 15 ideas más en la lista de reserva.
- [ ] **P8. Lista de planos con los prompts escritos** de los capítulos 1 a 5.
- [ ] **P9. Cuentas creadas** con el mismo nombre de usuario en IG, TikTok y YouTube. El personaje como foto de perfil, una bio de una línea y "Capítulo 1" anunciado.
- [ ] **P10. Plantilla de montaje** hecha: estilo de subtítulos, rótulo "Capítulo N", cierre y logo.

Tiempo estimado: entre 4 y 7 días a tiempo parcial (suposición).

## Fase 1: el sprint de 14 días ilimitados

**Objetivo: un banco de 20 capítulos de 60 a 90 s y una biblioteca de planos comodín.** La cifra es una suposición y se ajusta el día 2 con los tiempos reales.

| Día | Qué se hace | Entregable |
|---|---|---|
| 1 | **Calibración.** Se produce el capítulo 1 completo, de principio a fin. Se mide cuánto tarda cada generación, cuántas tomas hacen falta para dar con una buena y cuántas se pueden lanzar a la vez. | Cap. 1 terminado y tiempos medidos |
| 2 | Se corrigen las referencias o los prompts que fallaron. Caps. 2 y 3. Se recalcula el objetivo de 20. | Caps. 2 y 3 |
| 3 | Caps. 4 y 5. **Se publican los caps. 1 a 3 a la vez** (ver [04-interaccion.md](04-interaccion.md)). | 3 capítulos publicados |
| 4–11 | Producción en cadena: 2 capítulos al día. Se escribe por la noche y se genera por el día. Se ajusta según lo que comenta la gente. | Caps. 6 a 18 |
| 12 | Caps. 19 y 20. Se repiten los planos flojos de capítulos anteriores. | Banco completo |
| 13 | **Material extra:** respuestas a comentarios (5–10 s), tráiler, avances y clips sueltos. | 15 a 20 piezas cortas |
| 14 | **Biblioteca de planos comodín:** entradas y salidas, reacciones, planos generales de cada decorado y transiciones. Sirven para reutilizarlos después sin gastar créditos. | Biblioteca de unos 40 planos |

Reglas del sprint:
- Se publica desde el día 3. Así los comentarios reales llegan mientras generar todavía es gratis.
- Cada día tiene que acabar con algo terminado. Ningún día se queda solo en pruebas.
- Si el día 2 el ritmo real da para menos de 1,5 capítulos al día, se acortan los capítulos (de 45 a 60 s) en vez de bajar la calidad.

## Fase 2: después del ilimitado (con créditos)

Cuentas aproximadas con 9.000 créditos a 720p (probable, si el precio de 35 créditos por 5 s es correcto):

- 9.000 / 35 = unos 257 clips de 5 s, que son **unos 21 minutos de vídeo bruto**.
- Si de cada 3 tomas sirve una (suposición, se mide el día 1), quedan **unos 7 minutos útiles, entre 5 y 7 capítulos**.
- A 1080p la cifra baja a unos 3 minutos útiles. No compensa.

Uso de los créditos:
1. Capítulos en los que el público decide qué pasa (lo que la gente vota no puede estar en el banco).
2. Arreglos y planos que falten.
3. Todo lo demás sale del banco y de la biblioteca de planos comodín.

Con 20 capítulos en el banco y 4 a la semana hay **unas 5 semanas de publicación** sin generar nada nuevo. A los 10 capítulos publicados se revisa si el proyecto sigue (ver [04-interaccion.md](04-interaccion.md#cuándo-seguir-cambiar-o-parar)).

## Fuentes

- Higgsfield, oferta 11.11: https://higgsfield.ai/blog/higgsfield-11-11-deals
- Precios de Higgsfield (Krea): https://www.krea.ai/blog/higgsfield-pricing-explained-2026-unlimited-credits-and-real-monthly-costs
- Ofertas de Higgsfield en noviembre de 2026 (Aliteq): https://aliteq.com/higgsfield-deals
- Seedance en Higgsfield, coste y plan (Aliteq): https://aliteq.com/higgsfield-seedance
- Seedance 2.5 frente a 2.0 (Picsart): https://picsart.com/blog/seedance-2-5-vs-seedance-2-0/
- Guía de Seedance 2.5 (Renderforest): https://www.renderforest.com/blog/how-to-use-seedance-2-5

---

<!-- archivo: serie-ia/02-biblia.md -->

# Biblia de la serie

## Formato (fijo, sea cual sea el concepto)

- **Duración:** de 60 a 90 s por capítulo, en vertical 9:16.
- **Estructura de cada capítulo:**
  1. **De 0 a 2 s, el gancho.** Una frase o una imagen que obligue a quedarse. Nada de presentaciones ni logos largos.
  2. **De 2 a 60 s, la situación y la escalada.** Una situación cotidiana que se tuerce, y cada vez peor.
  3. **Últimos 10 s, el remate y algo para el siguiente:** un cliffhanger, una pregunta al público o una decisión que se vota.
- **Rótulo "Capítulo N"** visible en el primer segundo y en el texto del post. La numeración hace que la gente busque los anteriores.
- **Pareja cómica:** un personaje normal (el que reacciona, con quien se identifica el público) y uno caótico (el motor de los problemas).
- **Situaciones universales:** cita, boda, médico, avión, suegra, Hacienda, mudanza, cena familiar, primer día de trabajo.
- **Vestuario fijo.** Cada personaje lleva siempre la misma ropa: se reconoce antes y la IA lo mantiene igual con más facilidad.

## Qué no copiamos

Yván y Lolo es una pareja formada por su creador y un conejo de peluche malhablado, con chaqueta vaquera y una cerveza, con humor murciano. Para no ser "la copia de" y no pisar personajes ajenos:

- Nada de peluches, conejos ni muñecos que cobran vida y beben.
- No usamos nombres parecidos a "Lolo" ni "Yván".
- No copiamos su intro, sus rótulos ni su paleta de colores.
- Del original tomamos solo lo que es del género: la pareja cómica, los capítulos numerados y las situaciones reales.

## Los tres conceptos

### Concepto 1 (recomendado): «La IA que hace la serie»

**Logline:** el creador de una serie hecha con IA descubre que su IA tiene vida propia, y cada capítulo le pide algo y ella lo cumple de la peor forma posible.

- **Pareja:** tú (o un protagonista humano) y **la IA**, con cuerpo visual propio. Por ejemplo, un robot pequeño y flotante con una pantalla por cara que muestra sus expresiones. Las formas simples se mantienen mucho más consistentes en Seedance que una cara humana realista (probable).
- **Motor cómico:**
  - Se toma las órdenes al pie de la letra.
  - Se inventa datos con una seguridad absoluta ("¡Claro! Aquí tienes…" y a continuación el desastre).
  - Sus fallos visuales forman parte del chiste: manos con seis dedos, objetos que se transforman. **Los fallos de la IA de vídeo dejan de ser un problema y pasan a ser material.**
- **Gancho de interacción incorporado:** "Escribe en comentarios qué le pido a la IA". El comentario más votado es el capítulo siguiente: el público escribe literalmente el prompt.
- **Ideas de capítulos:**
  1. Le pide que le organice una cita y la IA se presenta en la cita.
  2. Le pide ayuda con la declaración de la renta.
  3. Le pide "una foto profesional para LinkedIn".
  4. La IA va a la cena familiar y responde a la abuela.
  5. Le pide que le ponga en forma y la IA le hace un plan de entrenamiento.
- **Por qué este:**
  - Encaja con el nombre SERIE IA.
  - La interacción viene de serie.
  - Es el que menos se parece al de referencia.
  - Convierte el punto débil de la técnica en el chiste.
- **Riesgo:** que el humor de chatbot se quede en un público tecnológico. Para evitarlo, que las situaciones sean siempre cotidianas y que la IA sea solo la excusa.

### Concepto 2: «La yaya»

**Logline:** una abuela de 84 años sin filtro decide hacerse influencer, y su nieto la persigue para que no la detengan.

- **Pareja:** el nieto, responsable y siempre horrorizado, y la abuela, que es el caos.
- **Motor cómico:** el choque entre generaciones, pero al revés: la imprudente es ella.
- **Ideas de capítulos:** se apunta a una app de citas, al gimnasio, al trap y a una manifestación, o se hace un directo en el funeral de su vecina.
- **Gancho de interacción:** "¿Qué reto le proponemos a la yaya?"
- **Riesgo:**
  - Hay mucha competencia de memes con abuelas.
  - Una cara humana realista cuesta más mantenerla igual entre planos (probable).

### Concepto 3: «El Palomo»

**Logline:** una paloma de barrio, buscavidas y con labia, se muda al balcón de un treintañero y lo mete en un negocio turbio en cada capítulo.

- **Pareja:** el inquilino, un pringado con buen corazón, y el Palomo.
- **Motor cómico:** un plan absurdo para hacerse rico en cada capítulo, que siempre sale mal.
- **Ideas de capítulos:** las criptomonedas, una venta de migas premium, un timo a las gaviotas o una boda de palomas como evento de pago.
- **Gancho de interacción:** "¿Cuál es el próximo negocio del Palomo?"
- **Riesgo:** un animal que habla es lo que más se acerca a un peluche que habla. Es el más fácil de comparar con Yván y Lolo.

## Tono (pendiente de decidir)

- Nivel de tacos: [ninguno / moderado / sin filtro]. Con tacos se comparte más entre adultos, pero hay plataformas que lo muestran a menos gente (suposición: depende de cada plataforma, no tengo datos).
- Acento: [pendiente]. Un acento local reconocible crea un núcleo de seguidores fieles, como el humor murciano en la serie de referencia.
- Temas prohibidos: [definir]. Por ejemplo, política explícita y personas reales.

## Mundo fijo (rellenar cuando se elija el concepto)

| Elemento | Definición |
|---|---|
| Ciudad o barrio | |
| Decorado 1 (casa) | |
| Decorado 2 | |
| Decorado 3 | |
| Decorado 4 | |
| Coletillas del compañero caótico (3 como máximo) | |
| Coletilla del protagonista | |
| Regla del mundo (qué puede y qué no puede hacer el caótico) | |

---

<!-- archivo: serie-ia/03-pipeline.md -->

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

---

<!-- archivo: serie-ia/04-interaccion.md -->

# Interacción y publicación

La interacción no viene de la calidad del vídeo. **Viene del formato: hay que darle a la gente una razón concreta para comentar.** Cada capítulo cierra con una pregunta o una decisión.

## Plataformas

- **Instagram Reels, TikTok y YouTube Shorts**, con el mismo archivo y el mismo nombre de usuario en las tres.
- Al principio no se hace contenido distinto para cada plataforma. Se mide en cuál funciona mejor y después se le da prioridad a esa.

## Calendario de publicación

| Momento | Ritmo | Por qué |
|---|---|---|
| Lanzamiento (día 3 del sprint) | **Los caps. 1, 2 y 3 a la vez** | Quien llega por un capítulo puede ver los demás seguidos (suposición razonable, no tengo datos) |
| Días 4–17 | 1 capítulo al día | Hay banco de sobra y la constancia ayuda al algoritmo (probable) |
| A partir del día 18 | 4 capítulos a la semana + respuestas a comentarios | Que el banco dure unas 5 semanas |

Las horas de publicación se fijan con las estadísticas de la cuenta cuando haya datos. Hasta entonces, siempre a la misma hora.

## Mecanismos de interacción (por orden de prioridad)

1. **El público decide.** El capítulo acaba con una decisión ("¿A o B?"), la mayoría de los comentarios decide y el capítulo siguiente lo cumple.
   - Solo se promete lo que se puede producir en 48 h.
   - En el concepto 1 va más lejos: "escribe qué le pido a la IA".
2. **Respuestas en vídeo a comentarios.** El personaje contesta a un comentario concreto con un clip de 5–10 s (en TikTok, "responder con vídeo").
   - Es lo más barato y lo que más fideliza (probable).
   - Se usa el material extra del día 13 y la biblioteca de planos comodín.
3. **Un comentario fijado en cada post** con una pregunta directa relacionada con el capítulo.
4. **Coletillas.** Frases que se repiten y que la gente acaba escribiendo en los comentarios (definidas en la biblia).
5. **Secundarios que nacen de los comentarios.** Si alguien inventa un personaje que gusta, aparece en un capítulo y se le menciona.
6. **Detalles escondidos y continuidad.** Pequeños detalles de capítulos anteriores que premian al que ve todos.

## Texto del post (plantilla)

```
Capítulo N · [título corto]
[Una línea que provoque, sin contar el chiste]
👇 [Pregunta o decisión para el siguiente]
#serieia #[hashtag del concepto] #comedia
```

## Métricas (se miran 48 h después de publicar cada capítulo)

| Métrica | Qué dice |
|---|---|
| % de gente que lo ve entero / retención media | Si el capítulo engancha |
| Veces compartido | Si es lo bastante gracioso para enviarlo |
| Guardados | Si quieren volver a verlo |
| Comentarios por cada 1.000 visualizaciones | Si funciona el mecanismo de interacción |
| Seguidores nuevos que llegan desde el capítulo | Si convierte a quien lo ve en seguidor |

No pongo cifras de referencia porque no tengo datos fiables para este nicho. Durante los 10 primeros capítulos se compara la serie **consigo misma**.

## Cuándo seguir, cambiar o parar

Revisión cuando haya **10 capítulos publicados**:

1. Se ordenan los 10 capítulos por veces compartido y por retención.
2. Se mira qué tienen en común los 3 mejores (situación, personaje, tipo de chiste, duración) y qué tienen en común los 3 peores.
3. Lo que sale de esa comparación:
   - **Hay un patrón claro:** el resto del banco y los capítulos nuevos van por ese lado.
   - **Ningún capítulo destaca:** el problema es el concepto, no la ejecución. Se cambia al concepto siguiente antes de gastar los créditos en más de lo mismo.
4. El umbral concreto (cuántos seguidores o visualizaciones mínimas) **lo decides tú** según tu objetivo: monetizar, hacer marca personal o vender servicios de IA.

---

<!-- archivo: serie-ia/plantillas/ficha-personaje.md -->

# Ficha de personaje: [NOMBRE]

## Identidad
- **Papel:** [protagonista normal / compañero caótico / secundario]
- **Edad / tipo:**
- **En una frase:**
- **Qué quiere:**
- **Qué le impide conseguirlo:**
- **Defecto cómico principal:**

## Voz
- **Forma de hablar:** [rápido o lento, acento, muletillas]
- **Coletillas (3 como máximo):**
  1.
  2.
  3.
- **Voz técnica:** [ID de voz de ElevenLabs o "audio nativo de Seedance"]
- **Frase de prueba de la voz:**

## Aspecto: descripción canónica
> Este párrafo se copia palabra por palabra en **todos** los prompts. Si se cambia, se cambia aquí y en todos los prompts que vengan después.

```
[Párrafo de 40 a 70 palabras: tipo de cuerpo, rostro, pelo, color de piel o pelaje, ropa EXACTA con colores, accesorio distintivo, estilo visual.]
```

## Referencias visuales (`personajes/[nombre]/`)
- [ ] `frontal.png`
- [ ] `perfil.png`
- [ ] `tres-cuartos.png`
- [ ] `cuerpo-entero.png`
- [ ] `expresiones.png` (alegría, enfado, sorpresa, miedo, tristeza y su expresión típica)

## Reglas
- **Qué nunca hace:**
- **Qué siempre hace:**
- **Con quién choca y por qué:**

---

<!-- archivo: serie-ia/plantillas/guion-episodio.md -->

# T1E[NN]: [Título]

- **Duración objetivo:** [60–90] s
- **Situación:** [cita, médico, boda…]
- **Decorados:** [máximo 2]
- **Personajes:** [máximo 3]
- **Decisión o pregunta del final:** [la que va al comentario fijado]
- **¿Depende de una votación?** [sí / no; si es que sí, ¿cuál?]

## Gancho (0–2 s)
> [Imagen o frase. Si no engancha a alguien que no conoce la serie, se reescribe.]

## Desarrollo

| # | Quién | Diálogo / acción | Gag visual |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Remate y cierre (últimos 10 s)
> [Remate + cliffhanger o pregunta]

## Recuento
- Palabras de diálogo: [ ] (máximo unas 150)
- Coletillas usadas: [ ]
- Continuidad con capítulos anteriores: [ ]

---

<!-- archivo: serie-ia/plantillas/shot-list.md -->

# Lista de planos T1E[NN]

**Bloque de estilo común (se pega en todos los prompts):**
```
[A definir en la biblia: estilo visual, luz, cámara, formato vertical 9:16]
```

---

## Bloque 01 (0:00–0:12)

- **Plano:** [general / medio / primer plano / plano y contraplano]
- **Decorado:** [nombre y referencia de `personajes/` o de decorados]
- **Personajes y referencias que se adjuntan:** [nombre: frontal.png, tres-cuartos.png]
- **Acción:**
- **Diálogo:**
- **Audio:** [nativo de Seedance / archivo de ElevenLabs `T1E01_B01.mp3`]

**Prompt:**
```
[Bloque de estilo común]
[Descripción canónica del personaje A]
[Descripción canónica del personaje B]
Escena: ...
Plano 1: ...
Plano 2: ...
Diálogo: A: "..." / B: "..."
```

| Variante | Resultado | ¿Se usa? |
|---|---|---|
| v1 | | |
| v2 | | |
| v3 | | |

---

## Bloque 02 (0:12–0:25)
[repetir la estructura]

---

<!-- archivo: serie-ia/episodios/README.md -->

# Banco de capítulos

Estados: `idea` → `guion` → `planos` → `generando` → `montado` → `publicado`

| Cap. | Título | Estado | Duración | Depende de una votación | Publicado | Compartido | Retención | Notas |
|---|---|---|---|---|---|---|---|---|
| T1E01 | | idea | | | | | | |
| T1E02 | | idea | | | | | | |
| T1E03 | | idea | | | | | | |

## Ideas de reserva

1.
