class Phone:
    __is_5g_enable = False

    def call_by_5g(self):
        self.__check_5g()

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")


phone = Phone()
phone.call_by_5g()