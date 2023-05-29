from ast import literal_eval


class System:
    def __init__(self):
        pass

    class var:
        def __init__(self):
            pass

        def type(self, var):
            __int = 1
            __str = 'a'
            __float = 1.5
            __complex = 1j
            __list = ["a", 1]
            __tuple = ("a", 1)
            __range = range(1)
            __dict = {"a": "a"}
            __set = {"a", "b"}
            __frozenset = frozenset({"a", "b"})
            __bool = True
            __bytes = b"Hello"
            __bytearray = bytearray(5)
            __memoryview = memoryview(bytes(5))
            if type(var) == type(__int):
                return "int"
            elif type(var) == type(__str):
                return "str"
            elif type(var) == type(__float):
                return "float"
            elif type(var) == type(__complex):
                return "complex"
            elif type(var) == type(__list):
                return "list"
            elif type(var) == type(__tuple):
                return "tuple"
            elif type(var) == type(__range):
                return "range"
            elif type(var) == type(__dict):
                return "dict"
            elif type(var) == type(__set):
                return "set"
            elif type(var) == type(__frozenset):
                return "frozenset"
            elif type(var) == type(__bool):
                return "bool"
            elif type(var) == type(__bytes):
                return "bytes"
            elif type(var) == type(__bytearray):
                return "bytearray"
            elif type(var) == type(__memoryview):
                return "memoryview"


class List:
    def __init__(self):
        self.list = []

    def add(self, add):
        self.list.append(add)

    def rem(self, pos):
        self.list.remove(pos)

    def remf(self):
        self.list.pop()

    def rema(self):
        return self.list.clear()

    def get(self, pos):
        return self.list[pos]

    def cnt(self, pos):
        return self.list.count(pos)

    def geta(self):
        return self.list[0:]

    def len(self):
        return len(self.list)

    def type(self, pos):
        __int = 1
        __str = 'a'
        __float = 1.5
        __complex = 1j
        __list = ["a", 1]
        __tuple = ("a", 1)
        __range = range(1)
        __dict = {"a": "a"}
        __set = {"a", "b"}
        __frozenset = frozenset({"a", "b"})
        __bool = True
        __bytes = b"Hello"
        __bytearray = bytearray(5)
        __memoryview = memoryview(bytes(5))
        global list
        if type(self.list[pos]) == type(__int):
            return "int"
        elif type(self.list[pos]) == type(__str):
            return "str"
        elif type(self.list[pos]) == type(__float):
            return "float"
        elif type(self.list[pos]) == type(__complex):
            return "complex"
        elif type(self.list[pos]) == type(__list):
            return "list"
        elif type(self.list[pos]) == type(__tuple):
            return "tuple"
        elif type(self.list[pos]) == type(__range):
            return "range"
        elif type(self.list[pos]) == type(__dict):
            return "dict"
        elif type(self.list[pos]) == type(__set):
            return "set"
        elif type(self.list[pos]) == type(__frozenset):
            return "frozenset"
        elif type(self.list[pos]) == type(__bool):
            return "bool"
        elif type(self.list[pos]) == type(__bytes):
            return "bytes"
        elif type(self.list[pos]) == type(__bytearray):
            return "bytearray"
        elif type(self.list[pos]) == type(__memoryview):
            return "memoryview"
class Dict:
    def __init__(self):
        self.dict = {}

    def add(self, name, value):
        self.dict[name] = value

    def rem(self, name):
        self.dict.pop(name)

    def get(self, name):
        return self.dict.get(name)

    def geta(self):
        return self.dict

    def type(self, pos):
        __int = 1
        __str = 'a'
        __float = 1.5
        __complex = 1j
        __list = ["a", 1]
        __tuple = ("a", 1)
        __range = range(1)
        __dict = {"a": "a"}
        __set = {"a", "b"}
        __frozenset = frozenset({"a", "b"})
        __bool = True
        __bytes = b"Hello"
        __bytearray = bytearray(5)
        __memoryview = memoryview(bytes(5))
        global list
        if type(self.dict[pos]) == type(__int):
            return "int"
        elif type(self.dict.get(pos)) == type(__str):
            return "str"
        elif type(self.dict.get(pos)) == type(__float):
            return "float"
        elif type(self.dict.get(pos)) == type(__complex):
            return "complex"
        elif type(self.dict.get(pos)) == type(__list):
            return "list"
        elif type(self.dict.get(pos)) == type(__tuple):
            return "tuple"
        elif type(self.dict.get(pos)) == type(__range):
            return "range"
        elif type(self.dict.get(pos)) == type(__dict):
            return "dict"
        elif type(self.dict.get(pos)) == type(__set):
            return "set"
        elif type(self.dict.get(pos)) == type(__frozenset):
            return "frozenset"
        elif type(self.dict.get(pos)) == type(__bool):
            return "bool"
        elif type(self.dict.get(pos)) == type(__bytes):
            return "bytes"
        elif type(self.dict.get(pos)) == type(__bytearray):
            return "bytearray"
        elif type(self.dict.get(pos)) == type(__memoryview):
            return "memoryview"
class Array:
    def __init__(self):
        self.array = []

    def add(self, arry):
        __arj = []
        if type(arry) == type(__arj):
            self.array.append(arry)
        else:
            print("Invalid Value use []")

    def remove(self, value):
        self.array.remove(value)

    def get(self, value):
        return self.array[value]

    def geto(self, pos, value):
        __arj = self.array[pos]
        return __arj[value]

    def addo(self, pos, value):
        self.array[pos].append(value)



class hexopen:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.open = open(self.file, self.mode)

    def readline(self, limit=-1):
        s = self.open.readline(limit).split(';')
        __q = ""
        __x = []
        for a in s:
            if a != "":
                __x.append(chr(literal_eval(a)))
                __q = "".join(__x)
        return __q

    def write(self, s):
        for char in s:
            self.open.write(str(hex(ord(char))) + ';')

    def writelines(self, lines):
        for char in lines:
            self.open.writelines(hex(ord(char)))

    def close(self, ):
        self.open.close()

    def flush(self):
        return self.open.flush()

    def seek(self, cookie, whence=0):
        return self.open.seek(cookie, whence)

    def fileno(self):
        return self.open.fileno()

    def tell(self):
        return self.open.tell()

    def truncate(self, pos=None):
        return self.open.truncate(pos)

    def isatty(self):
        return self.open.isatty()

    def seekable(self):
        return self.open.seekable()

    def readable(self):
        return self.open.readable()

    def writable(self):
        return self.open.writable()
