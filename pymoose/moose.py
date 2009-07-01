# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

import _moose
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class PySwigIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _moose.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _moose.PySwigIterator_value(*args)
    def incr(*args): return _moose.PySwigIterator_incr(*args)
    def decr(*args): return _moose.PySwigIterator_decr(*args)
    def distance(*args): return _moose.PySwigIterator_distance(*args)
    def equal(*args): return _moose.PySwigIterator_equal(*args)
    def copy(*args): return _moose.PySwigIterator_copy(*args)
    def next(*args): return _moose.PySwigIterator_next(*args)
    def previous(*args): return _moose.PySwigIterator_previous(*args)
    def advance(*args): return _moose.PySwigIterator_advance(*args)
    def __eq__(*args): return _moose.PySwigIterator___eq__(*args)
    def __ne__(*args): return _moose.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _moose.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _moose.PySwigIterator___isub__(*args)
    def __add__(*args): return _moose.PySwigIterator___add__(*args)
    def __sub__(*args): return _moose.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _moose.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class uint_vector(object):
    """Proxy of C++ uint_vector class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(*args):
        """iterator(self, PyObject PYTHON_SELF) -> PySwigIterator"""
        return _moose.uint_vector_iterator(*args)

    def __iter__(self): return self.iterator()
    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _moose.uint_vector___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> size_type"""
        return _moose.uint_vector___len__(*args)

    def pop(*args):
        """pop(self) -> value_type"""
        return _moose.uint_vector_pop(*args)

    def __getslice__(*args):
        """__getslice__(self, difference_type i, difference_type j) -> uint_vector"""
        return _moose.uint_vector___getslice__(*args)

    def __setslice__(*args):
        """__setslice__(self, difference_type i, difference_type j, uint_vector v)"""
        return _moose.uint_vector___setslice__(*args)

    def __delslice__(*args):
        """__delslice__(self, difference_type i, difference_type j)"""
        return _moose.uint_vector___delslice__(*args)

    def __delitem__(*args):
        """__delitem__(self, difference_type i)"""
        return _moose.uint_vector___delitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, difference_type i) -> value_type"""
        return _moose.uint_vector___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, difference_type i, value_type x)"""
        return _moose.uint_vector___setitem__(*args)

    def append(*args):
        """append(self, value_type x)"""
        return _moose.uint_vector_append(*args)

    def empty(*args):
        """empty(self) -> bool"""
        return _moose.uint_vector_empty(*args)

    def size(*args):
        """size(self) -> size_type"""
        return _moose.uint_vector_size(*args)

    def clear(*args):
        """clear(self)"""
        return _moose.uint_vector_clear(*args)

    def swap(*args):
        """swap(self, uint_vector v)"""
        return _moose.uint_vector_swap(*args)

    def get_allocator(*args):
        """get_allocator(self) -> allocator_type"""
        return _moose.uint_vector_get_allocator(*args)

    def begin(*args):
        """
        begin(self) -> iterator
        begin(self) -> const_iterator
        """
        return _moose.uint_vector_begin(*args)

    def end(*args):
        """
        end(self) -> iterator
        end(self) -> const_iterator
        """
        return _moose.uint_vector_end(*args)

    def rbegin(*args):
        """
        rbegin(self) -> reverse_iterator
        rbegin(self) -> const_reverse_iterator
        """
        return _moose.uint_vector_rbegin(*args)

    def rend(*args):
        """
        rend(self) -> reverse_iterator
        rend(self) -> const_reverse_iterator
        """
        return _moose.uint_vector_rend(*args)

    def pop_back(*args):
        """pop_back(self)"""
        return _moose.uint_vector_pop_back(*args)

    def erase(*args):
        """
        erase(self, iterator pos) -> iterator
        erase(self, iterator first, iterator last) -> iterator
        """
        return _moose.uint_vector_erase(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> uint_vector
        __init__(self, uint_vector ?) -> uint_vector
        __init__(self, size_type size) -> uint_vector
        __init__(self, size_type size, value_type value) -> uint_vector
        """
        this = _moose.new_uint_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args):
        """push_back(self, value_type x)"""
        return _moose.uint_vector_push_back(*args)

    def front(*args):
        """front(self) -> value_type"""
        return _moose.uint_vector_front(*args)

    def back(*args):
        """back(self) -> value_type"""
        return _moose.uint_vector_back(*args)

    def assign(*args):
        """assign(self, size_type n, value_type x)"""
        return _moose.uint_vector_assign(*args)

    def resize(*args):
        """
        resize(self, size_type new_size)
        resize(self, size_type new_size, value_type x)
        """
        return _moose.uint_vector_resize(*args)

    def insert(*args):
        """
        insert(self, iterator pos, value_type x) -> iterator
        insert(self, iterator pos, size_type n, value_type x)
        """
        return _moose.uint_vector_insert(*args)

    def reserve(*args):
        """reserve(self, size_type n)"""
        return _moose.uint_vector_reserve(*args)

    def capacity(*args):
        """capacity(self) -> size_type"""
        return _moose.uint_vector_capacity(*args)

    __swig_destroy__ = _moose.delete_uint_vector
    __del__ = lambda self : None;
uint_vector_swigregister = _moose.uint_vector_swigregister
uint_vector_swigregister(uint_vector)

class int_vector(object):
    """Proxy of C++ int_vector class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(*args):
        """iterator(self, PyObject PYTHON_SELF) -> PySwigIterator"""
        return _moose.int_vector_iterator(*args)

    def __iter__(self): return self.iterator()
    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _moose.int_vector___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> size_type"""
        return _moose.int_vector___len__(*args)

    def pop(*args):
        """pop(self) -> value_type"""
        return _moose.int_vector_pop(*args)

    def __getslice__(*args):
        """__getslice__(self, difference_type i, difference_type j) -> int_vector"""
        return _moose.int_vector___getslice__(*args)

    def __setslice__(*args):
        """__setslice__(self, difference_type i, difference_type j, int_vector v)"""
        return _moose.int_vector___setslice__(*args)

    def __delslice__(*args):
        """__delslice__(self, difference_type i, difference_type j)"""
        return _moose.int_vector___delslice__(*args)

    def __delitem__(*args):
        """__delitem__(self, difference_type i)"""
        return _moose.int_vector___delitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, difference_type i) -> value_type"""
        return _moose.int_vector___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, difference_type i, value_type x)"""
        return _moose.int_vector___setitem__(*args)

    def append(*args):
        """append(self, value_type x)"""
        return _moose.int_vector_append(*args)

    def empty(*args):
        """empty(self) -> bool"""
        return _moose.int_vector_empty(*args)

    def size(*args):
        """size(self) -> size_type"""
        return _moose.int_vector_size(*args)

    def clear(*args):
        """clear(self)"""
        return _moose.int_vector_clear(*args)

    def swap(*args):
        """swap(self, int_vector v)"""
        return _moose.int_vector_swap(*args)

    def get_allocator(*args):
        """get_allocator(self) -> allocator_type"""
        return _moose.int_vector_get_allocator(*args)

    def begin(*args):
        """
        begin(self) -> iterator
        begin(self) -> const_iterator
        """
        return _moose.int_vector_begin(*args)

    def end(*args):
        """
        end(self) -> iterator
        end(self) -> const_iterator
        """
        return _moose.int_vector_end(*args)

    def rbegin(*args):
        """
        rbegin(self) -> reverse_iterator
        rbegin(self) -> const_reverse_iterator
        """
        return _moose.int_vector_rbegin(*args)

    def rend(*args):
        """
        rend(self) -> reverse_iterator
        rend(self) -> const_reverse_iterator
        """
        return _moose.int_vector_rend(*args)

    def pop_back(*args):
        """pop_back(self)"""
        return _moose.int_vector_pop_back(*args)

    def erase(*args):
        """
        erase(self, iterator pos) -> iterator
        erase(self, iterator first, iterator last) -> iterator
        """
        return _moose.int_vector_erase(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> int_vector
        __init__(self, int_vector ?) -> int_vector
        __init__(self, size_type size) -> int_vector
        __init__(self, size_type size, value_type value) -> int_vector
        """
        this = _moose.new_int_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args):
        """push_back(self, value_type x)"""
        return _moose.int_vector_push_back(*args)

    def front(*args):
        """front(self) -> value_type"""
        return _moose.int_vector_front(*args)

    def back(*args):
        """back(self) -> value_type"""
        return _moose.int_vector_back(*args)

    def assign(*args):
        """assign(self, size_type n, value_type x)"""
        return _moose.int_vector_assign(*args)

    def resize(*args):
        """
        resize(self, size_type new_size)
        resize(self, size_type new_size, value_type x)
        """
        return _moose.int_vector_resize(*args)

    def insert(*args):
        """
        insert(self, iterator pos, value_type x) -> iterator
        insert(self, iterator pos, size_type n, value_type x)
        """
        return _moose.int_vector_insert(*args)

    def reserve(*args):
        """reserve(self, size_type n)"""
        return _moose.int_vector_reserve(*args)

    def capacity(*args):
        """capacity(self) -> size_type"""
        return _moose.int_vector_capacity(*args)

    __swig_destroy__ = _moose.delete_int_vector
    __del__ = lambda self : None;
int_vector_swigregister = _moose.int_vector_swigregister
int_vector_swigregister(int_vector)

class double_vector(object):
    """Proxy of C++ double_vector class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(*args):
        """iterator(self, PyObject PYTHON_SELF) -> PySwigIterator"""
        return _moose.double_vector_iterator(*args)

    def __iter__(self): return self.iterator()
    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _moose.double_vector___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> size_type"""
        return _moose.double_vector___len__(*args)

    def pop(*args):
        """pop(self) -> value_type"""
        return _moose.double_vector_pop(*args)

    def __getslice__(*args):
        """__getslice__(self, difference_type i, difference_type j) -> double_vector"""
        return _moose.double_vector___getslice__(*args)

    def __setslice__(*args):
        """__setslice__(self, difference_type i, difference_type j, double_vector v)"""
        return _moose.double_vector___setslice__(*args)

    def __delslice__(*args):
        """__delslice__(self, difference_type i, difference_type j)"""
        return _moose.double_vector___delslice__(*args)

    def __delitem__(*args):
        """__delitem__(self, difference_type i)"""
        return _moose.double_vector___delitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, difference_type i) -> value_type"""
        return _moose.double_vector___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, difference_type i, value_type x)"""
        return _moose.double_vector___setitem__(*args)

    def append(*args):
        """append(self, value_type x)"""
        return _moose.double_vector_append(*args)

    def empty(*args):
        """empty(self) -> bool"""
        return _moose.double_vector_empty(*args)

    def size(*args):
        """size(self) -> size_type"""
        return _moose.double_vector_size(*args)

    def clear(*args):
        """clear(self)"""
        return _moose.double_vector_clear(*args)

    def swap(*args):
        """swap(self, double_vector v)"""
        return _moose.double_vector_swap(*args)

    def get_allocator(*args):
        """get_allocator(self) -> allocator_type"""
        return _moose.double_vector_get_allocator(*args)

    def begin(*args):
        """
        begin(self) -> iterator
        begin(self) -> const_iterator
        """
        return _moose.double_vector_begin(*args)

    def end(*args):
        """
        end(self) -> iterator
        end(self) -> const_iterator
        """
        return _moose.double_vector_end(*args)

    def rbegin(*args):
        """
        rbegin(self) -> reverse_iterator
        rbegin(self) -> const_reverse_iterator
        """
        return _moose.double_vector_rbegin(*args)

    def rend(*args):
        """
        rend(self) -> reverse_iterator
        rend(self) -> const_reverse_iterator
        """
        return _moose.double_vector_rend(*args)

    def pop_back(*args):
        """pop_back(self)"""
        return _moose.double_vector_pop_back(*args)

    def erase(*args):
        """
        erase(self, iterator pos) -> iterator
        erase(self, iterator first, iterator last) -> iterator
        """
        return _moose.double_vector_erase(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> double_vector
        __init__(self, double_vector ?) -> double_vector
        __init__(self, size_type size) -> double_vector
        __init__(self, size_type size, value_type value) -> double_vector
        """
        this = _moose.new_double_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args):
        """push_back(self, value_type x)"""
        return _moose.double_vector_push_back(*args)

    def front(*args):
        """front(self) -> value_type"""
        return _moose.double_vector_front(*args)

    def back(*args):
        """back(self) -> value_type"""
        return _moose.double_vector_back(*args)

    def assign(*args):
        """assign(self, size_type n, value_type x)"""
        return _moose.double_vector_assign(*args)

    def resize(*args):
        """
        resize(self, size_type new_size)
        resize(self, size_type new_size, value_type x)
        """
        return _moose.double_vector_resize(*args)

    def insert(*args):
        """
        insert(self, iterator pos, value_type x) -> iterator
        insert(self, iterator pos, size_type n, value_type x)
        """
        return _moose.double_vector_insert(*args)

    def reserve(*args):
        """reserve(self, size_type n)"""
        return _moose.double_vector_reserve(*args)

    def capacity(*args):
        """capacity(self) -> size_type"""
        return _moose.double_vector_capacity(*args)

    __swig_destroy__ = _moose.delete_double_vector
    __del__ = lambda self : None;
double_vector_swigregister = _moose.double_vector_swigregister
double_vector_swigregister(double_vector)

class string_vector(object):
    """Proxy of C++ string_vector class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(*args):
        """iterator(self, PyObject PYTHON_SELF) -> PySwigIterator"""
        return _moose.string_vector_iterator(*args)

    def __iter__(self): return self.iterator()
    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _moose.string_vector___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> size_type"""
        return _moose.string_vector___len__(*args)

    def pop(*args):
        """pop(self) -> value_type"""
        return _moose.string_vector_pop(*args)

    def __getslice__(*args):
        """__getslice__(self, difference_type i, difference_type j) -> string_vector"""
        return _moose.string_vector___getslice__(*args)

    def __setslice__(*args):
        """__setslice__(self, difference_type i, difference_type j, string_vector v)"""
        return _moose.string_vector___setslice__(*args)

    def __delslice__(*args):
        """__delslice__(self, difference_type i, difference_type j)"""
        return _moose.string_vector___delslice__(*args)

    def __delitem__(*args):
        """__delitem__(self, difference_type i)"""
        return _moose.string_vector___delitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, difference_type i) -> value_type"""
        return _moose.string_vector___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, difference_type i, value_type x)"""
        return _moose.string_vector___setitem__(*args)

    def append(*args):
        """append(self, value_type x)"""
        return _moose.string_vector_append(*args)

    def empty(*args):
        """empty(self) -> bool"""
        return _moose.string_vector_empty(*args)

    def size(*args):
        """size(self) -> size_type"""
        return _moose.string_vector_size(*args)

    def clear(*args):
        """clear(self)"""
        return _moose.string_vector_clear(*args)

    def swap(*args):
        """swap(self, string_vector v)"""
        return _moose.string_vector_swap(*args)

    def get_allocator(*args):
        """get_allocator(self) -> allocator_type"""
        return _moose.string_vector_get_allocator(*args)

    def begin(*args):
        """
        begin(self) -> iterator
        begin(self) -> const_iterator
        """
        return _moose.string_vector_begin(*args)

    def end(*args):
        """
        end(self) -> iterator
        end(self) -> const_iterator
        """
        return _moose.string_vector_end(*args)

    def rbegin(*args):
        """
        rbegin(self) -> reverse_iterator
        rbegin(self) -> const_reverse_iterator
        """
        return _moose.string_vector_rbegin(*args)

    def rend(*args):
        """
        rend(self) -> reverse_iterator
        rend(self) -> const_reverse_iterator
        """
        return _moose.string_vector_rend(*args)

    def pop_back(*args):
        """pop_back(self)"""
        return _moose.string_vector_pop_back(*args)

    def erase(*args):
        """
        erase(self, iterator pos) -> iterator
        erase(self, iterator first, iterator last) -> iterator
        """
        return _moose.string_vector_erase(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> string_vector
        __init__(self, string_vector ?) -> string_vector
        __init__(self, size_type size) -> string_vector
        __init__(self, size_type size, value_type value) -> string_vector
        """
        this = _moose.new_string_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args):
        """push_back(self, value_type x)"""
        return _moose.string_vector_push_back(*args)

    def front(*args):
        """front(self) -> value_type"""
        return _moose.string_vector_front(*args)

    def back(*args):
        """back(self) -> value_type"""
        return _moose.string_vector_back(*args)

    def assign(*args):
        """assign(self, size_type n, value_type x)"""
        return _moose.string_vector_assign(*args)

    def resize(*args):
        """
        resize(self, size_type new_size)
        resize(self, size_type new_size, value_type x)
        """
        return _moose.string_vector_resize(*args)

    def insert(*args):
        """
        insert(self, iterator pos, value_type x) -> iterator
        insert(self, iterator pos, size_type n, value_type x)
        """
        return _moose.string_vector_insert(*args)

    def reserve(*args):
        """reserve(self, size_type n)"""
        return _moose.string_vector_reserve(*args)

    def capacity(*args):
        """capacity(self) -> size_type"""
        return _moose.string_vector_capacity(*args)

    __swig_destroy__ = _moose.delete_string_vector
    __del__ = lambda self : None;
string_vector_swigregister = _moose.string_vector_swigregister
string_vector_swigregister(string_vector)

class Id_vector(object):
    """Proxy of C++ Id_vector class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(*args):
        """iterator(self, PyObject PYTHON_SELF) -> PySwigIterator"""
        return _moose.Id_vector_iterator(*args)

    def __iter__(self): return self.iterator()
    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _moose.Id_vector___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> size_type"""
        return _moose.Id_vector___len__(*args)

    def pop(*args):
        """pop(self) -> value_type"""
        return _moose.Id_vector_pop(*args)

    def __getslice__(*args):
        """__getslice__(self, difference_type i, difference_type j) -> Id_vector"""
        return _moose.Id_vector___getslice__(*args)

    def __setslice__(*args):
        """__setslice__(self, difference_type i, difference_type j, Id_vector v)"""
        return _moose.Id_vector___setslice__(*args)

    def __delslice__(*args):
        """__delslice__(self, difference_type i, difference_type j)"""
        return _moose.Id_vector___delslice__(*args)

    def __delitem__(*args):
        """__delitem__(self, difference_type i)"""
        return _moose.Id_vector___delitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, difference_type i) -> value_type"""
        return _moose.Id_vector___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, difference_type i, value_type x)"""
        return _moose.Id_vector___setitem__(*args)

    def append(*args):
        """append(self, value_type x)"""
        return _moose.Id_vector_append(*args)

    def empty(*args):
        """empty(self) -> bool"""
        return _moose.Id_vector_empty(*args)

    def size(*args):
        """size(self) -> size_type"""
        return _moose.Id_vector_size(*args)

    def clear(*args):
        """clear(self)"""
        return _moose.Id_vector_clear(*args)

    def swap(*args):
        """swap(self, Id_vector v)"""
        return _moose.Id_vector_swap(*args)

    def get_allocator(*args):
        """get_allocator(self) -> allocator_type"""
        return _moose.Id_vector_get_allocator(*args)

    def begin(*args):
        """
        begin(self) -> iterator
        begin(self) -> const_iterator
        """
        return _moose.Id_vector_begin(*args)

    def end(*args):
        """
        end(self) -> iterator
        end(self) -> const_iterator
        """
        return _moose.Id_vector_end(*args)

    def rbegin(*args):
        """
        rbegin(self) -> reverse_iterator
        rbegin(self) -> const_reverse_iterator
        """
        return _moose.Id_vector_rbegin(*args)

    def rend(*args):
        """
        rend(self) -> reverse_iterator
        rend(self) -> const_reverse_iterator
        """
        return _moose.Id_vector_rend(*args)

    def pop_back(*args):
        """pop_back(self)"""
        return _moose.Id_vector_pop_back(*args)

    def erase(*args):
        """
        erase(self, iterator pos) -> iterator
        erase(self, iterator first, iterator last) -> iterator
        """
        return _moose.Id_vector_erase(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> Id_vector
        __init__(self, Id_vector ?) -> Id_vector
        __init__(self, size_type size) -> Id_vector
        __init__(self, size_type size, value_type value) -> Id_vector
        """
        this = _moose.new_Id_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args):
        """push_back(self, value_type x)"""
        return _moose.Id_vector_push_back(*args)

    def front(*args):
        """front(self) -> value_type"""
        return _moose.Id_vector_front(*args)

    def back(*args):
        """back(self) -> value_type"""
        return _moose.Id_vector_back(*args)

    def assign(*args):
        """assign(self, size_type n, value_type x)"""
        return _moose.Id_vector_assign(*args)

    def resize(*args):
        """
        resize(self, size_type new_size)
        resize(self, size_type new_size, value_type x)
        """
        return _moose.Id_vector_resize(*args)

    def insert(*args):
        """
        insert(self, iterator pos, value_type x) -> iterator
        insert(self, iterator pos, size_type n, value_type x)
        """
        return _moose.Id_vector_insert(*args)

    def reserve(*args):
        """reserve(self, size_type n)"""
        return _moose.Id_vector_reserve(*args)

    def capacity(*args):
        """capacity(self) -> size_type"""
        return _moose.Id_vector_capacity(*args)

    __swig_destroy__ = _moose.delete_Id_vector
    __del__ = lambda self : None;
Id_vector_swigregister = _moose.Id_vector_swigregister
Id_vector_swigregister(Id_vector)


def getParBuf(*args):
  """getParBuf(Conn c, unsigned int size) -> void"""
  return _moose.getParBuf(*args)

def getAsyncParBuf(*args):
  """getAsyncParBuf(Conn c, unsigned int size) -> void"""
  return _moose.getAsyncParBuf(*args)

def initNeutralCinfo(*args):
  """initNeutralCinfo() -> Cinfo"""
  return _moose.initNeutralCinfo(*args)

def separateString(*args):
  """separateString(string s, string_vector v, string separator)"""
  return _moose.separateString(*args)

def parseString(*args):
  """parseString(string s, string_vector v, char separators)"""
  return _moose.parseString(*args)
class Id(object):
    """Proxy of C++ Id class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def dumpState(*args):
        """dumpState(ostream stream)"""
        return _moose.Id_dumpState(*args)

    dumpState = staticmethod(dumpState)
    __swig_destroy__ = _moose.delete_Id
    __del__ = lambda self : None;
    def localId(*args):
        """
        localId(string path, string separator="/") -> Id
        localId(string path) -> Id
        """
        return _moose.Id_localId(*args)

    localId = staticmethod(localId)
    def childNode(*args):
        """childNode(Id parent) -> unsigned int"""
        return _moose.Id_childNode(*args)

    childNode = staticmethod(childNode)
    def childId(*args):
        """childId(Id parent) -> Id"""
        return _moose.Id_childId(*args)

    childId = staticmethod(childId)
    def scratchId(*args):
        """scratchId() -> Id"""
        return _moose.Id_scratchId(*args)

    scratchId = staticmethod(scratchId)
    def newId(*args):
        """newId() -> Id"""
        return _moose.Id_newId(*args)

    newId = staticmethod(newId)
    def initId(*args):
        """initId() -> Id"""
        return _moose.Id_initId(*args)

    initId = staticmethod(initId)
    def makeIdOnNode(*args):
        """makeIdOnNode(unsigned int childNode) -> Id"""
        return _moose.Id_makeIdOnNode(*args)

    makeIdOnNode = staticmethod(makeIdOnNode)
    def shellId(*args):
        """shellId() -> Id"""
        return _moose.Id_shellId(*args)

    shellId = staticmethod(shellId)
    def postId(*args):
        """postId(unsigned int node) -> Id"""
        return _moose.Id_postId(*args)

    postId = staticmethod(postId)
    def assignIndex(*args):
        """assignIndex(self, unsigned int index) -> Id"""
        return _moose.Id_assignIndex(*args)

    def newIdBlock(*args):
        """newIdBlock(unsigned int size, unsigned int node) -> unsigned int"""
        return _moose.Id_newIdBlock(*args)

    newIdBlock = staticmethod(newIdBlock)
    def generator(*args):
        """generator(unsigned int node) -> IdGenerator"""
        return _moose.Id_generator(*args)

    generator = staticmethod(generator)
    def path(*args):
        """
        path(self, string separator="/") -> string
        path(self) -> string
        """
        return _moose.Id_path(*args)

    def id(*args):
        """id(self) -> unsigned int"""
        return _moose.Id_id(*args)

    def index(*args):
        """index(self) -> unsigned int"""
        return _moose.Id_index(*args)

    def node(*args):
        """node(self) -> unsigned int"""
        return _moose.Id_node(*args)

    def isGlobal(*args):
        """isGlobal(self) -> bool"""
        return _moose.Id_isGlobal(*args)

    def setGlobal(*args):
        """setGlobal(self)"""
        return _moose.Id_setGlobal(*args)

    def setNode(*args):
        """setNode(self, unsigned int node)"""
        return _moose.Id_setNode(*args)

    def lastId(*args):
        """lastId() -> Id"""
        return _moose.Id_lastId(*args)

    lastId = staticmethod(lastId)
    def badId(*args):
        """badId() -> Id"""
        return _moose.Id_badId(*args)

    badId = staticmethod(badId)
    def str2Id(*args):
        """str2Id(string s) -> Id"""
        return _moose.Id_str2Id(*args)

    str2Id = staticmethod(str2Id)
    def id2str(*args):
        """id2str(Id id) -> string"""
        return _moose.Id_id2str(*args)

    id2str = staticmethod(id2str)
    def bad(*args):
        """bad(self) -> bool"""
        return _moose.Id_bad(*args)

    def good(*args):
        """good(self) -> bool"""
        return _moose.Id_good(*args)

    def zero(*args):
        """zero(self) -> bool"""
        return _moose.Id_zero(*args)

    def outOfRange(*args):
        """outOfRange(self) -> bool"""
        return _moose.Id_outOfRange(*args)

    def isProxy(*args):
        """isProxy(self) -> bool"""
        return _moose.Id_isProxy(*args)

    def __eq__(*args):
        """__eq__(self, Id other) -> bool"""
        return _moose.Id___eq__(*args)

    def __ne__(*args):
        """__ne__(self, Id other) -> bool"""
        return _moose.Id___ne__(*args)

    def __lt__(*args):
        """__lt__(self, Id other) -> bool"""
        return _moose.Id___lt__(*args)

    def setElement(*args):
        """setElement(self, Element e) -> bool"""
        return _moose.Id_setElement(*args)

    def __init__(self, *args): 
        """
        __init__(self) -> Id
        __init__(self, Nid nid) -> Id
        __init__(self, string path, string separator="/") -> Id
        __init__(self, string path) -> Id
        __init__(self, unsigned int i, unsigned int index=0) -> Id
        __init__(self, unsigned int i) -> Id
        """
        this = _moose.new_Id(*args)
        try: self.this.append(this)
        except: self.this = this
Id_swigregister = _moose.Id_swigregister
Id_swigregister(Id)

def Id_dumpState(*args):
  """Id_dumpState(ostream stream)"""
  return _moose.Id_dumpState(*args)

def Id_localId(*args):
  """
    localId(string path, string separator="/") -> Id
    Id_localId(string path) -> Id
    """
  return _moose.Id_localId(*args)

def Id_childNode(*args):
  """Id_childNode(Id parent) -> unsigned int"""
  return _moose.Id_childNode(*args)

def Id_childId(*args):
  """Id_childId(Id parent) -> Id"""
  return _moose.Id_childId(*args)

def Id_scratchId(*args):
  """Id_scratchId() -> Id"""
  return _moose.Id_scratchId(*args)

def Id_newId(*args):
  """Id_newId() -> Id"""
  return _moose.Id_newId(*args)

def Id_initId(*args):
  """Id_initId() -> Id"""
  return _moose.Id_initId(*args)

def Id_makeIdOnNode(*args):
  """Id_makeIdOnNode(unsigned int childNode) -> Id"""
  return _moose.Id_makeIdOnNode(*args)

def Id_shellId(*args):
  """Id_shellId() -> Id"""
  return _moose.Id_shellId(*args)

def Id_postId(*args):
  """Id_postId(unsigned int node) -> Id"""
  return _moose.Id_postId(*args)

def Id_newIdBlock(*args):
  """Id_newIdBlock(unsigned int size, unsigned int node) -> unsigned int"""
  return _moose.Id_newIdBlock(*args)

def Id_generator(*args):
  """Id_generator(unsigned int node) -> IdGenerator"""
  return _moose.Id_generator(*args)

def Id_lastId(*args):
  """Id_lastId() -> Id"""
  return _moose.Id_lastId(*args)

def Id_badId(*args):
  """Id_badId() -> Id"""
  return _moose.Id_badId(*args)

def Id_str2Id(*args):
  """Id_str2Id(string s) -> Id"""
  return _moose.Id_str2Id(*args)

def Id_id2str(*args):
  """Id_id2str(Id id) -> string"""
  return _moose.Id_id2str(*args)
cvar = _moose.cvar
Id.AnyIndex = _moose.cvar.Id_AnyIndex
Id.BadIndex = _moose.cvar.Id_BadIndex
Id.BadNode = _moose.cvar.Id_BadNode
Id.UnknownNode = _moose.cvar.Id_UnknownNode
Id.GlobalNode = _moose.cvar.Id_GlobalNode

class Nid(Id):
    """Proxy of C++ Nid class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> Nid
        __init__(self, Id id) -> Nid
        __init__(self, Id id, unsigned int node) -> Nid
        """
        this = _moose.new_Nid(*args)
        try: self.this.append(this)
        except: self.this = this
    def node(*args):
        """node(self) -> unsigned int"""
        return _moose.Nid_node(*args)

    def setNode(*args):
        """setNode(self, unsigned int node)"""
        return _moose.Nid_setNode(*args)

    __swig_destroy__ = _moose.delete_Nid
    __del__ = lambda self : None;
Nid_swigregister = _moose.Nid_swigregister
Nid_swigregister(Nid)

BUF_SIZE = _moose.BUF_SIZE
class Property(object):
    """Proxy of C++ Property class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def initialize(*args):
        """initialize(string fileName, int format)"""
        return _moose.Property_initialize(*args)

    initialize = staticmethod(initialize)
    def initDefaults(*args):
        """initDefaults()"""
        return _moose.Property_initDefaults(*args)

    initDefaults = staticmethod(initDefaults)
    def getProperty(*args):
        """getProperty(string key) -> string"""
        return _moose.Property_getProperty(*args)

    getProperty = staticmethod(getProperty)
    def setProperty(*args):
        """setProperty(string key, string value)"""
        return _moose.Property_setProperty(*args)

    setProperty = staticmethod(setProperty)
    def readProperties(*args):
        """readProperties(string fileName, int format) -> int"""
        return _moose.Property_readProperties(*args)

    readProperties = staticmethod(readProperties)
    def readEnvironment(*args):
        """readEnvironment()"""
        return _moose.Property_readEnvironment(*args)

    readEnvironment = staticmethod(readEnvironment)
    def getKeys(*args):
        """getKeys() -> string_vector"""
        return _moose.Property_getKeys(*args)

    getKeys = staticmethod(getKeys)
    def addSimPath(*args):
        """addSimPath(string path)"""
        return _moose.Property_addSimPath(*args)

    addSimPath = staticmethod(addSimPath)
    def setSimPath(*args):
        """setSimPath(string paths)"""
        return _moose.Property_setSimPath(*args)

    setSimPath = staticmethod(setSimPath)
    def getSimPath(*args):
        """getSimPath() -> string"""
        return _moose.Property_getSimPath(*args)

    getSimPath = staticmethod(getSimPath)
    __swig_destroy__ = _moose.delete_Property
    __del__ = lambda self : None;
Property_swigregister = _moose.Property_swigregister
Property_swigregister(Property)
Property.SIMPATH = _moose.cvar.Property_SIMPATH
Property.SIMNOTES = _moose.cvar.Property_SIMNOTES
Property.DOCPATH = _moose.cvar.Property_DOCPATH
Property.AUTOSCHEDULE = _moose.cvar.Property_AUTOSCHEDULE
Property.CREATESOLVER = _moose.cvar.Property_CREATESOLVER
Property.HOME = _moose.cvar.Property_HOME
Property.XML_FORMAT = _moose.cvar.Property_XML_FORMAT
Property.PROP_FORMAT = _moose.cvar.Property_PROP_FORMAT

def Property_initialize(*args):
  """Property_initialize(string fileName, int format)"""
  return _moose.Property_initialize(*args)

def Property_initDefaults(*args):
  """Property_initDefaults()"""
  return _moose.Property_initDefaults(*args)

def Property_getProperty(*args):
  """Property_getProperty(string key) -> string"""
  return _moose.Property_getProperty(*args)

def Property_setProperty(*args):
  """Property_setProperty(string key, string value)"""
  return _moose.Property_setProperty(*args)

def Property_readProperties(*args):
  """Property_readProperties(string fileName, int format) -> int"""
  return _moose.Property_readProperties(*args)

def Property_readEnvironment(*args):
  """Property_readEnvironment()"""
  return _moose.Property_readEnvironment(*args)

def Property_getKeys(*args):
  """Property_getKeys() -> string_vector"""
  return _moose.Property_getKeys(*args)

def Property_addSimPath(*args):
  """Property_addSimPath(string path)"""
  return _moose.Property_addSimPath(*args)

def Property_setSimPath(*args):
  """Property_setSimPath(string paths)"""
  return _moose.Property_setSimPath(*args)

def Property_getSimPath(*args):
  """Property_getSimPath() -> string"""
  return _moose.Property_getSimPath(*args)

class PathUtility(object):
    """Proxy of C++ PathUtility class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, string paths) -> PathUtility"""
        this = _moose.new_PathUtility(*args)
        try: self.this.append(this)
        except: self.this = this
    def addPath(*args):
        """addPath(self, string paths)"""
        return _moose.PathUtility_addPath(*args)

    def getPath(*args):
        """getPath(self, int index) -> string"""
        return _moose.PathUtility_getPath(*args)

    def getAllPaths(*args):
        """getAllPaths(self) -> string"""
        return _moose.PathUtility_getAllPaths(*args)

    def makeFilePath(*args):
        """makeFilePath(self, string fileName, int index) -> string"""
        return _moose.PathUtility_makeFilePath(*args)

    def size(*args):
        """size(self) -> size_t"""
        return _moose.PathUtility_size(*args)

    __swig_destroy__ = _moose.delete_PathUtility
    __del__ = lambda self : None;
PathUtility_swigregister = _moose.PathUtility_swigregister
PathUtility_swigregister(PathUtility)
PathUtility.PATH_SEPARATOR = _moose.cvar.PathUtility_PATH_SEPARATOR
PathUtility.DIR_SEPARATOR = _moose.cvar.PathUtility_DIR_SEPARATOR

ALL = _moose.ALL
VALUE = _moose.VALUE
LOOKUP = _moose.LOOKUP
SOURCE = _moose.SOURCE
DEST = _moose.DEST
SHARED = _moose.SHARED
SOLVE = _moose.SOLVE
THIS = _moose.THIS
GLOBAL = _moose.GLOBAL
DEL = _moose.DEL
class PyMooseContext(object):
    """Proxy of C++ PyMooseContext class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self) -> PyMooseContext"""
        this = _moose.new_PyMooseContext(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_PyMooseContext
    __del__ = lambda self : None;
    def getCwe(*args):
        """getCwe(self) -> Id"""
        return _moose.PyMooseContext_getCwe(*args)

    def setCwe(*args):
        """
        setCwe(self, Id elementId)
        setCwe(self, string path)
        """
        return _moose.PyMooseContext_setCwe(*args)

    def getShell(*args):
        """getShell(self) -> Id"""
        return _moose.PyMooseContext_getShell(*args)

    def id(*args):
        """id(self) -> Id"""
        return _moose.PyMooseContext_id(*args)

    def create(*args):
        """
        create(self, string type, string name, Id parent=Id::badId()) -> Id
        create(self, string type, string name) -> Id
        """
        return _moose.PyMooseContext_create(*args)

    def destroy(*args):
        """destroy(self, Id victim) -> bool"""
        return _moose.PyMooseContext_destroy(*args)

    def end(*args):
        """end(self)"""
        return _moose.PyMooseContext_end(*args)

    def recvCwe(*args):
        """recvCwe(Conn c, Id i)"""
        return _moose.PyMooseContext_recvCwe(*args)

    recvCwe = staticmethod(recvCwe)
    def recvElist(*args):
        """recvElist(Conn c, Id_vector elist)"""
        return _moose.PyMooseContext_recvElist(*args)

    recvElist = staticmethod(recvElist)
    def recvCreate(*args):
        """recvCreate(Conn c, Id i)"""
        return _moose.PyMooseContext_recvCreate(*args)

    recvCreate = staticmethod(recvCreate)
    def recvField(*args):
        """recvField(Conn c, string value)"""
        return _moose.PyMooseContext_recvField(*args)

    recvField = staticmethod(recvField)
    def recvWildcardList(*args):
        """recvWildcardList(Conn c, Id_vector value)"""
        return _moose.PyMooseContext_recvWildcardList(*args)

    recvWildcardList = staticmethod(recvWildcardList)
    def recvClocks(*args):
        """recvClocks(Conn c, double_vector dbls)"""
        return _moose.PyMooseContext_recvClocks(*args)

    recvClocks = staticmethod(recvClocks)
    def recvMessageList(*args):
        """recvMessageList(Conn c, Id_vector elist, string s)"""
        return _moose.PyMooseContext_recvMessageList(*args)

    recvMessageList = staticmethod(recvMessageList)
    def createPyMooseContext(*args):
        """createPyMooseContext(string contextName, string shellName) -> PyMooseContext"""
        return _moose.PyMooseContext_createPyMooseContext(*args)

    createPyMooseContext = staticmethod(createPyMooseContext)
    def destroyPyMooseContext(*args):
        """destroyPyMooseContext(PyMooseContext context)"""
        return _moose.PyMooseContext_destroyPyMooseContext(*args)

    destroyPyMooseContext = staticmethod(destroyPyMooseContext)
    def loadG(*args):
        """loadG(self, string script)"""
        return _moose.PyMooseContext_loadG(*args)

    def runG(*args):
        """runG(self, string statement)"""
        return _moose.PyMooseContext_runG(*args)

    def getField(*args):
        """getField(self, Id ?, string ?) -> string"""
        return _moose.PyMooseContext_getField(*args)

    def setField(*args):
        """setField(self, Id ?, string ?, string ?)"""
        return _moose.PyMooseContext_setField(*args)

    def getMessageList(*args):
        """
        getMessageList(self, Id obj, string field, bool incoming) -> string_vector
        getMessageList(self, Id obj, bool incoming) -> string_vector
        """
        return _moose.PyMooseContext_getMessageList(*args)

    def getParent(*args):
        """getParent(self, Id id) -> Id"""
        return _moose.PyMooseContext_getParent(*args)

    def getPath(*args):
        """getPath(self, Id id) -> string"""
        return _moose.PyMooseContext_getPath(*args)

    def getName(*args):
        """getName(self, Id id) -> string"""
        return _moose.PyMooseContext_getName(*args)

    def getChildren(*args):
        """
        getChildren(self, Id id) -> Id_vector
        getChildren(self, string path) -> Id_vector
        """
        return _moose.PyMooseContext_getChildren(*args)

    def pathToId(*args):
        """
        pathToId(self, string path, bool echo=True) -> Id
        pathToId(self, string path) -> Id
        """
        return _moose.PyMooseContext_pathToId(*args)

    def srandom(*args):
        """srandom(long seed)"""
        return _moose.PyMooseContext_srandom(*args)

    srandom = staticmethod(srandom)
    def step(*args):
        """
        step(self, double runTime)
        step(self, long multiple)
        step(self)
        """
        return _moose.PyMooseContext_step(*args)

    def reset(*args):
        """reset(self)"""
        return _moose.PyMooseContext_reset(*args)

    def stop(*args):
        """stop(self)"""
        return _moose.PyMooseContext_stop(*args)

    def setClock(*args):
        """
        setClock(self, int clockNo, double dt, int stage=0)
        setClock(self, int clockNo, double dt)
        """
        return _moose.PyMooseContext_setClock(*args)

    def getClocks(*args):
        """getClocks(self) -> double_vector"""
        return _moose.PyMooseContext_getClocks(*args)

    def useClock(*args):
        """
        useClock(self, string tickName, string path, string func="process")
        useClock(self, string tickName, string path)
        useClock(self, int tickNo, string path, string func="process")
        useClock(self, int tickNo, string path)
        """
        return _moose.PyMooseContext_useClock(*args)

    def addTask(*args):
        """addTask(self, string arg)"""
        return _moose.PyMooseContext_addTask(*args)

    def do_deep_copy(*args):
        """do_deep_copy(self, Id object, Id dest, string new_name)"""
        return _moose.PyMooseContext_do_deep_copy(*args)

    def copy(*args):
        """copy(self, Id src, Id dest_parent, string new_name)"""
        return _moose.PyMooseContext_copy(*args)

    def deepCopy(*args):
        """deepCopy(self, Id object, Id dest, string new_name) -> Id"""
        return _moose.PyMooseContext_deepCopy(*args)

    def move(*args):
        """move(self, Id object, Id dest, string new_name)"""
        return _moose.PyMooseContext_move(*args)

    def connect(*args):
        """connect(self, Id src, string srcField, Id dest, string destField) -> bool"""
        return _moose.PyMooseContext_connect(*args)

    def tabFill(*args):
        """tabFill(self, Id table, int xdivs, int mode)"""
        return _moose.PyMooseContext_tabFill(*args)

    def setupAlpha(*args):
        """
        setupAlpha(self, string channel, string gate, double_vector parms)
        setupAlpha(self, string channel, string gate, double AA, double AB, 
            double AC, double AD, double AF, double BA, double BB, 
            double BC, double BD, double BF, double size, 
            double min, double max)
        setupAlpha(self, Id gateId, double_vector parms)
        """
        return _moose.PyMooseContext_setupAlpha(*args)

    def setupTau(*args):
        """
        setupTau(self, string channel, string gate, double_vector parms)
        setupTau(self, string channel, string gate, double AA, double AB, 
            double AC, double AD, double AF, double BA, double BB, 
            double BC, double BD, double BF, double size, 
            double min, double max)
        setupTau(self, Id gateId, double_vector parms)
        """
        return _moose.PyMooseContext_setupTau(*args)

    def tweakAlpha(*args):
        """
        tweakAlpha(self, string channel, string gate)
        tweakAlpha(self, Id gateId)
        """
        return _moose.PyMooseContext_tweakAlpha(*args)

    def tweakTau(*args):
        """
        tweakTau(self, string channel, string gate)
        tweakTau(self, Id gateId)
        """
        return _moose.PyMooseContext_tweakTau(*args)

    def readCell(*args):
        """
        readCell(self, string filename, string cellpath, double cm, double rm, 
            double ra, double erestAct, double eleak)
        readCell(self, string filename, string cellpath, double_vector params)
        readCell(self, string fileName, string cellPath)
        """
        return _moose.PyMooseContext_readCell(*args)

    def readSBML(*args):
        """readSBML(self, string fileName, string modelPath)"""
        return _moose.PyMooseContext_readSBML(*args)

    def getCurrentTime(*args):
        """getCurrentTime(self) -> double"""
        return _moose.PyMooseContext_getCurrentTime(*args)

    def exists(*args):
        """
        exists(self, Id id) -> bool
        exists(self, string path) -> bool
        """
        return _moose.PyMooseContext_exists(*args)

    def createMap(*args):
        """
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0, double xo=0.0, 
            double yo=0.0, bool isObject=True)
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0, double xo=0.0, 
            double yo=0.0)
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0, double xo=0.0)
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0)
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny, 
            double dx=1.0)
        createMap(self, string src, string dest, unsigned int nx, unsigned int ny)
        createMap(self, Id src, Id dest, string name, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0, double xo=0.0, 
            double yo=0.0)
        createMap(self, Id src, Id dest, string name, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0, double xo=0.0)
        createMap(self, Id src, Id dest, string name, unsigned int nx, unsigned int ny, 
            double dx=1.0, double dy=1.0)
        createMap(self, Id src, Id dest, string name, unsigned int nx, unsigned int ny, 
            double dx=1.0)
        createMap(self, Id src, Id dest, string name, unsigned int nx, unsigned int ny)
        createMap(self, Id src, Id dest, string name, double_vector param)
        """
        return _moose.PyMooseContext_createMap(*args)

    def planarConnect(*args):
        """
        planarConnect(self, string src, string dst, double probability=1.0)
        planarConnect(self, string src, string dst)
        """
        return _moose.PyMooseContext_planarConnect(*args)

    def plannarDelay(*args):
        """plannarDelay(self, string src, double delay)"""
        return _moose.PyMooseContext_plannarDelay(*args)

    def planarWeight(*args):
        """planarWeight(self, string src, double weight)"""
        return _moose.PyMooseContext_planarWeight(*args)

    def className(*args):
        """className(self, Id objId) -> string"""
        return _moose.PyMooseContext_className(*args)

    def doc(*args):
        """doc(self, string className) -> string"""
        return _moose.PyMooseContext_doc(*args)

    def getNeighbours(*args):
        """
        getNeighbours(self, Id object, string fieldName="*") -> Id_vector
        getNeighbours(self, Id object) -> Id_vector
        """
        return _moose.PyMooseContext_getNeighbours(*args)

    def getFieldList(*args):
        """
        getFieldList(self, Id id, FieldType ftype=ALL) -> string_vector
        getFieldList(self, Id id) -> string_vector
        """
        return _moose.PyMooseContext_getFieldList(*args)

    parallel = property(_moose.PyMooseContext_parallel_get, _moose.PyMooseContext_parallel_set)
PyMooseContext_swigregister = _moose.PyMooseContext_swigregister
PyMooseContext_swigregister(PyMooseContext)

def PyMooseContext_recvCwe(*args):
  """PyMooseContext_recvCwe(Conn c, Id i)"""
  return _moose.PyMooseContext_recvCwe(*args)

def PyMooseContext_recvElist(*args):
  """PyMooseContext_recvElist(Conn c, Id_vector elist)"""
  return _moose.PyMooseContext_recvElist(*args)

def PyMooseContext_recvCreate(*args):
  """PyMooseContext_recvCreate(Conn c, Id i)"""
  return _moose.PyMooseContext_recvCreate(*args)

def PyMooseContext_recvField(*args):
  """PyMooseContext_recvField(Conn c, string value)"""
  return _moose.PyMooseContext_recvField(*args)

def PyMooseContext_recvWildcardList(*args):
  """PyMooseContext_recvWildcardList(Conn c, Id_vector value)"""
  return _moose.PyMooseContext_recvWildcardList(*args)

def PyMooseContext_recvClocks(*args):
  """PyMooseContext_recvClocks(Conn c, double_vector dbls)"""
  return _moose.PyMooseContext_recvClocks(*args)

def PyMooseContext_recvMessageList(*args):
  """PyMooseContext_recvMessageList(Conn c, Id_vector elist, string s)"""
  return _moose.PyMooseContext_recvMessageList(*args)

def PyMooseContext_createPyMooseContext(*args):
  """PyMooseContext_createPyMooseContext(string contextName, string shellName) -> PyMooseContext"""
  return _moose.PyMooseContext_createPyMooseContext(*args)

def PyMooseContext_destroyPyMooseContext(*args):
  """PyMooseContext_destroyPyMooseContext(PyMooseContext context)"""
  return _moose.PyMooseContext_destroyPyMooseContext(*args)

def PyMooseContext_srandom(*args):
  """PyMooseContext_srandom(long seed)"""
  return _moose.PyMooseContext_srandom(*args)
PyMooseContext.separator = _moose.cvar.PyMooseContext_separator

class PyMooseBase(object):
    """Proxy of C++ PyMooseBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _moose.delete_PyMooseBase
    __del__ = lambda self : None;
    def destroy(*args):
        """destroy(Id id) -> bool"""
        return _moose.PyMooseBase_destroy(*args)

    destroy = staticmethod(destroy)
    def endSimulation(*args):
        """endSimulation()"""
        return _moose.PyMooseBase_endSimulation(*args)

    endSimulation = staticmethod(endSimulation)
    def getType(*args):
        """getType(self) -> string"""
        return _moose.PyMooseBase_getType(*args)

    def getSeparator(*args):
        """getSeparator(self) -> string"""
        return _moose.PyMooseBase_getSeparator(*args)

    def getContext(*args):
        """getContext() -> PyMooseContext"""
        return _moose.PyMooseBase_getContext(*args)

    getContext = staticmethod(getContext)
    def getField(*args):
        """getField(self, string name) -> string"""
        return _moose.PyMooseBase_getField(*args)

    def setField(*args):
        """setField(self, string name, string value)"""
        return _moose.PyMooseBase_setField(*args)

    def getFieldList(*args):
        """
        getFieldList(self) -> string_vector
        getFieldList(self, FieldType ftype=ALL) -> string_vector
        getFieldList(self) -> string_vector
        """
        return _moose.PyMooseBase_getFieldList(*args)

    def neighbours(*args):
        """
        neighbours(self, string msgName="*") -> Id_vector
        neighbours(self) -> Id_vector
        """
        return _moose.PyMooseBase_neighbours(*args)

    def __get_className(*args):
        """__get_className(self) -> string"""
        return _moose.PyMooseBase___get_className(*args)

    def children(*args):
        """children(self) -> Id_vector"""
        return _moose.PyMooseBase_children(*args)

    def __get_parent(*args):
        """__get_parent(self) -> Id"""
        return _moose.PyMooseBase___get_parent(*args)

    def __get_path(*args):
        """__get_path(self) -> string"""
        return _moose.PyMooseBase___get_path(*args)

    def __get_id(*args):
        """__get_id(self) -> Id"""
        return _moose.PyMooseBase___get_id(*args)

    def __get_name(*args):
        """__get_name(self) -> string"""
        return _moose.PyMooseBase___get_name(*args)

    def useClock(*args):
        """
        useClock(self, int clockNo, string func="process")
        useClock(self, int clockNo)
        useClock(self, Id clock, string func="process")
        useClock(self, Id clock)
        """
        return _moose.PyMooseBase_useClock(*args)

    def connect(*args):
        """
        connect(self, string field, PyMooseBase dest, string destField) -> bool
        connect(self, string field, Id dest, string destField) -> bool
        """
        return _moose.PyMooseBase_connect(*args)

    def getMessageList(*args):
        """getMessageList(self, string field, bool isIncoming) -> string_vector"""
        return _moose.PyMooseBase_getMessageList(*args)

    def inMessages(*args):
        """inMessages(self) -> string_vector"""
        return _moose.PyMooseBase_inMessages(*args)

    def outMessages(*args):
        """outMessages(self) -> string_vector"""
        return _moose.PyMooseBase_outMessages(*args)

    def exists(*args):
        """
        exists(Id id) -> bool
        exists(string path) -> bool
        """
        return _moose.PyMooseBase_exists(*args)

    exists = staticmethod(exists)
    def le(*args):
        """le() -> Id_vector"""
        return _moose.PyMooseBase_le(*args)

    le = staticmethod(le)
    def pwe(*args):
        """pwe() -> Id"""
        return _moose.PyMooseBase_pwe(*args)

    pwe = staticmethod(pwe)
    def ce(*args):
        """
        ce(Id newElement) -> Id
        ce(string path) -> Id
        """
        return _moose.PyMooseBase_ce(*args)

    ce = staticmethod(ce)
    def pathToId(*args):
        """
        pathToId(string path, bool echo=True) -> Id
        pathToId(string path) -> Id
        """
        return _moose.PyMooseBase_pathToId(*args)

    pathToId = staticmethod(pathToId)
    def idToPath(*args):
        """idToPath(Id id) -> string"""
        return _moose.PyMooseBase_idToPath(*args)

    idToPath = staticmethod(idToPath)
    def getParent(*args):
        """getParent(Id id) -> Id"""
        return _moose.PyMooseBase_getParent(*args)

    getParent = staticmethod(getParent)
    def getChildren(*args):
        """getChildren(Id id) -> Id_vector"""
        return _moose.PyMooseBase_getChildren(*args)

    getChildren = staticmethod(getChildren)
    def initSimulation(*args):
        """initSimulation()"""
        return _moose.PyMooseBase_initSimulation(*args)

    initSimulation = staticmethod(initSimulation)
    id = property(_moose.PyMooseBase_id_get, _moose.PyMooseBase_id_set)
    parent = property(_moose.PyMooseBase_parent_get, _moose.PyMooseBase_parent_set)
    className = property(_moose.PyMooseBase_className_get)
    name = property(_moose.PyMooseBase_name_get)
    path = property(_moose.PyMooseBase_path_get)
PyMooseBase_swigregister = _moose.PyMooseBase_swigregister
PyMooseBase_swigregister(PyMooseBase)

def PyMooseBase_destroy(*args):
  """PyMooseBase_destroy(Id id) -> bool"""
  return _moose.PyMooseBase_destroy(*args)

def PyMooseBase_endSimulation(*args):
  """PyMooseBase_endSimulation()"""
  return _moose.PyMooseBase_endSimulation(*args)

def PyMooseBase_getContext(*args):
  """PyMooseBase_getContext() -> PyMooseContext"""
  return _moose.PyMooseBase_getContext(*args)

def PyMooseBase_exists(*args):
  """
    exists(Id id) -> bool
    PyMooseBase_exists(string path) -> bool
    """
  return _moose.PyMooseBase_exists(*args)

def PyMooseBase_le(*args):
  """PyMooseBase_le() -> Id_vector"""
  return _moose.PyMooseBase_le(*args)

def PyMooseBase_pwe(*args):
  """PyMooseBase_pwe() -> Id"""
  return _moose.PyMooseBase_pwe(*args)

def PyMooseBase_ce(*args):
  """
    ce(Id newElement) -> Id
    PyMooseBase_ce(string path) -> Id
    """
  return _moose.PyMooseBase_ce(*args)

def PyMooseBase_pathToId(*args):
  """
    pathToId(string path, bool echo=True) -> Id
    PyMooseBase_pathToId(string path) -> Id
    """
  return _moose.PyMooseBase_pathToId(*args)

def PyMooseBase_idToPath(*args):
  """PyMooseBase_idToPath(Id id) -> string"""
  return _moose.PyMooseBase_idToPath(*args)

def PyMooseBase_getParent(*args):
  """PyMooseBase_getParent(Id id) -> Id"""
  return _moose.PyMooseBase_getParent(*args)

def PyMooseBase_getChildren(*args):
  """PyMooseBase_getChildren(Id id) -> Id_vector"""
  return _moose.PyMooseBase_getChildren(*args)

def PyMooseBase_initSimulation(*args):
  """PyMooseBase_initSimulation()"""
  return _moose.PyMooseBase_initSimulation(*args)

from inspect import isclass

def doc(cls):
    """Return documentation string from MOOSE"""
    if isclass(cls):
        return PyMooseBase.getContext().doc(cls.__name__)
    elif isinstance(cls, PyMooseBase):
        return PyMooseBase.getContext().doc(cls.className)
    elif isinstance(cls, str):
        return PyMooseBase.getContext().doc(cls)		

class Neutral(PyMooseBase):
    """Proxy of C++ Neutral class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Neutral
        __init__(self, string path) -> Neutral
        __init__(self, string name, Id parentId) -> Neutral
        __init__(self, string name, PyMooseBase parent) -> Neutral
        __init__(self, string path, string fileName) -> Neutral
        __init__(self, Neutral src, string name, PyMooseBase parent) -> Neutral
        __init__(self, Neutral src, string name, Id parent) -> Neutral
        __init__(self, Id src, string name, Id parent) -> Neutral
        __init__(self, Neutral src, string path) -> Neutral
        """
        this = _moose.new_Neutral(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Neutral
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Neutral_getType(*args)

    def __get_childSrc(*args):
        """__get_childSrc(self) -> int"""
        return _moose.Neutral___get_childSrc(*args)

    def __set_childSrc(*args):
        """__set_childSrc(self, int childSrc)"""
        return _moose.Neutral___set_childSrc(*args)

    def __get_child(*args):
        """__get_child(self) -> int"""
        return _moose.Neutral___get_child(*args)

    def __set_child(*args):
        """__set_child(self, int child)"""
        return _moose.Neutral___set_child(*args)

    child = property(_moose.Neutral_child_get, _moose.Neutral_child_set)
Neutral_swigregister = _moose.Neutral_swigregister
Neutral_swigregister(Neutral)
Neutral.className_ = _moose.cvar.Neutral_className_

class Class(PyMooseBase):
    """Proxy of C++ Class class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Class
        __init__(self, string path, string name) -> Class
        __init__(self, string name, Id parentId) -> Class
        __init__(self, string name, PyMooseBase parent) -> Class
        __init__(self, Class src, string name, PyMooseBase parent) -> Class
        __init__(self, Class src, string name, Id parent) -> Class
        __init__(self, Id src, string name, Id parent) -> Class
        __init__(self, Class src, string path) -> Class
        """
        this = _moose.new_Class(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Class
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Class_getType(*args)

    def __set_name(*args):
        """__set_name(self, string name)"""
        return _moose.Class___set_name(*args)

    def __get_author(*args):
        """__get_author(self) -> string"""
        return _moose.Class___get_author(*args)

    def __get_description(*args):
        """__get_description(self) -> string"""
        return _moose.Class___get_description(*args)

    def __get_tick(*args):
        """__get_tick(self) -> unsigned int"""
        return _moose.Class___get_tick(*args)

    def __set_tick(*args):
        """__set_tick(self, unsigned int ?)"""
        return _moose.Class___set_tick(*args)

    def __get_stage(*args):
        """__get_stage(self) -> unsigned int"""
        return _moose.Class___get_stage(*args)

    def __set_stage(*args):
        """__set_stage(self, unsigned int ?)"""
        return _moose.Class___set_stage(*args)

    def __get_clock(*args):
        """__get_clock(self) -> string"""
        return _moose.Class___get_clock(*args)

    def setClock(*args):
        """setClock(self, string function, string clock)"""
        return _moose.Class_setClock(*args)

    name = property(_moose.Class_name_get, _moose.Class_name_set)
    author = property(_moose.Class_author_get, _moose.Class_author_set)
    description = property(_moose.Class_description_get, _moose.Class_description_set)
    tick = property(_moose.Class_tick_get, _moose.Class_tick_set)
    stage = property(_moose.Class_stage_get, _moose.Class_stage_set)
Class_swigregister = _moose.Class_swigregister
Class_swigregister(Class)
Class.className_ = _moose.cvar.Class_className_

class Cell(PyMooseBase):
    """Proxy of C++ Cell class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Cell
        __init__(self, string path) -> Cell
        __init__(self, string name, Id parentId) -> Cell
        __init__(self, string name, PyMooseBase parent) -> Cell
        __init__(self, Cell src, string name, PyMooseBase parent) -> Cell
        __init__(self, Cell src, string name, Id parent) -> Cell
        __init__(self, Id src, string name, Id parent) -> Cell
        __init__(self, Cell src, string path) -> Cell
        """
        this = _moose.new_Cell(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Cell
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Cell_getType(*args)

    def __set_method(*args):
        """__set_method(self, string method)"""
        return _moose.Cell___set_method(*args)

    def __get_method(*args):
        """__get_method(self) -> string"""
        return _moose.Cell___get_method(*args)

    def __get_variableDt(*args):
        """__get_variableDt(self) -> bool"""
        return _moose.Cell___get_variableDt(*args)

    def __get_implicit(*args):
        """__get_implicit(self) -> bool"""
        return _moose.Cell___get_implicit(*args)

    def __get_description(*args):
        """__get_description(self) -> string"""
        return _moose.Cell___get_description(*args)

    method = property(_moose.Cell_method_get, _moose.Cell_method_set)
    variableDt = property(_moose.Cell_variableDt_get, _moose.Cell_variableDt_set)
    implicit = property(_moose.Cell_implicit_get, _moose.Cell_implicit_set)
    description = property(_moose.Cell_description_get, _moose.Cell_description_set)
Cell_swigregister = _moose.Cell_swigregister
Cell_swigregister(Cell)
Cell.className_ = _moose.cvar.Cell_className_

class Tick(PyMooseBase):
    """Proxy of C++ Tick class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Tick
        __init__(self, string path) -> Tick
        __init__(self, string name, Id parentId) -> Tick
        __init__(self, string name, PyMooseBase parent) -> Tick
        __init__(self, Tick src, string name, PyMooseBase parent) -> Tick
        __init__(self, Tick src, string name, Id parent) -> Tick
        __init__(self, Id src, string name, Id parent) -> Tick
        __init__(self, Tick src, string path) -> Tick
        """
        this = _moose.new_Tick(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Tick
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Tick_getType(*args)

    def __get_dt(*args):
        """__get_dt(self) -> double"""
        return _moose.Tick___get_dt(*args)

    def __set_dt(*args):
        """__set_dt(self, double dt)"""
        return _moose.Tick___set_dt(*args)

    def __get_stage(*args):
        """__get_stage(self) -> int"""
        return _moose.Tick___get_stage(*args)

    def __set_stage(*args):
        """__set_stage(self, int stage)"""
        return _moose.Tick___set_stage(*args)

    def __get_ordinal(*args):
        """__get_ordinal(self) -> int"""
        return _moose.Tick___get_ordinal(*args)

    def __set_ordinal(*args):
        """__set_ordinal(self, int ordinal)"""
        return _moose.Tick___set_ordinal(*args)

    def __get_nextTime(*args):
        """__get_nextTime(self) -> double"""
        return _moose.Tick___get_nextTime(*args)

    def __set_nextTime(*args):
        """__set_nextTime(self, double nextTime)"""
        return _moose.Tick___set_nextTime(*args)

    def __set_path(*args):
        """__set_path(self, string path)"""
        return _moose.Tick___set_path(*args)

    def __get_updateDtSrc(*args):
        """__get_updateDtSrc(self) -> double"""
        return _moose.Tick___get_updateDtSrc(*args)

    def __set_updateDtSrc(*args):
        """__set_updateDtSrc(self, double updateDtSrc)"""
        return _moose.Tick___set_updateDtSrc(*args)

    dt = property(_moose.Tick_dt_get, _moose.Tick_dt_set)
    stage = property(_moose.Tick_stage_get, _moose.Tick_stage_set)
    ordinal = property(_moose.Tick_ordinal_get, _moose.Tick_ordinal_set)
    nextTime = property(_moose.Tick_nextTime_get, _moose.Tick_nextTime_set)
    updateDtSrc = property(_moose.Tick_updateDtSrc_get, _moose.Tick_updateDtSrc_set)
Tick_swigregister = _moose.Tick_swigregister
Tick_swigregister(Tick)
Tick.className_ = _moose.cvar.Tick_className_

class ClockJob(PyMooseBase):
    """Proxy of C++ ClockJob class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> ClockJob
        __init__(self, string path) -> ClockJob
        __init__(self, string name, Id parentId) -> ClockJob
        __init__(self, string name, PyMooseBase parent) -> ClockJob
        __init__(self, ClockJob src, string name, PyMooseBase parent) -> ClockJob
        __init__(self, ClockJob src, string name, Id parent) -> ClockJob
        __init__(self, Id src, string name, Id parent) -> ClockJob
        __init__(self, ClockJob src, string path) -> ClockJob
        """
        this = _moose.new_ClockJob(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_ClockJob
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.ClockJob_getType(*args)

    def __get_runTime(*args):
        """__get_runTime(self) -> double"""
        return _moose.ClockJob___get_runTime(*args)

    def __set_runTime(*args):
        """__set_runTime(self, double runTime)"""
        return _moose.ClockJob___set_runTime(*args)

    def __get_currentTime(*args):
        """__get_currentTime(self) -> double"""
        return _moose.ClockJob___get_currentTime(*args)

    def __set_currentTime(*args):
        """__set_currentTime(self, double currentTime)"""
        return _moose.ClockJob___set_currentTime(*args)

    def __get_nsteps(*args):
        """__get_nsteps(self) -> int"""
        return _moose.ClockJob___get_nsteps(*args)

    def __set_nsteps(*args):
        """__set_nsteps(self, int nsteps)"""
        return _moose.ClockJob___set_nsteps(*args)

    def __get_currentStep(*args):
        """__get_currentStep(self) -> int"""
        return _moose.ClockJob___get_currentStep(*args)

    def __set_currentStep(*args):
        """__set_currentStep(self, int currentStep)"""
        return _moose.ClockJob___set_currentStep(*args)

    def __get_start(*args):
        """__get_start(self) -> double"""
        return _moose.ClockJob___get_start(*args)

    def __set_start(*args):
        """__set_start(self, double start)"""
        return _moose.ClockJob___set_start(*args)

    def __get_step(*args):
        """__get_step(self) -> int"""
        return _moose.ClockJob___get_step(*args)

    def __set_step(*args):
        """__set_step(self, int step)"""
        return _moose.ClockJob___set_step(*args)

    def resched(*args):
        """resched(self)"""
        return _moose.ClockJob_resched(*args)

    def reinit(*args):
        """reinit(self)"""
        return _moose.ClockJob_reinit(*args)

    def stop(*args):
        """stop(self)"""
        return _moose.ClockJob_stop(*args)

    def getClocks(*args):
        """getClocks() -> double_vector"""
        return _moose.ClockJob_getClocks(*args)

    getClocks = staticmethod(getClocks)
    runTime = property(_moose.ClockJob_runTime_get, _moose.ClockJob_runTime_set)
    currentTime = property(_moose.ClockJob_currentTime_get, _moose.ClockJob_currentTime_set)
    nsteps = property(_moose.ClockJob_nsteps_get, _moose.ClockJob_nsteps_set)
    currentStep = property(_moose.ClockJob_currentStep_get, _moose.ClockJob_currentStep_set)
    start = property(_moose.ClockJob_start_get, _moose.ClockJob_start_set)
    step = property(_moose.ClockJob_step_get, _moose.ClockJob_step_set)
ClockJob_swigregister = _moose.ClockJob_swigregister
ClockJob_swigregister(ClockJob)
ClockJob.className_ = _moose.cvar.ClockJob_className_

def ClockJob_getClocks(*args):
  """ClockJob_getClocks() -> double_vector"""
  return _moose.ClockJob_getClocks(*args)

class Interpol(PyMooseBase):
    """Proxy of C++ Interpol class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Interpol
        __init__(self, string path) -> Interpol
        __init__(self, string name, Id parentId) -> Interpol
        __init__(self, string name, PyMooseBase parent) -> Interpol
        __init__(self, Interpol src, string name, PyMooseBase parent) -> Interpol
        __init__(self, Interpol src, string name, Id parent) -> Interpol
        __init__(self, Id src, string name, Id parent) -> Interpol
        __init__(self, Interpol src, string path) -> Interpol
        """
        this = _moose.new_Interpol(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Interpol
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Interpol_getType(*args)

    def __get_xmin(*args):
        """__get_xmin(self) -> double"""
        return _moose.Interpol___get_xmin(*args)

    def __set_xmin(*args):
        """__set_xmin(self, double xmin)"""
        return _moose.Interpol___set_xmin(*args)

    def __get_xmax(*args):
        """__get_xmax(self) -> double"""
        return _moose.Interpol___get_xmax(*args)

    def __set_xmax(*args):
        """__set_xmax(self, double xmax)"""
        return _moose.Interpol___set_xmax(*args)

    def __get_xdivs(*args):
        """__get_xdivs(self) -> int"""
        return _moose.Interpol___get_xdivs(*args)

    def __set_xdivs(*args):
        """__set_xdivs(self, int xdivs)"""
        return _moose.Interpol___set_xdivs(*args)

    def __get_mode(*args):
        """__get_mode(self) -> int"""
        return _moose.Interpol___get_mode(*args)

    def __set_mode(*args):
        """__set_mode(self, int mode)"""
        return _moose.Interpol___set_mode(*args)

    def __get_dx(*args):
        """__get_dx(self) -> double"""
        return _moose.Interpol___get_dx(*args)

    def __set_dx(*args):
        """__set_dx(self, double dx)"""
        return _moose.Interpol___set_dx(*args)

    def __get_sy(*args):
        """__get_sy(self) -> double"""
        return _moose.Interpol___get_sy(*args)

    def __set_sy(*args):
        """__set_sy(self, double sy)"""
        return _moose.Interpol___set_sy(*args)

    def __getitem__(*args):
        """__getitem__(self, unsigned int index) -> double"""
        return _moose.Interpol___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, unsigned int index, double value)"""
        return _moose.Interpol___setitem__(*args)

    def __iter__(*args):
        """__iter__(self) -> TableIterator"""
        return _moose.Interpol___iter__(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _moose.Interpol___len__(*args)

    def __get_calcMode(*args):
        """__get_calcMode(self) -> int"""
        return _moose.Interpol___get_calcMode(*args)

    def __set_calcMode(*args):
        """__set_calcMode(self, int calc_mode)"""
        return _moose.Interpol___set_calcMode(*args)

    def dumpFile(*args):
        """
        dumpFile(self) -> string
        dumpFile(self, string fileName, bool append=False)
        dumpFile(self, string fileName)
        """
        return _moose.Interpol_dumpFile(*args)

    def tabFill(*args):
        """tabFill(self, int xdivs, int mode)"""
        return _moose.Interpol_tabFill(*args)

    xmin = property(_moose.Interpol_xmin_get, _moose.Interpol_xmin_set)
    xmax = property(_moose.Interpol_xmax_get, _moose.Interpol_xmax_set)
    xdivs = property(_moose.Interpol_xdivs_get, _moose.Interpol_xdivs_set)
    mode = property(_moose.Interpol_mode_get, _moose.Interpol_mode_set)
    dx = property(_moose.Interpol_dx_get, _moose.Interpol_dx_set)
    sy = property(_moose.Interpol_sy_get, _moose.Interpol_sy_set)
    calcMode = property(_moose.Interpol_calcMode_get, _moose.Interpol_calcMode_set)
Interpol_swigregister = _moose.Interpol_swigregister
Interpol_swigregister(Interpol)
Interpol.className_ = _moose.cvar.Interpol_className_

class TableIterator(object):
    """Proxy of C++ TableIterator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, Interpol table) -> TableIterator"""
        this = _moose.new_TableIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    def __iter__(*args):
        """__iter__(self) -> TableIterator"""
        return _moose.TableIterator___iter__(*args)

    def __hasNext__(*args):
        """__hasNext__(self) -> bool"""
        return _moose.TableIterator___hasNext__(*args)

    def __next__(*args):
        """__next__(self) -> double"""
        return _moose.TableIterator___next__(*args)

    def _generator_(self):
    	if self.__hasNext__():
    		yield self.__next__()

    def next(self):
    	return self._generator_().next()
    	

    __swig_destroy__ = _moose.delete_TableIterator
    __del__ = lambda self : None;
TableIterator_swigregister = _moose.TableIterator_swigregister
TableIterator_swigregister(TableIterator)

class Table(Interpol):
    """Proxy of C++ Table class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Table
        __init__(self, string path) -> Table
        __init__(self, string name, Id parentId) -> Table
        __init__(self, string name, PyMooseBase parent) -> Table
        __init__(self, Table src, string name, PyMooseBase parent) -> Table
        __init__(self, Table src, string name, Id parent) -> Table
        __init__(self, Id src, string name, Id parent) -> Table
        __init__(self, Table src, string path) -> Table
        """
        this = _moose.new_Table(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Table
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Table_getType(*args)

    def __get_input(*args):
        """__get_input(self) -> double"""
        return _moose.Table___get_input(*args)

    def __set_input(*args):
        """__set_input(self, double input)"""
        return _moose.Table___set_input(*args)

    def __get_output(*args):
        """__get_output(self) -> double"""
        return _moose.Table___get_output(*args)

    def __set_output(*args):
        """__set_output(self, double output)"""
        return _moose.Table___set_output(*args)

    def __get_stepMode(*args):
        """__get_stepMode(self) -> int"""
        return _moose.Table___get_stepMode(*args)

    def __set_stepMode(*args):
        """__set_stepMode(self, int stepMode)"""
        return _moose.Table___set_stepMode(*args)

    def __get_stepSize(*args):
        """__get_stepSize(self) -> double"""
        return _moose.Table___get_stepSize(*args)

    def __set_stepSize(*args):
        """__set_stepSize(self, double stepSize)"""
        return _moose.Table___set_stepSize(*args)

    def __get_threshold(*args):
        """__get_threshold(self) -> double"""
        return _moose.Table___get_threshold(*args)

    def __set_threshold(*args):
        """__set_threshold(self, double threshold)"""
        return _moose.Table___set_threshold(*args)

    def createTable(*args):
        """createTable(self, int xdiv, double xmin, double xmax)"""
        return _moose.Table_createTable(*args)

    input = property(_moose.Table_input_get, _moose.Table_input_set)
    output = property(_moose.Table_output_get, _moose.Table_output_set)
    stepMode = property(_moose.Table_stepMode_get, _moose.Table_stepMode_set)
    stepSize = property(_moose.Table_stepSize_get, _moose.Table_stepSize_set)
    threshold = property(_moose.Table_threshold_get, _moose.Table_threshold_set)
Table_swigregister = _moose.Table_swigregister
Table_swigregister(Table)
Table.className_ = _moose.cvar.Table_className_

class SynChan(PyMooseBase):
    """Proxy of C++ SynChan class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> SynChan
        __init__(self, string path) -> SynChan
        __init__(self, string name, Id parentId) -> SynChan
        __init__(self, string name, PyMooseBase parent) -> SynChan
        __init__(self, SynChan src, string name, PyMooseBase parent) -> SynChan
        __init__(self, SynChan src, string name, Id parent) -> SynChan
        __init__(self, Id src, string name, Id parent) -> SynChan
        __init__(self, SynChan src, string path) -> SynChan
        """
        this = _moose.new_SynChan(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_SynChan
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.SynChan_getType(*args)

    def __get_Gbar(*args):
        """__get_Gbar(self) -> double"""
        return _moose.SynChan___get_Gbar(*args)

    def __set_Gbar(*args):
        """__set_Gbar(self, double Gbar)"""
        return _moose.SynChan___set_Gbar(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.SynChan___get_Ek(*args)

    def __set_Ek(*args):
        """__set_Ek(self, double Ek)"""
        return _moose.SynChan___set_Ek(*args)

    def __get_tau1(*args):
        """__get_tau1(self) -> double"""
        return _moose.SynChan___get_tau1(*args)

    def __set_tau1(*args):
        """__set_tau1(self, double tau1)"""
        return _moose.SynChan___set_tau1(*args)

    def __get_tau2(*args):
        """__get_tau2(self) -> double"""
        return _moose.SynChan___get_tau2(*args)

    def __set_tau2(*args):
        """__set_tau2(self, double tau2)"""
        return _moose.SynChan___set_tau2(*args)

    def __get_normalizeWeights(*args):
        """__get_normalizeWeights(self) -> bool"""
        return _moose.SynChan___get_normalizeWeights(*args)

    def __set_normalizeWeights(*args):
        """__set_normalizeWeights(self, bool normalizeWeights)"""
        return _moose.SynChan___set_normalizeWeights(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.SynChan___get_Gk(*args)

    def __set_Gk(*args):
        """__set_Gk(self, double Gk)"""
        return _moose.SynChan___set_Gk(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.SynChan___get_Ik(*args)

    def __set_Ik(*args):
        """__set_Ik(self, double Ik)"""
        return _moose.SynChan___set_Ik(*args)

    def __get_numSynapses(*args):
        """__get_numSynapses(self) -> unsigned int"""
        return _moose.SynChan___get_numSynapses(*args)

    def __set_numSynapses(*args):
        """__set_numSynapses(self, unsigned int numSynapses)"""
        return _moose.SynChan___set_numSynapses(*args)

    def __get_weight(*args):
        """__get_weight(self) -> double"""
        return _moose.SynChan___get_weight(*args)

    def __set_weight(*args):
        """__set_weight(self, double weight)"""
        return _moose.SynChan___set_weight(*args)

    def __get_delay(*args):
        """__get_delay(self) -> double"""
        return _moose.SynChan___get_delay(*args)

    def __set_delay(*args):
        """__set_delay(self, double delay)"""
        return _moose.SynChan___set_delay(*args)

    def __get_IkSrc(*args):
        """__get_IkSrc(self) -> double"""
        return _moose.SynChan___get_IkSrc(*args)

    def __set_IkSrc(*args):
        """__set_IkSrc(self, double IkSrc)"""
        return _moose.SynChan___set_IkSrc(*args)

    def __get_synapse(*args):
        """__get_synapse(self) -> double"""
        return _moose.SynChan___get_synapse(*args)

    def __set_synapse(*args):
        """__set_synapse(self, double synapse)"""
        return _moose.SynChan___set_synapse(*args)

    def __get_activation(*args):
        """__get_activation(self) -> double"""
        return _moose.SynChan___get_activation(*args)

    def __set_activation(*args):
        """__set_activation(self, double activation)"""
        return _moose.SynChan___set_activation(*args)

    def __get_modulator(*args):
        """__get_modulator(self) -> double"""
        return _moose.SynChan___get_modulator(*args)

    def __set_modulator(*args):
        """__set_modulator(self, double modulator)"""
        return _moose.SynChan___set_modulator(*args)

    Gbar = property(_moose.SynChan_Gbar_get, _moose.SynChan_Gbar_set)
    Ek = property(_moose.SynChan_Ek_get, _moose.SynChan_Ek_set)
    tau1 = property(_moose.SynChan_tau1_get, _moose.SynChan_tau1_set)
    tau2 = property(_moose.SynChan_tau2_get, _moose.SynChan_tau2_set)
    normalizeWeights = property(_moose.SynChan_normalizeWeights_get, _moose.SynChan_normalizeWeights_set)
    Gk = property(_moose.SynChan_Gk_get, _moose.SynChan_Gk_set)
    Ik = property(_moose.SynChan_Ik_get, _moose.SynChan_Ik_set)
    numSynapses = property(_moose.SynChan_numSynapses_get, _moose.SynChan_numSynapses_set)
    activation = property(_moose.SynChan_activation_get, _moose.SynChan_activation_set)
    modulator = property(_moose.SynChan_modulator_get, _moose.SynChan_modulator_set)
SynChan_swigregister = _moose.SynChan_swigregister
SynChan_swigregister(SynChan)
SynChan.className_ = _moose.cvar.SynChan_className_

class BinSynchan(PyMooseBase):
    """Proxy of C++ BinSynchan class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, ::Id id) -> BinSynchan
        __init__(self, string path) -> BinSynchan
        __init__(self, string name, ::Id parentId) -> BinSynchan
        __init__(self, string name, PyMooseBase parent) -> BinSynchan
        __init__(self, BinSynchan src, string name, PyMooseBase parent) -> BinSynchan
        __init__(self, BinSynchan src, string name, Id parent) -> BinSynchan
        __init__(self, Id src, string name, Id parent) -> BinSynchan
        __init__(self, BinSynchan src, string path) -> BinSynchan
        """
        this = _moose.new_BinSynchan(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_BinSynchan
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.BinSynchan_getType(*args)

    def __get_Gbar(*args):
        """__get_Gbar(self) -> double"""
        return _moose.BinSynchan___get_Gbar(*args)

    def __set_Gbar(*args):
        """__set_Gbar(self, double Gbar)"""
        return _moose.BinSynchan___set_Gbar(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.BinSynchan___get_Ek(*args)

    def __set_Ek(*args):
        """__set_Ek(self, double Ek)"""
        return _moose.BinSynchan___set_Ek(*args)

    def __get_tau1(*args):
        """__get_tau1(self) -> double"""
        return _moose.BinSynchan___get_tau1(*args)

    def __set_tau1(*args):
        """__set_tau1(self, double tau1)"""
        return _moose.BinSynchan___set_tau1(*args)

    def __get_tau2(*args):
        """__get_tau2(self) -> double"""
        return _moose.BinSynchan___get_tau2(*args)

    def __set_tau2(*args):
        """__set_tau2(self, double tau2)"""
        return _moose.BinSynchan___set_tau2(*args)

    def __get_normalizeWeights(*args):
        """__get_normalizeWeights(self) -> bool"""
        return _moose.BinSynchan___get_normalizeWeights(*args)

    def __set_normalizeWeights(*args):
        """__set_normalizeWeights(self, bool normalizeWeights)"""
        return _moose.BinSynchan___set_normalizeWeights(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.BinSynchan___get_Gk(*args)

    def __set_Gk(*args):
        """__set_Gk(self, double Gk)"""
        return _moose.BinSynchan___set_Gk(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.BinSynchan___get_Ik(*args)

    def __set_Ik(*args):
        """__set_Ik(self, double Ik)"""
        return _moose.BinSynchan___set_Ik(*args)

    def __get_numSynapses(*args):
        """__get_numSynapses(self) -> unsigned int"""
        return _moose.BinSynchan___get_numSynapses(*args)

    def __set_numSynapses(*args):
        """__set_numSynapses(self, unsigned int index, unsigned int num)"""
        return _moose.BinSynchan___set_numSynapses(*args)

    def __get_weight(*args):
        """__get_weight(self, unsigned int index) -> double"""
        return _moose.BinSynchan___get_weight(*args)

    def __set_weight(*args):
        """__set_weight(self, unsigned int index, double weight)"""
        return _moose.BinSynchan___set_weight(*args)

    def __get_delay(*args):
        """__get_delay(self, unsigned int index) -> double"""
        return _moose.BinSynchan___get_delay(*args)

    def __set_delay(*args):
        """__set_delay(self, unsigned int index, double delay)"""
        return _moose.BinSynchan___set_delay(*args)

    def __get_poolSize(*args):
        """__get_poolSize(self, unsigned int index) -> int"""
        return _moose.BinSynchan___get_poolSize(*args)

    def __set_poolSize(*args):
        """__set_poolSize(self, unsigned int index, int size)"""
        return _moose.BinSynchan___set_poolSize(*args)

    def __get_releaseP(*args):
        """__get_releaseP(self, unsigned int index) -> double"""
        return _moose.BinSynchan___get_releaseP(*args)

    def __set_releaseP(*args):
        """__set_releaseP(self, unsigned int index, double releaseP)"""
        return _moose.BinSynchan___set_releaseP(*args)

    def __get_releaseCount(*args):
        """__get_releaseCount(self, unsigned int index) -> double"""
        return _moose.BinSynchan___get_releaseCount(*args)

    def __set_releaseCount(*args):
        """__set_releaseCount(self, unsigned int index, double releaseCount)"""
        return _moose.BinSynchan___set_releaseCount(*args)

    def __get_synapse(*args):
        """__get_synapse(self) -> double"""
        return _moose.BinSynchan___get_synapse(*args)

    def __set_synapse(*args):
        """__set_synapse(self, double synapse)"""
        return _moose.BinSynchan___set_synapse(*args)

    def __get_activation(*args):
        """__get_activation(self) -> double"""
        return _moose.BinSynchan___get_activation(*args)

    def __set_activation(*args):
        """__set_activation(self, double activation)"""
        return _moose.BinSynchan___set_activation(*args)

    def __get_modulator(*args):
        """__get_modulator(self) -> double"""
        return _moose.BinSynchan___get_modulator(*args)

    def __set_modulator(*args):
        """__set_modulator(self, double modulator)"""
        return _moose.BinSynchan___set_modulator(*args)

    weight = property(_moose.BinSynchan_weight_get, _moose.BinSynchan_weight_set)
    delay = property(_moose.BinSynchan_delay_get, _moose.BinSynchan_delay_set)
    releaseP = property(_moose.BinSynchan_releaseP_get, _moose.BinSynchan_releaseP_set)
    poolSize = property(_moose.BinSynchan_poolSize_get, _moose.BinSynchan_poolSize_set)
    releaseCount = property(_moose.BinSynchan_releaseCount_get, _moose.BinSynchan_releaseCount_set)
    Gbar = property(_moose.BinSynchan_Gbar_get, _moose.BinSynchan_Gbar_set)
    Ek = property(_moose.BinSynchan_Ek_get, _moose.BinSynchan_Ek_set)
    tau1 = property(_moose.BinSynchan_tau1_get, _moose.BinSynchan_tau1_set)
    tau2 = property(_moose.BinSynchan_tau2_get, _moose.BinSynchan_tau2_set)
    normalizeWeights = property(_moose.BinSynchan_normalizeWeights_get, _moose.BinSynchan_normalizeWeights_set)
    Gk = property(_moose.BinSynchan_Gk_get, _moose.BinSynchan_Gk_set)
    Ik = property(_moose.BinSynchan_Ik_get, _moose.BinSynchan_Ik_set)
    numSynapses = property(_moose.BinSynchan_numSynapses_get, _moose.BinSynchan_numSynapses_set)
    activation = property(_moose.BinSynchan_activation_get, _moose.BinSynchan_activation_set)
    modulator = property(_moose.BinSynchan_modulator_get, _moose.BinSynchan_modulator_set)
BinSynchan_swigregister = _moose.BinSynchan_swigregister
BinSynchan_swigregister(BinSynchan)
BinSynchan.className_ = _moose.cvar.BinSynchan_className_

class StochSynchan(PyMooseBase):
    """Proxy of C++ StochSynchan class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> StochSynchan
        __init__(self, string path) -> StochSynchan
        __init__(self, string name, Id parentId) -> StochSynchan
        __init__(self, string name, PyMooseBase parent) -> StochSynchan
        __init__(self, StochSynchan src, string name, PyMooseBase parent) -> StochSynchan
        __init__(self, StochSynchan src, string name, Id parent) -> StochSynchan
        __init__(self, Id src, string name, Id parent) -> StochSynchan
        __init__(self, StochSynchan src, string path) -> StochSynchan
        """
        this = _moose.new_StochSynchan(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_StochSynchan
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.StochSynchan_getType(*args)

    def __get_Gbar(*args):
        """__get_Gbar(self) -> double"""
        return _moose.StochSynchan___get_Gbar(*args)

    def __set_Gbar(*args):
        """__set_Gbar(self, double Gbar)"""
        return _moose.StochSynchan___set_Gbar(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.StochSynchan___get_Ek(*args)

    def __set_Ek(*args):
        """__set_Ek(self, double Ek)"""
        return _moose.StochSynchan___set_Ek(*args)

    def __get_tau1(*args):
        """__get_tau1(self) -> double"""
        return _moose.StochSynchan___get_tau1(*args)

    def __set_tau1(*args):
        """__set_tau1(self, double tau1)"""
        return _moose.StochSynchan___set_tau1(*args)

    def __get_tau2(*args):
        """__get_tau2(self) -> double"""
        return _moose.StochSynchan___get_tau2(*args)

    def __set_tau2(*args):
        """__set_tau2(self, double tau2)"""
        return _moose.StochSynchan___set_tau2(*args)

    def __get_normalizeWeights(*args):
        """__get_normalizeWeights(self) -> bool"""
        return _moose.StochSynchan___get_normalizeWeights(*args)

    def __set_normalizeWeights(*args):
        """__set_normalizeWeights(self, bool normalizeWeights)"""
        return _moose.StochSynchan___set_normalizeWeights(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.StochSynchan___get_Gk(*args)

    def __set_Gk(*args):
        """__set_Gk(self, double Gk)"""
        return _moose.StochSynchan___set_Gk(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.StochSynchan___get_Ik(*args)

    def __set_Ik(*args):
        """__set_Ik(self, double Ik)"""
        return _moose.StochSynchan___set_Ik(*args)

    def __get_numSynapses(*args):
        """__get_numSynapses(self) -> unsigned int"""
        return _moose.StochSynchan___get_numSynapses(*args)

    def __set_numSynapses(*args):
        """__set_numSynapses(self, unsigned int index, unsigned int num)"""
        return _moose.StochSynchan___set_numSynapses(*args)

    def __get_weight(*args):
        """__get_weight(self, unsigned int index) -> double"""
        return _moose.StochSynchan___get_weight(*args)

    def __set_weight(*args):
        """__set_weight(self, unsigned int index, double weight)"""
        return _moose.StochSynchan___set_weight(*args)

    def __get_delay(*args):
        """__get_delay(self, unsigned int index) -> double"""
        return _moose.StochSynchan___get_delay(*args)

    def __set_delay(*args):
        """__set_delay(self, unsigned int index, double delay)"""
        return _moose.StochSynchan___set_delay(*args)

    def __get_releaseP(*args):
        """__get_releaseP(self, unsigned int index) -> double"""
        return _moose.StochSynchan___get_releaseP(*args)

    def __set_releaseP(*args):
        """__set_releaseP(self, unsigned int index, double releaseP)"""
        return _moose.StochSynchan___set_releaseP(*args)

    def __get_releaseCount(*args):
        """__get_releaseCount(self, unsigned int index) -> double"""
        return _moose.StochSynchan___get_releaseCount(*args)

    def __set_releaseCount(*args):
        """__set_releaseCount(self, unsigned int index, double releaseCount)"""
        return _moose.StochSynchan___set_releaseCount(*args)

    def __get_synapse(*args):
        """__get_synapse(self) -> double"""
        return _moose.StochSynchan___get_synapse(*args)

    def __set_synapse(*args):
        """__set_synapse(self, double synapse)"""
        return _moose.StochSynchan___set_synapse(*args)

    def __get_activation(*args):
        """__get_activation(self) -> double"""
        return _moose.StochSynchan___get_activation(*args)

    def __set_activation(*args):
        """__set_activation(self, double activation)"""
        return _moose.StochSynchan___set_activation(*args)

    def __get_modulator(*args):
        """__get_modulator(self) -> double"""
        return _moose.StochSynchan___get_modulator(*args)

    def __set_modulator(*args):
        """__set_modulator(self, double modulator)"""
        return _moose.StochSynchan___set_modulator(*args)

    weight = property(_moose.StochSynchan_weight_get, _moose.StochSynchan_weight_set)
    delay = property(_moose.StochSynchan_delay_get, _moose.StochSynchan_delay_set)
    releaseP = property(_moose.StochSynchan_releaseP_get, _moose.StochSynchan_releaseP_set)
    releaseCount = property(_moose.StochSynchan_releaseCount_get, _moose.StochSynchan_releaseCount_set)
    Gbar = property(_moose.StochSynchan_Gbar_get, _moose.StochSynchan_Gbar_set)
    Ek = property(_moose.StochSynchan_Ek_get, _moose.StochSynchan_Ek_set)
    tau1 = property(_moose.StochSynchan_tau1_get, _moose.StochSynchan_tau1_set)
    tau2 = property(_moose.StochSynchan_tau2_get, _moose.StochSynchan_tau2_set)
    normalizeWeights = property(_moose.StochSynchan_normalizeWeights_get, _moose.StochSynchan_normalizeWeights_set)
    Gk = property(_moose.StochSynchan_Gk_get, _moose.StochSynchan_Gk_set)
    Ik = property(_moose.StochSynchan_Ik_get, _moose.StochSynchan_Ik_set)
    numSynapses = property(_moose.StochSynchan_numSynapses_get, _moose.StochSynchan_numSynapses_set)
    activation = property(_moose.StochSynchan_activation_get, _moose.StochSynchan_activation_set)
    modulator = property(_moose.StochSynchan_modulator_get, _moose.StochSynchan_modulator_set)
StochSynchan_swigregister = _moose.StochSynchan_swigregister
StochSynchan_swigregister(StochSynchan)
StochSynchan.className_ = _moose.cvar.StochSynchan_className_

class SpikeGen(PyMooseBase):
    """Proxy of C++ SpikeGen class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> SpikeGen
        __init__(self, string path) -> SpikeGen
        __init__(self, string name, Id parentId) -> SpikeGen
        __init__(self, string name, PyMooseBase parent) -> SpikeGen
        __init__(self, SpikeGen src, string name, PyMooseBase parent) -> SpikeGen
        __init__(self, SpikeGen src, string name, Id parent) -> SpikeGen
        __init__(self, Id src, string name, Id parent) -> SpikeGen
        __init__(self, SpikeGen src, string path) -> SpikeGen
        """
        this = _moose.new_SpikeGen(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_SpikeGen
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.SpikeGen_getType(*args)

    def __get_threshold(*args):
        """__get_threshold(self) -> double"""
        return _moose.SpikeGen___get_threshold(*args)

    def __set_threshold(*args):
        """__set_threshold(self, double threshold)"""
        return _moose.SpikeGen___set_threshold(*args)

    def __get_refractT(*args):
        """__get_refractT(self) -> double"""
        return _moose.SpikeGen___get_refractT(*args)

    def __set_refractT(*args):
        """__set_refractT(self, double refractT)"""
        return _moose.SpikeGen___set_refractT(*args)

    def __get_absRefractT(*args):
        """__get_absRefractT(self) -> double"""
        return _moose.SpikeGen___get_absRefractT(*args)

    def __set_absRefractT(*args):
        """__set_absRefractT(self, double abs_refract)"""
        return _moose.SpikeGen___set_absRefractT(*args)

    def __get_amplitude(*args):
        """__get_amplitude(self) -> double"""
        return _moose.SpikeGen___get_amplitude(*args)

    def __set_amplitude(*args):
        """__set_amplitude(self, double amplitude)"""
        return _moose.SpikeGen___set_amplitude(*args)

    def __get_state(*args):
        """__get_state(self) -> double"""
        return _moose.SpikeGen___get_state(*args)

    def __set_state(*args):
        """__set_state(self, double state)"""
        return _moose.SpikeGen___set_state(*args)

    def __get_event(*args):
        """__get_event(self) -> double"""
        return _moose.SpikeGen___get_event(*args)

    def __set_event(*args):
        """__set_event(self, double event)"""
        return _moose.SpikeGen___set_event(*args)

    def __get_Vm(*args):
        """__get_Vm(self) -> double"""
        return _moose.SpikeGen___get_Vm(*args)

    def __set_Vm(*args):
        """__set_Vm(self, double Vm)"""
        return _moose.SpikeGen___set_Vm(*args)

    threshold = property(_moose.SpikeGen_threshold_get, _moose.SpikeGen_threshold_set)
    refractT = property(_moose.SpikeGen_refractT_get, _moose.SpikeGen_refractT_set)
    absRefractT = property(_moose.SpikeGen_absRefractT_get, _moose.SpikeGen_absRefractT_set)
    amplitude = property(_moose.SpikeGen_amplitude_get, _moose.SpikeGen_amplitude_set)
    state = property(_moose.SpikeGen_state_get, _moose.SpikeGen_state_set)
    event = property(_moose.SpikeGen_event_get, _moose.SpikeGen_event_set)
    Vm = property(_moose.SpikeGen_Vm_get, _moose.SpikeGen_Vm_set)
SpikeGen_swigregister = _moose.SpikeGen_swigregister
SpikeGen_swigregister(SpikeGen)
SpikeGen.className_ = _moose.cvar.SpikeGen_className_

class RandomSpike(PyMooseBase):
    """Proxy of C++ RandomSpike class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> RandomSpike
        __init__(self, string path) -> RandomSpike
        __init__(self, string name, Id parentId) -> RandomSpike
        __init__(self, string name, PyMooseBase parent) -> RandomSpike
        __init__(self, RandomSpike src, string name, PyMooseBase parent) -> RandomSpike
        __init__(self, RandomSpike src, string name, Id parent) -> RandomSpike
        __init__(self, Id src, string name, Id parent) -> RandomSpike
        __init__(self, RandomSpike src, string path) -> RandomSpike
        """
        this = _moose.new_RandomSpike(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_RandomSpike
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.RandomSpike_getType(*args)

    def __get_minAmp(*args):
        """__get_minAmp(self) -> double"""
        return _moose.RandomSpike___get_minAmp(*args)

    def __set_minAmp(*args):
        """__set_minAmp(self, double minAmp)"""
        return _moose.RandomSpike___set_minAmp(*args)

    def __get_maxAmp(*args):
        """__get_maxAmp(self) -> double"""
        return _moose.RandomSpike___get_maxAmp(*args)

    def __set_maxAmp(*args):
        """__set_maxAmp(self, double maxAmp)"""
        return _moose.RandomSpike___set_maxAmp(*args)

    def __get_rate(*args):
        """__get_rate(self) -> double"""
        return _moose.RandomSpike___get_rate(*args)

    def __set_rate(*args):
        """__set_rate(self, double rate)"""
        return _moose.RandomSpike___set_rate(*args)

    def __get_resetValue(*args):
        """__get_resetValue(self) -> double"""
        return _moose.RandomSpike___get_resetValue(*args)

    def __set_resetValue(*args):
        """__set_resetValue(self, double resetValue)"""
        return _moose.RandomSpike___set_resetValue(*args)

    def __get_state(*args):
        """__get_state(self) -> double"""
        return _moose.RandomSpike___get_state(*args)

    def __set_state(*args):
        """__set_state(self, double state)"""
        return _moose.RandomSpike___set_state(*args)

    def __get_absRefract(*args):
        """__get_absRefract(self) -> double"""
        return _moose.RandomSpike___get_absRefract(*args)

    def __set_absRefract(*args):
        """__set_absRefract(self, double absRefract)"""
        return _moose.RandomSpike___set_absRefract(*args)

    def __get_lastEvent(*args):
        """__get_lastEvent(self) -> double"""
        return _moose.RandomSpike___get_lastEvent(*args)

    def __get_reset(*args):
        """__get_reset(self) -> int"""
        return _moose.RandomSpike___get_reset(*args)

    def __set_reset(*args):
        """__set_reset(self, int reset)"""
        return _moose.RandomSpike___set_reset(*args)

    minAmp = property(_moose.RandomSpike_minAmp_get, _moose.RandomSpike_minAmp_set)
    maxAmp = property(_moose.RandomSpike_maxAmp_get, _moose.RandomSpike_maxAmp_set)
    rate = property(_moose.RandomSpike_rate_get, _moose.RandomSpike_rate_set)
    resetValue = property(_moose.RandomSpike_resetValue_get, _moose.RandomSpike_resetValue_set)
    state = property(_moose.RandomSpike_state_get, _moose.RandomSpike_state_set)
    absRefract = property(_moose.RandomSpike_absRefract_get, _moose.RandomSpike_absRefract_set)
    lastEvent = property(_moose.RandomSpike_lastEvent_get, _moose.RandomSpike_lastEvent_set)
    reset = property(_moose.RandomSpike_reset_get, _moose.RandomSpike_reset_set)
RandomSpike_swigregister = _moose.RandomSpike_swigregister
RandomSpike_swigregister(RandomSpike)
RandomSpike.className_ = _moose.cvar.RandomSpike_className_

class PulseGen(PyMooseBase):
    """Proxy of C++ PulseGen class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> PulseGen
        __init__(self, string path) -> PulseGen
        __init__(self, string name, Id parentId) -> PulseGen
        __init__(self, string name, PyMooseBase parent) -> PulseGen
        __init__(self, PulseGen src, string name, PyMooseBase parent) -> PulseGen
        __init__(self, PulseGen src, string name, Id parent) -> PulseGen
        __init__(self, Id src, string name, Id parent) -> PulseGen
        __init__(self, PulseGen src, string path) -> PulseGen
        """
        this = _moose.new_PulseGen(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_PulseGen
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.PulseGen_getType(*args)

    def __get_firstLevel(*args):
        """__get_firstLevel(self) -> double"""
        return _moose.PulseGen___get_firstLevel(*args)

    def __set_firstLevel(*args):
        """__set_firstLevel(self, double firstLevel)"""
        return _moose.PulseGen___set_firstLevel(*args)

    def __get_firstWidth(*args):
        """__get_firstWidth(self) -> double"""
        return _moose.PulseGen___get_firstWidth(*args)

    def __set_firstWidth(*args):
        """__set_firstWidth(self, double firstWidth)"""
        return _moose.PulseGen___set_firstWidth(*args)

    def __get_firstDelay(*args):
        """__get_firstDelay(self) -> double"""
        return _moose.PulseGen___get_firstDelay(*args)

    def __set_firstDelay(*args):
        """__set_firstDelay(self, double firstDelay)"""
        return _moose.PulseGen___set_firstDelay(*args)

    def __get_secondLevel(*args):
        """__get_secondLevel(self) -> double"""
        return _moose.PulseGen___get_secondLevel(*args)

    def __set_secondLevel(*args):
        """__set_secondLevel(self, double secondLevel)"""
        return _moose.PulseGen___set_secondLevel(*args)

    def __get_secondWidth(*args):
        """__get_secondWidth(self) -> double"""
        return _moose.PulseGen___get_secondWidth(*args)

    def __set_secondWidth(*args):
        """__set_secondWidth(self, double secondWidth)"""
        return _moose.PulseGen___set_secondWidth(*args)

    def __get_secondDelay(*args):
        """__get_secondDelay(self) -> double"""
        return _moose.PulseGen___get_secondDelay(*args)

    def __set_secondDelay(*args):
        """__set_secondDelay(self, double secondDelay)"""
        return _moose.PulseGen___set_secondDelay(*args)

    def __get_baseLevel(*args):
        """__get_baseLevel(self) -> double"""
        return _moose.PulseGen___get_baseLevel(*args)

    def __set_baseLevel(*args):
        """__set_baseLevel(self, double baseLevel)"""
        return _moose.PulseGen___set_baseLevel(*args)

    def __get_output(*args):
        """__get_output(self) -> double"""
        return _moose.PulseGen___get_output(*args)

    def __get_trigTime(*args):
        """__get_trigTime(self) -> double"""
        return _moose.PulseGen___get_trigTime(*args)

    def __set_trigTime(*args):
        """__set_trigTime(self, double trigTime)"""
        return _moose.PulseGen___set_trigTime(*args)

    def __get_trigMode(*args):
        """__get_trigMode(self) -> int"""
        return _moose.PulseGen___get_trigMode(*args)

    def __set_trigMode(*args):
        """__set_trigMode(self, int trigMode)"""
        return _moose.PulseGen___set_trigMode(*args)

    def __get_prevInput(*args):
        """__get_prevInput(self) -> int"""
        return _moose.PulseGen___get_prevInput(*args)

    firstLevel = property(_moose.PulseGen_firstLevel_get, _moose.PulseGen_firstLevel_set)
    firstWidth = property(_moose.PulseGen_firstWidth_get, _moose.PulseGen_firstWidth_set)
    firstDelay = property(_moose.PulseGen_firstDelay_get, _moose.PulseGen_firstDelay_set)
    secondLevel = property(_moose.PulseGen_secondLevel_get, _moose.PulseGen_secondLevel_set)
    secondWidth = property(_moose.PulseGen_secondWidth_get, _moose.PulseGen_secondWidth_set)
    secondDelay = property(_moose.PulseGen_secondDelay_get, _moose.PulseGen_secondDelay_set)
    baseLevel = property(_moose.PulseGen_baseLevel_get, _moose.PulseGen_baseLevel_set)
    output = property(_moose.PulseGen_output_get, _moose.PulseGen_output_set)
    trigTime = property(_moose.PulseGen_trigTime_get, _moose.PulseGen_trigTime_set)
    trigMode = property(_moose.PulseGen_trigMode_get, _moose.PulseGen_trigMode_set)
    prevInput = property(_moose.PulseGen_prevInput_get, _moose.PulseGen_prevInput_set)
PulseGen_swigregister = _moose.PulseGen_swigregister
PulseGen_swigregister(PulseGen)
PulseGen.className_ = _moose.cvar.PulseGen_className_

class Nernst(PyMooseBase):
    """Proxy of C++ Nernst class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Nernst
        __init__(self, string path) -> Nernst
        __init__(self, string name, Id parentId) -> Nernst
        __init__(self, string name, PyMooseBase parent) -> Nernst
        __init__(self, Nernst src, string name, PyMooseBase parent) -> Nernst
        __init__(self, Nernst src, string name, Id parent) -> Nernst
        __init__(self, Id src, string name, Id parent) -> Nernst
        __init__(self, Nernst src, string path) -> Nernst
        """
        this = _moose.new_Nernst(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Nernst
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Nernst_getType(*args)

    def __get_E(*args):
        """__get_E(self) -> double"""
        return _moose.Nernst___get_E(*args)

    def __set_E(*args):
        """__set_E(self, double E)"""
        return _moose.Nernst___set_E(*args)

    def __get_Temperature(*args):
        """__get_Temperature(self) -> double"""
        return _moose.Nernst___get_Temperature(*args)

    def __set_Temperature(*args):
        """__set_Temperature(self, double Temperature)"""
        return _moose.Nernst___set_Temperature(*args)

    def __get_valence(*args):
        """__get_valence(self) -> int"""
        return _moose.Nernst___get_valence(*args)

    def __set_valence(*args):
        """__set_valence(self, int valence)"""
        return _moose.Nernst___set_valence(*args)

    def __get_Cin(*args):
        """__get_Cin(self) -> double"""
        return _moose.Nernst___get_Cin(*args)

    def __set_Cin(*args):
        """__set_Cin(self, double Cin)"""
        return _moose.Nernst___set_Cin(*args)

    def __get_Cout(*args):
        """__get_Cout(self) -> double"""
        return _moose.Nernst___get_Cout(*args)

    def __set_Cout(*args):
        """__set_Cout(self, double Cout)"""
        return _moose.Nernst___set_Cout(*args)

    def __get_scale(*args):
        """__get_scale(self) -> double"""
        return _moose.Nernst___get_scale(*args)

    def __set_scale(*args):
        """__set_scale(self, double scale)"""
        return _moose.Nernst___set_scale(*args)

    def __get_ESrc(*args):
        """__get_ESrc(self) -> double"""
        return _moose.Nernst___get_ESrc(*args)

    def __set_ESrc(*args):
        """__set_ESrc(self, double ESrc)"""
        return _moose.Nernst___set_ESrc(*args)

    def __get_CinMsg(*args):
        """__get_CinMsg(self) -> double"""
        return _moose.Nernst___get_CinMsg(*args)

    def __set_CinMsg(*args):
        """__set_CinMsg(self, double CinMsg)"""
        return _moose.Nernst___set_CinMsg(*args)

    def __get_CoutMsg(*args):
        """__get_CoutMsg(self) -> double"""
        return _moose.Nernst___get_CoutMsg(*args)

    def __set_CoutMsg(*args):
        """__set_CoutMsg(self, double CoutMsg)"""
        return _moose.Nernst___set_CoutMsg(*args)

    E = property(_moose.Nernst_E_get, _moose.Nernst_E_set)
    Temperature = property(_moose.Nernst_Temperature_get, _moose.Nernst_Temperature_set)
    valence = property(_moose.Nernst_valence_get, _moose.Nernst_valence_set)
    Cin = property(_moose.Nernst_Cin_get, _moose.Nernst_Cin_set)
    Cout = property(_moose.Nernst_Cout_get, _moose.Nernst_Cout_set)
    scale = property(_moose.Nernst_scale_get, _moose.Nernst_scale_set)
Nernst_swigregister = _moose.Nernst_swigregister
Nernst_swigregister(Nernst)
Nernst.className_ = _moose.cvar.Nernst_className_

class CaConc(PyMooseBase):
    """Proxy of C++ CaConc class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, ::Id id) -> CaConc
        __init__(self, string path) -> CaConc
        __init__(self, string name, ::Id parentId) -> CaConc
        __init__(self, string name, PyMooseBase parent) -> CaConc
        __init__(self, CaConc src, string name, PyMooseBase parent) -> CaConc
        __init__(self, CaConc src, string name, Id parent) -> CaConc
        __init__(self, Id src, string name, Id parent) -> CaConc
        __init__(self, CaConc src, string path) -> CaConc
        """
        this = _moose.new_CaConc(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_CaConc
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.CaConc_getType(*args)

    def __get_Ca(*args):
        """__get_Ca(self) -> double"""
        return _moose.CaConc___get_Ca(*args)

    def __set_Ca(*args):
        """__set_Ca(self, double Ca)"""
        return _moose.CaConc___set_Ca(*args)

    def __get_CaBasal(*args):
        """__get_CaBasal(self) -> double"""
        return _moose.CaConc___get_CaBasal(*args)

    def __set_CaBasal(*args):
        """__set_CaBasal(self, double CaBasal)"""
        return _moose.CaConc___set_CaBasal(*args)

    def __get_Ca_base(*args):
        """__get_Ca_base(self) -> double"""
        return _moose.CaConc___get_Ca_base(*args)

    def __set_Ca_base(*args):
        """__set_Ca_base(self, double Ca_base)"""
        return _moose.CaConc___set_Ca_base(*args)

    def __get_tau(*args):
        """__get_tau(self) -> double"""
        return _moose.CaConc___get_tau(*args)

    def __set_tau(*args):
        """__set_tau(self, double tau)"""
        return _moose.CaConc___set_tau(*args)

    def __get_B(*args):
        """__get_B(self) -> double"""
        return _moose.CaConc___get_B(*args)

    def __set_B(*args):
        """__set_B(self, double B)"""
        return _moose.CaConc___set_B(*args)

    Ca = property(_moose.CaConc_Ca_get, _moose.CaConc_Ca_set)
    CaBasal = property(_moose.CaConc_CaBasal_get, _moose.CaConc_CaBasal_set)
    Ca_base = property(_moose.CaConc_Ca_base_get, _moose.CaConc_Ca_base_set)
    tau = property(_moose.CaConc_tau_get, _moose.CaConc_tau_set)
    B = property(_moose.CaConc_B_get, _moose.CaConc_B_set)
CaConc_swigregister = _moose.CaConc_swigregister
CaConc_swigregister(CaConc)
CaConc.className_ = _moose.cvar.CaConc_className_

class HHGate(PyMooseBase):
    """Proxy of C++ HHGate class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> HHGate
        __init__(self, string path) -> HHGate
        __init__(self, string name, Id parentId) -> HHGate
        __init__(self, string name, PyMooseBase parent) -> HHGate
        __init__(self, HHGate src, string name, PyMooseBase parent) -> HHGate
        __init__(self, HHGate src, string name, Id parent) -> HHGate
        __init__(self, Id src, string name, Id parent) -> HHGate
        __init__(self, HHGate src, string path) -> HHGate
        """
        this = _moose.new_HHGate(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_HHGate
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.HHGate_getType(*args)

    def __get_A(*args):
        """__get_A(self) -> Interpol"""
        return _moose.HHGate___get_A(*args)

    def __get_B(*args):
        """__get_B(self) -> Interpol"""
        return _moose.HHGate___get_B(*args)

    def tabFill(*args):
        """tabFill(self, int xdivs, int mode)"""
        return _moose.HHGate_tabFill(*args)

    def setupAlpha(*args):
        """
        setupAlpha(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000, double min=-0.1, 
            double max=0.05)
        setupAlpha(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000, double min=-0.1)
        setupAlpha(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000)
        setupAlpha(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF)
        """
        return _moose.HHGate_setupAlpha(*args)

    def setupTau(*args):
        """
        setupTau(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000, double min=-0.1, 
            double max=0.05)
        setupTau(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000, double min=-0.1)
        setupTau(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF, double size=3000)
        setupTau(self, double AA, double AB, double AC, double AD, double AF, 
            double BA, double BB, double BC, double BD, 
            double BF)
        """
        return _moose.HHGate_setupTau(*args)

    def tweakAlpha(*args):
        """tweakAlpha(self)"""
        return _moose.HHGate_tweakAlpha(*args)

    def tweakTau(*args):
        """tweakTau(self)"""
        return _moose.HHGate_tweakTau(*args)

    A = property(_moose.HHGate_A_get, _moose.HHGate_A_set)
    B = property(_moose.HHGate_B_get, _moose.HHGate_B_set)
HHGate_swigregister = _moose.HHGate_swigregister
HHGate_swigregister(HHGate)
HHGate.className_ = _moose.cvar.HHGate_className_

class HHChannel(PyMooseBase):
    """Proxy of C++ HHChannel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> HHChannel
        __init__(self, string path) -> HHChannel
        __init__(self, string name, Id parentId) -> HHChannel
        __init__(self, string name, PyMooseBase parent) -> HHChannel
        __init__(self, HHChannel src, string name, PyMooseBase parent) -> HHChannel
        __init__(self, HHChannel src, string name, Id parent) -> HHChannel
        __init__(self, HHChannel src, string path) -> HHChannel
        __init__(self, Id src, string name, Id parent) -> HHChannel
        """
        this = _moose.new_HHChannel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_HHChannel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.HHChannel_getType(*args)

    def __get_Gbar(*args):
        """__get_Gbar(self) -> double"""
        return _moose.HHChannel___get_Gbar(*args)

    def __set_Gbar(*args):
        """__set_Gbar(self, double Gbar)"""
        return _moose.HHChannel___set_Gbar(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.HHChannel___get_Ek(*args)

    def __set_Ek(*args):
        """__set_Ek(self, double Ek)"""
        return _moose.HHChannel___set_Ek(*args)

    def __get_Xpower(*args):
        """__get_Xpower(self) -> double"""
        return _moose.HHChannel___get_Xpower(*args)

    def __set_Xpower(*args):
        """__set_Xpower(self, double Xpower)"""
        return _moose.HHChannel___set_Xpower(*args)

    def __get_Ypower(*args):
        """__get_Ypower(self) -> double"""
        return _moose.HHChannel___get_Ypower(*args)

    def __set_Ypower(*args):
        """__set_Ypower(self, double Ypower)"""
        return _moose.HHChannel___set_Ypower(*args)

    def __get_Zpower(*args):
        """__get_Zpower(self) -> double"""
        return _moose.HHChannel___get_Zpower(*args)

    def __set_Zpower(*args):
        """__set_Zpower(self, double Zpower)"""
        return _moose.HHChannel___set_Zpower(*args)

    def __get_instant(*args):
        """__get_instant(self) -> int"""
        return _moose.HHChannel___get_instant(*args)

    def __set_instant(*args):
        """__set_instant(self, int instant)"""
        return _moose.HHChannel___set_instant(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.HHChannel___get_Gk(*args)

    def __set_Gk(*args):
        """__set_Gk(self, double Gk)"""
        return _moose.HHChannel___set_Gk(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.HHChannel___get_Ik(*args)

    def __get_X(*args):
        """__get_X(self) -> double"""
        return _moose.HHChannel___get_X(*args)

    def __set_X(*args):
        """__set_X(self, double X)"""
        return _moose.HHChannel___set_X(*args)

    def __get_Y(*args):
        """__get_Y(self) -> double"""
        return _moose.HHChannel___get_Y(*args)

    def __set_Y(*args):
        """__set_Y(self, double Y)"""
        return _moose.HHChannel___set_Y(*args)

    def __get_Z(*args):
        """__get_Z(self) -> double"""
        return _moose.HHChannel___get_Z(*args)

    def __set_Z(*args):
        """__set_Z(self, double Z)"""
        return _moose.HHChannel___set_Z(*args)

    def __get_useConcentration(*args):
        """__get_useConcentration(self) -> int"""
        return _moose.HHChannel___get_useConcentration(*args)

    def __set_useConcentration(*args):
        """__set_useConcentration(self, int useConcentration)"""
        return _moose.HHChannel___set_useConcentration(*args)

    Gbar = property(_moose.HHChannel_Gbar_get, _moose.HHChannel_Gbar_set)
    Ek = property(_moose.HHChannel_Ek_get, _moose.HHChannel_Ek_set)
    Gk = property(_moose.HHChannel_Gk_get, _moose.HHChannel_Gk_set)
    Xpower = property(_moose.HHChannel_Xpower_get, _moose.HHChannel_Xpower_set)
    Ypower = property(_moose.HHChannel_Ypower_get, _moose.HHChannel_Ypower_set)
    Zpower = property(_moose.HHChannel_Zpower_get, _moose.HHChannel_Zpower_set)
    X = property(_moose.HHChannel_X_get, _moose.HHChannel_X_set)
    Y = property(_moose.HHChannel_Y_get, _moose.HHChannel_Y_set)
    Z = property(_moose.HHChannel_Z_get, _moose.HHChannel_Z_set)
    instant = property(_moose.HHChannel_instant_get, _moose.HHChannel_instant_set)
    useConcentration = property(_moose.HHChannel_useConcentration_get, _moose.HHChannel_useConcentration_set)
HHChannel_swigregister = _moose.HHChannel_swigregister
HHChannel_swigregister(HHChannel)
HHChannel.className_ = _moose.cvar.HHChannel_className_

class Mg_block(PyMooseBase):
    """Proxy of C++ Mg_block class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Mg_block
        __init__(self, string path) -> Mg_block
        __init__(self, string name, Id parentId) -> Mg_block
        __init__(self, string name, PyMooseBase parent) -> Mg_block
        __init__(self, Mg_block src, string name, PyMooseBase parent) -> Mg_block
        __init__(self, Mg_block src, string name, Id parent) -> Mg_block
        __init__(self, Id src, string name, Id parent) -> Mg_block
        __init__(self, Mg_block src, string path) -> Mg_block
        """
        this = _moose.new_Mg_block(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Mg_block
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Mg_block_getType(*args)

    def __get_KMg_A(*args):
        """__get_KMg_A(self) -> double"""
        return _moose.Mg_block___get_KMg_A(*args)

    def __set_KMg_A(*args):
        """__set_KMg_A(self, double KMg_A)"""
        return _moose.Mg_block___set_KMg_A(*args)

    def __get_KMg_B(*args):
        """__get_KMg_B(self) -> double"""
        return _moose.Mg_block___get_KMg_B(*args)

    def __set_KMg_B(*args):
        """__set_KMg_B(self, double KMg_B)"""
        return _moose.Mg_block___set_KMg_B(*args)

    def __get_CMg(*args):
        """__get_CMg(self) -> double"""
        return _moose.Mg_block___get_CMg(*args)

    def __set_CMg(*args):
        """__set_CMg(self, double CMg)"""
        return _moose.Mg_block___set_CMg(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.Mg_block___get_Ik(*args)

    def __set_Ik(*args):
        """__set_Ik(self, double Ik)"""
        return _moose.Mg_block___set_Ik(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.Mg_block___get_Gk(*args)

    def __set_Gk(*args):
        """__set_Gk(self, double Gk)"""
        return _moose.Mg_block___set_Gk(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.Mg_block___get_Ek(*args)

    def __set_Ek(*args):
        """__set_Ek(self, double Ek)"""
        return _moose.Mg_block___set_Ek(*args)

    def __get_Zk(*args):
        """__get_Zk(self) -> double"""
        return _moose.Mg_block___get_Zk(*args)

    def __set_Zk(*args):
        """__set_Zk(self, double Zk)"""
        return _moose.Mg_block___set_Zk(*args)

    KMg_A = property(_moose.Mg_block_KMg_A_get, _moose.Mg_block_KMg_A_set)
    K_MgB = property(_moose.Mg_block_K_MgB_get, _moose.Mg_block_K_MgB_set)
    CMg = property(_moose.Mg_block_CMg_get, _moose.Mg_block_CMg_set)
    Ik = property(_moose.Mg_block_Ik_get, _moose.Mg_block_Ik_set)
    Gk = property(_moose.Mg_block_Gk_get, _moose.Mg_block_Gk_set)
    Ek = property(_moose.Mg_block_Ek_get, _moose.Mg_block_Ek_set)
    Zk = property(_moose.Mg_block_Zk_get, _moose.Mg_block_Zk_set)
Mg_block_swigregister = _moose.Mg_block_swigregister
Mg_block_swigregister(Mg_block)
Mg_block.className_ = _moose.cvar.Mg_block_className_

class Compartment(PyMooseBase):
    """Proxy of C++ Compartment class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, ::Id id) -> Compartment
        __init__(self, string path) -> Compartment
        __init__(self, string name, ::Id parentId) -> Compartment
        __init__(self, string name, PyMooseBase parent) -> Compartment
        __init__(self, Compartment src, string name, PyMooseBase parent) -> Compartment
        __init__(self, Compartment src, string name, Id parent) -> Compartment
        __init__(self, Id src, string name, Id parent) -> Compartment
        __init__(self, Compartment src, string path) -> Compartment
        """
        this = _moose.new_Compartment(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Compartment
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Compartment_getType(*args)

    def __get_Vm(*args):
        """__get_Vm(self) -> double"""
        return _moose.Compartment___get_Vm(*args)

    def __set_Vm(*args):
        """__set_Vm(self, double Vm)"""
        return _moose.Compartment___set_Vm(*args)

    def __get_Cm(*args):
        """__get_Cm(self) -> double"""
        return _moose.Compartment___get_Cm(*args)

    def __set_Cm(*args):
        """__set_Cm(self, double Cm)"""
        return _moose.Compartment___set_Cm(*args)

    def __get_Em(*args):
        """__get_Em(self) -> double"""
        return _moose.Compartment___get_Em(*args)

    def __set_Em(*args):
        """__set_Em(self, double Em)"""
        return _moose.Compartment___set_Em(*args)

    def __get_Im(*args):
        """__get_Im(self) -> double"""
        return _moose.Compartment___get_Im(*args)

    def __set_Im(*args):
        """__set_Im(self, double Im)"""
        return _moose.Compartment___set_Im(*args)

    def __get_inject(*args):
        """__get_inject(self) -> double"""
        return _moose.Compartment___get_inject(*args)

    def __set_inject(*args):
        """__set_inject(self, double inject)"""
        return _moose.Compartment___set_inject(*args)

    def __get_initVm(*args):
        """__get_initVm(self) -> double"""
        return _moose.Compartment___get_initVm(*args)

    def __set_initVm(*args):
        """__set_initVm(self, double initVm)"""
        return _moose.Compartment___set_initVm(*args)

    def __get_Rm(*args):
        """__get_Rm(self) -> double"""
        return _moose.Compartment___get_Rm(*args)

    def __set_Rm(*args):
        """__set_Rm(self, double Rm)"""
        return _moose.Compartment___set_Rm(*args)

    def __get_Ra(*args):
        """__get_Ra(self) -> double"""
        return _moose.Compartment___get_Ra(*args)

    def __set_Ra(*args):
        """__set_Ra(self, double Ra)"""
        return _moose.Compartment___set_Ra(*args)

    def __get_diameter(*args):
        """__get_diameter(self) -> double"""
        return _moose.Compartment___get_diameter(*args)

    def __set_diameter(*args):
        """__set_diameter(self, double diameter)"""
        return _moose.Compartment___set_diameter(*args)

    def __get_length(*args):
        """__get_length(self) -> double"""
        return _moose.Compartment___get_length(*args)

    def __set_length(*args):
        """__set_length(self, double length)"""
        return _moose.Compartment___set_length(*args)

    def __get_x(*args):
        """__get_x(self) -> double"""
        return _moose.Compartment___get_x(*args)

    def __set_x(*args):
        """__set_x(self, double x)"""
        return _moose.Compartment___set_x(*args)

    def __get_y(*args):
        """__get_y(self) -> double"""
        return _moose.Compartment___get_y(*args)

    def __set_y(*args):
        """__set_y(self, double y)"""
        return _moose.Compartment___set_y(*args)

    def __get_z(*args):
        """__get_z(self) -> double"""
        return _moose.Compartment___get_z(*args)

    def __set_z(*args):
        """__set_z(self, double z)"""
        return _moose.Compartment___set_z(*args)

    def __get_x0(*args):
        """__get_x0(self) -> double"""
        return _moose.Compartment___get_x0(*args)

    def __set_x0(*args):
        """__set_x0(self, double x)"""
        return _moose.Compartment___set_x0(*args)

    def __get_y0(*args):
        """__get_y0(self) -> double"""
        return _moose.Compartment___get_y0(*args)

    def __set_y0(*args):
        """__set_y0(self, double y)"""
        return _moose.Compartment___set_y0(*args)

    def __get_z0(*args):
        """__get_z0(self) -> double"""
        return _moose.Compartment___get_z0(*args)

    def __set_z0(*args):
        """__set_z0(self, double z)"""
        return _moose.Compartment___set_z0(*args)

    Vm = property(_moose.Compartment_Vm_get, _moose.Compartment_Vm_set)
    Cm = property(_moose.Compartment_Cm_get, _moose.Compartment_Cm_set)
    Em = property(_moose.Compartment_Em_get, _moose.Compartment_Em_set)
    Im = property(_moose.Compartment_Im_get, _moose.Compartment_Im_set)
    inject = property(_moose.Compartment_inject_get, _moose.Compartment_inject_set)
    initVm = property(_moose.Compartment_initVm_get, _moose.Compartment_initVm_set)
    Rm = property(_moose.Compartment_Rm_get, _moose.Compartment_Rm_set)
    Ra = property(_moose.Compartment_Ra_get, _moose.Compartment_Ra_set)
    diameter = property(_moose.Compartment_diameter_get, _moose.Compartment_diameter_set)
    length = property(_moose.Compartment_length_get, _moose.Compartment_length_set)
    x = property(_moose.Compartment_x_get, _moose.Compartment_x_set)
    y = property(_moose.Compartment_y_get, _moose.Compartment_y_set)
    z = property(_moose.Compartment_z_get, _moose.Compartment_z_set)
Compartment_swigregister = _moose.Compartment_swigregister
Compartment_swigregister(Compartment)
Compartment.className_ = _moose.cvar.Compartment_className_

class NeuroScan(PyMooseBase):
    """Proxy of C++ NeuroScan class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> NeuroScan
        __init__(self, string path) -> NeuroScan
        __init__(self, string name, Id parentId) -> NeuroScan
        __init__(self, string name, PyMooseBase parent) -> NeuroScan
        __init__(self, NeuroScan src, string name, PyMooseBase parent) -> NeuroScan
        __init__(self, NeuroScan src, string name, Id parent) -> NeuroScan
        __init__(self, NeuroScan src, string path) -> NeuroScan
        __init__(self, Id src, string name, Id parent) -> NeuroScan
        """
        this = _moose.new_NeuroScan(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_NeuroScan
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.NeuroScan_getType(*args)

    def __get_VDiv(*args):
        """__get_VDiv(self) -> int"""
        return _moose.NeuroScan___get_VDiv(*args)

    def __set_VDiv(*args):
        """__set_VDiv(self, int VDiv)"""
        return _moose.NeuroScan___set_VDiv(*args)

    def __get_VMin(*args):
        """__get_VMin(self) -> double"""
        return _moose.NeuroScan___get_VMin(*args)

    def __set_VMin(*args):
        """__set_VMin(self, double VMin)"""
        return _moose.NeuroScan___set_VMin(*args)

    def __get_VMax(*args):
        """__get_VMax(self) -> double"""
        return _moose.NeuroScan___get_VMax(*args)

    def __set_VMax(*args):
        """__set_VMax(self, double VMax)"""
        return _moose.NeuroScan___set_VMax(*args)

    def __get_CaDiv(*args):
        """__get_CaDiv(self) -> int"""
        return _moose.NeuroScan___get_CaDiv(*args)

    def __set_CaDiv(*args):
        """__set_CaDiv(self, int CaDiv)"""
        return _moose.NeuroScan___set_CaDiv(*args)

    def __get_CaMin(*args):
        """__get_CaMin(self) -> double"""
        return _moose.NeuroScan___get_CaMin(*args)

    def __set_CaMin(*args):
        """__set_CaMin(self, double CaMin)"""
        return _moose.NeuroScan___set_CaMin(*args)

    def __get_CaMax(*args):
        """__get_CaMax(self) -> double"""
        return _moose.NeuroScan___get_CaMax(*args)

    def __set_CaMax(*args):
        """__set_CaMax(self, double CaMax)"""
        return _moose.NeuroScan___set_CaMax(*args)

    VDiv = property(_moose.NeuroScan_VDiv_get, _moose.NeuroScan_VDiv_set)
    VMin = property(_moose.NeuroScan_VMin_get, _moose.NeuroScan_VMin_set)
    VMax = property(_moose.NeuroScan_VMax_get, _moose.NeuroScan_VMax_set)
    CaDiv = property(_moose.NeuroScan_CaDiv_get, _moose.NeuroScan_CaDiv_set)
    CaMin = property(_moose.NeuroScan_CaMin_get, _moose.NeuroScan_CaMin_set)
    CaMax = property(_moose.NeuroScan_CaMax_get, _moose.NeuroScan_CaMax_set)
NeuroScan_swigregister = _moose.NeuroScan_swigregister
NeuroScan_swigregister(NeuroScan)
NeuroScan.className_ = _moose.cvar.NeuroScan_className_

class HSolve(PyMooseBase):
    """Proxy of C++ HSolve class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> HSolve
        __init__(self, string path) -> HSolve
        __init__(self, string name, Id parentId) -> HSolve
        __init__(self, string name, PyMooseBase parent) -> HSolve
        __init__(self, HSolve src, string name, PyMooseBase parent) -> HSolve
        __init__(self, HSolve src, string name, Id parent) -> HSolve
        __init__(self, Id src, string name, Id parent) -> HSolve
        __init__(self, HSolve src, string path) -> HSolve
        """
        this = _moose.new_HSolve(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_HSolve
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.HSolve_getType(*args)

    def __get_seed_path(*args):
        """__get_seed_path(self) -> string"""
        return _moose.HSolve___get_seed_path(*args)

    def __set_seed_path(*args):
        """__set_seed_path(self, string path)"""
        return _moose.HSolve___set_seed_path(*args)

    def __get_NDiv(*args):
        """__get_NDiv(self) -> int"""
        return _moose.HSolve___get_NDiv(*args)

    def __set_NDiv(*args):
        """__set_NDiv(self, int NDiv)"""
        return _moose.HSolve___set_NDiv(*args)

    def __get_VLo(*args):
        """__get_VLo(self) -> double"""
        return _moose.HSolve___get_VLo(*args)

    def __set_VLo(*args):
        """__set_VLo(self, double VLo)"""
        return _moose.HSolve___set_VLo(*args)

    def __get_VHi(*args):
        """__get_VHi(self) -> double"""
        return _moose.HSolve___get_VHi(*args)

    def __set_VHi(*args):
        """__set_VHi(self, double VHi)"""
        return _moose.HSolve___set_VHi(*args)

    seedPath = property(_moose.HSolve_seedPath_get, _moose.HSolve_seedPath_set)
    NDiv = property(_moose.HSolve_NDiv_get, _moose.HSolve_NDiv_set)
    VLo = property(_moose.HSolve_VLo_get, _moose.HSolve_VLo_set)
    VHi = property(_moose.HSolve_VHi_get, _moose.HSolve_VHi_set)
HSolve_swigregister = _moose.HSolve_swigregister
HSolve_swigregister(HSolve)
HSolve.className_ = _moose.cvar.HSolve_className_

class Kintegrator(PyMooseBase):
    """Proxy of C++ Kintegrator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Kintegrator
        __init__(self, string path) -> Kintegrator
        __init__(self, string name, Id parentId) -> Kintegrator
        __init__(self, string name, PyMooseBase parent) -> Kintegrator
        __init__(self, Kintegrator src, string name, PyMooseBase parent) -> Kintegrator
        __init__(self, Kintegrator src, string name, Id parent) -> Kintegrator
        __init__(self, Id src, string name, Id parent) -> Kintegrator
        __init__(self, Kintegrator src, string path) -> Kintegrator
        """
        this = _moose.new_Kintegrator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Kintegrator
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Kintegrator_getType(*args)

    def __get_isInitiatilized(*args):
        """__get_isInitiatilized(self) -> bool"""
        return _moose.Kintegrator___get_isInitiatilized(*args)

    def __set_isInitiatilized(*args):
        """__set_isInitiatilized(self, bool isInitiatilized)"""
        return _moose.Kintegrator___set_isInitiatilized(*args)

    def imethod(*args):
        """
        imethod(self) -> string
        imethod(self, string ?) -> string
        """
        return _moose.Kintegrator_imethod(*args)

    isInitiatilized = property(_moose.Kintegrator_isInitiatilized_get, _moose.Kintegrator_isInitiatilized_set)
Kintegrator_swigregister = _moose.Kintegrator_swigregister
Kintegrator_swigregister(Kintegrator)
Kintegrator.className_ = _moose.cvar.Kintegrator_className_

class MathFunc(PyMooseBase):
    """Proxy of C++ MathFunc class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> MathFunc
        __init__(self, string path) -> MathFunc
        __init__(self, string name, Id parentId) -> MathFunc
        __init__(self, string name, PyMooseBase parent) -> MathFunc
        __init__(self, MathFunc src, string name, PyMooseBase parent) -> MathFunc
        __init__(self, MathFunc src, string name, Id parent) -> MathFunc
        __init__(self, MathFunc src, string path) -> MathFunc
        __init__(self, Id src, string name, Id parent) -> MathFunc
        """
        this = _moose.new_MathFunc(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_MathFunc
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.MathFunc_getType(*args)

    def __get_mathML(*args):
        """__get_mathML(self) -> string"""
        return _moose.MathFunc___get_mathML(*args)

    def __set_mathML(*args):
        """__set_mathML(self, string mathML)"""
        return _moose.MathFunc___set_mathML(*args)

    def __get_function(*args):
        """__get_function(self) -> string"""
        return _moose.MathFunc___get_function(*args)

    def __set_function(*args):
        """__set_function(self, string function)"""
        return _moose.MathFunc___set_function(*args)

    def __get_result(*args):
        """__get_result(self) -> double"""
        return _moose.MathFunc___get_result(*args)

    def __set_result(*args):
        """__set_result(self, double result)"""
        return _moose.MathFunc___set_result(*args)

    mathML = property(_moose.MathFunc_mathML_get, _moose.MathFunc_mathML_set)
    function = property(_moose.MathFunc_function_get, _moose.MathFunc_function_set)
    result = property(_moose.MathFunc_result_get, _moose.MathFunc_result_set)
MathFunc_swigregister = _moose.MathFunc_swigregister
MathFunc_swigregister(MathFunc)
MathFunc.className_ = _moose.cvar.MathFunc_className_

class Stoich(PyMooseBase):
    """Proxy of C++ Stoich class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Stoich
        __init__(self, string path) -> Stoich
        __init__(self, string name, Id parentId) -> Stoich
        __init__(self, string name, PyMooseBase parent) -> Stoich
        __init__(self, Stoich src, string name, PyMooseBase parent) -> Stoich
        __init__(self, Stoich src, string name, Id parent) -> Stoich
        __init__(self, Id src, string name, Id parent) -> Stoich
        __init__(self, Stoich src, string path) -> Stoich
        """
        this = _moose.new_Stoich(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Stoich
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Stoich_getType(*args)

    def __get_nMols(*args):
        """__get_nMols(self) -> unsigned int"""
        return _moose.Stoich___get_nMols(*args)

    def __set_nMols(*args):
        """__set_nMols(self, unsigned int nMols)"""
        return _moose.Stoich___set_nMols(*args)

    def __get_nVarMols(*args):
        """__get_nVarMols(self) -> unsigned int"""
        return _moose.Stoich___get_nVarMols(*args)

    def __set_nVarMols(*args):
        """__set_nVarMols(self, unsigned int nVarMols)"""
        return _moose.Stoich___set_nVarMols(*args)

    def __get_nSumTot(*args):
        """__get_nSumTot(self) -> unsigned int"""
        return _moose.Stoich___get_nSumTot(*args)

    def __set_nSumTot(*args):
        """__set_nSumTot(self, unsigned int nSumTot)"""
        return _moose.Stoich___set_nSumTot(*args)

    def __get_nBuffered(*args):
        """__get_nBuffered(self) -> unsigned int"""
        return _moose.Stoich___get_nBuffered(*args)

    def __set_nBuffered(*args):
        """__set_nBuffered(self, unsigned int nBuffered)"""
        return _moose.Stoich___set_nBuffered(*args)

    def __get_nReacs(*args):
        """__get_nReacs(self) -> unsigned int"""
        return _moose.Stoich___get_nReacs(*args)

    def __set_nReacs(*args):
        """__set_nReacs(self, unsigned int nReacs)"""
        return _moose.Stoich___set_nReacs(*args)

    def __get_nEnz(*args):
        """__get_nEnz(self) -> unsigned int"""
        return _moose.Stoich___get_nEnz(*args)

    def __set_nEnz(*args):
        """__set_nEnz(self, unsigned int nEnz)"""
        return _moose.Stoich___set_nEnz(*args)

    def __get_nMMenz(*args):
        """__get_nMMenz(self) -> unsigned int"""
        return _moose.Stoich___get_nMMenz(*args)

    def __set_nMMenz(*args):
        """__set_nMMenz(self, unsigned int nMMenz)"""
        return _moose.Stoich___set_nMMenz(*args)

    def __get_nExternalRates(*args):
        """__get_nExternalRates(self) -> unsigned int"""
        return _moose.Stoich___get_nExternalRates(*args)

    def __set_nExternalRates(*args):
        """__set_nExternalRates(self, unsigned int nExternalRates)"""
        return _moose.Stoich___set_nExternalRates(*args)

    def __get_useOneWayReacs(*args):
        """__get_useOneWayReacs(self) -> bool"""
        return _moose.Stoich___get_useOneWayReacs(*args)

    def __set_useOneWayReacs(*args):
        """__set_useOneWayReacs(self, bool useOneWayReacs)"""
        return _moose.Stoich___set_useOneWayReacs(*args)

    def path(*args):
        """
        path(self) -> string
        path(self, string path) -> string
        """
        return _moose.Stoich_path(*args)

    def __get_rateVectorSize(*args):
        """__get_rateVectorSize(self) -> unsigned int"""
        return _moose.Stoich___get_rateVectorSize(*args)

    def __set_rateVectorSize(*args):
        """__set_rateVectorSize(self, unsigned int rateVectorSize)"""
        return _moose.Stoich___set_rateVectorSize(*args)

    nMols = property(_moose.Stoich_nMols_get, _moose.Stoich_nMols_set)
    nVarMols = property(_moose.Stoich_nVarMols_get, _moose.Stoich_nVarMols_set)
    nSumTot = property(_moose.Stoich_nSumTot_get, _moose.Stoich_nSumTot_set)
    nBuffered = property(_moose.Stoich_nBuffered_get, _moose.Stoich_nBuffered_set)
    nReacs = property(_moose.Stoich_nReacs_get, _moose.Stoich_nReacs_set)
    nEnz = property(_moose.Stoich_nEnz_get, _moose.Stoich_nEnz_set)
    nMMenz = property(_moose.Stoich_nMMenz_get, _moose.Stoich_nMMenz_set)
    nExternalRates = property(_moose.Stoich_nExternalRates_get, _moose.Stoich_nExternalRates_set)
    useOneWayReacs = property(_moose.Stoich_useOneWayReacs_get, _moose.Stoich_useOneWayReacs_set)
    rateVectorSize = property(_moose.Stoich_rateVectorSize_get, _moose.Stoich_rateVectorSize_set)
Stoich_swigregister = _moose.Stoich_swigregister
Stoich_swigregister(Stoich)
Stoich.className_ = _moose.cvar.Stoich_className_

class KineticHub(PyMooseBase):
    """Proxy of C++ KineticHub class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> KineticHub
        __init__(self, string path) -> KineticHub
        __init__(self, string name, Id parentId) -> KineticHub
        __init__(self, string name, PyMooseBase parent) -> KineticHub
        __init__(self, KineticHub src, string name, PyMooseBase parent) -> KineticHub
        __init__(self, KineticHub src, string name, Id parent) -> KineticHub
        __init__(self, Id src, string name, Id parent) -> KineticHub
        __init__(self, KineticHub src, string path) -> KineticHub
        """
        this = _moose.new_KineticHub(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_KineticHub
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.KineticHub_getType(*args)

    def __get_nMol(*args):
        """__get_nMol(self) -> unsigned int"""
        return _moose.KineticHub___get_nMol(*args)

    def __set_nMol(*args):
        """__set_nMol(self, unsigned int nMol)"""
        return _moose.KineticHub___set_nMol(*args)

    def __get_nReac(*args):
        """__get_nReac(self) -> unsigned int"""
        return _moose.KineticHub___get_nReac(*args)

    def __set_nReac(*args):
        """__set_nReac(self, unsigned int nReac)"""
        return _moose.KineticHub___set_nReac(*args)

    def __get_nEnz(*args):
        """__get_nEnz(self) -> unsigned int"""
        return _moose.KineticHub___get_nEnz(*args)

    def __set_nEnz(*args):
        """__set_nEnz(self, unsigned int nEnz)"""
        return _moose.KineticHub___set_nEnz(*args)

    def destroy(*args):
        """destroy(self)"""
        return _moose.KineticHub_destroy(*args)

    def __get_molSum(*args):
        """__get_molSum(self) -> double"""
        return _moose.KineticHub___get_molSum(*args)

    def __set_molSum(*args):
        """__set_molSum(self, double molSum)"""
        return _moose.KineticHub___set_molSum(*args)

    nMol = property(_moose.KineticHub_nMol_get, _moose.KineticHub_nMol_set)
    nReac = property(_moose.KineticHub_nReac_get, _moose.KineticHub_nReac_set)
    nEnz = property(_moose.KineticHub_nEnz_get, _moose.KineticHub_nEnz_set)
    molSum = property(_moose.KineticHub_molSum_get, _moose.KineticHub_molSum_set)
KineticHub_swigregister = _moose.KineticHub_swigregister
KineticHub_swigregister(KineticHub)
KineticHub.className_ = _moose.cvar.KineticHub_className_

class Enzyme(PyMooseBase):
    """Proxy of C++ Enzyme class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Enzyme
        __init__(self, string path) -> Enzyme
        __init__(self, string name, Id parentId) -> Enzyme
        __init__(self, string name, PyMooseBase parent) -> Enzyme
        __init__(self, Enzyme src, string name, PyMooseBase parent) -> Enzyme
        __init__(self, Enzyme src, string name, Id parent) -> Enzyme
        __init__(self, Id src, string name, Id parent) -> Enzyme
        __init__(self, Enzyme src, string path) -> Enzyme
        """
        this = _moose.new_Enzyme(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Enzyme
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Enzyme_getType(*args)

    def __get_k1(*args):
        """__get_k1(self) -> double"""
        return _moose.Enzyme___get_k1(*args)

    def __set_k1(*args):
        """__set_k1(self, double k1)"""
        return _moose.Enzyme___set_k1(*args)

    def __get_k2(*args):
        """__get_k2(self) -> double"""
        return _moose.Enzyme___get_k2(*args)

    def __set_k2(*args):
        """__set_k2(self, double k2)"""
        return _moose.Enzyme___set_k2(*args)

    def __get_k3(*args):
        """__get_k3(self) -> double"""
        return _moose.Enzyme___get_k3(*args)

    def __set_k3(*args):
        """__set_k3(self, double k3)"""
        return _moose.Enzyme___set_k3(*args)

    def __get_Km(*args):
        """__get_Km(self) -> double"""
        return _moose.Enzyme___get_Km(*args)

    def __set_Km(*args):
        """__set_Km(self, double Km)"""
        return _moose.Enzyme___set_Km(*args)

    def __get_kcat(*args):
        """__get_kcat(self) -> double"""
        return _moose.Enzyme___get_kcat(*args)

    def __set_kcat(*args):
        """__set_kcat(self, double kcat)"""
        return _moose.Enzyme___set_kcat(*args)

    def __get_mode(*args):
        """__get_mode(self) -> bool"""
        return _moose.Enzyme___get_mode(*args)

    def __set_mode(*args):
        """__set_mode(self, bool mode)"""
        return _moose.Enzyme___set_mode(*args)

    def __get_scaleKm(*args):
        """__get_scaleKm(self) -> double"""
        return _moose.Enzyme___get_scaleKm(*args)

    def __set_scaleKm(*args):
        """__set_scaleKm(self, double scaleKm)"""
        return _moose.Enzyme___set_scaleKm(*args)

    def __get_scaleKcat(*args):
        """__get_scaleKcat(self) -> double"""
        return _moose.Enzyme___get_scaleKcat(*args)

    def __set_scaleKcat(*args):
        """__set_scaleKcat(self, double scaleKcat)"""
        return _moose.Enzyme___set_scaleKcat(*args)

    def __get_intramol(*args):
        """__get_intramol(self) -> double"""
        return _moose.Enzyme___get_intramol(*args)

    def __set_intramol(*args):
        """__set_intramol(self, double intramol)"""
        return _moose.Enzyme___set_intramol(*args)

    k1 = property(_moose.Enzyme_k1_get, _moose.Enzyme_k1_set)
    k2 = property(_moose.Enzyme_k2_get, _moose.Enzyme_k2_set)
    k3 = property(_moose.Enzyme_k3_get, _moose.Enzyme_k3_set)
    Km = property(_moose.Enzyme_Km_get, _moose.Enzyme_Km_set)
    kcat = property(_moose.Enzyme_kcat_get, _moose.Enzyme_kcat_set)
    mode = property(_moose.Enzyme_mode_get, _moose.Enzyme_mode_set)
Enzyme_swigregister = _moose.Enzyme_swigregister
Enzyme_swigregister(Enzyme)
Enzyme.className_ = _moose.cvar.Enzyme_className_

class Reaction(PyMooseBase):
    """Proxy of C++ Reaction class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Reaction
        __init__(self, string path) -> Reaction
        __init__(self, string name, Id parentId) -> Reaction
        __init__(self, string name, PyMooseBase parent) -> Reaction
        __init__(self, Reaction src, string name, PyMooseBase parent) -> Reaction
        __init__(self, Reaction src, string name, Id parent) -> Reaction
        __init__(self, Id src, string name, Id parent) -> Reaction
        __init__(self, Reaction src, string path) -> Reaction
        """
        this = _moose.new_Reaction(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Reaction
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Reaction_getType(*args)

    def __get_kf(*args):
        """__get_kf(self) -> double"""
        return _moose.Reaction___get_kf(*args)

    def __set_kf(*args):
        """__set_kf(self, double kf)"""
        return _moose.Reaction___set_kf(*args)

    def __get_kb(*args):
        """__get_kb(self) -> double"""
        return _moose.Reaction___get_kb(*args)

    def __set_kb(*args):
        """__set_kb(self, double kb)"""
        return _moose.Reaction___set_kb(*args)

    def __get_scaleKf(*args):
        """__get_scaleKf(self) -> double"""
        return _moose.Reaction___get_scaleKf(*args)

    def __set_scaleKf(*args):
        """__set_scaleKf(self, double scaleKf)"""
        return _moose.Reaction___set_scaleKf(*args)

    def __get_scaleKb(*args):
        """__get_scaleKb(self) -> double"""
        return _moose.Reaction___get_scaleKb(*args)

    def __set_scaleKb(*args):
        """__set_scaleKb(self, double scaleKb)"""
        return _moose.Reaction___set_scaleKb(*args)

    kf = property(_moose.Reaction_kf_get, _moose.Reaction_kf_set)
    kb = property(_moose.Reaction_kb_get, _moose.Reaction_kb_set)
    scaleKf = property(_moose.Reaction_scaleKf_get, _moose.Reaction_scaleKf_set)
    scaleKb = property(_moose.Reaction_scaleKb_get, _moose.Reaction_scaleKb_set)
Reaction_swigregister = _moose.Reaction_swigregister
Reaction_swigregister(Reaction)
Reaction.className_ = _moose.cvar.Reaction_className_

class Molecule(PyMooseBase):
    """Proxy of C++ Molecule class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Molecule
        __init__(self, string path) -> Molecule
        __init__(self, string name, Id parentId) -> Molecule
        __init__(self, string name, PyMooseBase parent) -> Molecule
        __init__(self, Molecule src, string name, PyMooseBase parent) -> Molecule
        __init__(self, Molecule src, string name, Id parent) -> Molecule
        __init__(self, Id src, string name, Id parent) -> Molecule
        __init__(self, Molecule src, string path) -> Molecule
        """
        this = _moose.new_Molecule(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Molecule
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Molecule_getType(*args)

    def __get_nInit(*args):
        """__get_nInit(self) -> double"""
        return _moose.Molecule___get_nInit(*args)

    def __set_nInit(*args):
        """__set_nInit(self, double nInit)"""
        return _moose.Molecule___set_nInit(*args)

    def __get_volumeScale(*args):
        """__get_volumeScale(self) -> double"""
        return _moose.Molecule___get_volumeScale(*args)

    def __set_volumeScale(*args):
        """__set_volumeScale(self, double volumeScale)"""
        return _moose.Molecule___set_volumeScale(*args)

    def __get_n(*args):
        """__get_n(self) -> double"""
        return _moose.Molecule___get_n(*args)

    def __set_n(*args):
        """__set_n(self, double n)"""
        return _moose.Molecule___set_n(*args)

    def __get_mode(*args):
        """__get_mode(self) -> int"""
        return _moose.Molecule___get_mode(*args)

    def __set_mode(*args):
        """__set_mode(self, int mode)"""
        return _moose.Molecule___set_mode(*args)

    def __get_slave_enable(*args):
        """__get_slave_enable(self) -> int"""
        return _moose.Molecule___get_slave_enable(*args)

    def __set_slave_enable(*args):
        """__set_slave_enable(self, int slave_enable)"""
        return _moose.Molecule___set_slave_enable(*args)

    def __get_conc(*args):
        """__get_conc(self) -> double"""
        return _moose.Molecule___get_conc(*args)

    def __set_conc(*args):
        """__set_conc(self, double conc)"""
        return _moose.Molecule___set_conc(*args)

    def __get_concInit(*args):
        """__get_concInit(self) -> double"""
        return _moose.Molecule___get_concInit(*args)

    def __set_concInit(*args):
        """__set_concInit(self, double concInit)"""
        return _moose.Molecule___set_concInit(*args)

    def __get_nSrc(*args):
        """__get_nSrc(self) -> double"""
        return _moose.Molecule___get_nSrc(*args)

    def __set_nSrc(*args):
        """__set_nSrc(self, double nSrc)"""
        return _moose.Molecule___set_nSrc(*args)

    def __get_sumTotal(*args):
        """__get_sumTotal(self) -> double"""
        return _moose.Molecule___get_sumTotal(*args)

    def __set_sumTotal(*args):
        """__set_sumTotal(self, double sumTotal)"""
        return _moose.Molecule___set_sumTotal(*args)

    nInit = property(_moose.Molecule_nInit_get, _moose.Molecule_nInit_set)
    volumeScale = property(_moose.Molecule_volumeScale_get, _moose.Molecule_volumeScale_set)
    n = property(_moose.Molecule_n_get, _moose.Molecule_n_set)
    mode = property(_moose.Molecule_mode_get, _moose.Molecule_mode_set)
    slave_enable = property(_moose.Molecule_slave_enable_get, _moose.Molecule_slave_enable_set)
    conc = property(_moose.Molecule_conc_get, _moose.Molecule_conc_set)
    concInit = property(_moose.Molecule_concInit_get, _moose.Molecule_concInit_set)
    nSrc = property(_moose.Molecule_nSrc_get, _moose.Molecule_nSrc_set)
    sumTotal = property(_moose.Molecule_sumTotal_get, _moose.Molecule_sumTotal_set)
Molecule_swigregister = _moose.Molecule_swigregister
Molecule_swigregister(Molecule)
Molecule.className_ = _moose.cvar.Molecule_className_


def mtrand(*args):
  """mtrand() -> double"""
  return _moose.mtrand(*args)

def mtseed(*args):
  """mtseed(long seed)"""
  return _moose.mtseed(*args)

def genrand_int32(*args):
  """genrand_int32() -> unsigned long"""
  return _moose.genrand_int32(*args)
class Probability(object):
    """Proxy of C++ Probability class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _moose.delete_Probability
    __del__ = lambda self : None;
    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Probability_getMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Probability_getVariance(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Probability_getNextSample(*args)

Probability_swigregister = _moose.Probability_swigregister
Probability_swigregister(Probability)

class Binomial(Probability):
    """Proxy of C++ Binomial class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> Binomial
        __init__(self, long n, double p) -> Binomial
        """
        this = _moose.new_Binomial(*args)
        try: self.this.append(this)
        except: self.this = this
    def getN(*args):
        """getN(self) -> long"""
        return _moose.Binomial_getN(*args)

    def getP(*args):
        """getP(self) -> double"""
        return _moose.Binomial_getP(*args)

    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Binomial_getMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Binomial_getVariance(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Binomial_getNextSample(*args)

    __swig_destroy__ = _moose.delete_Binomial
    __del__ = lambda self : None;
Binomial_swigregister = _moose.Binomial_swigregister
Binomial_swigregister(Binomial)

class Gamma(Probability):
    """Proxy of C++ Gamma class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, double alpha, double theta) -> Gamma"""
        this = _moose.new_Gamma(*args)
        try: self.this.append(this)
        except: self.this = this
    def getAlpha(*args):
        """getAlpha(self) -> double"""
        return _moose.Gamma_getAlpha(*args)

    def getTheta(*args):
        """getTheta(self) -> double"""
        return _moose.Gamma_getTheta(*args)

    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Gamma_getMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Gamma_getVariance(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Gamma_getNextSample(*args)

    __swig_destroy__ = _moose.delete_Gamma
    __del__ = lambda self : None;
Gamma_swigregister = _moose.Gamma_swigregister
Gamma_swigregister(Gamma)

ALIAS = _moose.ALIAS
BOX_MUELLER = _moose.BOX_MUELLER
ZIGGURAT = _moose.ZIGGURAT
class Normal(Probability):
    """Proxy of C++ Normal class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, double mean=0.0, double variance=1.0, NormalGenerator algorithm=ALIAS) -> Normal
        __init__(self, double mean=0.0, double variance=1.0) -> Normal
        __init__(self, double mean=0.0) -> Normal
        __init__(self) -> Normal
        """
        this = _moose.new_Normal(*args)
        try: self.this.append(this)
        except: self.this = this
    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Normal_getMean(*args)

    def setMean(*args):
        """setMean(self, double value)"""
        return _moose.Normal_setMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Normal_getVariance(*args)

    def setVariance(*args):
        """setVariance(self, double value)"""
        return _moose.Normal_setVariance(*args)

    def getMethod(*args):
        """getMethod(self) -> int"""
        return _moose.Normal_getMethod(*args)

    def setMethod(*args):
        """setMethod(self, NormalGenerator method)"""
        return _moose.Normal_setMethod(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Normal_getNextSample(*args)

    __swig_destroy__ = _moose.delete_Normal
    __del__ = lambda self : None;
Normal_swigregister = _moose.Normal_swigregister
Normal_swigregister(Normal)

class Poisson(Probability):
    """Proxy of C++ Poisson class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, double mean=1.0) -> Poisson
        __init__(self) -> Poisson
        """
        this = _moose.new_Poisson(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Poisson
    __del__ = lambda self : None;
    def setMean(*args):
        """setMean(self, double mean)"""
        return _moose.Poisson_setMean(*args)

    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Poisson_getMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Poisson_getVariance(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Poisson_getNextSample(*args)

Poisson_swigregister = _moose.Poisson_swigregister
Poisson_swigregister(Poisson)

LOGARITHMIC = _moose.LOGARITHMIC
RANDOM_MINIMIZATION = _moose.RANDOM_MINIMIZATION
class Exponential(Probability):
    """Proxy of C++ Exponential class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, double mean) -> Exponential
        __init__(self, ExponentialGenerator generator, double mean) -> Exponential
        """
        this = _moose.new_Exponential(*args)
        try: self.this.append(this)
        except: self.this = this
    def getMean(*args):
        """getMean(self) -> double"""
        return _moose.Exponential_getMean(*args)

    def getVariance(*args):
        """getVariance(self) -> double"""
        return _moose.Exponential_getVariance(*args)

    def getNextSample(*args):
        """getNextSample(self) -> double"""
        return _moose.Exponential_getNextSample(*args)

    __swig_destroy__ = _moose.delete_Exponential
    __del__ = lambda self : None;
Exponential_swigregister = _moose.Exponential_swigregister
Exponential_swigregister(Exponential)

class RandGenerator(PyMooseBase):
    """Proxy of C++ RandGenerator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> RandGenerator
        __init__(self, string className, string path) -> RandGenerator
        __init__(self, string className, string name, Id parentId) -> RandGenerator
        __init__(self, RandGenerator src, string name, PyMooseBase parent) -> RandGenerator
        __init__(self, RandGenerator src, string name, Id parent) -> RandGenerator
        __init__(self, Id src, string name, Id parent) -> RandGenerator
        __init__(self, RandGenerator src, string path) -> RandGenerator
        __init__(self, string className, string name, PyMooseBase parent) -> RandGenerator
        """
        this = _moose.new_RandGenerator(*args)
        try: self.this.append(this)
        except: self.this = this
    def getType(*args):
        """getType(self) -> string"""
        return _moose.RandGenerator_getType(*args)

    def __get_sample(*args):
        """__get_sample(self) -> double"""
        return _moose.RandGenerator___get_sample(*args)

    def __set_sample(*args):
        """__set_sample(self, double sample)"""
        return _moose.RandGenerator___set_sample(*args)

    def __get_mean(*args):
        """__get_mean(self) -> double"""
        return _moose.RandGenerator___get_mean(*args)

    def __set_mean(*args):
        """__set_mean(self, double mean)"""
        return _moose.RandGenerator___set_mean(*args)

    def __get_variance(*args):
        """__get_variance(self) -> double"""
        return _moose.RandGenerator___get_variance(*args)

    def __set_variance(*args):
        """__set_variance(self, double variance)"""
        return _moose.RandGenerator___set_variance(*args)

    def __get_output(*args):
        """__get_output(self) -> double"""
        return _moose.RandGenerator___get_output(*args)

    def __set_output(*args):
        """__set_output(self, double output)"""
        return _moose.RandGenerator___set_output(*args)

    sample = property(_moose.RandGenerator_sample_get, _moose.RandGenerator_sample_set)
    mean = property(_moose.RandGenerator_mean_get, _moose.RandGenerator_mean_set)
    variance = property(_moose.RandGenerator_variance_get, _moose.RandGenerator_variance_set)
    __swig_destroy__ = _moose.delete_RandGenerator
    __del__ = lambda self : None;
RandGenerator_swigregister = _moose.RandGenerator_swigregister
RandGenerator_swigregister(RandGenerator)
RandGenerator.className_ = _moose.cvar.RandGenerator_className_

class UniformRng(RandGenerator):
    """Proxy of C++ UniformRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> UniformRng
        __init__(self, string path) -> UniformRng
        __init__(self, string name, Id parentId) -> UniformRng
        __init__(self, string name, PyMooseBase parent) -> UniformRng
        __init__(self, UniformRng src, string name, PyMooseBase parent) -> UniformRng
        __init__(self, UniformRng src, string name, Id parent) -> UniformRng
        __init__(self, Id src, string name, Id parent) -> UniformRng
        __init__(self, UniformRng src, string path) -> UniformRng
        """
        this = _moose.new_UniformRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_UniformRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.UniformRng_getType(*args)

    def __get_min(*args):
        """__get_min(self) -> double"""
        return _moose.UniformRng___get_min(*args)

    def __set_min(*args):
        """__set_min(self, double min)"""
        return _moose.UniformRng___set_min(*args)

    def __get_max(*args):
        """__get_max(self) -> double"""
        return _moose.UniformRng___get_max(*args)

    def __set_max(*args):
        """__set_max(self, double max)"""
        return _moose.UniformRng___set_max(*args)

    mean = property(_moose.UniformRng_mean_get, _moose.UniformRng_mean_set)
    variance = property(_moose.UniformRng_variance_get, _moose.UniformRng_variance_set)
    min = property(_moose.UniformRng_min_get, _moose.UniformRng_min_set)
    max = property(_moose.UniformRng_max_get, _moose.UniformRng_max_set)
UniformRng_swigregister = _moose.UniformRng_swigregister
UniformRng_swigregister(UniformRng)
UniformRng.className_ = _moose.cvar.UniformRng_className_

class GammaRng(RandGenerator):
    """Proxy of C++ GammaRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> GammaRng
        __init__(self, string path) -> GammaRng
        __init__(self, string name, Id parentId) -> GammaRng
        __init__(self, string name, PyMooseBase parent) -> GammaRng
        __init__(self, GammaRng src, string name, PyMooseBase parent) -> GammaRng
        __init__(self, GammaRng src, string name, Id parent) -> GammaRng
        __init__(self, Id src, string name, Id parent) -> GammaRng
        __init__(self, GammaRng src, string path) -> GammaRng
        """
        this = _moose.new_GammaRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_GammaRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.GammaRng_getType(*args)

    def __get_alpha(*args):
        """__get_alpha(self) -> double"""
        return _moose.GammaRng___get_alpha(*args)

    def __set_alpha(*args):
        """__set_alpha(self, double alpha)"""
        return _moose.GammaRng___set_alpha(*args)

    def __get_theta(*args):
        """__get_theta(self) -> double"""
        return _moose.GammaRng___get_theta(*args)

    def __set_theta(*args):
        """__set_theta(self, double theta)"""
        return _moose.GammaRng___set_theta(*args)

    alpha = property(_moose.GammaRng_alpha_get, _moose.GammaRng_alpha_set)
    theta = property(_moose.GammaRng_theta_get, _moose.GammaRng_theta_set)
GammaRng_swigregister = _moose.GammaRng_swigregister
GammaRng_swigregister(GammaRng)
GammaRng.className_ = _moose.cvar.GammaRng_className_

class ExponentialRng(RandGenerator):
    """Proxy of C++ ExponentialRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> ExponentialRng
        __init__(self, string path) -> ExponentialRng
        __init__(self, string name, Id parentId) -> ExponentialRng
        __init__(self, string name, PyMooseBase parent) -> ExponentialRng
        __init__(self, ExponentialRng src, string name, PyMooseBase parent) -> ExponentialRng
        __init__(self, ExponentialRng src, string name, Id parent) -> ExponentialRng
        __init__(self, Id src, string name, Id parent) -> ExponentialRng
        __init__(self, ExponentialRng src, string path) -> ExponentialRng
        """
        this = _moose.new_ExponentialRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_ExponentialRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.ExponentialRng_getType(*args)

    def __set_mean(*args):
        """__set_mean(self, double mean)"""
        return _moose.ExponentialRng___set_mean(*args)

    def __get_method(*args):
        """__get_method(self) -> int"""
        return _moose.ExponentialRng___get_method(*args)

    def __set_method(*args):
        """__set_method(self, int method)"""
        return _moose.ExponentialRng___set_method(*args)

    mean = property(_moose.ExponentialRng_mean_get, _moose.ExponentialRng_mean_set)
    method = property(_moose.ExponentialRng_method_get, _moose.ExponentialRng_method_set)
ExponentialRng_swigregister = _moose.ExponentialRng_swigregister
ExponentialRng_swigregister(ExponentialRng)
ExponentialRng.className_ = _moose.cvar.ExponentialRng_className_

class BinomialRng(RandGenerator):
    """Proxy of C++ BinomialRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> BinomialRng
        __init__(self, string path) -> BinomialRng
        __init__(self, string name, Id parentId) -> BinomialRng
        __init__(self, string name, PyMooseBase parent) -> BinomialRng
        __init__(self, BinomialRng src, string name, PyMooseBase parent) -> BinomialRng
        __init__(self, BinomialRng src, string name, Id parent) -> BinomialRng
        __init__(self, Id src, string name, Id parent) -> BinomialRng
        __init__(self, BinomialRng src, string path) -> BinomialRng
        """
        this = _moose.new_BinomialRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_BinomialRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.BinomialRng_getType(*args)

    def __get_n(*args):
        """__get_n(self) -> int"""
        return _moose.BinomialRng___get_n(*args)

    def __set_n(*args):
        """__set_n(self, int n)"""
        return _moose.BinomialRng___set_n(*args)

    def __get_p(*args):
        """__get_p(self) -> double"""
        return _moose.BinomialRng___get_p(*args)

    def __set_p(*args):
        """__set_p(self, double p)"""
        return _moose.BinomialRng___set_p(*args)

    n = property(_moose.BinomialRng_n_get, _moose.BinomialRng_n_set)
    p = property(_moose.BinomialRng_p_get, _moose.BinomialRng_p_set)
BinomialRng_swigregister = _moose.BinomialRng_swigregister
BinomialRng_swigregister(BinomialRng)
BinomialRng.className_ = _moose.cvar.BinomialRng_className_

class PoissonRng(RandGenerator):
    """Proxy of C++ PoissonRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> PoissonRng
        __init__(self, string path) -> PoissonRng
        __init__(self, string name, Id parentId) -> PoissonRng
        __init__(self, string name, PyMooseBase parent) -> PoissonRng
        __init__(self, PoissonRng src, string name, PyMooseBase parent) -> PoissonRng
        __init__(self, PoissonRng src, string name, Id parent) -> PoissonRng
        __init__(self, Id src, string name, Id parent) -> PoissonRng
        __init__(self, PoissonRng src, string path) -> PoissonRng
        """
        this = _moose.new_PoissonRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_PoissonRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.PoissonRng_getType(*args)

    def __set_mean(*args):
        """__set_mean(self, double mean)"""
        return _moose.PoissonRng___set_mean(*args)

    mean = property(_moose.PoissonRng_mean_get, _moose.PoissonRng_mean_set)
PoissonRng_swigregister = _moose.PoissonRng_swigregister
PoissonRng_swigregister(PoissonRng)
PoissonRng.className_ = _moose.cvar.PoissonRng_className_

class NormalRng(RandGenerator):
    """Proxy of C++ NormalRng class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> NormalRng
        __init__(self, string path) -> NormalRng
        __init__(self, string name, Id parentId) -> NormalRng
        __init__(self, string name, PyMooseBase parent) -> NormalRng
        __init__(self, NormalRng src, string name, PyMooseBase parent) -> NormalRng
        __init__(self, NormalRng src, string name, Id parent) -> NormalRng
        __init__(self, Id src, string name, Id parent) -> NormalRng
        __init__(self, NormalRng src, string path) -> NormalRng
        """
        this = _moose.new_NormalRng(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_NormalRng
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.NormalRng_getType(*args)

    def __set_mean(*args):
        """__set_mean(self, double mean)"""
        return _moose.NormalRng___set_mean(*args)

    def __set_variance(*args):
        """__set_variance(self, double variance)"""
        return _moose.NormalRng___set_variance(*args)

    def __get_method(*args):
        """__get_method(self) -> int"""
        return _moose.NormalRng___get_method(*args)

    def __set_method(*args):
        """__set_method(self, int method)"""
        return _moose.NormalRng___set_method(*args)

    mean = property(_moose.NormalRng_mean_get, _moose.NormalRng_mean_set)
    variance = property(_moose.NormalRng_variance_get, _moose.NormalRng_variance_set)
    method = property(_moose.NormalRng_method_get, _moose.NormalRng_method_set)
NormalRng_swigregister = _moose.NormalRng_swigregister
NormalRng_swigregister(NormalRng)
NormalRng.className_ = _moose.cvar.NormalRng_className_

class KineticManager(PyMooseBase):
    """Proxy of C++ KineticManager class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> KineticManager
        __init__(self, string path) -> KineticManager
        __init__(self, string name, Id parentId) -> KineticManager
        __init__(self, string name, PyMooseBase parent) -> KineticManager
        __init__(self, KineticManager src, string name, PyMooseBase parent) -> KineticManager
        __init__(self, KineticManager src, string name, Id parent) -> KineticManager
        __init__(self, KineticManager src, string path) -> KineticManager
        __init__(self, Id src, string name, Id parent) -> KineticManager
        """
        this = _moose.new_KineticManager(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_KineticManager
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.KineticManager_getType(*args)

    def __get_autoMode(*args):
        """__get_autoMode(self) -> bool"""
        return _moose.KineticManager___get_autoMode(*args)

    def __set_autoMode(*args):
        """__set_autoMode(self, bool autoMode)"""
        return _moose.KineticManager___set_autoMode(*args)

    def __get_stochastic(*args):
        """__get_stochastic(self) -> bool"""
        return _moose.KineticManager___get_stochastic(*args)

    def __set_stochastic(*args):
        """__set_stochastic(self, bool stochastic)"""
        return _moose.KineticManager___set_stochastic(*args)

    def __get_spatial(*args):
        """__get_spatial(self) -> bool"""
        return _moose.KineticManager___get_spatial(*args)

    def __set_spatial(*args):
        """__set_spatial(self, bool spatial)"""
        return _moose.KineticManager___set_spatial(*args)

    def __get_method(*args):
        """__get_method(self) -> string"""
        return _moose.KineticManager___get_method(*args)

    def __set_method(*args):
        """__set_method(self, string method)"""
        return _moose.KineticManager___set_method(*args)

    def __get_variableDt(*args):
        """__get_variableDt(self) -> bool"""
        return _moose.KineticManager___get_variableDt(*args)

    def __get_singleParticle(*args):
        """__get_singleParticle(self) -> bool"""
        return _moose.KineticManager___get_singleParticle(*args)

    def __get_multiscale(*args):
        """__get_multiscale(self) -> bool"""
        return _moose.KineticManager___get_multiscale(*args)

    def __get_implicit(*args):
        """__get_implicit(self) -> bool"""
        return _moose.KineticManager___get_implicit(*args)

    def __get_description(*args):
        """__get_description(self) -> string"""
        return _moose.KineticManager___get_description(*args)

    def __get_recommendedDt(*args):
        """__get_recommendedDt(self) -> double"""
        return _moose.KineticManager___get_recommendedDt(*args)

    def __get_eulerError(*args):
        """__get_eulerError(self) -> double"""
        return _moose.KineticManager___get_eulerError(*args)

    def __set_eulerError(*args):
        """__set_eulerError(self, double eulerError)"""
        return _moose.KineticManager___set_eulerError(*args)

    autoMode = property(_moose.KineticManager_autoMode_get, _moose.KineticManager_autoMode_set)
    stochastic = property(_moose.KineticManager_stochastic_get, _moose.KineticManager_stochastic_set)
    spatial = property(_moose.KineticManager_spatial_get, _moose.KineticManager_spatial_set)
    method = property(_moose.KineticManager_method_get, _moose.KineticManager_method_set)
    variableDt = property(_moose.KineticManager_variableDt_get, _moose.KineticManager_variableDt_set)
    singleParticle = property(_moose.KineticManager_singleParticle_get, _moose.KineticManager_singleParticle_set)
    multiscale = property(_moose.KineticManager_multiscale_get, _moose.KineticManager_multiscale_set)
    implicit = property(_moose.KineticManager_implicit_get, _moose.KineticManager_implicit_set)
    description = property(_moose.KineticManager_description_get, _moose.KineticManager_description_set)
    recommendedDt = property(_moose.KineticManager_recommendedDt_get, _moose.KineticManager_recommendedDt_set)
    eulerError = property(_moose.KineticManager_eulerError_get, _moose.KineticManager_eulerError_set)
KineticManager_swigregister = _moose.KineticManager_swigregister
KineticManager_swigregister(KineticManager)
KineticManager.className_ = _moose.cvar.KineticManager_className_

class KinCompt(PyMooseBase):
    """Proxy of C++ KinCompt class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> KinCompt
        __init__(self, string path) -> KinCompt
        __init__(self, string name, Id parentId) -> KinCompt
        __init__(self, string name, PyMooseBase parent) -> KinCompt
        __init__(self, KinCompt src, string name, PyMooseBase parent) -> KinCompt
        __init__(self, KinCompt src, string name, Id parent) -> KinCompt
        __init__(self, KinCompt src, string path) -> KinCompt
        __init__(self, Id src, string name, Id parent) -> KinCompt
        """
        this = _moose.new_KinCompt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_KinCompt
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.KinCompt_getType(*args)

    def __get_volume(*args):
        """__get_volume(self) -> double"""
        return _moose.KinCompt___get_volume(*args)

    def __set_volume(*args):
        """__set_volume(self, double volume)"""
        return _moose.KinCompt___set_volume(*args)

    def __get_area(*args):
        """__get_area(self) -> double"""
        return _moose.KinCompt___get_area(*args)

    def __set_area(*args):
        """__set_area(self, double area)"""
        return _moose.KinCompt___set_area(*args)

    def __get_perimeter(*args):
        """__get_perimeter(self) -> double"""
        return _moose.KinCompt___get_perimeter(*args)

    def __set_perimeter(*args):
        """__set_perimeter(self, double perimeter)"""
        return _moose.KinCompt___set_perimeter(*args)

    def __get_size(*args):
        """__get_size(self) -> double"""
        return _moose.KinCompt___get_size(*args)

    def __set_size(*args):
        """__set_size(self, double size)"""
        return _moose.KinCompt___set_size(*args)

    def __get_numDimensions(*args):
        """__get_numDimensions(self) -> unsigned int"""
        return _moose.KinCompt___get_numDimensions(*args)

    def __set_numDimensions(*args):
        """__set_numDimensions(self, unsigned int numDimensions)"""
        return _moose.KinCompt___set_numDimensions(*args)

    volume = property(_moose.KinCompt_volume_get, _moose.KinCompt_volume_set)
    area = property(_moose.KinCompt_area_get, _moose.KinCompt_area_set)
    perimeter = property(_moose.KinCompt_perimeter_get, _moose.KinCompt_perimeter_set)
    size = property(_moose.KinCompt_size_get, _moose.KinCompt_size_set)
    numDimensions = property(_moose.KinCompt_numDimensions_get, _moose.KinCompt_numDimensions_set)
KinCompt_swigregister = _moose.KinCompt_swigregister
KinCompt_swigregister(KinCompt)
KinCompt.className_ = _moose.cvar.KinCompt_className_

class Panel(PyMooseBase):
    """Proxy of C++ Panel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Panel
        __init__(self, string path) -> Panel
        __init__(self, string name, Id parentId) -> Panel
        __init__(self, string name, PyMooseBase parent) -> Panel
        __init__(self, Panel src, string name, PyMooseBase parent) -> Panel
        __init__(self, Panel src, string name, Id parent) -> Panel
        __init__(self, Panel src, string path) -> Panel
        __init__(self, Id src, string name, Id parent) -> Panel
        __init__(self, string typeName, string objectName, Id parentId) -> Panel
        __init__(self, string typeName, string path) -> Panel
        __init__(self, string typeName, string objectName, PyMooseBase parent) -> Panel
        """
        this = _moose.new_Panel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Panel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Panel_getType(*args)

    def __get_nPts(*args):
        """__get_nPts(self) -> unsigned int"""
        return _moose.Panel___get_nPts(*args)

    def __get_nDims(*args):
        """__get_nDims(self) -> unsigned int"""
        return _moose.Panel___get_nDims(*args)

    def __get_nNeighbors(*args):
        """__get_nNeighbors(self) -> unsigned int"""
        return _moose.Panel___get_nNeighbors(*args)

    def __get_shapeId(*args):
        """__get_shapeId(self) -> unsigned int"""
        return _moose.Panel___get_shapeId(*args)

    def __get_coords(*args):
        """__get_coords(self) -> double_vector"""
        return _moose.Panel___get_coords(*args)

    nPts = property(_moose.Panel_nPts_get, _moose.Panel_nPts_set)
    nDims = property(_moose.Panel_nDims_get, _moose.Panel_nDims_set)
    nNeighbors = property(_moose.Panel_nNeighbors_get, _moose.Panel_nNeighbors_set)
    shapeId = property(_moose.Panel_shapeId_get, _moose.Panel_shapeId_set)
    coords = property(_moose.Panel_coords_get)
Panel_swigregister = _moose.Panel_swigregister
Panel_swigregister(Panel)
Panel.className_ = _moose.cvar.Panel_className_

class DiskPanel(Panel):
    """Proxy of C++ DiskPanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> DiskPanel
        __init__(self, string path) -> DiskPanel
        __init__(self, string name, Id parentId) -> DiskPanel
        __init__(self, string name, PyMooseBase parent) -> DiskPanel
        __init__(self, DiskPanel src, string name, PyMooseBase parent) -> DiskPanel
        __init__(self, DiskPanel src, string name, Id parent) -> DiskPanel
        __init__(self, DiskPanel src, string path) -> DiskPanel
        __init__(self, Id src, string name, Id parent) -> DiskPanel
        """
        this = _moose.new_DiskPanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_DiskPanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.DiskPanel_getType(*args)

DiskPanel_swigregister = _moose.DiskPanel_swigregister
DiskPanel_swigregister(DiskPanel)
DiskPanel.className_ = _moose.cvar.DiskPanel_className_

class CylPanel(Panel):
    """Proxy of C++ CylPanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> CylPanel
        __init__(self, string path) -> CylPanel
        __init__(self, string name, Id parentId) -> CylPanel
        __init__(self, string name, PyMooseBase parent) -> CylPanel
        __init__(self, CylPanel src, string name, PyMooseBase parent) -> CylPanel
        __init__(self, CylPanel src, string name, Id parent) -> CylPanel
        __init__(self, CylPanel src, string path) -> CylPanel
        __init__(self, Id src, string name, Id parent) -> CylPanel
        """
        this = _moose.new_CylPanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_CylPanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.CylPanel_getType(*args)

CylPanel_swigregister = _moose.CylPanel_swigregister
CylPanel_swigregister(CylPanel)
CylPanel.className_ = _moose.cvar.CylPanel_className_

class HemispherePanel(Panel):
    """Proxy of C++ HemispherePanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> HemispherePanel
        __init__(self, string path) -> HemispherePanel
        __init__(self, string name, Id parentId) -> HemispherePanel
        __init__(self, string name, PyMooseBase parent) -> HemispherePanel
        __init__(self, HemispherePanel src, string name, PyMooseBase parent) -> HemispherePanel
        __init__(self, HemispherePanel src, string name, Id parent) -> HemispherePanel
        __init__(self, HemispherePanel src, string path) -> HemispherePanel
        __init__(self, Id src, string name, Id parent) -> HemispherePanel
        """
        this = _moose.new_HemispherePanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_HemispherePanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.HemispherePanel_getType(*args)

HemispherePanel_swigregister = _moose.HemispherePanel_swigregister
HemispherePanel_swigregister(HemispherePanel)
HemispherePanel.className_ = _moose.cvar.HemispherePanel_className_

class SpherePanel(Panel):
    """Proxy of C++ SpherePanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> SpherePanel
        __init__(self, string path) -> SpherePanel
        __init__(self, string name, Id parentId) -> SpherePanel
        __init__(self, string name, PyMooseBase parent) -> SpherePanel
        __init__(self, SpherePanel src, string name, PyMooseBase parent) -> SpherePanel
        __init__(self, SpherePanel src, string name, Id parent) -> SpherePanel
        __init__(self, SpherePanel src, string path) -> SpherePanel
        __init__(self, Id src, string name, Id parent) -> SpherePanel
        """
        this = _moose.new_SpherePanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_SpherePanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.SpherePanel_getType(*args)

SpherePanel_swigregister = _moose.SpherePanel_swigregister
SpherePanel_swigregister(SpherePanel)
SpherePanel.className_ = _moose.cvar.SpherePanel_className_

class TriPanel(Panel):
    """Proxy of C++ TriPanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> TriPanel
        __init__(self, string path) -> TriPanel
        __init__(self, string name, Id parentId) -> TriPanel
        __init__(self, string name, PyMooseBase parent) -> TriPanel
        __init__(self, TriPanel src, string name, PyMooseBase parent) -> TriPanel
        __init__(self, TriPanel src, string name, Id parent) -> TriPanel
        __init__(self, TriPanel src, string path) -> TriPanel
        __init__(self, Id src, string name, Id parent) -> TriPanel
        """
        this = _moose.new_TriPanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_TriPanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.TriPanel_getType(*args)

TriPanel_swigregister = _moose.TriPanel_swigregister
TriPanel_swigregister(TriPanel)
TriPanel.className_ = _moose.cvar.TriPanel_className_

class RectPanel(Panel):
    """Proxy of C++ RectPanel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> RectPanel
        __init__(self, string path) -> RectPanel
        __init__(self, string name, Id parentId) -> RectPanel
        __init__(self, string name, PyMooseBase parent) -> RectPanel
        __init__(self, RectPanel src, string name, PyMooseBase parent) -> RectPanel
        __init__(self, RectPanel src, string name, Id parent) -> RectPanel
        __init__(self, RectPanel src, string path) -> RectPanel
        __init__(self, Id src, string name, Id parent) -> RectPanel
        """
        this = _moose.new_RectPanel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_RectPanel
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.RectPanel_getType(*args)

RectPanel_swigregister = _moose.RectPanel_swigregister
RectPanel_swigregister(RectPanel)
RectPanel.className_ = _moose.cvar.RectPanel_className_

class Surface(PyMooseBase):
    """Proxy of C++ Surface class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Surface
        __init__(self, string path) -> Surface
        __init__(self, string name, Id parentId) -> Surface
        __init__(self, string name, PyMooseBase parent) -> Surface
        __init__(self, Surface src, string name, PyMooseBase parent) -> Surface
        __init__(self, Surface src, string name, Id parent) -> Surface
        __init__(self, Surface src, string path) -> Surface
        __init__(self, Id src, string name, Id parent) -> Surface
        """
        this = _moose.new_Surface(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Surface
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Surface_getType(*args)

    def __get_volume(*args):
        """__get_volume(self) -> double"""
        return _moose.Surface___get_volume(*args)

    volume = property(_moose.Surface_volume_get, _moose.Surface_volume_set)
Surface_swigregister = _moose.Surface_swigregister
Surface_swigregister(Surface)
Surface.className_ = _moose.cvar.Surface_className_

class Geometry(PyMooseBase):
    """Proxy of C++ Geometry class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> Geometry
        __init__(self, string path) -> Geometry
        __init__(self, string name, Id parentId) -> Geometry
        __init__(self, string name, PyMooseBase parent) -> Geometry
        __init__(self, Geometry src, string name, PyMooseBase parent) -> Geometry
        __init__(self, Geometry src, string name, Id parent) -> Geometry
        __init__(self, Geometry src, string path) -> Geometry
        __init__(self, Id src, string name, Id parent) -> Geometry
        """
        this = _moose.new_Geometry(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_Geometry
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.Geometry_getType(*args)

    def __get_epsilon(*args):
        """__get_epsilon(self) -> double"""
        return _moose.Geometry___get_epsilon(*args)

    def __set_epsilon(*args):
        """__set_epsilon(self, double epsilon)"""
        return _moose.Geometry___set_epsilon(*args)

    def __get_neighdist(*args):
        """__get_neighdist(self) -> double"""
        return _moose.Geometry___get_neighdist(*args)

    def __set_neighdist(*args):
        """__set_neighdist(self, double neighdist)"""
        return _moose.Geometry___set_neighdist(*args)

    epsilon = property(_moose.Geometry_epsilon_get, _moose.Geometry_epsilon_set)
    neighdist = property(_moose.Geometry_neighdist_get, _moose.Geometry_neighdist_set)
Geometry_swigregister = _moose.Geometry_swigregister
Geometry_swigregister(Geometry)
Geometry.className_ = _moose.cvar.Geometry_className_

class AscFile(PyMooseBase):
    """Proxy of C++ AscFile class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> AscFile
        __init__(self, string path) -> AscFile
        __init__(self, string name, Id parentId) -> AscFile
        __init__(self, string name, PyMooseBase parent) -> AscFile
        __init__(self, AscFile src, string name, PyMooseBase parent) -> AscFile
        __init__(self, AscFile src, string name, Id parent) -> AscFile
        __init__(self, AscFile src, string path) -> AscFile
        __init__(self, Id src, string name, Id parent) -> AscFile
        """
        this = _moose.new_AscFile(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_AscFile
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.AscFile_getType(*args)

    def __get_fileName(*args):
        """__get_fileName(self) -> string"""
        return _moose.AscFile___get_fileName(*args)

    def __set_fileName(*args):
        """__set_fileName(self, string fileName)"""
        return _moose.AscFile___set_fileName(*args)

    def __get_appendFlag(*args):
        """__get_appendFlag(self) -> int"""
        return _moose.AscFile___get_appendFlag(*args)

    def __set_appendFlag(*args):
        """__set_appendFlag(self, int appendFlag)"""
        return _moose.AscFile___set_appendFlag(*args)

    fileName = property(_moose.AscFile_fileName_get, _moose.AscFile_fileName_set)
    appendFlag = property(_moose.AscFile_appendFlag_get, _moose.AscFile_appendFlag_set)
AscFile_swigregister = _moose.AscFile_swigregister
AscFile_swigregister(AscFile)
AscFile.className_ = _moose.cvar.AscFile_className_

class DifShell(PyMooseBase):
    """Proxy of C++ DifShell class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> DifShell
        __init__(self, string path) -> DifShell
        __init__(self, string name, Id parentId) -> DifShell
        __init__(self, string name, PyMooseBase parent) -> DifShell
        __init__(self, DifShell src, string name, PyMooseBase parent) -> DifShell
        __init__(self, DifShell src, string name, Id parent) -> DifShell
        __init__(self, DifShell src, string path) -> DifShell
        __init__(self, Id src, string name, Id parent) -> DifShell
        """
        this = _moose.new_DifShell(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_DifShell
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.DifShell_getType(*args)

    def __get_C(*args):
        """__get_C(self) -> double"""
        return _moose.DifShell___get_C(*args)

    def __get_Ceq(*args):
        """__get_Ceq(self) -> double"""
        return _moose.DifShell___get_Ceq(*args)

    def __set_Ceq(*args):
        """__set_Ceq(self, double Ceq)"""
        return _moose.DifShell___set_Ceq(*args)

    def __get_D(*args):
        """__get_D(self) -> double"""
        return _moose.DifShell___get_D(*args)

    def __set_D(*args):
        """__set_D(self, double D)"""
        return _moose.DifShell___set_D(*args)

    def __get_valence(*args):
        """__get_valence(self) -> double"""
        return _moose.DifShell___get_valence(*args)

    def __set_valence(*args):
        """__set_valence(self, double valence)"""
        return _moose.DifShell___set_valence(*args)

    def __get_leak(*args):
        """__get_leak(self) -> double"""
        return _moose.DifShell___get_leak(*args)

    def __set_leak(*args):
        """__set_leak(self, double leak)"""
        return _moose.DifShell___set_leak(*args)

    def __get_shapeMode(*args):
        """__get_shapeMode(self) -> unsigned int"""
        return _moose.DifShell___get_shapeMode(*args)

    def __set_shapeMode(*args):
        """__set_shapeMode(self, unsigned int shapeMode)"""
        return _moose.DifShell___set_shapeMode(*args)

    def __get_length(*args):
        """__get_length(self) -> double"""
        return _moose.DifShell___get_length(*args)

    def __set_length(*args):
        """__set_length(self, double length)"""
        return _moose.DifShell___set_length(*args)

    def __get_diameter(*args):
        """__get_diameter(self) -> double"""
        return _moose.DifShell___get_diameter(*args)

    def __set_diameter(*args):
        """__set_diameter(self, double diameter)"""
        return _moose.DifShell___set_diameter(*args)

    def __get_thickness(*args):
        """__get_thickness(self) -> double"""
        return _moose.DifShell___get_thickness(*args)

    def __set_thickness(*args):
        """__set_thickness(self, double thickness)"""
        return _moose.DifShell___set_thickness(*args)

    def __get_volume(*args):
        """__get_volume(self) -> double"""
        return _moose.DifShell___get_volume(*args)

    def __set_volume(*args):
        """__set_volume(self, double volume)"""
        return _moose.DifShell___set_volume(*args)

    def __get_outerArea(*args):
        """__get_outerArea(self) -> double"""
        return _moose.DifShell___get_outerArea(*args)

    def __set_outerArea(*args):
        """__set_outerArea(self, double outerArea)"""
        return _moose.DifShell___set_outerArea(*args)

    def __get_innerArea(*args):
        """__get_innerArea(self) -> double"""
        return _moose.DifShell___get_innerArea(*args)

    def __set_innerArea(*args):
        """__set_innerArea(self, double innerArea)"""
        return _moose.DifShell___set_innerArea(*args)

    C = property(_moose.DifShell_C_get, _moose.DifShell_C_set)
    Ceq = property(_moose.DifShell_Ceq_get, _moose.DifShell_Ceq_set)
    D = property(_moose.DifShell_D_get, _moose.DifShell_D_set)
    valence = property(_moose.DifShell_valence_get, _moose.DifShell_valence_set)
    leak = property(_moose.DifShell_leak_get, _moose.DifShell_leak_set)
    shapeMode = property(_moose.DifShell_shapeMode_get, _moose.DifShell_shapeMode_set)
    length = property(_moose.DifShell_length_get, _moose.DifShell_length_set)
    diameter = property(_moose.DifShell_diameter_get, _moose.DifShell_diameter_set)
    thickness = property(_moose.DifShell_thickness_get, _moose.DifShell_thickness_set)
    volume = property(_moose.DifShell_volume_get, _moose.DifShell_volume_set)
    outerArea = property(_moose.DifShell_outerArea_get, _moose.DifShell_outerArea_set)
    innerArea = property(_moose.DifShell_innerArea_get, _moose.DifShell_innerArea_set)
DifShell_swigregister = _moose.DifShell_swigregister
DifShell_swigregister(DifShell)
DifShell.className_ = _moose.cvar.DifShell_className_

class GssaStoich(PyMooseBase):
    """Proxy of C++ GssaStoich class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> GssaStoich
        __init__(self, string path) -> GssaStoich
        __init__(self, string name, Id parentId) -> GssaStoich
        __init__(self, string name, PyMooseBase parent) -> GssaStoich
        __init__(self, GssaStoich src, string name, PyMooseBase parent) -> GssaStoich
        __init__(self, GssaStoich src, string name, Id parent) -> GssaStoich
        __init__(self, GssaStoich src, string path) -> GssaStoich
        __init__(self, Id src, string name, Id parent) -> GssaStoich
        """
        this = _moose.new_GssaStoich(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_GssaStoich
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.GssaStoich_getType(*args)

    def __get_method(*args):
        """__get_method(self) -> string"""
        return _moose.GssaStoich___get_method(*args)

    def __set_method(*args):
        """__set_method(self, string method)"""
        return _moose.GssaStoich___set_method(*args)

    def __set_path(*args):
        """__set_path(self, string path)"""
        return _moose.GssaStoich___set_path(*args)

    method = property(_moose.GssaStoich_method_get, _moose.GssaStoich_method_set)
    path = property(_moose.GssaStoich_path_get, _moose.GssaStoich_path_set)
GssaStoich_swigregister = _moose.GssaStoich_swigregister
GssaStoich_swigregister(GssaStoich)
GssaStoich.className_ = _moose.cvar.GssaStoich_className_

class TauPump(PyMooseBase):
    """Proxy of C++ TauPump class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> TauPump
        __init__(self, string path) -> TauPump
        __init__(self, string name, Id parentId) -> TauPump
        __init__(self, string name, PyMooseBase parent) -> TauPump
        __init__(self, TauPump src, string name, PyMooseBase parent) -> TauPump
        __init__(self, TauPump src, string name, Id parent) -> TauPump
        __init__(self, TauPump src, string path) -> TauPump
        __init__(self, Id src, string name, Id parent) -> TauPump
        """
        this = _moose.new_TauPump(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_TauPump
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.TauPump_getType(*args)

    def __get_pumpRate(*args):
        """__get_pumpRate(self) -> double"""
        return _moose.TauPump___get_pumpRate(*args)

    def __set_pumpRate(*args):
        """__set_pumpRate(self, double pumpRate)"""
        return _moose.TauPump___set_pumpRate(*args)

    def __get_eqConc(*args):
        """__get_eqConc(self) -> double"""
        return _moose.TauPump___get_eqConc(*args)

    def __set_eqConc(*args):
        """__set_eqConc(self, double eqConc)"""
        return _moose.TauPump___set_eqConc(*args)

    def __get_TA(*args):
        """__get_TA(self) -> double"""
        return _moose.TauPump___get_TA(*args)

    def __set_TA(*args):
        """__set_TA(self, double TA)"""
        return _moose.TauPump___set_TA(*args)

    def __get_TB(*args):
        """__get_TB(self) -> double"""
        return _moose.TauPump___get_TB(*args)

    def __set_TB(*args):
        """__set_TB(self, double TB)"""
        return _moose.TauPump___set_TB(*args)

    def __get_TC(*args):
        """__get_TC(self) -> double"""
        return _moose.TauPump___get_TC(*args)

    def __set_TC(*args):
        """__set_TC(self, double TC)"""
        return _moose.TauPump___set_TC(*args)

    def __get_TV(*args):
        """__get_TV(self) -> double"""
        return _moose.TauPump___get_TV(*args)

    def __set_TV(*args):
        """__set_TV(self, double TV)"""
        return _moose.TauPump___set_TV(*args)

    pumpRate = property(_moose.TauPump_pumpRate_get, _moose.TauPump_pumpRate_set)
    eqConc = property(_moose.TauPump_eqConc_get, _moose.TauPump_eqConc_set)
    TA = property(_moose.TauPump_TA_get, _moose.TauPump_TA_set)
    TB = property(_moose.TauPump_TB_get, _moose.TauPump_TB_set)
    TC = property(_moose.TauPump_TC_get, _moose.TauPump_TC_set)
    TV = property(_moose.TauPump_TV_get, _moose.TauPump_TV_set)
TauPump_swigregister = _moose.TauPump_swigregister
TauPump_swigregister(TauPump)
TauPump.className_ = _moose.cvar.TauPump_className_

class TimeTable(PyMooseBase):
    """Proxy of C++ TimeTable class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> TimeTable
        __init__(self, string path) -> TimeTable
        __init__(self, string name, Id parentId) -> TimeTable
        __init__(self, string name, PyMooseBase parent) -> TimeTable
        __init__(self, TimeTable src, string name, PyMooseBase parent) -> TimeTable
        __init__(self, TimeTable src, string name, Id parent) -> TimeTable
        __init__(self, TimeTable src, string path) -> TimeTable
        __init__(self, Id src, string name, Id parent) -> TimeTable
        """
        this = _moose.new_TimeTable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_TimeTable
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.TimeTable_getType(*args)

    def __get_maxTime(*args):
        """__get_maxTime(self) -> double"""
        return _moose.TimeTable___get_maxTime(*args)

    def __set_maxTime(*args):
        """__set_maxTime(self, double maxTime)"""
        return _moose.TimeTable___set_maxTime(*args)

    def __get_tableVector(*args):
        """__get_tableVector(self) -> double_vector"""
        return _moose.TimeTable___get_tableVector(*args)

    def __set_tableVector(*args):
        """__set_tableVector(self, double_vector tableVector)"""
        return _moose.TimeTable___set_tableVector(*args)

    def __get_tableSize(*args):
        """__get_tableSize(self) -> unsigned int"""
        return _moose.TimeTable___get_tableSize(*args)

    maxTime = property(_moose.TimeTable_maxTime_get, _moose.TimeTable_maxTime_set)
    tableVector = property(_moose.TimeTable_tableVector_get)
    tableSize = property(_moose.TimeTable_tableSize_get, _moose.TimeTable_tableSize_set)
TimeTable_swigregister = _moose.TimeTable_swigregister
TimeTable_swigregister(TimeTable)
TimeTable.className_ = _moose.cvar.TimeTable_className_

class RC(PyMooseBase):
    """Proxy of C++ RC class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> RC
        __init__(self, string path) -> RC
        __init__(self, string name, Id parentId) -> RC
        __init__(self, string name, PyMooseBase parent) -> RC
        __init__(self, RC src, string name, PyMooseBase parent) -> RC
        __init__(self, RC src, string name, Id parent) -> RC
        __init__(self, RC src, string path) -> RC
        __init__(self, Id src, string name, Id parent) -> RC
        """
        this = _moose.new_RC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_RC
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.RC_getType(*args)

    def __get_V0(*args):
        """__get_V0(self) -> double"""
        return _moose.RC___get_V0(*args)

    def __set_V0(*args):
        """__set_V0(self, double V0)"""
        return _moose.RC___set_V0(*args)

    def __get_R(*args):
        """__get_R(self) -> double"""
        return _moose.RC___get_R(*args)

    def __set_R(*args):
        """__set_R(self, double R)"""
        return _moose.RC___set_R(*args)

    def __get_C(*args):
        """__get_C(self) -> double"""
        return _moose.RC___get_C(*args)

    def __set_C(*args):
        """__set_C(self, double C)"""
        return _moose.RC___set_C(*args)

    def __get_state(*args):
        """__get_state(self) -> double"""
        return _moose.RC___get_state(*args)

    def __get_inject(*args):
        """__get_inject(self) -> double"""
        return _moose.RC___get_inject(*args)

    def __set_inject(*args):
        """__set_inject(self, double inject)"""
        return _moose.RC___set_inject(*args)

    V0 = property(_moose.RC_V0_get, _moose.RC_V0_set)
    R = property(_moose.RC_R_get, _moose.RC_R_set)
    C = property(_moose.RC_C_get, _moose.RC_C_set)
    state = property(_moose.RC_state_get, _moose.RC_state_set)
    inject = property(_moose.RC_inject_get, _moose.RC_inject_set)
RC_swigregister = _moose.RC_swigregister
RC_swigregister(RC)
RC.className_ = _moose.cvar.RC_className_

class PIDController(PyMooseBase):
    """Proxy of C++ PIDController class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> PIDController
        __init__(self, string path) -> PIDController
        __init__(self, string name, Id parentId) -> PIDController
        __init__(self, string name, PyMooseBase parent) -> PIDController
        __init__(self, PIDController src, string name, PyMooseBase parent) -> PIDController
        __init__(self, PIDController src, string name, Id parent) -> PIDController
        __init__(self, PIDController src, string path) -> PIDController
        __init__(self, Id src, string name, Id parent) -> PIDController
        """
        this = _moose.new_PIDController(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_PIDController
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.PIDController_getType(*args)

    def __get_gain(*args):
        """__get_gain(self) -> double"""
        return _moose.PIDController___get_gain(*args)

    def __set_gain(*args):
        """__set_gain(self, double gain)"""
        return _moose.PIDController___set_gain(*args)

    def __get_saturation(*args):
        """__get_saturation(self) -> double"""
        return _moose.PIDController___get_saturation(*args)

    def __set_saturation(*args):
        """__set_saturation(self, double saturation)"""
        return _moose.PIDController___set_saturation(*args)

    def __get_command(*args):
        """__get_command(self) -> double"""
        return _moose.PIDController___get_command(*args)

    def __set_command(*args):
        """__set_command(self, double command)"""
        return _moose.PIDController___set_command(*args)

    def __get_sensed(*args):
        """__get_sensed(self) -> double"""
        return _moose.PIDController___get_sensed(*args)

    def __get_tauI(*args):
        """__get_tauI(self) -> double"""
        return _moose.PIDController___get_tauI(*args)

    def __set_tauI(*args):
        """__set_tauI(self, double tauI)"""
        return _moose.PIDController___set_tauI(*args)

    def __get_tauD(*args):
        """__get_tauD(self) -> double"""
        return _moose.PIDController___get_tauD(*args)

    def __set_tauD(*args):
        """__set_tauD(self, double tauD)"""
        return _moose.PIDController___set_tauD(*args)

    def __get_output(*args):
        """__get_output(self) -> double"""
        return _moose.PIDController___get_output(*args)

    gain = property(_moose.PIDController_gain_get, _moose.PIDController_gain_set)
    saturation = property(_moose.PIDController_saturation_get, _moose.PIDController_saturation_set)
    command = property(_moose.PIDController_command_get, _moose.PIDController_command_set)
    sensed = property(_moose.PIDController_sensed_get, _moose.PIDController_sensed_set)
    tauI = property(_moose.PIDController_tauI_get, _moose.PIDController_tauI_set)
    tauD = property(_moose.PIDController_tauD_get, _moose.PIDController_tauD_set)
    output = property(_moose.PIDController_output_get, _moose.PIDController_output_set)
PIDController_swigregister = _moose.PIDController_swigregister
PIDController_swigregister(PIDController)
PIDController.className_ = _moose.cvar.PIDController_className_

class DiffAmp(PyMooseBase):
    """Proxy of C++ DiffAmp class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> DiffAmp
        __init__(self, string path) -> DiffAmp
        __init__(self, string name, Id parentId) -> DiffAmp
        __init__(self, string name, PyMooseBase parent) -> DiffAmp
        __init__(self, DiffAmp src, string name, PyMooseBase parent) -> DiffAmp
        __init__(self, DiffAmp src, string name, Id parent) -> DiffAmp
        __init__(self, DiffAmp src, string path) -> DiffAmp
        __init__(self, Id src, string name, Id parent) -> DiffAmp
        """
        this = _moose.new_DiffAmp(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_DiffAmp
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.DiffAmp_getType(*args)

    def __get_gain(*args):
        """__get_gain(self) -> double"""
        return _moose.DiffAmp___get_gain(*args)

    def __set_gain(*args):
        """__set_gain(self, double gain)"""
        return _moose.DiffAmp___set_gain(*args)

    def __get_saturation(*args):
        """__get_saturation(self) -> double"""
        return _moose.DiffAmp___get_saturation(*args)

    def __set_saturation(*args):
        """__set_saturation(self, double saturation)"""
        return _moose.DiffAmp___set_saturation(*args)

    def __get_plus(*args):
        """__get_plus(self) -> double"""
        return _moose.DiffAmp___get_plus(*args)

    def __get_minus(*args):
        """__get_minus(self) -> double"""
        return _moose.DiffAmp___get_minus(*args)

    def __get_output(*args):
        """__get_output(self) -> double"""
        return _moose.DiffAmp___get_output(*args)

    gain = property(_moose.DiffAmp_gain_get, _moose.DiffAmp_gain_set)
    saturation = property(_moose.DiffAmp_saturation_get, _moose.DiffAmp_saturation_set)
    plus = property(_moose.DiffAmp_plus_get, _moose.DiffAmp_plus_set)
    minus = property(_moose.DiffAmp_minus_get, _moose.DiffAmp_minus_set)
    output = property(_moose.DiffAmp_output_get, _moose.DiffAmp_output_set)
DiffAmp_swigregister = _moose.DiffAmp_swigregister
DiffAmp_swigregister(DiffAmp)
DiffAmp.className_ = _moose.cvar.DiffAmp_className_

class IntFire(PyMooseBase):
    """Proxy of C++ IntFire class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> IntFire
        __init__(self, string path) -> IntFire
        __init__(self, string name, Id parentId) -> IntFire
        __init__(self, string name, PyMooseBase parent) -> IntFire
        __init__(self, IntFire src, string name, PyMooseBase parent) -> IntFire
        __init__(self, IntFire src, string name, Id parent) -> IntFire
        __init__(self, IntFire src, string path) -> IntFire
        __init__(self, Id src, string name, Id parent) -> IntFire
        """
        this = _moose.new_IntFire(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_IntFire
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.IntFire_getType(*args)

    def __get_Vt(*args):
        """__get_Vt(self) -> double"""
        return _moose.IntFire___get_Vt(*args)

    def __set_Vt(*args):
        """__set_Vt(self, double Vt)"""
        return _moose.IntFire___set_Vt(*args)

    def __get_Vr(*args):
        """__get_Vr(self) -> double"""
        return _moose.IntFire___get_Vr(*args)

    def __set_Vr(*args):
        """__set_Vr(self, double Vr)"""
        return _moose.IntFire___set_Vr(*args)

    def __get_Rm(*args):
        """__get_Rm(self) -> double"""
        return _moose.IntFire___get_Rm(*args)

    def __set_Rm(*args):
        """__set_Rm(self, double Rm)"""
        return _moose.IntFire___set_Rm(*args)

    def __get_Cm(*args):
        """__get_Cm(self) -> double"""
        return _moose.IntFire___get_Cm(*args)

    def __set_Cm(*args):
        """__set_Cm(self, double Cm)"""
        return _moose.IntFire___set_Cm(*args)

    def __get_Vm(*args):
        """__get_Vm(self) -> double"""
        return _moose.IntFire___get_Vm(*args)

    def __set_Vm(*args):
        """__set_Vm(self, double Vm)"""
        return _moose.IntFire___set_Vm(*args)

    def __get_tau(*args):
        """__get_tau(self) -> double"""
        return _moose.IntFire___get_tau(*args)

    def __get_Em(*args):
        """__get_Em(self) -> double"""
        return _moose.IntFire___get_Em(*args)

    def __set_Em(*args):
        """__set_Em(self, double Em)"""
        return _moose.IntFire___set_Em(*args)

    def __get_refractT(*args):
        """__get_refractT(self) -> double"""
        return _moose.IntFire___get_refractT(*args)

    def __set_refractT(*args):
        """__set_refractT(self, double refractT)"""
        return _moose.IntFire___set_refractT(*args)

    def __get_initVm(*args):
        """__get_initVm(self) -> double"""
        return _moose.IntFire___get_initVm(*args)

    def __set_initVm(*args):
        """__set_initVm(self, double initVm)"""
        return _moose.IntFire___set_initVm(*args)

    def __get_inject(*args):
        """__get_inject(self) -> double"""
        return _moose.IntFire___get_inject(*args)

    def __set_inject(*args):
        """__set_inject(self, double inject)"""
        return _moose.IntFire___set_inject(*args)

    Vt = property(_moose.IntFire_Vt_get, _moose.IntFire_Vt_set)
    Vr = property(_moose.IntFire_Vr_get, _moose.IntFire_Vr_set)
    Rm = property(_moose.IntFire_Rm_get, _moose.IntFire_Rm_set)
    Cm = property(_moose.IntFire_Cm_get, _moose.IntFire_Cm_set)
    Vm = property(_moose.IntFire_Vm_get, _moose.IntFire_Vm_set)
    tau = property(_moose.IntFire_tau_get, _moose.IntFire_tau_set)
    Em = property(_moose.IntFire_Em_get, _moose.IntFire_Em_set)
    refractT = property(_moose.IntFire_refractT_get, _moose.IntFire_refractT_set)
    initVm = property(_moose.IntFire_initVm_get, _moose.IntFire_initVm_set)
    inject = property(_moose.IntFire_inject_get, _moose.IntFire_inject_set)
IntFire_swigregister = _moose.IntFire_swigregister
IntFire_swigregister(IntFire)
IntFire.className_ = _moose.cvar.IntFire_className_

class IzhikevichNrn(PyMooseBase):
    """Proxy of C++ IzhikevichNrn class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> IzhikevichNrn
        __init__(self, string path) -> IzhikevichNrn
        __init__(self, string name, Id parentId) -> IzhikevichNrn
        __init__(self, string name, PyMooseBase parent) -> IzhikevichNrn
        __init__(self, IzhikevichNrn src, string name, PyMooseBase parent) -> IzhikevichNrn
        __init__(self, IzhikevichNrn src, string name, Id parent) -> IzhikevichNrn
        __init__(self, IzhikevichNrn src, string path) -> IzhikevichNrn
        __init__(self, Id src, string name, Id parent) -> IzhikevichNrn
        """
        this = _moose.new_IzhikevichNrn(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_IzhikevichNrn
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.IzhikevichNrn_getType(*args)

    def __get_Vmax(*args):
        """__get_Vmax(self) -> double"""
        return _moose.IzhikevichNrn___get_Vmax(*args)

    def __set_Vmax(*args):
        """__set_Vmax(self, double Vmax)"""
        return _moose.IzhikevichNrn___set_Vmax(*args)

    def __get_c(*args):
        """__get_c(self) -> double"""
        return _moose.IzhikevichNrn___get_c(*args)

    def __set_c(*args):
        """__set_c(self, double c)"""
        return _moose.IzhikevichNrn___set_c(*args)

    def __get_d(*args):
        """__get_d(self) -> double"""
        return _moose.IzhikevichNrn___get_d(*args)

    def __set_d(*args):
        """__set_d(self, double d)"""
        return _moose.IzhikevichNrn___set_d(*args)

    def __get_a(*args):
        """__get_a(self) -> double"""
        return _moose.IzhikevichNrn___get_a(*args)

    def __set_a(*args):
        """__set_a(self, double a)"""
        return _moose.IzhikevichNrn___set_a(*args)

    def __get_b(*args):
        """__get_b(self) -> double"""
        return _moose.IzhikevichNrn___get_b(*args)

    def __set_b(*args):
        """__set_b(self, double b)"""
        return _moose.IzhikevichNrn___set_b(*args)

    def __get_Vm(*args):
        """__get_Vm(self) -> double"""
        return _moose.IzhikevichNrn___get_Vm(*args)

    def __set_Vm(*args):
        """__set_Vm(self, double Vm)"""
        return _moose.IzhikevichNrn___set_Vm(*args)

    def __get_u(*args):
        """__get_u(self) -> double"""
        return _moose.IzhikevichNrn___get_u(*args)

    def __get_Im(*args):
        """__get_Im(self) -> double"""
        return _moose.IzhikevichNrn___get_Im(*args)

    def __get_initVm(*args):
        """__get_initVm(self) -> double"""
        return _moose.IzhikevichNrn___get_initVm(*args)

    def __set_initVm(*args):
        """__set_initVm(self, double initVm)"""
        return _moose.IzhikevichNrn___set_initVm(*args)

    def __get_initU(*args):
        """__get_initU(self) -> double"""
        return _moose.IzhikevichNrn___get_initU(*args)

    def __set_initU(*args):
        """__set_initU(self, double initU)"""
        return _moose.IzhikevichNrn___set_initU(*args)

    def __get_alpha(*args):
        """__get_alpha(self) -> double"""
        return _moose.IzhikevichNrn___get_alpha(*args)

    def __set_alpha(*args):
        """__set_alpha(self, double alpha)"""
        return _moose.IzhikevichNrn___set_alpha(*args)

    def __get_beta(*args):
        """__get_beta(self) -> double"""
        return _moose.IzhikevichNrn___get_beta(*args)

    def __set_beta(*args):
        """__set_beta(self, double beta)"""
        return _moose.IzhikevichNrn___set_beta(*args)

    def __get_gamma(*args):
        """__get_gamma(self) -> double"""
        return _moose.IzhikevichNrn___get_gamma(*args)

    def __set_gamma(*args):
        """__set_gamma(self, double gamma)"""
        return _moose.IzhikevichNrn___set_gamma(*args)

    Vmax = property(_moose.IzhikevichNrn_Vmax_get, _moose.IzhikevichNrn_Vmax_set)
    c = property(_moose.IzhikevichNrn_c_get, _moose.IzhikevichNrn_c_set)
    d = property(_moose.IzhikevichNrn_d_get, _moose.IzhikevichNrn_d_set)
    a = property(_moose.IzhikevichNrn_a_get, _moose.IzhikevichNrn_a_set)
    b = property(_moose.IzhikevichNrn_b_get, _moose.IzhikevichNrn_b_set)
    Vm = property(_moose.IzhikevichNrn_Vm_get, _moose.IzhikevichNrn_Vm_set)
    u = property(_moose.IzhikevichNrn_u_get, _moose.IzhikevichNrn_u_set)
    Im = property(_moose.IzhikevichNrn_Im_get, _moose.IzhikevichNrn_Im_set)
    initVm = property(_moose.IzhikevichNrn_initVm_get, _moose.IzhikevichNrn_initVm_set)
    initU = property(_moose.IzhikevichNrn_initU_get, _moose.IzhikevichNrn_initU_set)
    alpha = property(_moose.IzhikevichNrn_alpha_get, _moose.IzhikevichNrn_alpha_set)
    beta = property(_moose.IzhikevichNrn_beta_get, _moose.IzhikevichNrn_beta_set)
    gamma = property(_moose.IzhikevichNrn_gamma_get, _moose.IzhikevichNrn_gamma_set)
IzhikevichNrn_swigregister = _moose.IzhikevichNrn_swigregister
IzhikevichNrn_swigregister(IzhikevichNrn)
IzhikevichNrn.className_ = _moose.cvar.IzhikevichNrn_className_

class GHK(PyMooseBase):
    """Proxy of C++ GHK class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, Id id) -> GHK
        __init__(self, string path) -> GHK
        __init__(self, string name, Id parentId) -> GHK
        __init__(self, string name, PyMooseBase parent) -> GHK
        __init__(self, GHK src, string name, PyMooseBase parent) -> GHK
        __init__(self, GHK src, string name, Id parent) -> GHK
        __init__(self, GHK src, string path) -> GHK
        __init__(self, Id src, string name, Id parent) -> GHK
        """
        this = _moose.new_GHK(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _moose.delete_GHK
    __del__ = lambda self : None;
    def getType(*args):
        """getType(self) -> string"""
        return _moose.GHK_getType(*args)

    def __get_Ik(*args):
        """__get_Ik(self) -> double"""
        return _moose.GHK___get_Ik(*args)

    def __get_Gk(*args):
        """__get_Gk(self) -> double"""
        return _moose.GHK___get_Gk(*args)

    def __get_Ek(*args):
        """__get_Ek(self) -> double"""
        return _moose.GHK___get_Ek(*args)

    def __get_T(*args):
        """__get_T(self) -> double"""
        return _moose.GHK___get_T(*args)

    def __set_T(*args):
        """__set_T(self, double T)"""
        return _moose.GHK___set_T(*args)

    def __get_p(*args):
        """__get_p(self) -> double"""
        return _moose.GHK___get_p(*args)

    def __set_p(*args):
        """__set_p(self, double p)"""
        return _moose.GHK___set_p(*args)

    def __get_Vm(*args):
        """__get_Vm(self) -> double"""
        return _moose.GHK___get_Vm(*args)

    def __set_Vm(*args):
        """__set_Vm(self, double Vm)"""
        return _moose.GHK___set_Vm(*args)

    def __get_Cin(*args):
        """__get_Cin(self) -> double"""
        return _moose.GHK___get_Cin(*args)

    def __set_Cin(*args):
        """__set_Cin(self, double Cin)"""
        return _moose.GHK___set_Cin(*args)

    def __get_Cout(*args):
        """__get_Cout(self) -> double"""
        return _moose.GHK___get_Cout(*args)

    def __set_Cout(*args):
        """__set_Cout(self, double Cout)"""
        return _moose.GHK___set_Cout(*args)

    def __get_valency(*args):
        """__get_valency(self) -> double"""
        return _moose.GHK___get_valency(*args)

    def __set_valency(*args):
        """__set_valency(self, double valency)"""
        return _moose.GHK___set_valency(*args)

    Ik = property(_moose.GHK_Ik_get, _moose.GHK_Ik_set)
    Gk = property(_moose.GHK_Gk_get, _moose.GHK_Gk_set)
    Ek = property(_moose.GHK_Ek_get, _moose.GHK_Ek_set)
    T = property(_moose.GHK_T_get, _moose.GHK_T_set)
    p = property(_moose.GHK_p_get, _moose.GHK_p_set)
    Vm = property(_moose.GHK_Vm_get, _moose.GHK_Vm_set)
    Cin = property(_moose.GHK_Cin_get, _moose.GHK_Cin_set)
    Cout = property(_moose.GHK_Cout_get, _moose.GHK_Cout_set)
    valency = property(_moose.GHK_valency_get, _moose.GHK_valency_set)
GHK_swigregister = _moose.GHK_swigregister
GHK_swigregister(GHK)
GHK.className_ = _moose.cvar.GHK_className_



