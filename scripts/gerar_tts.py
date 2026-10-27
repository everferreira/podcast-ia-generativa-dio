#!/usr/bin/env python3
"""Gera os áudios do podcast com edge-tts (vozes pt-BR reais, sem chave)."""
import asyncio, json, os, sys
import edge_tts

OUT = "/mnt/c/Users/conta/DIO/podcast-ia-generativa-dio/audio/raw"
os.makedirs(OUT, exist_ok=True)

VOZES = {
    "MARIA": "pt-BR-FranciscaNeural",      # host
    "ANA": "pt-BR-ThalitaMultilingualNeural",  # convidada
}

FALAS = [
    ("MARIA", "Você já imaginou um banco que responde na hora, qualquer hora, e ainda explica cada passo do que está fazendo? Pois é, isso não é mais ficção científica. Eu sou a Mara, e no episódio de hoje a gente conversa sobre IA generativa no setor financeiro. Não do ponto de vista teórico, mas do que já está acontecendo de verdade. Pra me ajudar nessa conversa, está comigo a Ana, analista de inovação de um grande banco. Ana, bem-vinda!"),
    ("ANA", "Obrigada, Mara! Que bom estar aqui. E olha, esse tema é o que mais tem dado o que falar nos corredores do banco. No bom sentido."),
    ("MARIA", "Então me conta: qual é a aplicação mais real de IA generativa dentro de um banco hoje?"),
    ("ANA", "Sem dúvida é o atendimento. Chatbots e assistentes que respondem dúvidas 24 horas, resumem conversas pro atendente humano retomar o contexto em segundos. O cliente não espera na fila, e o time humano foca nos casos que realmente precisam de gente. É ganho pros dois lados."),
    ("MARIA", "E a IA explica o que ela faz? Porque banco mexe com dinheiro, né? Confiança é tudo."),
    ("ANA", "Exatamente. E é por isso que os bons projetos não deixam a IA responder sozinha. Ela sugere, resume, organiza. Mas o número, o valor, a condição, isso sempre passa por verificação. A gente ensina o modelo a dizer não sei quando não tem certeza. Isso é ouro."),
    ("MARIA", "Legal demais. E além do atendimento, onde mais essa tecnologia aparece?"),
    ("ANA", "Na análise de documentos. Contrato, extrato, comprovante: a IA lê e devolve um resumo estruturado pro analista. Quem antes lia vinte páginas, agora confere um resumo e foca nos pontos críticos. A decisão continua sendo humana, mas o tempo de leitura despenca."),
    ("MARIA", "E isso vale pra crédito? Pra fraude?"),
    ("ANA", "Vale. Na fraude, a IA generativa entra na explicação: quando uma transação é sinalizada, ela transforma aquele alerta técnico numa explicação legível pro investigador. O modelo preditivo aponta, a generativa explica. É um time de dois."),
    ("MARIA", "Beleza, mas eu imagino que nem tudo são flores. O que precisa de cuidado?"),
    ("ANA", "Três coisas. Primeiro, alucinação: a IA pode inventar resposta com cara de verdade, então nunca deixe ela responder valor sem fonte oficial. Segundo, dados sensíveis: informação de cliente não entra em ferramenta sem avaliação de segurança. Terceiro, viés: modelo aprende do que já existe, e histórico de crédito tem preconceito embutido. Auditoria contínua não é opcional."),
    ("MARIA", "Então não é só pedir e confiar."),
    ("ANA", "Nunca. Mas quando você tem humano no loop, verificação e governança, a produtividade sobe e o risco fica controlado."),
    ("MARIA", "Ana, se você tivesse que deixar uma mensagem pra quem tá começando nesse mundo, o que diria?"),
    ("ANA", "Diria pra não ter medo de testar, mas testar com responsabilidade. Comece por um processo repetitivo, meça o tempo que economizou, e coloque sempre uma revisão humana. IA generativa no banco não substitui julgamento. Ela devolve tempo pra você usar o seu."),
    ("MARIA", "Perfeito, Ana. E pra quem ouviu até aqui: IA generativa no setor financeiro é sobre devolver tempo, não sobre substituir pessoas. Fica a reflexão. Eu sou a Mara, e esse foi o nosso episódio. Até a próxima!"),
]

async def gen(idx, nome, texto):
    voz = VOZES[nome]
    # divide falas longas em chunks <= ~450 chars para evitar throttle/limite
    chunks = [texto[i:i+450] for i in range(0, len(texto), 450)] or [texto]
    for j, ch in enumerate(chunks):
        f = f"{OUT}/fala_{idx:02d}_{nome}_{j:02d}.mp3"
        for tentativa in range(4):
            try:
                com = edge_tts.Communicate(ch, voz, rate="-8%", volume="+0%")
                await com.save(f)
                print(f"OK {f} ({nome} chunk {j})", flush=True)
                break
            except Exception as e:
                print(f"RETRY {f} tentativa {tentativa+1}: {type(e).__name__}", flush=True)
                await asyncio.sleep(6 * (tentativa + 1))
        else:
            print(f"FALHOU DEFINITIVO {f}", flush=True)
            raise SystemExit(1)

async def main():
    for i, (nome, texto) in enumerate(FALAS):
        await gen(i, nome, texto)

asyncio.run(main())
print("TODAS AS FALAS GERADAS")
