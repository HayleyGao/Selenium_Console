import configparser

config_path = r'C:\Users\caiwenjie\PycharmProjects\selenium_demo\RPA_Console_testEnv\common\config.ini'


class ReadConfig:
    def __init__(self):
        """
        为了方便后续统一管理，这里给了个默认的地址file_path。
        :param file_path:
        """
        # file_path=r'C:\Users\caiwenjie\PycharmProjects\selenium_demo\RPA_Console_testEnv\common\config.ini'
        self.config = configparser.ConfigParser()  # 创建解析对象
        self.config.read(config_path, encoding='utf-8')  # 读取文件

    def getOptionValue(self, section_param, key_name):
        """
        通过section和key获取对应字段的value。
        :param section_param:
        :param key_name:
        :return:
        """
        option = self.config.get(section_param, key_name)
        return option

    def readConf_sections(self):
        """
        获取ini配置文件中所有的sections.
        :param :
        :return:返回的是个list.
        """
        sections = self.config.sections()
        return sections

    def readConf_items(self, section_param):
        """
        section_param,配置文件中的section的名称。
        :param section_param:
        :return:以元组的格式返回section的内容
        """
        items = self.config.items(section_param)
        return items


if __name__ == '__main__':
    ReadConfig().getOptionValue('environment', 'url')
