import random
import string

def gerar_senha(tamanho=12):
    if tamanho < 8:
        raise ValueError("O tamanho mínimo da senha deve ser 8 caracteres.")
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    todos = string.ascii_letters + string.digits + string.punctuation
    senha += [random.choice(todos) for _ in range(tamanho - 4)]
    random.shuffle(senha)
    return ''.join(senha)

def validar_senha(senha):
    if len(senha) < 8: return False
    if not any(c.islower() for c in senha): return False
    if not any(c.isupper() for c in senha): return False
    if not any(c.isdigit() for c in senha): return False
    if not any(c in string.punctuation for c in senha): return False
    return True
