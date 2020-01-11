##################################################
# Copyright (c) Xuanyi Dong [GitHub D-X-Y], 2019 #
##################################################
from .search_model_darts    import TinyNetworkDarts
from .search_model_gdas     import TinyNetworkGDAS
from .search_model_setn     import TinyNetworkSETN
from .search_model_enas     import TinyNetworkENAS
from .search_model_random   import TinyNetworkRANDOM
from .genotypes             import Structure as CellStructure, architectures as CellArchitectures

nas_super_nets = {'DARTS-V1': TinyNetworkDarts,
                  'DARTS-V2': TinyNetworkDarts,
                  'GDAS'    : TinyNetworkGDAS,
                  'SETN'    : TinyNetworkSETN,
                  'ENAS'    : TinyNetworkENAS,
                  'RANDOM'  : TinyNetworkRANDOM}
