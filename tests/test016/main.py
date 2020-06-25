"""
Proxy is a structural design pattern that lets you provide a
substitute or placeholder for another object. A proxy controls
access to the original object, allowing you to perform
something either before or after the request gets through to
the original object.
"""

from abc import  ABC, abstractmethod

class Subject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
    интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    """
    Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """
    Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        :return:
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access Prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")

def client_code(subject: Subject) -> None:
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    :param subject:
    :return:
    """

    subject.request()

if __name__ == '__main__':
    print("Client: Executing he client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing he client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)