================================
The Adaptor Programming Language
================================

A lightweight programming language designed for WebAssembly.

.. contents:: Table of Contents
   :depth: 4
   :backlinks: none

.. warning::
    WIP: This project is under development.

.. code-block:: plaintext

    fn on_pizza(thing: string) string {
        let response = thing + " on pizza"
        return response 
    }

    fn main() {
        let things = ["cheese", "salami", "pineapple"]
        for thing in things {
            println(on_pizza(thing))
        }
    }

Why Adaptor?
============

Compact 
-------

Small 
-----

* Lightweight compiler that embeddable for web project.

Language Reference
==================

Primitive types
---------------

Numbers
^^^^^^^

* ``void``

* ``i64``

* ``i32``

* ``isize``

* ``u64``

* ``u32``

* ``usize``

* ``f64``

* ``f32``

Boolean
^^^^^^^

* ``bool``

String
^^^^^^

* ``string``

Statements
----------

``if else``
^^^^^^^^^^^

``for``
^^^^^^^

``while``
^^^^^^^^^

adpx
----

.. code-block::

   ctx.html(
     _ {
       h1("Hello world")
     }
   )

FFI
---
