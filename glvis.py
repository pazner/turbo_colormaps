from turbo_colormap import interpolate_or_clip, turbo_colormap_data

palette_number = 37
use_all_pts = False
npts = len(turbo_colormap_data) if use_all_pts else 40
print("const int RGB_Palette_{}_Size = {}; // turbo".format(palette_number, npts))
print("double RGB_Palette_{}[RGB_Palette_{}_Size][3] =\n{{".format(palette_number, palette_number))

for i in range(npts):
   x = i/(npts-1.)
   if use_all_pts:
      r,g,b = turbo_colormap_data[i]
   else:
      r,g,b = interpolate_or_clip(turbo_colormap_data, x)
   suffix = "" if i == npts-1 else ","
   print("   {{{:.8f}, {:.8f}, {:.8f}}}{}".format(r, g, b, suffix))

print("};")
