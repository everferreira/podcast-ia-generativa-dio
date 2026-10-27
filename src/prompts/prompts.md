# Prompts utilizados na criação do podcast

Este arquivo documenta os prompts reais utilizados para gerar o podcast.

## 1. Prompt de roteiro (ChatGPT)

```
Crie um roteiro de podcast de 5 minutos sobre IA generativa no setor financeiro,
em formato de diálogo entre duas pessoas, com linguagem acessível, sem jargão
técnico pesado. Abertura, desenvolvimento com 3 pontos principais e encerramento
com reflexão.
```

**Resultado:** roteiro em diálogo entre Mara (host) e Ana (convidada, analista de
inovação bancária), com abertura, 3 pontos (atendimento, análise de documentos,
cuidados/riscos) e encerramento.

## 2. Prompt de personas

```
Sugira duas personas femininas com nomes brasileiros: uma host experiente e uma
convidada analista de inovação em banco.
```

**Resultado:** Mara (host) e Ana (convidada).

## 3. Prompt de tom

```
Mantenha tom leve, didático e otimista, com pausas naturais e perguntas que
aproximem o ouvinte. Evite termos como 'revolucionário', 'game changer' e
promessas exageradas.
```

## 4. Prompt da capa (imagem gerada com IA)

```
capa de podcast profissional, microfone dourado com ondas de audio luminosas,
tema tecnologico financeiro, fundo azul escuro, neon, vibrante, sem texto
```

**Ferramenta:** OpenAI GPT-5 Image Mini (via API OpenRouter)

## 5. Geração de voz (TTS)

- Ferramenta: Microsoft Edge TTS (gratuito, sem chave)
- Voz da host (Mara): `pt-BR-FranciscaNeural`
- Voz da convidada (Ana): `pt-BR-ThalitaMultilingualNeural`
- Parâmetros: rate -8%, chunks <= 450 caracteres (evita throttling do serviço)

## 6. Edição (ffmpeg)

- Concatenação das 17 falas com pausa de 0,45s entre falas
- Normalização de volume (ganho fixo + limiter; `loudnorm` quebrava a duração em áudio mono)
- Fade in de 1,2s e fade out final de 3s
- Saída: MP3 192kbps, ~4 minutos
