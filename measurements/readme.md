# Measurements

Suggested naming convention:

```
YourName_[lightcone/box].hdf5
```

so that if anyone wants to provide measurements in both lightcone and boxes we can distinguish them.

## Semi-analytical models

## Empirical models
### File format PascalHitz_lightcone.hdf5:
`z_bins` corresponds to 20 redshift bins with a constant width of 5 MHz (~0.01 in redshift) in the frequency range of 700-800 MHz.
```
with h5py.File( outfile, "w" ) as f :

    # Redshift distribution
    group_zdist = f.create_group('redshift_distribution')
    group_zdist.create_dataset( 'zdist', data = zdist )
    group_zdist.create_dataset( 'zbins', data = z_bins )

    # Density parameter
    group_omega = f.create_group('omega_hi')
    group_omega.create_dataset( 'zmhi', data = zmhi )
    group_omega.create_dataset( 'Vz', data = shell_volume )
    group_omega.create_dataset( 'rhocrit', data = rho_crit )
    group_omega['zmhi'].attrs['units'] = '[Msun]'
    group_omega['Vz'].attrs['units'] = '[Mpc^3]'
    group_omega['rhocrit'].attrs['units'] = '[Msun/Mpc^3]'

    # MHIMh relation
    group_mhimh = f.create_group('MHIMh')
    group_mhimh.create_dataset('NMHI-NMh', data = MHIMh )

    # HI mass function
    group_nmhi = f.create_group('nmhi')
    group_nmhi.create_dataset('NMHI', data = NMHI )
    group_nmhi.create_dataset('Vz', data = shell_volume)
    group_nmhi['Vz'].attrs['units'] = '[Mpc^3]'

    # Power Spectrum (on a box)
    group_pk = f.create_group('pk')
    group_pk.create_dataset('kh', data = kh)
    group_pk.create_dataset('Pk0_marked', data = Pk0_marked)
    group_pk.create_dataset('Pk0', data = Pk0)
    group_pk['kh'].attrs['units'] = '[h/Mpc]'
    group_pk['Pk0_marked'].attrs['units'] = '[(Mpc/h)^3]'
    group_pk['Pk0'].attrs['units'] = '[(Mpc/h)^3]'
    group_pk.attrs['kMin'] = kMin 
    group_pk.attrs['kNyq'] = kNyq
    group_pk.attrs['shot_marked'] = shot_marked
    group_pk.attrs['shot'] = shot
    group_pk.attrs['redshifts'] = redshifts

    # Angular Power Spectrum (on lightcone)
    group_cell = f.create_group('cell')
    group_cell.create_dataset('ell', data = ell)
    group_cell.create_dataset('Cell_marked', data = cl_marked_tot)
    group_cell.create_dataset('Cell', data = cl_tot)
    group_cell.attrs['shot_marked'] = shot_noise_marked
    group_cell.attrs['shot'] = shot_noise
    group_cell.attrs['fsky'] = fsky
```

## Fast approximations
