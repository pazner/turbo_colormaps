from turbo_colormap import interpolate_or_clip, turbo_colormap_data

f = open("turbo.ct", "w")

print('<?xml version="1.0"?>', file=f)
print('<Object name="ColorTable">', file=f)
print('  <Field name="Version" type="string">1.11.0</Field>', file=f)
print('  <Object name="ColorControlPointList">', file=f)

use_all_pts = False
npts = len(turbo_colormap_data) if use_all_pts else 40

for i in range(npts):
   pos = i/(npts-1.)
   if use_all_pts:
      rgb = turbo_colormap_data[i]
   else:
      rgb = interpolate_or_clip(turbo_colormap_data, pos)
   r = int(rgb[0]*255)
   g = int(rgb[1]*255)
   b = int(rgb[2]*255)
   a = 255
   print('    <Object name="ColorControlPoint">', file=f)
   print('      <Field name="colors" type="unsignedCharArray" length="4">',r,g,b,a,'</Field>', file=f)
   print('      <Field name="position" type="float">{:.8f}</Field>'.format(pos), file=f)
   print('    </Object>', file=f)

print('  </Object>', file=f)
print('</Object>', file=f)

f.close()
