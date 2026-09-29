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

def peticion(lineas):
    cuerpo = {
        "text": ' <break time="0.8s" /> '.join(lineas),
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8,
                           "style": 0.15, "use_speaker_boost": True},
    }
    cabeceras = {"Content-Type": "application/json", "Accept": "application/json"}
    req = urllib.request.Request(URL, data=json.dumps(cuerpo).encode("utf-8"),
                                 headers=cabeceras, method="POST")
    return urllib.request.urlopen(req, timeout=300)

def escribir_error(codigo, cuerpo):
    with open(os.path.join(AQUI, "ERROR.txt"), "w", encoding="utf-8") as f:
        f.write(f"HTTP {codigo}\n\n{cuerpo}\n")

def main():
    with open(os.path.join(AQUI, "lineas.json"), encoding="utf-8") as f:
        lineas = json.load(f)

    try:
        resp = peticion(lineas)
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
    err = os.path.join(AQUI, "ERROR.txt")
    if os.path.exists(err):
        os.remove(err)
    print("OK", {k: type(v).__name__ for k, v in datos.items()})

if __name__ == "__main__":
    main()
