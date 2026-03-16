
# Sistema de Permissões - Aula 07
# Aluno: Márcio Oliveira

cargo = input("Digite seu cargo (admin/tecnico/usuario): ").lower()
conta_ativa = input("A conta está ativa? (sim/nao): ").lower() == "sim"
horario_comercial = input("Está no horário comercial? (sim/nao): ").lower() == "sim"

# Lógica de acesso complexa
if cargo == "admin":
    print("ACESSO TOTAL LIBERADO.")
elif cargo == "tecnico" and conta_ativa:
    print("ACESSO PARA MANUTENÇÃO LIBERADO.")
elif cargo == "usuario" and conta_ativa and horario_comercial:
    print("ACESSO PADRÃO LIBERADO.")
else:
    print("ACESSO NEGADO. Verifique suas credenciais.")
