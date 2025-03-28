##############################################################################################
# Imports

import numpy

##############################################################################################
# statistics

##########################
# 1-point

# redshift distribution (IM: z<3, Gxys: z<0.5)
def redshift_distribution ( redshift, zbins=10 ) :
    return numpy.histogram( redshift, bins=zbins )[0]

# Omega_HI
def Omega_HI ( MHI_tot, rho_crit0, Volume = 1.0 ) :
    return MHI_tot / Volume / rho_crit0

# MHI-Mh relation
def MHIMh_relation ( MHI, Mh, bins=10 ) :
    """Returns the 2D histogram with Mh to MHI relation.
    The first dimension runs on the HI mass and 
    the second dimension on the halo mass
    
    Parameters
    ----------
    MHI : ndarray
       array with HI mass of galaxies
    Mh : ndarray
       array with halo mass of galaxies
    bins : str or scalar or iterable or tuple of iterables
       same as numpy.histogram2d
    
    Returns
    -------
    MHIMh : ndarray shape(nMHI,nMh)
       The bi-dimensional histogram of samples `MHI` and `Mh`. Values in `MHI`
       are histogrammed along the first dimension and values in `Mh` are
       histogrammed along the second dimension.
    """
    return numpy.histogram2d( MHI, Mh, bins=bins )

# HI mass function
def dnHIdlnMHI ( MHI, bins=10, Volume = 1.0 ) :
    """Computes the HI mass function

    Parameters
    ----------
    MHI : ndarray
       array with HI mass of galaxies
    bins : ndarray
       a monotonically increasing array of bin edges,
       including the rightmost edge, allowing for non-uniform bin widths
    Volume : scalar
       the size of the simulated comoving volume (assuming cMpc/h units)
    
    Returns
    -------
    MHI_cen : ndarray
       centre of the HI mass bins
    dndlnM : ndarray
       HI mass function
    error : ndarray
       Poisson error on the HI mass function
    """
    NHI, *_ = numpy.histogram( MHI, bins=bins )
    dlnMHI = numpy.diff(numpy.log(bins))
    return (
        0.5 * (bins[1:]+bins[:-1]),
        NHI / Volume / dlnMHI, 
        numpy.sqrt( NHI ) / Volume / dlnMHI, 
    )

# Number counts
def number_counts () :
    pass

##########################
# 2-point

# Power spectrum on a box

# Cls projected map

# bias?

##############################################################################################
