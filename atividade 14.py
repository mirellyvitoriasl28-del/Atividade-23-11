14. Valide uma senha exigindo no mínimo 8 caracteres, 1 maiúscula, 1 minúscula, 1 número e 1 especial (!@#$%^&*).
R:
def validar_senha(senha):
    return (
        len(senha) >= 8
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(c in "!@#$%^&*" for c in senha)
    )
