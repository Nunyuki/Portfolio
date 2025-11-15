from utils.setup import setup_page, st
from utils.style import img_to_base64, formation_block_info

setup_page("🎓 Mon Parcours de Formation")

ponyo_b64 = img_to_base64("assets/ghibli/ponyo.png")

st.markdown("""
<p style="text-align:center; font-size:17px;">
Chaque étape de mon parcours a renforcé mes compétences techniques, ma rigueur analytique et ma passion pour l’innovation numérique.
</p>
""", unsafe_allow_html=True)

formation_block_info(
    "🏛 Université Paris Dauphine – PSL",
    "Licence 3 à Master 2 MIAGE (Méthodes Informatiques Appliquées à la Gestion des Entreprises)",
    "2022 – 2025 | Alternance chez SwissLife Banque Privée",
    """
    - **Master 2 MIAGE – Systèmes d’Information et Transition Numérique** (2024–2025) – Moyenne : 14.96  
      > Approfondissement en gouvernance des SI, DevOps, cloud et architecture d’entreprise.  
        
    - **Master 1 MIAGE** (2023–2024) – Moyenne : 13.63  
      > Analyse fonctionnelle, gestion de projets agiles, conception d’applications (Angular / Spring Boot).  

    - **Licence 3 MIAGE** (2022–2023) – Moyenne : 14.27  
      > Introduction à l’ingénierie des systèmes d’information, bases de données avancées et décisionnel.  
        
    - Faits marquants
      > Ces trois années en alternance m’ont permis de mettre en pratique ce que j’apprenais en cours et de comprendre la vraie vie en entreprise. Travailler chez SwissLife Banque Privée m’a appris à collaborer efficacement, à gérer des projets concrets et à apprécier l’importance de l’expérience terrain. C’est une période où j’ai beaucoup grandi sur le plan professionnel et personnel.
        """
)

formation_block_info(
    "🎓 Sorbonne Université",
    "Licence 1 & 2 – MIPI puis Bi-disciplinaire Informatique - Gestion",
    "2020 – 2022",
    """
    - **Licence 2** (2021–2022) – Majeure Informatique, Mineure Gestion – Moyenne : 15.32  
    > Formation équilibrée entre logique informatique, développement, base de données, comptabilité, économie et marketing.
      
    - **Licence 1 MIPI** (2020–2021) - Mathématiques, Informatique, Physique, Ingénierie – Option Mathématiques – Moyenne : 15.35  
    > Approfondissement en algorithmique, raisonnement logique et bases de la programmation scientifique.
    
    - Faits marquants
    > J’ai découvert ma passion pour l’informatique et confirmé que c’était la voie que je voulais suivre. Les matières variées m’ont donné un socle solide, et l’approche bi-disciplinaire m’a permis de développer un regard pratique sur la gestion et l’informatique. C’est là que j’ai pris confiance dans mes choix et commencé à envisager mon parcours en alternance.
    """
)

formation_block_info(
    "🏫 Lycée Henri Wallon – Aubervilliers",
    "Baccalauréat Scientifique | Spécialité Mathématiques | Mention Très Bien",
    "2017 – 2020",
    """
    - Langues étudiées
    > Anglais, Chinois, Latin, Italien  
    
    - Faits marquants
    > Ces années m’ont appris à réfléchir à mes projets futurs et à explorer différents domaines. J’ai beaucoup aimé les sciences et les mathématiques, l’envie de comprendre et de créer qui s’est affirmée. Cette période a posé les bases de ma curiosité et de mon goût pour les défis intellectuels.
    """
)

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:15px; margin-top:30px;">
    <img src="data:image/png;base64,{ponyo_b64}" width="90"/>
    <p style="margin:0; font-size:16px;">🐠 Ponyo veille sur mon parcours et chaque étape me fait grandir ! 🐠</p>
</div>
""", unsafe_allow_html=True)
