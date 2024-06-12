####################################################################################################
#
# Invoking X3D model self-test:
#
#   $ python MetadataNodeExamplesX3D4.py
#
# Python package x3d.py package is available on PyPI for import.
#   This approach simplifies Python X3D deployment and use.
#   https://pypi.org/project/x3d
#
# Installation:
#       pip install x3d
# or
#       python -m pip install x3d
#
# Developer options for loading x3d package in other Python programs:
#
#    from x3d import *  # preferred approach, terser source that avoids x3d.* class prefixes
#
# or
#    import x3d         # traditional way to subclass x3d package, all classes require x3d.* prefix,
#                       # but python source is very verbose, for example x3d.Material x3d.Shape etc.
#                       # X3dToPython.xslt stylesheet insertPackagePrefix=true supports this option.
#
####################################################################################################

from x3dkw import *

newModel=X3D(profile='Immersive',version='4.0',
  head=head(
    children=[
    meta(content='MetadataNodeExamplesX3D4.x3d',name='title'),
    meta(content='Simple examples of meta statements, comments, WorldInfo node and typed metadata nodes.',name='description'),
    meta(content='Don Brutzman',name='creator'),
    meta(content='30 September 2011',name='created'),
    meta(content='30 September 2023',name='modified'),
    meta(content='Original name MetadataNodeExamples.x3d, split and renamed since handling of metadata containerField defaults changed in X3D4.',name='reference'),
    meta(content='MetadataNodeExamplesX3D3.x3d',name='reference'),
    meta(content='X3D 4.0 Architecture, ISO/IEC 19775-1:2023, 4 Concepts, 4.3.2 Root nodes',name='specificationSection'),
    meta(content='https://www.web3d.org/specifications/X3Dv4Draft/ISO-IEC19775-1v4-IS.proof/Part01/concepts.html#Rootnodes',name='specificationUrl'),
    meta(content='Information in head and meta elements is retained after a scene is parsed and loaded, and can be referenced via the Scene Access Interface (SAI) or Document Object Model (DOM)',name='info'),
    meta(content='Authoring note: MetadataBoolean requires X3D version 4.0, as used in this example scene',name='info'),
    meta(content='The following referenced chapter is published online but was not included in the printed book.',name='reference'),
    meta(content='Chapter15MetadataInformation.html',name='reference'),
    meta(content='https://x3dgraphics.com/chapters/Chapter15MetadataInformation.html',name='reference'),
    meta(content='https://X3dGraphics.com',name='reference'),
    meta(content='https://www.web3d.org/x3d/content/examples/X3dResources.html',name='reference'),
    meta(content='Copyright 2006, Daly Realism and Don Brutzman',name='rights'),
    meta(content='X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com',name='subject'),
    meta(content='https://www.web3d.org/x3d/content/examples/X3dForWebAuthors/Chapter15Metadata/MetadataNodeExamplesX3D4.x3d',name='identifier'),
    meta(content='X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit',name='generator'),
    meta(content='../license.html',name='license')]),
  Scene=Scene(
    #  May 2017: X3D4 Architecture Specification clarification allows Metadata nodes at top level of Scene graph. 
    children=[
    MetadataString(name='TestRootMetadataNode',value=["Check whether scene root Metadata* node is satisfactory.","Note that all SFString values must be quoted."]),
    #  Comments can appear between nodes (XML elements) but are not retained after a scene is parsed, loaded and playing 
    WorldInfo(DEF='MyWorldInfo',info=["Metadata strings","can go here","as string array values"],title='MetadataNodeExamplesX3D4.x3d Example Scene',
      #  Structured information can go in Metadata nodes. Note that any X3D node can contain a single Metadata node with containerField='metadata' 
      metadata=MetadataSet(DEF='MyMetadataSetNode',name='Metadata_name',reference='SomeReferenceStandard 1.2.3c',
        value=[
        MetadataSet(DEF='MyMetadatSetNode2',name='should be first'),
        MetadataBoolean(DEF='MyMetadataBooleanNode',name='Coin Flip',reference='MetadataBoolean supported in X3D v3.3 and later',value=[True,False,True,False]),
        MetadataDouble(DEF='MyMetadataDoubleNode',name='Metadata_name',reference='SomeReferenceStandard 1.2.3c',value=[3.141592658,2.71812181]),
        MetadataFloat(DEF='MyMetadataFloatNode',name='Metadata_name',reference='SomeReferenceStandard 1.2.3c',value=[9.8,6.023e+23]),
        MetadataInteger(DEF='MyMetadataIntegerNode',name='Metadata_name',reference='SomeReferenceStandard 1.2.3c',value=[6,28,496]),
        MetadataString(DEF='MyMetadataStringNode',name='Metadata_name',reference='SomeReferenceStandard 1.2.3c',value=["Part 27","P27","p27"])],
        metadata=MetadataSet(DEF='NestedMetadataSetNode',name='TestNestedMetadataSetNodes',
          #  MetadataSet can also contain multiple Metadata nodes with default containerField='value' including USE nodes 
          value=[
          MetadataString(USE='MyMetadataStringNode'),
          MetadataInteger(USE='MyMetadataIntegerNode'),
          MetadataFloat(USE='MyMetadataFloatNode'),
          MetadataFloat(name='coefficients',value=[3.141592653,2.7128,1,0])]))),
    Background(skyColor=[(0,0.439216,0.760784)]),
    Viewpoint(description='View scene source to see metadata examples',position=(0,0,9)),
    Anchor(description='Load scene index page',parameter=["target=_blank"],url=["MetadataNodeExamplesIndex.html","https://www.web3d.org/x3d/content/examples/X3dForWebAuthors/Chapter15Metadata/MetadataNodeExamplesIndex.html"],
      children=[
      Shape(
        geometry=Text(string=["View scene source","to see","metadata examples"],
          fontStyle=FontStyle(justify=["MIDDLE","MIDDLE"])),
        appearance=Appearance(
          material=Material(diffuseColor=(1,0.992157,0.039216))))])])
) # X3D model complete

####################################################################################################
# Self-test diagnostics
####################################################################################################

print('Self-test diagnostics for MetadataNodeExamplesX3D4.py:')
if        metaDiagnostics(newModel): # built-in utility method in X3D class
    print(metaDiagnostics(newModel)) # display meta info, hint, warning, error, TODO values in this model
# print('check newModel.XML() serialization...')
newModelXML= newModel.XML() # test export method XML() for exceptions during export
#newModel.XMLvalidate()
print(newModelXML) # diagnostic

try:
#   print('check newModel.VRML() serialization...')
    newModelVRML=newModel.VRML() # test export method VRML() for exceptions during export
    print(prependLineNumbers(newModelVRML)) # debug
    print("Python-to-VRML export of VRML output successful", flush=True)
except Exception as err: # usually BaseException
    # https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python
    print("*** Python-to-VRML export of VRML output failed:", type(err).__name__, err)
    if newModelVRML: # may have failed to generate
        print(prependLineNumbers(newModelVRML, err.lineno))

try:
#   print('check newModel.JSON() serialization...')
    newModelJSON=newModel.JSON() # test export method JSON() for exceptions during export
#   print(prependLineNumbers(newModelJSON)) # debug
    print("Python-to-JSON export of JSON output successful (under development)")
except Exception as err: # usually SyntaxError
    print("*** Python-to-JSON export of JSON output failed:", type(err).__name__, err)
    if newModelJSON: # may have failed to generate
        print(prependLineNumbers(newModelJSON,err.lineno))

print("python MetadataNodeExamplesX3D4.py load and self-test diagnostics complete.")
