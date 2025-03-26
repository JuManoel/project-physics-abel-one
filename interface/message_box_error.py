from CTkMessagebox import CTkMessagebox

def show_error(message: str = "Something went wrong!!!"):
    CTkMessagebox(title="Error", message=message, icon="cancel")