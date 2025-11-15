from utils.setup import setup_page
from utils.ui import exp_block_info
from utils.experiences import experiences
from utils.images import NOFACE

setup_page("💼 Mes Expériences Professionnelles")

for exp in experiences:
    exp_block_info(
        title=exp["title"],
        company=exp["company"],
        place=exp["place"],
        period=exp["period"],
        tools=exp["tools"],
        summary=exp["summary"],
        details=exp["details"],
        logo_path=exp.get("logo")
    )

from utils.ui import mascot_row
mascot_row(NOFACE, "👻 NoFace gagne de l'expérience avec moi à chaque endroit ! 👻", size=140)