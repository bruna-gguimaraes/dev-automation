import psutil
import time


def verificar_saude_sistema():
    # 1. Calcula o tempo ligado (Uptime)
    boot_time = psutil.boot_time()  # Timestamp do último boot
    tempo_atual = time.time()
    tempo_ligado_segundos = tempo_atual - boot_time

    horas_ligado = tempo_ligado_segundos / 3600
    dias_ligado = horas_ligado / 24

    # 2. Conta os processos ativos
    total_processos = len(psutil.pids())

    # 3. Pega o uso geral de memória RAM
    memoria = psutil.virtual_memory()
    uso_memoria_porcentagem = memoria.percent

    print("=== DIAGNÓSTICO DE SISTEMA ===")
    print(f"🖥️  Tempo ligado: {dias_ligado:.1f} dias ({horas_ligado:.1f} horas)")
    print(f"⚙️  Processos ativos: {total_processos}")
    print(f"🧠 Memória RAM em uso: {uso_memoria_porcentagem}%")
    print("-" * 30)

    # 4. Regras de Decisão (Critérios para sugerir reinicialização)
    # Exemplo: Mais de 5 dias ligado OU mais de 400 processos OU RAM acima de 85%
    precisa_reiniciar = False
    motivos = []

    if dias_ligado > 5:
        precisa_reiniciar = True
        motivos.append(
            f"O notebook está ligado há {dias_ligado:.1f} dias sem reiniciar."
        )

    if total_processos > 400:
        precisa_reiniciar = True
        motivos.append(f"Há um volume alto de processos ativos ({total_processos}).")

    if uso_memoria_porcentagem > 85:
        precisa_reiniciar = True
        motivos.append(
            f"O uso de memória RAM está elevado ({uso_memoria_porcentagem}%)."
        )

    # 5. Resultado
    if precisa_reiniciar:
        print("⚠️  RECOMENDAÇÃO: É altamente recomendável reiniciar a máquina!")
        print("Motivos:")
        for motivo in motivos:
            print(f" - {motivo}")
    else:
        print(
            "✅ O sistema está saudável e com boa performance. Reinicialização não"
            " é necessária no momento."
        )


if __name__ == "__main__":
    verificar_saude_sistema()
