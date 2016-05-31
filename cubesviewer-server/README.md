CubesViewer Server - Backend for CubesViewer OLAP visualizer
============================================================

About
-----

[CubesViewer](http://jjmontesl.github.io/cubesviewer/) is a visual, web-based tool
application for exploring and analyzing OLAP databases served by the Cubes OLAP Framework.

CubesViewer is divided in two parts: the client side application and an optional server side
web application (this one), which adds features like view saving and sharing.

This is the home of the CubesViewer fully-featured *server side* web application.

Download
--------

Please visit the [CubesViewer main project page](http://www.cubesviewer.com/) for download information.


Requirements
------------

CubesViewer Server uses Django 1.9, and has been tested with SQLite, PostgreSQL and MySQL database systems
(other database systems may also work as long as they are supported by Django).

You need a configured and running [Cubes Server](http://databrewery.org/cubes.html) version 1.0.x or later.
Your Cubes model may use some extra configuration if you wish to use features like date
filters and range filters (see Documentation below).

Note that the database or databases served by Cubes OLAP are not related to CubesViewer Server database backend
(although it can be the same database instance, it doesn't have to).

For further information, see the Documentation section below.


Documentation
-------------

Check documentation on main CubesViewer site:

* [CubesViewer Documentation](https://github.com/jjmontesl/cubesviewer/blob/master/doc/guide/index.md)
* [CubesViewer 2.0 Release Notes](https://github.com/jjmontesl/cubesviewer/blob/master/RELEASE-NOTES.md)
* [CubesViewer Main site](https://www.cubesviewer.com)


Support
=======

You can use the Cubes discuss group for CubesViewer related questions,
and report bugs or features via CubesViewer Server issue tracker:

* User group: http://groups.google.com/group/cubes-discuss
* Report bugs: https://github.com/jjmontesl/cubesviewer-server/issues

If you are using or trying CubesViewer, we'd love to hear from you (please tweet #cubesviewer).

Source
======

Github source repository:

* https://github.com/jjmontesl/cubesviewer
* https://github.com/jjmontesl/cubesviewer-server

Authors
=======

CubesViewer is written and maintained by Jose Juan Montes
and other contributors.

See AUTHORS file for more information.

License
=======

CubesViewer is licensed under MIT license.

For full license see the LICENSE file.

