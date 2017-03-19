import bpy
op = bpy.context.active_operator

op.AutoUpdate = True
op.SphereMesh = False
op.SmoothMesh = True
op.Subdivision = 256
op.MeshSize = 2.0
op.XOffset = 0.0
op.YOffset = 0.0
op.RandomSeed = 1
op.NoiseSize = 0.33000001311302185
op.NoiseType = 'hetero_terrain'
op.BasisType = '0'
op.VLBasisType = '0'
op.Distortion = 1.0
op.HardNoise = False
op.NoiseDepth = 8
op.mDimension = 0.8799999952316284
op.mLacunarity = 2.200000047683716
op.mOffset = 0.7300002574920654
op.mGain = 1.0
op.MarbleBias = '0'
op.MarbleSharp = '0'
op.MarbleShape = '0'
op.Invert = False
op.Height = 0.20000000298023224
op.Offset = 0.0
op.Falloff = '1'
op.Sealevel = 0.0
op.Plateaulevel = 1.0
op.Strata = 5.0
op.StrataType = '0'