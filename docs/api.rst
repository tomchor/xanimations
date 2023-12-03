.. currentmodule:: xanimations

API Reference
=============

:class:`~xanimations.Movie` class
----------------------------


.. autosummary::
   :toctree: api/

   Movie

Presets
-------

Plot functions that can be supplied to the :class:`~xanimations.Movie` constructor
as the second positional argument.

They have a signature of the type:

.. code-block::

    def plotfunc(da, fig, timestamp, framedim, **kwargs):
        ...

.. autosummary::
   :toctree: api/

   rotating_globe
   ~xanimations.presets.basic
