import configparser

def readconfig(section, key):
    config = configparser.ConfigParser()
    config.read('/Users/oluwatofunmiajibola/PycharmProjects/First Personal Project/Configurations/config.cfg')
    return config.get(section, key)

readconfig('Details', 'Application URL')