from PyQt5.QtWidgets import QLabel, QCheckBox, QComboBox, QLineEdit


def estiloPorTipo(tipo, nivel: int = 0):
    if isinstance(tipo, QCheckBox):
        return f"""
        QCheckBox {{
        font: 12pt "Avenir LT Std";
        color: #040D14;
        margin-left: {nivel*12}px;
    
        font-weight: 150;
    }}
    
    QCheckBox::indicator:unchecked {{
        image: url(:/indicador/CheckBoxFalse.png);
    }}
    
    QCheckBox::indicator:checked {{
        image: url(:/indicador/checkBoxTrue.png);
    }}
"""
    elif isinstance(tipo, QComboBox):
        pass
    elif isinstance(tipo, QLineEdit):
        pass
    else:
        return ""
