Use the "l10n-sync" skill (read .agents/skills/l10n-sync/SKILL.md).
  
  I want you to update the "nls.json" files
   
● Read
  /home/zorin/Documents/VSC-extension/F1/.agents/skills/l10n-sync/SKIL
  L.md

  Now let me find the skill directory and the nls files:
● Glob "**/*.nls*.json"
    ╰ path=/home/zorin/Documents/VSC-extension/F1
  12 files
    package.nls.json, package.nls.es.json, package.nls.hi.json +9 more
● Glob ".agents/skills/l10n-sync/scripts/*.py"
    ╰ path=/home/zorin/Documents/VSC-extension/F1
  1 file
    l10n.py
● Task list created
● Shell cd /home/zorin/Documents/VSC-extension/F1 && python3 -B
  .agents/skills/l10n-sync/scripts/l10n.py plan --source
  package.nls.json 2>&1
● Read /home/zorin/Documents/VSC-extension/F1/.l10n-work/jobs.json
● Tasks updated

  Now I'll write the translations for all 11 languages into
  results.json:
● Write /home/zorin/Documents/VSC-extension/F1/.l10n-work/results.json
  added 46 lines in results.json
     1+  {                                                            
     2+    "package.nls.ar.json": {                                   
     3+      "displayName": "F1 [AI] composer",                       
     +      "description": "مركز CLI للذكاء الاصطناعي الشامل: مفتاح   
     واحد لتشغيل وتبديل وإدارة Claude Code وCodex وCopilot وCursor    
     وKiro وKilo Code وOpenCode وGrok وAntigravity أو أي وكيل برمجي   
     مخصص — جنبًا إلى جنب في بيئة التطوير الخاصة بك. اكتب مطالبات أفضل 
     مع إشارات @-الملفات والصور والترجمة التلقائية والصوت. ثبّت مهارات 
     الوكيل وتتبع الاستخدام وابدأ كل CLI بذاكرة مشروعك حتى يعرف قاعدة 
     الكود الخاصة بك منذ البداية."                                    
     5+    },                                                         
     6+    "package.nls.de.json": {                                   
     7+      "displayName": "F1 [AI] composer",                       
     +      "description": "All-in-One KI-CLI-Hub: Eine Taste zum     
     Starten, Wechseln und Verwalten von Claude Code, Codex, Copilot, 
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity oder einem  
     beliebigen benutzerdefinierten Coding-Agenten – nebeneinander in 
     Ihrer IDE. Schreiben Sie bessere Prompts mit @-Dateiverweisen,   
     Bildern, automatischer Übersetzung und Spracheingabe.            
     Installieren Sie Agenten-Skills, verfolgen Sie die Nutzung und   
     statten Sie jede CLI mit dem Projektspeicher aus, damit sie Ihre 
     Codebasis von Anfang an kennt."                                  
     9+    },                                                         
    10+    "package.nls.es.json": {                                   
    11+      "displayName": "F1 [AI] composer",                       
    1+      "description": "Hub de CLI de IA todo en uno: una tecla   
     para lanzar, cambiar y gestionar Claude Code, Codex, Copilot,    
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity o cualquier 
     agente de codificación personalizado — uno al lado del otro en tu
     IDE. Escribe mejores prompts con menciones @-archivo, imágenes,  
     traducción automática y voz. Instala Skills de agente, rastrea el
     uso y prepara cada CLI con la memoria de tu proyecto para que    
     empiece conociendo tu código base."                              
    13+    },                                                         
    14+    "package.nls.fr.json": {                                   
    15+      "displayName": "F1 [AI] composer",                       
    1+      "description": "Hub CLI IA tout-en-un : une touche pour   
     lancer, basculer et gérer Claude Code, Codex, Copilot, Cursor,   
     Kiro, Kilo Code, OpenCode, Grok, Antigravity ou tout agent de    
     codage personnalisé — côte à côte dans votre IDE. Rédigez de     
     meilleures invites avec des mentions @-fichier, des images, la   
     traduction automatique et la voix. Installez des compétences     
     d'agent, suivez l'utilisation et initialisez chaque CLI avec la  
     mémoire de votre projet pour qu'il commence déjà en connaissant  
    17+    },                                                         
    18+    "package.nls.hi.json": {                                   
    19+      "displayName": "F1 [AI] composer",                       
    2+      "description": "ऑल-इन-वन AI CLI हब: एक हॉटकी से Claude Code, 
     Codex, Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok,         
     Antigravity या किसी भी कस्टम कोडिंग एजेंट को लॉन्च करें, बदलें और प्रबंधित करें — अपने IDE 
     में साथ-साथ। @-फ़ाइल मेंशन, इमेज, ऑटो-ट्रांसलेशन और वॉयस के साथ बेहतर प्रॉम्प्ट लिखें। एजेंट स्किल्स 
     इंस्टॉल करें, उपयोग ट्रैक करें और हर CLI को अपने प्रोजेक्ट की मेमोरी से तैयार करें ताकि वह शुरू से 
    21+    },                                                         
    22+    "package.nls.ja.json": {                                   
    23+      "displayName": "F1 [AI] composer",                       
    2+      "description": "オールインワン AI CLI                     
     ハブ：ホットキー1つで Claude                                     
     Code、Codex、Copilot、Cursor、Kiro、Kilo                         
     Code、OpenCode、Grok、Antigravity、またはカスタムコーディングエー
     ジェントを起動・切替・管理 — IDE                                 
     内で並べて使用可能。@-ファイル参照、画像、自動翻訳、音声を活用し 
     てより良いプロンプトを作成。エージェントスキルをインストールし、 
     使用状況を追跡し、すべての CLI                                   
     にプロジェクトのメモリを事前に読み込ませて、最初からコードベース 
    25+    },                                                         
    26+    "package.nls.ko.json": {                                   
    27+      "displayName": "F1 [AI] composer",                       
    2+      "description": "올인원 AI CLI 허브: 단 하나의 단축키로    
     Claude Code, Codex, Copilot, Cursor, Kiro, Kilo Code, OpenCode,  
     Grok, Antigravity 또는 커스텀 코딩 에이전트를 실행·전환·관리 —   
     IDE에서 나란히 사용. @-파일 멘션, 이미지, 자동 번역, 음성으로 더 
     나은 프롬프트 작성. 에이전트 스킬을 설치하고 사용량을 추적하며,  
     모든 CLI에 프로젝트 메모리를 미리 로드하여 처음부터 코드베이스를 
     파악한 상태로 시작하세요."                                       
    29+    },                                                         
    30+    "package.nls.pt-br.json": {                                
    31+      "displayName": "F1 [AI] composer",                       
    3+      "description": "Hub de CLI de IA tudo-em-um: um atalho    
     para lançar, alternar e gerenciar Claude Code, Codex, Copilot,   
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity ou qualquer 
     agente de codificação personalizado — lado a lado na sua IDE.    
     Escreva prompts melhores com menções @-arquivo, imagens, tradução
     automática e voz. Instale Skills de agente, acompanhe o uso e    
     prepare cada CLI com a memória do seu projeto para que ele comece
     já conhecendo sua base de código."                               
    33+    },                                                         
    34+    "package.nls.ru.json": {                                   
    35+      "displayName": "F1 [AI] composer",                       
    3+      "description": "Универсальный AI CLI-хаб: одна горячая    
     клавиша для запуска, переключения и управления Claude Code,      
     Codex, Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok,         
     Antigravity или любым пользовательским агентом — бок о бок в     
     вашей IDE. Создавайте лучшие промпты с @-упоминаниями файлов,    
     изображениями, автопереводом и голосом. Устанавливайте навыки    
     агента, отслеживайте использование и инициализируйте каждый CLI  
     памятью проекта, чтобы он сразу знал вашу кодовую базу."         
    37+    },                                                         
    38+    "package.nls.vi.json": {                                   
    39+      "displayName": "F1 [AI] composer",                       
    4+      "description": "Trung tâm CLI AI tất cả trong một: một    
     phím tắt để khởi chạy, chuyển đổi và quản lý Claude Code, Codex, 
     Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity    
     hoặc bất kỳ tác nhân lập trình tùy chỉnh nào — cạnh nhau trong   
     IDE của bạn. Viết lời nhắc tốt hơn với đề cập @-tệp, hình ảnh,   
     dịch tự động và giọng nói. Cài đặt kỹ năng tác nhân, theo dõi mức
     sử dụng và khởi tạo mỗi CLI với bộ nhớ dự án để nó bắt đầu đã    
    41+    },                                                         
    42+    "package.nls.zh-cn.json": {                                
    43+      "displayName": "F1 [AI] composer",                       
    4+      "description": "一体化 AI CLI                             
     中心：一个快捷键即可启动、切换和管理 Claude                      
     Code、Codex、Copilot、Cursor、Kiro、Kilo                         
     Code、OpenCode、Grok、Antigravity 或任何自定义编码智能体——在您的 
     IDE 中并排运行。通过                                             
     @-文件引用、图片、自动翻译和语音功能编写更好的提示词。安装智能体 
     技能、追踪使用情况，并为每个 CLI                                 
     预加载项目记忆，让它从一开始就了解您的代码库。"                  
    45+    }                                                          
    46+  }                                                            
● Shell cd /home/zorin/Documents/VSC-extension/F1 && python3 -B
  .agents/skills/l10n-sync/scripts/l10n.py apply 2>&1

  The "same as English" note is for displayName: "F1 [AI] composer" —
  that's intentional, it's a brand name. Now verify and clean up:
● Shell cd /home/zorin/Documents/VSC-extension/F1 && python3 -B
  .agents/skills/l10n-sync/scripts/l10n.py verify --source
  package.nls.json 2>&1

  All clean. Removing .l10n-work/:
● Shell rm -rf /home/zorin/Documents/VSC-extension/F1/.l10n-work
● Tasks updated

  Ready 🎉 — localization complete:
  
  ┌────────────────────────┬───────┬──────┬────────┬────────┐
  │ file                   │ lang  │ mode │ blocks │ status │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.ar.json    │ ar    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.de.json    │ de    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.es.json    │ es    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.fr.json    │ fr    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.hi.json    │ hi    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.ja.json    │ ja    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.ko.json    │ ko    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.pt-br.json │ pt-br │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.ru.json    │ ru    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.vi.json    │ vi    │ full │ 2      │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┼────────┤
  │ package.nls.zh-cn.json │ zh-cn │ full │ 2      │ ✅     │
  └────────────────────────┴───────┴──────┴────────┴────────┘
  
  │ displayName: "F1 [AI] composer" is kept identical in all languages
  — it's a brand name, intentional.

▸ Credits: 1.26 • Time: 1m 34s
