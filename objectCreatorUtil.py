import maya.cmds as cmds

def createCone(prefix, name, num):
	for i in range(num):
		cmds.polyCone(
			name='{prefix}{name}{index:0>4}_GEO'.format(prefix=prefix,
				name=name
				,index=(i+1)
				)
			)

def createCube(prefix, name, num):
	for i in range(num):
		cmds.polyCube(
			name='{prefix}{name}{index:0>4}_GEO'.format(prefix=prefix,
				name=name
				,index=(i+1)
				)
			)

def createSphere(prefix, name, num):
	for i in range(num):
		cmds.polySphere(
			name='{prefix}{name}{index:0>4}_GEO'.format(prefix=prefix,
				name=name
				,index=(i+1)
				)
			)

def createTorus(prefix, name, num):
	for i in range(num):
		cmds.polyTorus(
			name='{prefix}{name}{index:0>4}_GEO'.format(prefix=prefix,
				name=name
				,index=(i+1)
				)
			)
def createCylinder(prefix, name, num):
	for i in range(num):
		cmds.polyCylinder(
			name='{prefix}{name}{index:0>4}_GEO'.format(prefix=prefix,
				name=name
				,index=(i+1)
				)
			)
