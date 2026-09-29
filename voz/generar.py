#!/usr/bin/env python3
"""Genera la locución de Moreno Studio con ElevenLabs (con timestamps)."""
import base64
import json
import os
import sys
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
URL = ("https://api.elevenlabs.io/v1/text-to-speech/6xftrpatV0jGmFHxDjUv/"
       "with-timestamps?output_format=mp3_44100_128")

LINEAS = [
    "Hoy, tu próximo cliente ya te está buscando.",
    "La pregunta es qué encuentra. Somos Moreno Studio.",
    "Creamos marcas que se recuerdan.",
    "Campañas de temporada, sin estudio ni rodaje.",
    "Y tiendas conectadas a todo, pensadas para convertir.",
    "Así, tus visitas empiezan a comprar.",
    "Y los resultados se notan.",
    "Nos ocupamos de todo: marca, campañas, tienda, embudos y sistemas con IA.",
    "Cuéntanos qué te está frenando. Te respondemos en menos de veinticuatro horas.",
    "Moreno Studio.",
]


def clave_env():
    for k, v in os.environ.items():
        if "ELEVEN" in k.upper() and v:
            return v
    return None


def peticion(usar_clave):
    cuerpo = {
        "text": ' <break time="0.8s" /> '.join(LINEAS),
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8,
                           "style": 0.15, "use_speaker_boost": True},
    }
    cabeceras = {"Content-Type": "application/json", "Accept": "application/json"}
    if usar_clave:
        clave = clave_env()
        if not clave:
            return None
        cabeceras["xi-api-key"] = clave
    req = urllib.request.Request(URL, data=json.dumps(cuerpo).encode("utf-8"),
                                 headers=cabeceras, method="POST")
    return urllib.request.urlopen(req, timeout=300)


def escribir_error(codigo, cuerpo):
    with open(os.path.join(AQUI, "ERROR.txt"), "w", encoding="utf-8") as f:
        f.write(f"HTTP {codigo}\n\n{cuerpo}\n")


def main():
    with open(os.path.join(AQUI, "lineas.json"), "w", encoding="utf-8") as f:
        json.dump(LINEAS, f, ensure_ascii=False, indent=2)

    try:
        try:
            resp = peticion(False)
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise
            resp = peticion(True)
            if resp is None:
                raise
        datos = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        escribir_error(e.code, e.read().decode("utf-8", "replace"))
        sys.exit(1)
    except Exception as e:  # red, JSON, etc.
        escribir_error("N/A", repr(e))
        sys.exit(1)

    audio = datos.pop("audio_base64", None)
    if not audio:
        escribir_error("200 sin audio_base64", json.dumps(datos, ensure_ascii=False)[:5000])
        sys.exit(1)
    with open(os.path.join(AQUI, "voz.mp3"), "wb") as f:
        f.write(base64.b64decode(audio))
    with open(os.path.join(AQUI, "voz_alignment.json"), "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print("OK", {k: type(v).__name__ for k, v in datos.items()})


if __name__ == "__main__":
    main()
