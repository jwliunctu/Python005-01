from configparser import ConfigParser
import os

def read_db_config(section='redis'):
    self_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    init_file = os.path.join(self_dir, "config.ini")

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(init_file)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, init_file))
    # print(items)
    return dict(items)

if __name__ == "__main__":
    print(read_db_config())
