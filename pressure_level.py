# Taken from https://github.com/geoschem/gcpy/blob/master/gcpy/grid/vert.py

import numpy as np
from numpy import asarray

# Definitions for the GEOS-5 pressure levels
# Entry 0 is the surface
# Constant offsets, in hPa
GEOS_5_AK = [0.000000e+00, 4.804826e-02, 6.593752e+00, 1.313480e+01,
             1.961311e+01, 2.609201e+01, 3.257081e+01, 3.898201e+01,
             4.533901e+01, 5.169611e+01, 5.805321e+01, 6.436264e+01,
             7.062198e+01, 7.883422e+01, 8.909992e+01, 9.936521e+01,
             1.091817e+02, 1.189586e+02, 1.286959e+02, 1.429100e+02,
             1.562600e+02, 1.696090e+02, 1.816190e+02, 1.930970e+02,
             2.032590e+02, 2.121500e+02, 2.187760e+02, 2.238980e+02,
             2.243630e+02, 2.168650e+02, 2.011920e+02, 1.769300e+02,
             1.503930e+02, 1.278370e+02, 1.086630e+02, 9.236572e+01,
             7.851231e+01, 6.660341e+01, 5.638791e+01, 4.764391e+01,
             4.017541e+01, 3.381001e+01, 2.836781e+01, 2.373041e+01,
             1.979160e+01, 1.645710e+01, 1.364340e+01, 1.127690e+01,
             9.292942e+00, 7.619842e+00, 6.216801e+00, 5.046801e+00,
             4.076571e+00, 3.276431e+00, 2.620211e+00, 2.084970e+00,
             1.650790e+00, 1.300510e+00, 1.019440e+00, 7.951341e-01,
             6.167791e-01, 4.758061e-01, 3.650411e-01, 2.785261e-01,
             2.113490e-01, 1.594950e-01, 1.197030e-01, 8.934502e-02,
             6.600001e-02, 4.758501e-02, 3.270000e-02, 2.000000e-02,
             1.000000e-02 ]
GEOS_5_AK = np.array(GEOS_5_AK)

# Pressure factor, in hPa
GEOS_5_BK = [1.000000e+00, 9.849520e-01, 9.634060e-01, 9.418650e-01,
             9.203870e-01, 8.989080e-01, 8.774290e-01, 8.560180e-01,
             8.346609e-01, 8.133039e-01, 7.919469e-01, 7.706375e-01,
             7.493782e-01, 7.211660e-01, 6.858999e-01, 6.506349e-01,
             6.158184e-01, 5.810415e-01, 5.463042e-01, 4.945902e-01,
             4.437402e-01, 3.928911e-01, 3.433811e-01, 2.944031e-01,
             2.467411e-01, 2.003501e-01, 1.562241e-01, 1.136021e-01,
             6.372006e-02, 2.801004e-02, 6.960025e-03, 8.175413e-09,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
             0.000000e+00 ]
GEOS_5_BK = np.array(GEOS_5_BK)

def calc_grid_pressure(Ak, Bk, sfc_pressure):
    """ Calculates pressure grid from surface pressures and Ak/Bk values.
    Parameters
    ----------
    Ak:  float
        Vector of pressure offsets, hPa
    Bk: float
        Vector of pressure factors, unitless
    Returns
    -------
    pressure_grid: float
        Array of pressure values based on Ak and Bk.
    Notes
    -----
    #TODO
    Examples
    --------
    #TODO
    See Also
    --------
    [NONE]
    """
    sfc_pressure = asarray(sfc_pressure)
    if ~np.isscalar(sfc_pressure):
        _Ak = np.copy(Ak)
        _Bk = np.copy(Bk)
        while np.ndim(_Ak) <= np.ndim(sfc_pressure):
            _Ak = np.expand_dims(_Ak,axis=_Ak.ndim)
            _Bk = np.expand_dims(_Bk,axis=_Ak.ndim)
        _sfc_pressure = np.expand_dims(sfc_pressure,axis=0)
    else:
        _Ak = Ak
        _Bk = Bk
    grid_pressure = _Ak + _Bk*_sfc_pressure

    return grid_pressure

def get_reference_pressure(sfc_pressure=1000.0):
    """
    Get pressure at edges (73 levels). Default 1000 hpa surface pressure matches data at
    http://wiki.seas.harvard.edu/geos-chem/index.php/GEOS-Chem_vertical_grids#72-layer_vertical_grid
    """
    return calc_grid_pressure(GEOS_5_AK, GEOS_5_BK, sfc_pressure)