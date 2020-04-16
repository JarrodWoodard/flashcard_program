
import random

# Terms dictionary

python_flashcards = {
    ">>>": "The default Python prompt of the interactive shell. Often seen for \n"
           "code examples which can be executed interactively in the interpreter.",
    "...": "Can refer to: \nThe default Python prompt of the interactive shell when entering\n"
           " the code for an indented code block, when within a pair of matching left and right \n"
           "delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator."
           " \n-or-\n The Ellipsis built-in constant.",
    "2to3": "A tool that tries to convert Python 2.x code to Python 3.x code by handling most of the \n"
            " which can be detected by parsing the source and traversing the parse tree. 2to3 is available \n"
            "in the standard library as lib2to3; a standalone entry point is provided as Tools/scripts/2to3. "
            "\nSee 2to3 - Automated Python 2 to 3 code translation.",
    "abstract base class": "Abstract base classes complement duck-typing by providing a way to define interfaces\n"
                           "when other techniques like hasattr() would be clumsy or subtly wrong (for example with \n"
                           "magic methods). ABCs introduce virtual subclasses, which are classes that don\'t inherit\n"
                           "from a class but are still recognized by isinstance() and issubclass(); \n"
                           "see the abc module documentation. Python comes with many built-in ABCs for \n"
                           "data structures (in the collections.abc module), numbers (in the numbers module), \n"
                           "streams (in the io module), import finders and loaders (in the importlib.abc module). \n"
                           "You can create your own ABCs with the abc module,",
    "Annotation": "A label associated with a variable, a class attribute or a function parameter or return value,\n"
                  " used by convention as a type hint. \nAnnotations of local variables cannot be accessed at \n"
                  "untime, but annotations of global variables, class attributes, and functions are stored in the \n"
                  "__annotations__ special attribute of modules, classes, and functions, respectively. "
                  "\nSee variable annotation, function annotation, PEP 484 and PEP 526,\n"
                  " which describe this functionality.",
    "Argument": "A value passed to a function (or method) when calling the function. \n"
                "There are two kinds of argument:"
                "\n keyword argument: an argument preceded by an identifier (e.g. name=) in a function call\n"
                " or passed as a value in a dictionary preceded by **. For example, 3 and 5 \n"
                "are both keyword arguments in the following"
                "\ncalls to complex():"
                "\n\ncomplex(real=3, imag=5)"
                "\n\ncomplex(**{\'real\': 3, \'imag\': 5})\n-and-"
                "\npositional argument: an argument that is not a keyword argument.\n"
                " Positional arguments can appear at the beginning of an argument list and/or be passed \n"
                "as elements of an iterable preceded by *. For example, 3 and 5 are both positional\n"
                " arguments in the following calls:"
                "\ncomplex(3, 5)\ncomplex(*(3, 5))\nArguments are assigned to the named local variables in a \n"
                "function body. See the Calls section for the rules governing this assignment. Syntactically,\n"
                " any expression can be used to represent an argument; the evaluated value is\n"
                " assigned to the local variable."
                "\nSee also the parameter glossary entry, the FAQ question on the difference between arguments \n"
                "and parameters, and PEP 362.",
    "asynchronous context manager": "An object which controls the environment seen in an async with statement by \n"
                                    "defining __aenter__() and __aexit__() methods. Introduced by PEP 492.",
    "asynchronous generator": "A function which returns an asynchronous generator iterator. It looks like a \n"
                              "coroutine function defined with async def except that it contains yield expressions \n"
                              "for producing a series of values usable in an async for loop."
                              "\nUsually refers to an asynchronous generator function, but may refer to an\n"
                              " asynchronous generator iterator in some contexts. In cases where the\n"
                              " intended meaning isn\'t clear, using the full terms avoids ambiguity.An asynchronous\n"
                              " generator function may contain await expressions as well as async for, \n"
                              "and async with statements.",
    "asynchronous generator iterator": "An object created by a asynchronous generator function. \n"
                                       "This is an asynchronous iterator which when called using the __\n"
                                       "anext__() method returns an awaitable object which will execute the body of\n"
                                       " the asynchronous generator function until the next yield expression. \n"
                                       "Each yield temporarily suspends processing, remembering the location\n"
                                       " execution state (including local variables and pending try-statements). \n"
                                       "When the asynchronous generator iterator effectively resumes with another \n"
                                       "awaitable returned by __anext__(), it picks up where it left off. \n"
                                       "See PEP 492 and PEP 525.",
    "asynchronous iterable": "An object, that can be used in an async for statement. \n"
                             "Must return an asynchronous iterator from its __aiter__() method. Introduced by PEP 492.",
    "asynchronous iterator": "An object that implements the __aiter__() and __anext__() methods. __anext__ must\n"
                             " return an awaitable object. async for resolves the awaitables returned by \n"
                             "an asynchronous iterator\'s __anext__() method until it raises a StopAsyncIteration \n"
                             "exception. Introduced by PEP 492.",
    "attribute": "A value associated with an object which is referenced by name using dotted expressions. \n"
                 "For example, if an object o has an attribute a it would be referenced as o.a.",
    "awaitable": "An object that can be used in an await expression. Can be a coroutine or an object with an __\n"
                 "await__() mnethod. See also PEP 492.",
    "BDFL": "Benevolent Dictator For Life, a.k.a. Guido van Rossum, Python\'s creator.",
    "binary file": "A file object able to read and write bytes-like objects. Examples of binary files are\n"
                   " files opened in binary mode (\'rb\', \'wb\' or \'rb+\'), sys.stdin.buffer, sys.stdout.buffer, \n"
                   "and instances of io.BytesIO and gzip.GzipFile. See also text file for a file object able \n"
                   "to read and write str objects.",
    "bytes-like object": "An object that supports the Buffer Protocol and can export a C-contiguous buffer. This\n"
                         " includes all bytes, bytearray, and array.array objects, as well as many common memoryview \n"
                         "objects. Bytes-like objects can be used for various operations that work with binary \n"
                         "data; these include compression, saving to a binary file, and sending over a socket. \n"
                         "Some operations need the binary data to be mutable. The documentation often refers to\n"
                         " these as \"read-write bytes-like objects\". Example mutable buffer objects include \n"
                         "bytearray and a memoryview of a bytearray. Other operations require the binary data to\n"
                         " be stored in immutable objects (\"read-only bytes-like objects\"); examples of these\n"
                         " include bytes and a memoryview of a bytes object.",
    "bytecode": "Python source code is compiled into bytecode, the internal representation of a Python program \n"
                "in the CPython interpreter. The bytecode is also cached in .pyc files so that executing the same \n"
                "file is faster the second time (recompilation from source to bytecode can be avoided).\n"
                " This \"intermediate language\" is said to run on a virtual machine that executes the machine code\n"
                " corresponding to each bytecode. Do note that bytecodes are not expected to work between different \n"
                "Python virtual machines, nor to be stable between Python releases. "
                "\nA list of bytecode instructions can be found in the documentation for the dis module.",
    "class": "A template for creating user-defined objects. Class definitions normally contain method definitions \n"
             "which operate on instances of the class.",
    "class variable": "A variable defined in a class and intended to be modified only at class level \n"
                      "(i.e., not in an instance of the class).",
    "coercion": "The implicit conversion of an instance of one type to another during an operation which involves \n"
                "two arguments of the same type. For example, int(3.15) converts the floating point number to the \n"
                "integer 3, but in 3+4.5, each argument is of a different type (one int, one float), and both must\n"
                " be converted to the same type before they can be added or it will raise a TypeError. Without \n"
                "coercion, all arguments of even compatible types would have to be normalized to the same value by \n"
                "the programmer, e.g., float(3)+4.5 rather than just 3+4.5.",
    "complex number": "An extension of the familiar real number system in which all numbers are expressed as \n"
                      "a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the \n"
                      "imaginary unit (the square root of -1), often written i in mathematics or j in engineering. \n"
                      "Python has built-in support for complex numbers, which are written with this latter\n"
                      " notation; the imaginary part is written with a j suffix, e.g., 3+1j. To get access to \n"
                      "complex equivalents of the math module, use cmath. Use of complex numbers is a fairly \n"
                      "advanced mathematical feature. If you\'re not aware of a need for them, it\'s almost certain\n"
                      " you can safely ignore them.",
    "context manager": "An object which controls the environment seen in a with statement by defining \n"
                       "__enter__() and __exit__() methods. See PEP 343.",
    "context variable": "A variable which can have different values depending on its context. \n"
                        "This is similar to Thread-Local Storage in which each execution thread may have a \n"
                        "different value for a variable. However, with context variables, there may be several \n"
                        "contexts in one execution thread and the main usage for context variables is to keep track \n"
                        "of variables in concurrent asynchronous tasks. See contextvars.",
    "contiguous": "A buffer is considered contiguous exactly if it is either C-contiguous or Fortran contiguous. \n"
                  "Zero-dimensional buffers are C and Fortran contiguous. In one-dimensional arrays, the items must \n"
                  "be laid out in memory next to each other, in order of increasing indexes starting from zero.\n"
                  " In multidimensional C-contiguous arrays, the last index varies the fastest when visiting items \n"
                  "in order of memory address. However, in Fortran contiguous arrays, \n"
                  "the first index varies the fastest.",
    "coroutine": "Coroutines are a more generalized form of subroutines. Subroutines are entered at one point\n"
                 " and exited at another point. Coroutines can be entered, exited, and resumed at many different \n"
                 "points. They can be implemented with the async def statement. See also PEP 492.",
    "coroutine function": "A function which returns a coroutine object. A coroutine function may be defined \n"
                          "with the async def statement, and may contain await, async for, and async with keywords. \n"
                          "These were introduced by PEP 492.",
    "CPython": "The canonical implementation of the Python programming language, as distributed on python.org. \n"
               "The term \"CPython\" is used when necessary to distinguish this implementation from others such as \n"
               "Jython or IronPython.",
    "decorator": "A function returning another function, usually applied as a function transformation using the \n"
                 "@wrapper syntax. Common examples for decorators are classmethod() and staticmethod()."
                 "\nThe decorator syntax is merely syntactic sugar, the following two function definitions are \n"
                 "semantically equivalent:\ndef f(...):\n...\nf = staticmethod(f)"
                 "\n@staticmethod\ndef f(...):\n..."
                 "\nThe same concept exists for classes, but is less commonly used there. See the \n"
                 "documentation for function definitions and class definitions for more about decorators.",
    "descriptor": "Any object which defines the methods __get__(), __set__(), or __delete__(). When a class \n"
                  "attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. \n"
                  "Normally, using a.b to get, set or delete an attribute looks up the object named b in the class \n"
                  "dictionary for a, but if b is a descriptor, the respective descriptor method gets called. \n"
                  "Understanding descriptors is a key to a deep understanding of Python because they are the basis \n"
                  "for many features including functions, methods, properties, class methods, static methods, and \n"
                  "reference to super classes.\nFor more information about descriptors\' methods, \n"
                  "see Implementing Descriptors.",
    "dictionary": "An associative array, where arbitrary keys are mapped to values. The keys can be any object with \n"
                  "__hash__() and __eq__() methods. Called a hash in Perl.",
    "dictionary view": "The objects returned from dict.keys(), dict.values(), and dict.items() are called dictionary\n"
                       " views. They provide a dynamic view on the dictionary’s entries, which means that when \n"
                       "the dictionary changes, the view reflects these changes. To force the dictionary view to \n"
                       "become a full list use list(dictview). See Dictionary view objects.",
    "docstring": "A string literal which appears as the first expression in a class, function or module. While \n"
                 "ignored when the suite is executed, it is recognized by the compiler and put into the __doc__ \n"
                 "attribute of the enclosing class, function or module. Since it is available via introspection, \n"
                 "it is the canonical place for documentation of the object.",
    "duck-typing": "A programming style which does not look at an object\'s type to determine if it has the right \n"
                   "interface; instead, the method or attribute is simply called or used (\"If it looks like a duck \n"
                   "and quacks like a duck, it must be a duck.\") By emphasizing interfaces rather than specific \n"
                   "types, well-designed code improves its flexibility by allowing polymorphic substitution. \n"
                   "Duck-typing avoids tests using type() or isinstance(). (Note, however, that duck-typing can be \n"
                   "complemented with abstract base classes.) Instead, it typically employs hasattr() tests or \n"
                   "EAFP programming.",
    "EAFP": "Easier to ask for forgiveness than permission. This common Python coding style assumes the existence \n"
            "of valid keys or attributes and catches exceptions if the assumption proves false. This clean and \n"
            "fast style is characterized by the presence of many try and except statements. The technique contrasts \n"
            "with the LBYL style common to many other languages such as C.",
    "expression": "A piece of syntax which can be evaluated to some value. In other words, an expression is an \n"
                  "accumulation of expression elements like literals, names, attribute access, operators or function \n"
                  "calls which all return a value. In contrast to many other languages, not all language constructs \n"
                  "are expressions. There are also statements which cannot be used as expressions, such as while. \n"
                  "Assignments are also statements, not expressions.",
    "extension module": "A module written in C or C++, using Python\'s C API to interact with the \n"
                        "core and with user code.",
    "f-string": "String literals prefixed with \'f\' or \'F\' are commonly called \"f-strings\" which is short \n"
                "for formatted string literals. See also PEP 498.",
    "file object": "An object exposing a file-oriented API (with methods such as read() or write()) to an \n"
                   "underlying resource. Depending on the way it was created, a file object can mediate access \n"
                   "to a real on-disk file or to another type of storage or communication device (for example \n"
                   "standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called \n"
                   "file-like objects or streams."
                   "\nThere are actually three categories of file objects: raw binary files, buffered binary \n"
                   "files and text files. Their interfaces are defined in the io module. The canonical way to \n"
                   "create a file object is by using the open() function.",
    "file-like object": "A synonym for file object.",
    "finder": "An object that tries to find the loader for a module that is being imported."
              "\nSince Python 3.3, there are two types of finder: meta path finders for use with sys.meta_path, \n"
              "and path entry finders for use with sys.path_hooks.\nSee PEP 302, PEP 420 and PEP 451 for much \n"
              "more detail.",
    "floor division": "Mathematical division that rounds down to nearest integer. The floor division operator \n"
                      "is //. For example, the expression 11 // 4 evaluates to 2 in contrast to the 2.75 returned \n"
                      "by float true division. Note that (-11) // 4 is -3 because that is -2.75 rounded downward. \n"
                      "See PEP 238.",
    "function": "A series of statements which returns some value to a caller. It can also be passed zero or more \n"
                "arguments which may be used in the execution of the body. See also parameter, method, \n"
                "and the Function definitions section.",
    "function annotation": "An annotation of a function parameter or return value."
                           "\nFunction annotations are usually used for type hints: for example, this function is \n"
                           "expected to take two int arguments and is also expected to have an int return value:"
                           "\ndef sum_two_numbers(a: int, b: int) -> int:\n   return a + b\nFunction annotation \n"
                           "syntax is explained in section Function definitions.\nSee variable annotation and \n"
                           "PEP 484, which describe this functionality.",
    "__future__": "A pseudo-module which programmers can use to enable new language features which are not \n"
                  "compatible with the current interpreter.\nBy importing the __future__ module and evaluating \n"
                  "its variables, you can see when a new feature was first added to the language and when it \n"
                  "becomes the default:\n>>>\n>>> import __future__\n>>> __future__.division"
                  "\n_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)",
    "garbage collection": "The process of freeing memory when it is not used anymore. Python performs garbage \n"
                          "collection via reference counting and a cyclic garbage collector that is able to \n"
                          "detect and break reference cycles. The garbage collector can be controlled \n"
                          "using the gc module.",
    "generator": "A function which returns a generator iterator. It looks like a normal function except that it \n"
                 "contains yield expressions for producing a series of values usable in a for-loop or that can \n"
                 "be retrieved one at a time with the next() function."
                 "\nUsually refers to a generator function, but may refer to a generator iterator in some contexts. \n"
                 "In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.",
    "generator iterator": "An object created by a generator function.\nEach yield temporarily suspends processing, \n"
                          "remembering the location execution state (including local variables and pending \n"
                          "try-statements). When the generator iterator resumes, it picks up where it left off \n"
                          "(in contrast to functions which start fresh on every invocation).",
    "generator expression": "An expression that returns an iterator. It looks like a normal expression followed \n"
                            "by a for clause defining a loop variable, range, and an optional if clause. The \n"
                            "combined expression generates values for an enclosing function:\n>>>"
                            "\n>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81\n285",
    "generic function": "A function composed of multiple functions implementing the same operation for different \n"
                        "types. Which implementation should be used during a call is determined by the \n"
                        "dispatch algorithm.\nSee also the single dispatch glossary entry, the functools.\n"
                        "singledispatch() decorator, and PEP 443.",
    "GIL": "See global interpreter lock.",
    "global interpreter lock": "The mechanism used by the CPython interpreter to assure that only one thread \n"
                               "executes Python bytecode at a time. This simplifies the CPython implementation \n"
                               "by making the object model (including critical built-in types such as dict) \n"
                               "implicitly safe against concurrent access. Locking the entire interpreter \n"
                               "makes it easier for the interpreter to be multi-threaded, at the expense of \n"
                               "much of the parallelism afforded by multi-processor machines."
                               "\nHowever, some extension modules, either standard or third-party, are designed \n"
                               "so as to release the GIL when doing computationally-intensive tasks such as \n"
                               "compression or hashing. Also, the GIL is always released when doing I/O."
                               "\nPast efforts to create a \"free-threaded\" interpreter (one which locks shared \n"
                               "data at a much finer granularity) have not been successful because performance \n"
                               "suffered in the common single-processor case. It is believed that overcoming \n"
                               "this performance issue would make the implementation much more complicated and \n"
                               "therefore costlier to maintain.",
    "hash-based pyc": "A bytecode cache file that uses the hash rather than the last-modified time of the \n"
                      "corresponding source file to determine its validity. See Cached bytecode invalidation.",
    "hashable": "An object is hashable if it has a hash value which never changes during its lifetime (it needs \n"
                "a __hash__() method), and can be compared to other objects (it needs an __eq__() method). \n"
                "Hashable objects which compare equal must have the same hash value.\nHashability makes an \n"
                "object usable as a dictionary key and a set member, because these data structures use the \n"
                "hash value internally.\nMost of Python’s immutable built-in objects are hashable; mutable \n"
                "containers (such as lists or dictionaries) are not; immutable containers (such as tuples and \n"
                "frozensets) are only hashable if their elements are hashable. Objects which are instances of \n"
                "user-defined classes are hashable by default. They all compare unequal (except with themselves), \n"
                "and their hash value is derived from their id().",
    "IDLE": "An Integrated Development Environment for Python. IDLE is a basic editor and interpreter environment \n"
            "which ships with the standard distribution of Python.",
    "immutable": "An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an \n"
                 "object cannot be altered. A new object has to be created if a different value has to be stored. \n"
                 "They play an important role in places where a constant hash value is needed, for example as a key \n"
                 "in a dictionary.",
    "import path": "A list of locations (or path entries) that are searched by the path based finder for modules \n"
                   "to import. During import, this list of locations usually comes from sys.path, but for \n"
                   "subpackages it may also come from the parent package’s __path__ attribute.",
    "importing": "The process by which Python code in one module is made available to Python code in another module.",
    "importer": "An object that both finds and loads a module; both a finder and loader object.",
    "interactive": "Python has an interactive interpreter which means you can enter statements and expressions \n"
                   "at the interpreter prompt, immediately execute them and see their results. Just launch python \n"
                   "with no arguments (possibly by selecting it from your computer’s main menu). It is a very \n"
                   "powerful way to test out new ideas or inspect modules and packages (remember help(x)).",
    "interpreted": "Python is an interpreted language, as opposed to a compiled one, though the distinction can \n"
                   "be blurry because of the presence of the bytecode compiler. This means that source files can \n"
                   "be run directly without explicitly creating an executable which is then run. Interpreted \n"
                   "languages typically have a shorter development/debug cycle than compiled ones, though their \n"
                   "programs generally also run more slowly. See also interactive.",
    "interpreter shutdown": "When asked to shut down, the Python interpreter enters a special phase where it \n"
                            "gradually releases all allocated resources, such as modules and various critical \n"
                            "internal structures. It also makes several calls to the garbage collector. This \n"
                            "can trigger the execution of code in user-defined destructors or weakref callbacks. \n"
                            "Code executed during the shutdown phase can encounter various exceptions as the \n"
                            "resources it relies on may not function anymore (common examples are library modules \n"
                            "or the warnings machinery).\nThe main reason for interpreter shutdown is that \n"
                            "the __main__ module or the script being run has finished executing.",
    "iterable": "An object capable of returning its members one at a time. Examples of iterables include all \n"
                "sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, \n"
                "and objects of any classes you define with an __iter__() method or with a __getitem__() method \n"
                "that implements Sequence semantics.\nIterables can be used in a for loop and in many other places \n"
                "where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to \n"
                "the built-in function iter(), it returns an iterator for the object. This iterator is good for one \n"
                "pass over the set of values. When using iterables, it is usually not necessary to call iter() or \n"
                "deal with iterator objects yourself. The for statement does that automatically for you, creating a \n"
                "temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, \n"
                "sequence, and generator.",
    "iterator": "An object representing a stream of data. Repeated calls to the iterator’s __next__() method \n"
                "(or passing it to the built-in function next()) return successive items in the stream. When no more \n"
                "data are available a StopIteration exception is raised instead. At this point, the iterator object \n"
                "is exhausted and any further calls to its __next__() method just raise StopIteration again. \n"
                "Iterators are required to have an __iter__() method that returns the iterator object itself so \n"
                "every iterator is also iterable and may be used in most places where other iterables are accepted. \n"
                "One notable exception is code which attempts multiple iteration passes. A container object \n"
                "(such as a list) produces a fresh new iterator each time you pass it to the iter() function or \n"
                "use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator \n"
                "object used in the previous iteration pass, making it appear like an empty container."
                "\nMore information can be found in Iterator Types.",
    "key function": "A key function or collation function is a callable that returns a value used for sorting or \n"
                    "ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale \n"
                    "specific sort conventions.\nA number of tools in Python accept key functions to control how \n"
                    "elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), \n"
                    "heapq.merge(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby()."
                    "\nThere are several ways to create a key function. For example. the str.lower() method can \n"
                    "serve as a key function for case insensitive sorts. Alternatively, a key function can be \n"
                    "built from a lambda expression such as lambda r: (r[0], r[2]). Also, the operator module \n"
                    "provides three key function constructors: attrgetter(), itemgetter(), and methodcaller(). \n"
                    "See the Sorting HOW TO for examples of how to create and use key functions.",
    "keyword argument": "See argument.",
    "lambda": "An anonymous inline function consisting of a single expression which is evaluated when the function \n"
              "is called. The syntax to create a lambda function is lambda [parameters]: expression",
    "LBYL": "Look before you leap. This coding style explicitly tests for pre-conditions before making calls or \n"
            "lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if \n"
            "statements.\nIn a multi-threaded environment, the LBYL approach can risk introducing a race condition \n"
            "between \"the looking\" and \"the leaping\". For example, the code, if key in mapping: return \n"
            "mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. \n"
            "This issue can be solved with locks or by using the EAFP approach.",
    "list": "A built-in Python sequence. Despite its name it is more akin to an array in other languages than to \n"
            "a linked list since access to elements is O(1).",
    "list comprehension": "A compact way to process all or part of the elements in a sequence and return a list \n"
                          "with the results. result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] \n"
                          "generates a list of strings containing even hex numbers (0x..) in the range from \n"
                          "0 to 255. The if clause is optional. If omitted, all elements in range(256) are processed.",
    "loader": "An object that loads a module. It must define a method named load_module(). A loader is typically \n"
              "returned by a finder. See PEP 302 for details and importlib.abc.Loader for an abstract base class.",
    "magic method": "An informal synonym for special method.",
    "mapping": "A container object that supports arbitrary key lookups and implements the methods specified in the \n"
               "Mapping or MutableMapping abstract base classes. Examples include dict, collections.defaultdict, \n"
               "collections.OrderedDict and collections.Counter.",
    "meta path finder": "A finder returned by a search of sys.meta_path. Meta path finders are related to, \n"
                        "but different from path entry finders."
                        "\nSee importlib.abc.MetaPathFinder for the methods that meta path finders implement.",
    "metaclass": "The class of a class. Class definitions create a class name, a class dictionary, and a list of \n"
                 "base classes. The metaclass is responsible for taking those three arguments and creating the \n"
                 "class. Most object oriented programming languages provide a default implementation. What makes \n"
                 "Python special is that it is possible to create custom metaclasses. Most users never need this \n"
                 "tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have \n"
                 "been used for logging attribute access, adding thread-safety, tracking object creation, \n"
                 "implementing singletons, and many other tasks.\nMore information can be found in Metaclasses.",
    "method": "A function which is defined inside a class body. If called as an attribute of an instance of that \n"
              "class, the method will get the instance object as its first argument (which is usually called self). \n"
              "See function and nested scope.",
    "method resolution order": "Method Resolution Order is the order in which base classes are searched for a \n"
                               "member during lookup. See The Python 2.3 Method Resolution Order for details of the \n"
                               "algorithm used by the Python interpreter since the 2.3 release.",
    "module": "An object that serves as an organizational unit of Python code. Modules have a namespace containing \n"
              "arbitrary Python objects. Modules are loaded into Python by the process of importing\nSee also package.",
    "module spec": "A namespace containing the import-related information used to load a module. An instance of \n"
                   "importlib.machinery.ModuleSpec.",
    "MRO": "See method resolution order.",
    "mutable": "Mutable objects can change their value but keep their id(). See also immutable.",
    "named tuple": "The term “named tuple” applies to any type or class that inherits from tuple and whose \n"
                   "indexable elements are also accessible using named attributes. The type or class may have \n"
                   "other features as well.\nSeveral built-in types are named tuples, including the values returned \n"
                   "by time.localtime() and os.stat(). Another example is sys.float_info:\n>>>"
                   "\n>>> sys.float_info[1]                   # indexed access\n1024\n>>> sys.float_info.max_\n"
                   "exp              # named field access\n1024\n>>> isinstance(sys.float_info, tuple)   # kind \n"
                   "of tuple\nTrue\nSome named tuples are built-in types (such as the above examples). \n"
                   "Alternatively, a named tuple can be created from a regular class definition that inherits \n"
                   "from tuple and that defines named fields. Such a class can be written by hand or it can be \n"
                   "created with the factory function collections.namedtuple(). The latter technique also adds some \n"
                   "extra methods that may not be found in hand-written or built-in named tuples.",
    "namespace": "The place where a variable is stored. Namespaces are implemented as dictionaries. There are the \n"
                 "local, global and built-in namespaces as well as nested namespaces in objects (in methods). \n"
                 "Namespaces support modularity by preventing naming conflicts. For instance, the functions \n"
                 "builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid \n"
                 "readability and maintainability by making it clear which module implements a function. For \n"
                 "instance, writing random.seed() or itertools.islice() makes it clear that those functions are \n"
                 "implemented by the random and itertools modules, respectively.",
    "namespace package": "A PEP 420 package which serves only as a container for subpackages. Namespace packages \n"
                         "may have no physical representation, and specifically are not like a regular package \n"
                         "because they have no __init__.py file.\nSee also module.",
    "nested scope": "The ability to refer to a variable in an enclosing definition. For instance, a function \n"
                    "defined inside another function can refer to variables in the outer function. Note that \n"
                    "nested scopes by default work only for reference and not for assignment. Local variables \n"
                    "both read and write in the innermost scope. Likewise, global variables read and write to \n"
                    "the global namespace. The nonlocal allows writing to outer scopes.",
    "new-style class": "Old name for the flavor of classes now used for all class objects. In earlier Python \n"
                       "versions, only new-style classes could use Python’s newer, versatile features like __\n"
                       "slots__, descriptors, properties, __getattribute__(), class methods, and static methods.",
    "object": "Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base \n"
              "class of any new-style class.",
    "package": "A Python module which can contain submodules or recursively, subpackages. Technically, a package \n"
               "is a Python module with an __path__ attribute.\nSee also regular package and namespace package.",
    "parameter": "A named entity in a function (or method) definition that specifies an argument (or in some cases, \n"
                 "arguments) that the function can accept. There are five kinds of parameter:"
                 "\npositional-or-keyword: specifies an argument that can be passed either positionally or as a \n"
                 "keyword argument. This is the default kind of parameter, for example foo and bar in the following:\n"
                 "def func(foo, bar=None): ...\npositional-only: specifies an argument that can be supplied only \n"
                 "by position. Positional-only parameters can be defined by including a / character in the parameter \n"
                 "list of the function definition after them, for example posonly1 and posonly2 in the following:"
                 "\ndef func(posonly1, posonly2, /, positional_or_keyword): ..."
                 "\nkeyword-only: specifies an argument that can be supplied only by keyword. Keyword-only \n"
                 "parameters can be defined by including a single var-positional parameter or bare * in the \n"
                 "parameter list of the function definition before them, for example kw_only1 and kw_only2 in \n"
                 "the following:\ndef func(arg, *, kw_only1, kw_only2): ..."
                 "\nvar-positional: specifies that an arbitrary sequence of positional arguments can be \n"
                 "provided (in addition to any positional arguments already accepted by other parameters). \n"
                 "Such a parameter can be defined by prepending the parameter name with *, for example args \n"
                 "in the following:\ndef func(*args, **kwargs): ..."
                 "\nvar-keyword: specifies that arbitrarily many keyword arguments can be provided (in addition \n"
                 "to any keyword arguments already accepted by other parameters). Such a parameter can be defined \n"
                 "by prepending the parameter name with **, for example kwargs in the example above."
                 "\nParameters can specify both optional and required arguments, as well as default values for \n"
                 "some optional arguments.\nSee also the argument glossary entry, the FAQ question on the \n"
                 "difference between arguments and parameters, the inspect.Parameter class, the Function \n"
                 "definitions section, and PEP 362.",
    "path entry": "A single location on the import path which the path based finder consults to find modules \n"
                  "for importing.",
    "path entry finder": "A finder returned by a callable on sys.path_hooks (i.e. a path entry hook) which knows \n"
                         "how to locate modules given a path entry."
                         "\nSee importlib.abc.PathEntryFinder for the methods that path entry finders implement.",
    "path entry hook": "A callable on the sys.path_hook list which returns a path entry finder if it knows how to \n"
                       "find modules on a specific path entry.",
    "path based finder": "One of the default meta path finders which searches an import path for modules.",
    "path-like object": "An object representing a file system path. A path-like object is either a str or bytes \n"
                        "object representing a path, or an object implementing the os.PathLike protocol. An object \n"
                        "that supports the os.PathLike protocol can be converted to a str or bytes file system \n"
                        "path by calling the os.fspath() function; os.fsdecode() and os.fsencode() can be used to \n"
                        "guarantee a str or bytes result instead, respectively. Introduced by PEP 519.",
    "PEP": "Python Enhancement Proposal. A PEP is a design document providing information to the Python community, \n"
           "or describing a new feature for Python or its processes or environment. PEPs should provide a concise \n"
           "technical specification and a rationale for proposed features."
           "\nPEPs are intended to be the primary mechanisms for proposing major new features, for collecting \n"
           "community input on an issue, and for documenting the design decisions that have gone into Python. \n"
           "The PEP author is responsible for building consensus within the community and documenting dissenting \n"
           "opinions.\nSee PEP 1.",
    "portion": "A set of files in a single directory (possibly stored in a zip file) that contribute to a \n"
               "namespace package, as defined in PEP 420.",
    "positional argument": "See argument.",
    "provisional API": "A provisional API is one which has been deliberately excluded from the standard \n"
                       "library\'s backwards compatibility guarantees. While major changes to such interfaces are \n"
                       "not expected, as long as they are marked provisional, backwards incompatible changes \n"
                       "(up to and including removal of the interface) may occur if deemed necessary by core \n"
                       "developers. Such changes will not be made gratuitously – they will occur only if serious \n"
                       "fundamental flaws are uncovered that were missed prior to the inclusion of the API."
                       "\nEven for provisional APIs, backwards incompatible changes are seen as a \"solution of \n"
                       "last resort\" - every attempt will still be made to find a backwards compatible resolution \n"
                       "to any identified problems.\nThis process allows the standard library to continue to evolve \n"
                       "over time, without locking in problematic design errors for extended periods of time. \n"
                       "See PEP 411 for more details.",
    "provisional package": "See provisional API.",
    "Python 3000": "Nickname for the Python 3.x release line (coined long ago when the release of version 3 was \n"
                   "something in the distant future.) This is also abbreviated \"Py3k\".",
    "Pythonic": "An idea or piece of code which closely follows the most common idioms of the Python language, \n"
                "rather than implementing code using concepts common to other languages. For example, a common \n"
                "idiom in Python is to loop over all elements of an iterable using a for statement. Many other \n"
                "languages don\'t have this type of construct, so people unfamiliar with Python sometimes use a \n"
                "numerical counter instead:\nfor i in range(len(food)):\n    print(food[i])\nAs opposed to the \n"
                "cleaner, Pythonic method:\nfor piece in food:\n    print(piece)",
    "qualified name": "A dotted name showing the “path” from a module’s global scope to a class, function or method \n"
                      "defined in that module, as defined in PEP 3155. For top-level functions and classes, the \n"
                      "qualified name is the same as the object’s name:\n>>>\n>>> class C:\n...     class D:"
                      "\n...         def meth(self):\n...             pass\n...\n>>> C.__qualname__\n\'C\'"
                      "\n>>> C.D.__qualname__\n\'C.D\'\n>>> C.D.meth.__qualname__\n\'C.D.meth\'\nWhen used to refer \n"
                      "to modules, the fully qualified name means the entire dotted path to the module, including \n"
                      "any parent packages, e.g. email.mime.text:\n>>>\n>>> import email.mime.text"
                      "\n>>> email.mime.text.__name__\n\'email.mime.text\',",
    "reference count": "The number of references to an object. When the reference count of an object drops to \n"
                       "zero, it is deallocated. Reference counting is generally not visible to Python code, but \n"
                       "it is a key element of the CPython implementation. The sys module defines a getrefcount() \n"
                       "function that programmers can call to return the reference count for a particular object.",
    "regular package": "A traditional package, such as a directory containing an __init__.py file.\n"
                       "See also namespace package.",
    "__slots__": "A declaration inside a class that saves memory by pre-declaring space for instance attributes \n"
                 "and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get \n"
                 "right and is best reserved for rare cases where there are large numbers of instances in a \n"
                 "memory-critical application.",
    "sequence": "An iterable which supports efficient element access using integer indices via the __getitem__() \n"
                "special method and defines a __len__() method that returns the length of the sequence. Some \n"
                "built-in sequence types are list, str, tuple, and bytes. Note that dict also supports \n"
                "__getitem__() and __len__(), but is considered a mapping rather than a sequence because the lookups \n"
                "use arbitrary immutable keys rather than integers.\nThe collections.abc.Sequence abstract base \n"
                "class defines a much richer interface that goes beyond just __getitem__() and __len__(), adding \n"
                "count(), index(), __contains__(), and __reversed__(). Types that implement this expanded \n"
                "interface can be registered explicitly using register().",
    "single dispatch": "A form of generic function dispatch where the implementation is chosen based on the type \n"
                       "of a single argument.",
    "slice": "An object usually containing a portion of a sequence. A slice is created using the subscript \n"
             "notation, [] with colons between numbers when several are given, such as in variable_name[1:3:5]. \n"
             "The bracket (subscript) notation uses slice objects internally.",
    "special method": "A method that is called implicitly by Python to execute a certain operation on a type, \n"
                      "such as addition. Such methods have names starting and ending with double underscores. \n"
                      "Special methods are documented in Special method names.",
    "statement": "A statement is part of a suite (a \'block\" of code). A statement is either an expression or \n"
                 "one of several constructs with a keyword, such as if, while or for.",
    "text encoding": "A codec which encodes Unicode strings to bytes.",
    "text file": "A file object able to read and write str objects. Often, a text file actually accesses a \n"
                 "byte-oriented datastream and handles the text encoding automatically. Examples of text files \n"
                 "are files opened in text mode (\'r\' or \'w\'), sys.stdin, sys.stdout, and instances of io.StringIO."
                 "\nSee also binary file for a file object able to read and write bytes-like objects.",
    "triple-quoted string": "A string which is bound by three instances of either a quotation mark (\") or an \n"
                            "apostrophe (\'). While they don\'t provide any functionality not available with \n"
                            "single-quoted strings, they are useful for a number of reasons. They allow you to \n"
                            "include unescaped single and double quotes within a string and they can span multiple \n"
                            "lines without the use of the continuation character, making them especially useful \n"
                            "when writing docstrings.",
    "type": "The type of a Python object determines what kind of object it is; every object has a type. An object\'s \n"
            "type is accessible as its __class__ attribute or can be retrieved with type(obj).",
    "type alias": "A synonym for a type, created by assigning the type to an identifier."
                  "\nType aliases are useful for simplifying type hints. For example:\nfrom typing import List, Tuple"
                  "\ndef remove_gray_shades("
                  "\n        colors: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:\n    pass"
                  "\ncould be made more readable like this:\nfrom typing import List, Tuple"
                  "\nColor = Tuple[int, int, int]\ndef remove_gray_shades(colors: List[Color]) -> List[Color]:"
                  "\n    pass\nSee typing and PEP 484, which describe this functionality.\n\"type hint\":"
                  "\nAn annotation that specifies the expected type for a variable, a class attribute, or a \n"
                  "function parameter or return value.\nType hints are optional and are not enforced by Python \n"
                  "but they are useful to static type analysis tools, and aid IDEs with code completion and \n"
                  "refactoring.\nType hints of global variables, class attributes, and functions, but not local \n"
                  "variables, can be accessed using typing.get_type_hints()."
                  "\nSee typing and PEP 484, which describe this functionality.",
    "universal newlines": "A manner of interpreting text streams in which all of the following are recognized as \n"
                          "ending a line: the Unix end-of-line convention \'\\n\', the Windows convention \'\\r\\n\',\n"
                          " and the old Macintosh convention \'\\r\'. See PEP 278 and PEP 3116, as well as \n"
                          "bytes.splitlines() for an additional use.",
    "variable annotation": "An annotation of a variable or a class attribute.\nWhen annotating a variable or a \n"
                           "class attribute, assignment is optional:\nclass C\nfield: \'annotation\' "
                           "\nVariable annotations are usually used for type hints: for example this variable is \n"
                           "expected to take int values:\ncount: int = 0\nVariable annotation syntax is explained \n"
                           "in section Annotated assignment statements.\nSee function annotation, PEP 484 and \n"
                           "PEP 526, which describe this functionality.",
    "virtual environment": "A cooperatively isolated runtime environment that allows Python users and applications \n"
                           "to install and upgrade Python distribution packages without interfering with the \n"
                           "behaviour of other Python applications running on the same system.\nSee also venv.",
    "virtual machine": "A computer defined entirely in software. Python\'s virtual machine executes the bytecode \n"
                       "emitted by the bytecode compiler.",
    "Zen of Python": "Listing of Python design principles and philosophies that are helpful in understanding and \n"
                     "using the language. The listing can be found by typing \"import this\" at the interactive \n"
                     "prompt.mpt of the interactive shell. Often seen for code examples which can be executed \n"
                     "interactively in the interpreter."
}


# The menu options

menu_dictionary = {
    1: "Get a flashcard challenge",
    2: "option 2 (unused)",
    3: "Program Guthub address",
    4: "Quit"
}

# Program introduction

print("Please select an option:")
user_input = input(list(menu_dictionary.items()))

# The main program loop

while user_input != "4":

    if user_input == "1":
        random_flashcard_pair = random_flashcard_key, random_flashcard_value = random.choice(list(python_flashcards.items()))
        print("\n" + random_flashcard_value + "\n")

        guess = str(input("What is the term? \n \n"))
        if guess == random_flashcard_key:
            print("\nCorrect!\n")

        else:
            YN_input = input("\nSorry, incorrect. Would you like to know the answer?\nEnter \'1\' for \'yes\' and anything else for 'no'. \n")
            if YN_input == "1":
                print("\n" + random_flashcard_key + "\n")
            else:
                continue

        user_input = input(menu_dictionary)
    elif user_input == "2":
        print("\n2?\n")
        user_input = input(menu_dictionary)
    elif user_input == "3":
        print("\nhttps://github.com/JarrodWoodard/flashcard_program\n")
        user_input = input(menu_dictionary)
    else:
        print("Invalid input, Please select an option from the menu:")
        user_input = input(menu_dictionary)

