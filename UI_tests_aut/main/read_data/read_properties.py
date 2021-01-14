from jproperties import Properties


class PropertiesReader:

    @classmethod
    def load_properties_from_file(cls, key_property):
        configs = Properties()
        # with open('../test_config.read_data', 'rb') as config_file:
        with open(
                "C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/UI_tests_aut/test_config.properties",
                'rb') as config_file:
            configs.load(config_file)

            return configs.get(key_property)

    @classmethod
    def get_value(cls, key_property):
        prop = cls.load_properties_from_file(key_property)
        if prop is None: raise Exception

        return prop

    @classmethod
    def if_save_running_time(cls):
        time_save = cls.get_value('saveTimeTestRunning').data
        if time_save == 'True':
            return True
        elif time_save == 'False':
            return False
        else:
            raise Exception("Wrong 'saveTimeTestRunning' value. It should be True or False")
