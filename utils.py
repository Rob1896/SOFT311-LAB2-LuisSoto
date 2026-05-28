import time
#funcion para guardar una captura de pantalla con un nombre basado en el nombre del test y la fecha/hora actual
def save_screenshot(page, request, extra=""):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    test_name = request.node.name.replace("[", "_").replace("]", "_")
    filename = f"screenshots/{test_name}{('_' + extra) if extra else ''}_{timestamp}.png"
    page.screenshot(path=filename, full_page=True)
