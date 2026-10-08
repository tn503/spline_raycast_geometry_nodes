
Deform spline in Blender geometry nodes.

Converting nodes into python script using node-to-python add-on.

## Update3:
Add parameter, Division and Division Seed.
Make clump splines when Taget Faces has no loose edges.

Update2:
Fix wrong domain size division.

Update1:
Add Max Neighbors parameter.

# Usage:
1. Taget Object: Faces, or Faces with some loose edge lines([]_, []__/, etc...).
2. Spline intersects Taget Faces, starts deforming.
3. Only Faces -> Mean Point(split Division parameter number). Has loose edge line -> using Interpolate Curves nodes with Max Neighbors parameter.

