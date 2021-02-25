# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
def handshakes(n):
    s = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            s.append((i, j))
    return s


n = 5
handshakes_list = handshakes(n)
print(f"Комбинации рукопожатий: {handshakes_list}")
print(f"Количество рукопожатий: {len(handshakes_list)}")
