<p align="center">
<img 
    src="./assets/cover.png"
    width="300"
/>
</p>

<p align="center">
<a href="https://dio.me/">
    <img 
        src="https://img.shields.io/badge/DIO-Bootcamp%20CAIXA-28DA77?logo=youtube" 
        alt="DIO - Bootcamp CAIXA">
</a>
<a href="https://github.com/everferreira">
    <img 
        src="https://img.shields.io/badge/Ever%20Ferreira-GitHub-0a1e3d?logo=github" 
        alt="GitHub - Ever Ferreira">
</a>
<img src="https://img.shields.io/badge/IA%20Generativa-Gerado%20com%20IA-5a6a82" alt="Gerado com IA">
</p>

<p align="center">
    preview do podcast
</p>

<div align="center">
    <audio src="output/podcast_editado.mp3" controls title="Podcast editado"></audio>
</div>

# 🎙️ PODCAST — IA Generativa no Setor Financeiro

> ℹ️ **NOTE:** Projeto do Bootcamp **CAIXA - IA Generativa** da [DIO](https://dio.me)

Podcast em formato de diálogo (Mara e Ana) sobre IA generativa no setor
financeiro: atendimento, análise de documentos, fraude e os cuidados
necessários. Roteiro, vozes e capa gerados com IA Generativa.

## 💻 Tecnologias utilizadas no projeto

- [ChatGPT](https://chat.openai.com/) — roteiro e personas
- [OpenAI GPT-5 Image Mini](https://openrouter.ai/) — capa gerada por IA
- [Microsoft Edge TTS](https://github.com/rany2/edge-tts) — vozes sintetizadas
  (FranciscaNeural + ThalitaMultilingualNeural, pt-BR)
- [ffmpeg](https://ffmpeg.org/) — edição, concatenação e normalização

## ✨ Como foi feito ?

- Roteiro gerado via ChatGPT
- Áudio gerado via Edge TTS (duas vozes pt-BR)
- Capa gerada via IA de imagem
- Edição via ffmpeg (pausas, fades e normalização)

## 🧠 Prompts

| Ação | prompt |
|------|--------|
| Roteiro | Crie um roteiro de podcast de 5 minutos sobre IA generativa no setor financeiro, em formato de diálogo entre duas pessoas, com linguagem acessível, sem jargão técnico pesado. Abertura, desenvolvimento com 3 pontos principais e encerramento com reflexão. |
| Personas | Sugira duas personas femininas com nomes brasileiros: uma host experiente e uma convidada analista de inovação em banco. |
| Tom | Mantenha tom leve, didático e otimista, com pausas naturais e perguntas que aproximem o ouvinte. Evite termos como 'revolucionário', 'game changer' e promessas exageradas. |
| Capa | capa de podcast profissional, microfone dourado com ondas de audio luminosas, tema tecnologico financeiro, fundo azul escuro, neon, vibrante, sem texto |

> 📄 Prompts detalhados e especificações técnicas em [`src/prompts/prompts.md`](src/prompts/prompts.md)

## 📚 Materiais

- Roteiro completo em [`src/roteiro.md`](src/roteiro.md)
- Prompts em [`src/prompts/prompts.md`](src/prompts/prompts.md)
- Áudio final em `output/podcast_editado.mp3`
- Capa em `assets/cover.png`
- Script de geração de voz em `scripts/gerar_tts.py`

## 🛠️ Instruções de execução

1. Clone o repositório
2. Instale o Edge TTS: `pip install edge-tts`
3. Gere as falas: `python3 scripts/gerar_tts.py`
4. Monte o episódio final com ffmpeg (ver `src/prompts/prompts.md`)

## 📊 Estrutura do projeto

```
podcast-ia-generativa-dio/
├── assets/
│   └── cover.png               # capa do podcast
├── audio/
│   └── raw/                    # falas individuais (TTS)
├── output/
│   └── podcast_editado.mp3     # episódio final
├── scripts/
│   └── gerar_tts.py            # gera vozes com Edge TTS
└── src/
    ├── roteiro.md              # roteiro completo
    └── prompts/
        └── prompts.md          # prompts utilizados
```

## 👩‍💻 Autora

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/104384378?v=4"
    />
    <p>&nbsp&nbsp&nbspEver Maria Tobias Ferreira<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/everferreira">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/evermaria">LinkedIn</a>
    </p>
</p>
<br/><br/>
<p>

---

⌨️ com 💜 por [Ever Ferreira](https://github.com/everferreira) — Bootcamp CAIXA - IA Generativa (DIO)
