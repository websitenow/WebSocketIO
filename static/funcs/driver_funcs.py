from selenium.webdriver.common.by import By

def handle_func(driver, func, *args, **kwargs):
    if driver:
        return func(driver,*args, **kwargs)
    else:
        print("O driver não foi Inicializado!")

def try_handler(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return None

def insert(driver, text, typ, loc):
    if (text and typ and loc):
        el = handle_func(driver, try_handler, getElementByX, loc, typ)
        if el:
            el.clear()
            el.send_keys(text)
            print("Insert Success!")
        else:
            print("Elemento não encontrado para inserção.")
    else:
        print("text ou typ ou loc é invalido")

def getElementByX(driver, loc, typ):
    by = None
    typ = typ.strip().lower()
    if typ == "xpath":
        by = By.XPATH
    elif typ == "text":
        by = By.XPATH
        loc = f"//*[text()='{loc}']"
    elif typ == "id":
        by = By.ID
    if typ == "name":
        by = By.CLASS_NAME
    if by:
        el = driver.find_element(by, loc)
        return el
    return None