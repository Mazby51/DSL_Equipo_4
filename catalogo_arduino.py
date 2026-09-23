PINES_DIGITALES = set(range(0, 14))

PINES_DIGITALES_RESERVADOS = {
    0: "RX (recepción serial / USB)",
    1: "TX (transmisión serial / USB)",
}

PINES_ANALOGICOS = {f"A{i}" for i in range(0, 6)}

MODOS_PERMITIDOS = {
    'digital':   {'entrada', 'salida'},
    'analogico': {'entrada'},
}

def es_pin_digital_valido(pin):
    return isinstance(pin, int) and pin in PINES_DIGITALES


def es_pin_analogico_valido(pin):
    return isinstance(pin, str) and pin in PINES_ANALOGICOS


def es_pin_reservado(pin):
    return isinstance(pin, int) and pin in PINES_DIGITALES_RESERVADOS


def descripcion_reservado(pin):
    return PINES_DIGITALES_RESERVADOS.get(pin)


def modo_permitido(tipo, modo):
    return modo in MODOS_PERMITIDOS.get(tipo, set())


def modos_de(tipo):
    return set(MODOS_PERMITIDOS.get(tipo, set()))


def resumen_catalogo():
    lineas = []
    lineas.append("Catálogo de pines del Arduino Uno")
    lineas.append("=" * 50)
    lineas.append("")
    lineas.append(f"Pines digitales  : 0 a 13  ({len(PINES_DIGITALES)} pines)")
    lineas.append(f"Pines analógicos : A0 a A5  ({len(PINES_ANALOGICOS)} pines)")
    lineas.append("")
    lineas.append("Modos permitidos:")
    for tipo, modos in MODOS_PERMITIDOS.items():
        lineas.append(f"  - {tipo:10s} : {', '.join(sorted(modos))}")
    lineas.append("")
    lineas.append("Advertencias:")
    for pin, desc in sorted(PINES_DIGITALES_RESERVADOS.items()):
        lineas.append(f"  - Pin {pin}: {desc}")
    return "\n".join(lineas)