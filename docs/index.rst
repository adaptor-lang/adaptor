The Adaptor Programming Language
================================

A lightweight programming language designed for WebAssembly.

.. contents:: Table of Contents
   :depth: 3 
   :backlinks: none

.. warning::
    WIP: This project is under development.

.. code-block:: plaintext
   
    fn on_pizza(thing: string) string {
        let greeting = thing + " on pizza"
        return greeting 
    }

    fn main() {
        let things = ["cheese", "salami", "pineapple"]
        for thing in things {
            printf(on_pizza(thing))
        }
    }

Why Adaptor?
------------

Compact 
^^^^^^^

Small 
^^^^^

* Lightweight compiler that embeddable for web project.

Specifications
--------------

Primitive types
^^^^^^^^^^^^^^^

* ``void``

* ``i64``

* ``i32``

* ``isize``

* ``u64``

* ``u32``

* ``usize``

* ``f64``

* ``f32``

* ``bool``

* ``string``
