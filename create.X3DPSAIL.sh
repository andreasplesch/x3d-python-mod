#!/usr/bin/env bash

java -cp "saxon-he-12.1.jar;xmlresolver-5.1.1.jar;xmlresolver-5.1.1-data.jar" net.sf.saxon.Transform -warnings:recover -expand:on -s:X3DUnifiedObjectModel-4.0-2023-07-02.xml -xsl:src/X3duomToX3dPythonPackageCF.xslt X3dPackageDirectory=python
