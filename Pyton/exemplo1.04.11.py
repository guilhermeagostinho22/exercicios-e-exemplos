#exemplo1
alunos = [
    "aalunos_20",
    "ealunos_100",
    "balunos_22",
    "falunos_201",
    "calunos_10",
    "dalunos_01",
]#Ordenar pelo numero do aluno
sorted(alunos, key=lambda x: int(x[6:]))

