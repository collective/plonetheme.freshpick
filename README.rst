
Introduction
============

The ``plonetheme.freshpick`` package uses the **theming** and **packaging** features
available in `plone.app.theming`_ to make this theme easily
available in `Plone 4.1`_ or higher.

Installation
------------

Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.x with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.

.. image:: https://github.com/collective/plonetheme.freshpick/raw/master/screenshot0.png
  :width: 1024px
  :alt: Create a Plone site from ZMI
  :align: center

Zip file
~~~~~~~~

If you are an end user, you might enjoy installation via zip file import.

1. Download the zip file: https://raw.github.com/collective/plonetheme.freshpick/master/freshpick.zip
2. Import the theme from the Diazo theme control panel.

.. image:: https://github.com/collective/plonetheme.freshpick/raw/master/screenshot1.png
  :width: 1024px
  :alt: Import the Diazo theme zip file
  :align: center


Buildout
~~~~~~~~

If you are a developer, you might enjoy installation via buildout.

Add ``plonetheme.freshpick`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        plonetheme.freshpick

Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel.

.. image:: https://github.com/collective/plonetheme.freshpick/raw/master/screenshot2.png
  :width: 1024px
  :alt: For select the Diazo theme just click on Activate button
  :align: center

That's it!

You should see:

.. image:: https://raw.github.com/collective/plonetheme.freshpick/master/plonetheme/freshpick/theme/freshpick/preview.png
  :width: 1024px
  :alt: plonetheme.freshpick preview
  :align: center

.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
