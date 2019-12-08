from turbo_colormap import interpolate_or_clip, turbo_colormap_data

f = open("turbo.xml", "w")

print('<ColorMaps>', file=f)
print('<ColorMap name="Turbo" space="RGB">', file=f)

use_all_pts = False
npts = len(turbo_colormap_data) if use_all_pts else 40

for i in range(npts):
   x = i/(npts-1.)
   if use_all_pts:
      r,g,b = turbo_colormap_data[i]
   else:
      r, g, b = interpolate_or_clip(turbo_colormap_data, x)
   print('<Point x="{:.8f}" o="1.0" r="{:.8f}" g="{:.8f}" b="{:.8f}" />'.format(x, r, g, b), file=f)

print('</ColorMap>', file=f)
print('</ColorMaps>', file=f)
