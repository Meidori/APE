from zeep import Client


class Calculator:
    def __init__(self):
        self.wsdl_url_translate = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
        self.wsdl_url_calculate = "http://www.dneonline.com/calculator.asmx?WSDL"
        self.client_tr = Client(wsdl=self.wsdl_url_translate)
        self.client_ca = Client(wsdl=self.wsdl_url_calculate)

    def get_all_methods(self):
        print("Доступные методы:")
        methods_tr = self.client_tr.service
        methods_ca = self.client_ca.service
        for x in methods_tr:
            print(x[0])
        for x in methods_ca:
            print(x[0])

    def number_to_words(self, num):
        response = self.client_tr.service.NumberToWords(ubiNum=num)
        print("❯ ", response)

    def number_to_dollars(self, num):
        response = self.client_tr.service.NumberToDollars(dNum=num)
        print("❯ ", response)

    def add(self, num1, num2):
        response = self.client_ca.service.Add(intA=num1, intB=num2)
        print("❯ ", response)

    def subtract(self, num1, num2):
        response = self.client_ca.service.Subtract(intA=num1, intB=num2)
        print("❯ ", response)

    def multiply(self, num1, num2):
        response = self.client_ca.service.Multiply(intA=num1, intB=num2)
        print("❯ ", response)

    def divide(self, num1, num2):
        if num2 == 0:
            print("На ноль делить нельзя")
            return
        response = self.client_ca.service.Divide(intA=num1, intB=num2)
        print("❯ ", response)

    def menu(self):
        choice = 0
        while True:
            print("========MENU========")
            print("1. Перевести число в текст")
            print("2. Перевести число в текст - доллары и центы")
            print("3. Сложение двух чисел")
            print("4. Вычетание двух чисел")
            print("5. Умножение двух чисел")
            print("6. Деление двух чисел")
            print("0. Выход")

            choice = int(input())
            if choice == 1:
                num = float(input("Введите число: "))
                self.number_to_words(num)
            elif choice == 2:
                num = float(input("Введите число: "))
                self.number_to_dollars(num)
            elif choice == 3:
                num1 = int(input("Введите первое целое число: "))
                num2 = int(input("Введите второе целое число: "))
                self.add(num1, num2)
            elif choice == 4:
                num1 = int(input("Введите первое целое число: "))
                num2 = int(input("Введите второе целое число: "))
                self.subtract(num1, num2)
            elif choice == 5:
                num1 = int(input("Введите первое целое число: "))
                num2 = int(input("Введите второе целое число: "))
                self.multiply(num1, num2)
            elif choice == 6:
                num1 = int(input("Введите первое целое число: "))
                num2 = int(input("Введите второе целое число: "))
                self.divide(num1, num2)
            elif choice == 0:
                print("Выход...")
                break


def main():
    calculator = Calculator()
    calculator.get_all_methods()
    calculator.menu()


if __name__ == "__main__":
    main()
