def estiloMenu() -> str:
    return"""
        QMenu {
            background-color: white;
            border-radius: 8px;
            border: 1px solid lightgrey;
        }
        
        QMenu::item {
            font: 12pt "Avenir LT Std";
            color: #3F4E8C;
            padding: 8px 16px;
        
            background-color: white;
            border: 0px solid none;
            border-radius: 8px;
        }
        
        QMenu::item:selected {
            font: 12pt "Avenir LT Std";
            color: #3F4E8C;
            padding: 8px 16px;
        
            background-color: #F4F5F8;
            border: 0px solid none;
            border-radius: 8px;
        }
    """