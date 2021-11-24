from util.enums.processoEnums import NaturezaProcesso


def checkNatureza(natureza: NaturezaProcesso, ativar=True):
    if natureza == NaturezaProcesso.administrativo:
        grupoNome = '#gbAdmnistrativo::title'
    else:
        grupoNome = '#gbJudicial::title'

    if ativar:
        backgroundColor = 'background-color: #3A405A;'
    else:
        backgroundColor = 'background-color: grey;'

    return grupoNome + """ {
        subcontrol-position: top left;
        """ + backgroundColor + """
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        color: white;
    	padding: 4px;
}"""

