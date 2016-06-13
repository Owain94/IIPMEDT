def prefix() -> str:
    """
    Controleert waar het script uitgevoerd wordt. Aan de hand daarvan wordt er
    een prefix gegeven voor folders. Dit kan handig zijn voor de mappen audio
    en datafiles.

    :return: pad prefix als string
    """
    if __name__ == '__main__':
        return '../'
    else:
        return './'
