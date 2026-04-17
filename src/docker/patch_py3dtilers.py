"""
Patch py3dtilers ObjTiler to support C3F_N3F_V3F vertex format.
This format is produced by pymeshlab when exporting OBJ with vertex colors and normals:
  v x y z r g b   (non-standard OBJ extension)
  vn nx ny nz

Pywavefront identifies this as C3F_N3F_V3F (color=3f, normal=3f, vertex=3f).
py3dtilers' obj.py did not handle this format, causing "No feature found in source".
"""

import os

path = '/opt/conda/envs/mesh23Dtile/lib/python3.10/site-packages/py3dtilers/ObjTiler/obj.py'

with open(path) as f:
    content = f.read()

old = "        else:\n            print(\"Unsuported format\", vertex_format)\n            return False"

new = (
    "        # Contains colors, normals and vertex positions (e.g. from pymeshlab with vertex colors)\n"
    "        elif vertex_format == 'C3F_N3F_V3F':\n"
    "            # Layout per vertex: [c0,c1,c2, n0,n1,n2, v0,v1,v2] = 9 floats; 27 per triangle\n"
    "            for i in range(0, length, 27):\n"
    "                triangle = [np.array(vertices[n + 6:n + 9]) for n in range(i, i + 27, 9)]\n"
    "                triangles.append(triangle)\n"
    "        else:\n"
    "            print(\"Unsuported format\", vertex_format)\n"
    "            return False"
)

if "elif vertex_format == 'C3F_N3F_V3F':" in content:
    print("Already patched, skipping.")
elif old not in content:
    print("ERROR: target string not found in obj.py — patch failed.")
    print("File content around 'Unsuported':")
    idx = content.find("Unsuported")
    print(content[max(0, idx-200):idx+200])
    exit(1)
else:
    content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)
    print("Successfully patched py3dtilers obj.py with C3F_N3F_V3F support.")
