from builtins import object
# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_presto')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_presto')
    _presto = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_presto', [dirname(__file__)])
        except ImportError:
            import _presto
            return _presto
        try:
            _mod = imp.load_module('_presto', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _presto = swig_import_helper()
    del swig_import_helper
else:
    import _presto
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object(object) : pass
        pass
    _newclass = 0

class fcomplex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fcomplex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fcomplex, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _presto.fcomplex_r_set
    __swig_getmethods__["r"] = _presto.fcomplex_r_get
    if _newclass:
        r = _swig_property(_presto.fcomplex_r_get, _presto.fcomplex_r_set)
    __swig_setmethods__["i"] = _presto.fcomplex_i_set
    __swig_getmethods__["i"] = _presto.fcomplex_i_get
    if _newclass:
        i = _swig_property(_presto.fcomplex_i_get, _presto.fcomplex_i_set)

    def __init__(self):
        this = _presto.new_fcomplex()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_fcomplex
    __del__ = lambda self: None
fcomplex_swigregister = _presto.fcomplex_swigregister
fcomplex_swigregister(fcomplex)

SQRT2 = _presto.SQRT2
PI = _presto.PI
TWOPI = _presto.TWOPI
DEGTORAD = _presto.DEGTORAD
RADTODEG = _presto.RADTODEG
PIBYTWO = _presto.PIBYTWO
SOL = _presto.SOL
SECPERJULYR = _presto.SECPERJULYR
SECPERDAY = _presto.SECPERDAY
ARCSEC2RAD = _presto.ARCSEC2RAD
SEC2RAD = _presto.SEC2RAD
LOWACC = _presto.LOWACC
HIGHACC = _presto.HIGHACC
INTERBIN = _presto.INTERBIN
INTERPOLATE = _presto.INTERPOLATE
NO_CHECK_ALIASED = _presto.NO_CHECK_ALIASED
CHECK_ALIASED = _presto.CHECK_ALIASED
CONV = _presto.CONV
CORR = _presto.CORR
INPLACE_CONV = _presto.INPLACE_CONV
INPLACE_CORR = _presto.INPLACE_CORR
FFTDK = _presto.FFTDK
FFTD = _presto.FFTD
FFTK = _presto.FFTK
NOFFTS = _presto.NOFFTS
RAW = _presto.RAW
PREPPED = _presto.PREPPED
FFT = _presto.FFT
SAME = _presto.SAME

def read_wisdom():
    return _presto.read_wisdom()
read_wisdom = _presto.read_wisdom

def good_factor(nn):
    return _presto.good_factor(nn)
good_factor = _presto.good_factor

def fftwcall(indata, isign):
    return _presto.fftwcall(indata, isign)
fftwcall = _presto.fftwcall

def tablesixstepfft(indata, isign):
    return _presto.tablesixstepfft(indata, isign)
tablesixstepfft = _presto.tablesixstepfft

def realfft(data, isign):
    return _presto.realfft(data, isign)
realfft = _presto.realfft
class infodata(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, infodata, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, infodata, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ra_s"] = _presto.infodata_ra_s_set
    __swig_getmethods__["ra_s"] = _presto.infodata_ra_s_get
    if _newclass:
        ra_s = _swig_property(_presto.infodata_ra_s_get, _presto.infodata_ra_s_set)
    __swig_setmethods__["dec_s"] = _presto.infodata_dec_s_set
    __swig_getmethods__["dec_s"] = _presto.infodata_dec_s_get
    if _newclass:
        dec_s = _swig_property(_presto.infodata_dec_s_get, _presto.infodata_dec_s_set)
    __swig_setmethods__["N"] = _presto.infodata_N_set
    __swig_getmethods__["N"] = _presto.infodata_N_get
    if _newclass:
        N = _swig_property(_presto.infodata_N_get, _presto.infodata_N_set)
    __swig_setmethods__["dt"] = _presto.infodata_dt_set
    __swig_getmethods__["dt"] = _presto.infodata_dt_get
    if _newclass:
        dt = _swig_property(_presto.infodata_dt_get, _presto.infodata_dt_set)
    __swig_setmethods__["fov"] = _presto.infodata_fov_set
    __swig_getmethods__["fov"] = _presto.infodata_fov_get
    if _newclass:
        fov = _swig_property(_presto.infodata_fov_get, _presto.infodata_fov_set)
    __swig_setmethods__["mjd_f"] = _presto.infodata_mjd_f_set
    __swig_getmethods__["mjd_f"] = _presto.infodata_mjd_f_get
    if _newclass:
        mjd_f = _swig_property(_presto.infodata_mjd_f_get, _presto.infodata_mjd_f_set)
    __swig_setmethods__["dm"] = _presto.infodata_dm_set
    __swig_getmethods__["dm"] = _presto.infodata_dm_get
    if _newclass:
        dm = _swig_property(_presto.infodata_dm_get, _presto.infodata_dm_set)
    __swig_setmethods__["freq"] = _presto.infodata_freq_set
    __swig_getmethods__["freq"] = _presto.infodata_freq_get
    if _newclass:
        freq = _swig_property(_presto.infodata_freq_get, _presto.infodata_freq_set)
    __swig_setmethods__["freqband"] = _presto.infodata_freqband_set
    __swig_getmethods__["freqband"] = _presto.infodata_freqband_get
    if _newclass:
        freqband = _swig_property(_presto.infodata_freqband_get, _presto.infodata_freqband_set)
    __swig_setmethods__["chan_wid"] = _presto.infodata_chan_wid_set
    __swig_getmethods__["chan_wid"] = _presto.infodata_chan_wid_get
    if _newclass:
        chan_wid = _swig_property(_presto.infodata_chan_wid_get, _presto.infodata_chan_wid_set)
    __swig_setmethods__["wavelen"] = _presto.infodata_wavelen_set
    __swig_getmethods__["wavelen"] = _presto.infodata_wavelen_get
    if _newclass:
        wavelen = _swig_property(_presto.infodata_wavelen_get, _presto.infodata_wavelen_set)
    __swig_setmethods__["waveband"] = _presto.infodata_waveband_set
    __swig_getmethods__["waveband"] = _presto.infodata_waveband_get
    if _newclass:
        waveband = _swig_property(_presto.infodata_waveband_get, _presto.infodata_waveband_set)
    __swig_setmethods__["energy"] = _presto.infodata_energy_set
    __swig_getmethods__["energy"] = _presto.infodata_energy_get
    if _newclass:
        energy = _swig_property(_presto.infodata_energy_get, _presto.infodata_energy_set)
    __swig_setmethods__["energyband"] = _presto.infodata_energyband_set
    __swig_getmethods__["energyband"] = _presto.infodata_energyband_get
    if _newclass:
        energyband = _swig_property(_presto.infodata_energyband_get, _presto.infodata_energyband_set)
    __swig_setmethods__["num_chan"] = _presto.infodata_num_chan_set
    __swig_getmethods__["num_chan"] = _presto.infodata_num_chan_get
    if _newclass:
        num_chan = _swig_property(_presto.infodata_num_chan_get, _presto.infodata_num_chan_set)
    __swig_setmethods__["mjd_i"] = _presto.infodata_mjd_i_set
    __swig_getmethods__["mjd_i"] = _presto.infodata_mjd_i_get
    if _newclass:
        mjd_i = _swig_property(_presto.infodata_mjd_i_get, _presto.infodata_mjd_i_set)
    __swig_setmethods__["ra_h"] = _presto.infodata_ra_h_set
    __swig_getmethods__["ra_h"] = _presto.infodata_ra_h_get
    if _newclass:
        ra_h = _swig_property(_presto.infodata_ra_h_get, _presto.infodata_ra_h_set)
    __swig_setmethods__["ra_m"] = _presto.infodata_ra_m_set
    __swig_getmethods__["ra_m"] = _presto.infodata_ra_m_get
    if _newclass:
        ra_m = _swig_property(_presto.infodata_ra_m_get, _presto.infodata_ra_m_set)
    __swig_setmethods__["dec_d"] = _presto.infodata_dec_d_set
    __swig_getmethods__["dec_d"] = _presto.infodata_dec_d_get
    if _newclass:
        dec_d = _swig_property(_presto.infodata_dec_d_get, _presto.infodata_dec_d_set)
    __swig_setmethods__["dec_m"] = _presto.infodata_dec_m_set
    __swig_getmethods__["dec_m"] = _presto.infodata_dec_m_get
    if _newclass:
        dec_m = _swig_property(_presto.infodata_dec_m_get, _presto.infodata_dec_m_set)
    __swig_setmethods__["bary"] = _presto.infodata_bary_set
    __swig_getmethods__["bary"] = _presto.infodata_bary_get
    if _newclass:
        bary = _swig_property(_presto.infodata_bary_get, _presto.infodata_bary_set)
    __swig_setmethods__["numonoff"] = _presto.infodata_numonoff_set
    __swig_getmethods__["numonoff"] = _presto.infodata_numonoff_get
    if _newclass:
        numonoff = _swig_property(_presto.infodata_numonoff_get, _presto.infodata_numonoff_set)
    __swig_setmethods__["notes"] = _presto.infodata_notes_set
    __swig_getmethods__["notes"] = _presto.infodata_notes_get
    if _newclass:
        notes = _swig_property(_presto.infodata_notes_get, _presto.infodata_notes_set)
    __swig_setmethods__["name"] = _presto.infodata_name_set
    __swig_getmethods__["name"] = _presto.infodata_name_get
    if _newclass:
        name = _swig_property(_presto.infodata_name_get, _presto.infodata_name_set)
    __swig_setmethods__["object"] = _presto.infodata_object_set
    __swig_getmethods__["object"] = _presto.infodata_object_get
    if _newclass:
        object = _swig_property(_presto.infodata_object_get, _presto.infodata_object_set)
    __swig_setmethods__["instrument"] = _presto.infodata_instrument_set
    __swig_getmethods__["instrument"] = _presto.infodata_instrument_get
    if _newclass:
        instrument = _swig_property(_presto.infodata_instrument_get, _presto.infodata_instrument_set)
    __swig_setmethods__["observer"] = _presto.infodata_observer_set
    __swig_getmethods__["observer"] = _presto.infodata_observer_get
    if _newclass:
        observer = _swig_property(_presto.infodata_observer_get, _presto.infodata_observer_set)
    __swig_setmethods__["analyzer"] = _presto.infodata_analyzer_set
    __swig_getmethods__["analyzer"] = _presto.infodata_analyzer_get
    if _newclass:
        analyzer = _swig_property(_presto.infodata_analyzer_get, _presto.infodata_analyzer_set)
    __swig_setmethods__["telescope"] = _presto.infodata_telescope_set
    __swig_getmethods__["telescope"] = _presto.infodata_telescope_get
    if _newclass:
        telescope = _swig_property(_presto.infodata_telescope_get, _presto.infodata_telescope_set)
    __swig_setmethods__["band"] = _presto.infodata_band_set
    __swig_getmethods__["band"] = _presto.infodata_band_get
    if _newclass:
        band = _swig_property(_presto.infodata_band_get, _presto.infodata_band_set)
    __swig_setmethods__["filt"] = _presto.infodata_filt_set
    __swig_getmethods__["filt"] = _presto.infodata_filt_get
    if _newclass:
        filt = _swig_property(_presto.infodata_filt_get, _presto.infodata_filt_set)

    def __init__(self):
        this = _presto.new_infodata()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_infodata
    __del__ = lambda self: None
infodata_swigregister = _presto.infodata_swigregister
infodata_swigregister(infodata)


def readinf(data, filenm):
    return _presto.readinf(data, filenm)
readinf = _presto.readinf

def writeinf(data):
    return _presto.writeinf(data)
writeinf = _presto.writeinf
class orbitparams(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, orbitparams, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, orbitparams, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _presto.orbitparams_p_set
    __swig_getmethods__["p"] = _presto.orbitparams_p_get
    if _newclass:
        p = _swig_property(_presto.orbitparams_p_get, _presto.orbitparams_p_set)
    __swig_setmethods__["e"] = _presto.orbitparams_e_set
    __swig_getmethods__["e"] = _presto.orbitparams_e_get
    if _newclass:
        e = _swig_property(_presto.orbitparams_e_get, _presto.orbitparams_e_set)
    __swig_setmethods__["x"] = _presto.orbitparams_x_set
    __swig_getmethods__["x"] = _presto.orbitparams_x_get
    if _newclass:
        x = _swig_property(_presto.orbitparams_x_get, _presto.orbitparams_x_set)
    __swig_setmethods__["w"] = _presto.orbitparams_w_set
    __swig_getmethods__["w"] = _presto.orbitparams_w_get
    if _newclass:
        w = _swig_property(_presto.orbitparams_w_get, _presto.orbitparams_w_set)
    __swig_setmethods__["t"] = _presto.orbitparams_t_set
    __swig_getmethods__["t"] = _presto.orbitparams_t_get
    if _newclass:
        t = _swig_property(_presto.orbitparams_t_get, _presto.orbitparams_t_set)
    __swig_setmethods__["pd"] = _presto.orbitparams_pd_set
    __swig_getmethods__["pd"] = _presto.orbitparams_pd_get
    if _newclass:
        pd = _swig_property(_presto.orbitparams_pd_get, _presto.orbitparams_pd_set)
    __swig_setmethods__["wd"] = _presto.orbitparams_wd_set
    __swig_getmethods__["wd"] = _presto.orbitparams_wd_get
    if _newclass:
        wd = _swig_property(_presto.orbitparams_wd_get, _presto.orbitparams_wd_set)

    def __init__(self):
        this = _presto.new_orbitparams()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_orbitparams
    __del__ = lambda self: None
orbitparams_swigregister = _presto.orbitparams_swigregister
orbitparams_swigregister(orbitparams)

class psrparams(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psrparams, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psrparams, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jname"] = _presto.psrparams_jname_set
    __swig_getmethods__["jname"] = _presto.psrparams_jname_get
    if _newclass:
        jname = _swig_property(_presto.psrparams_jname_get, _presto.psrparams_jname_set)
    __swig_setmethods__["bname"] = _presto.psrparams_bname_set
    __swig_getmethods__["bname"] = _presto.psrparams_bname_get
    if _newclass:
        bname = _swig_property(_presto.psrparams_bname_get, _presto.psrparams_bname_set)
    __swig_setmethods__["alias"] = _presto.psrparams_alias_set
    __swig_getmethods__["alias"] = _presto.psrparams_alias_get
    if _newclass:
        alias = _swig_property(_presto.psrparams_alias_get, _presto.psrparams_alias_set)
    __swig_setmethods__["ra2000"] = _presto.psrparams_ra2000_set
    __swig_getmethods__["ra2000"] = _presto.psrparams_ra2000_get
    if _newclass:
        ra2000 = _swig_property(_presto.psrparams_ra2000_get, _presto.psrparams_ra2000_set)
    __swig_setmethods__["dec2000"] = _presto.psrparams_dec2000_set
    __swig_getmethods__["dec2000"] = _presto.psrparams_dec2000_get
    if _newclass:
        dec2000 = _swig_property(_presto.psrparams_dec2000_get, _presto.psrparams_dec2000_set)
    __swig_setmethods__["dm"] = _presto.psrparams_dm_set
    __swig_getmethods__["dm"] = _presto.psrparams_dm_get
    if _newclass:
        dm = _swig_property(_presto.psrparams_dm_get, _presto.psrparams_dm_set)
    __swig_setmethods__["timepoch"] = _presto.psrparams_timepoch_set
    __swig_getmethods__["timepoch"] = _presto.psrparams_timepoch_get
    if _newclass:
        timepoch = _swig_property(_presto.psrparams_timepoch_get, _presto.psrparams_timepoch_set)
    __swig_setmethods__["p"] = _presto.psrparams_p_set
    __swig_getmethods__["p"] = _presto.psrparams_p_get
    if _newclass:
        p = _swig_property(_presto.psrparams_p_get, _presto.psrparams_p_set)
    __swig_setmethods__["pd"] = _presto.psrparams_pd_set
    __swig_getmethods__["pd"] = _presto.psrparams_pd_get
    if _newclass:
        pd = _swig_property(_presto.psrparams_pd_get, _presto.psrparams_pd_set)
    __swig_setmethods__["pdd"] = _presto.psrparams_pdd_set
    __swig_getmethods__["pdd"] = _presto.psrparams_pdd_get
    if _newclass:
        pdd = _swig_property(_presto.psrparams_pdd_get, _presto.psrparams_pdd_set)
    __swig_setmethods__["f"] = _presto.psrparams_f_set
    __swig_getmethods__["f"] = _presto.psrparams_f_get
    if _newclass:
        f = _swig_property(_presto.psrparams_f_get, _presto.psrparams_f_set)
    __swig_setmethods__["fd"] = _presto.psrparams_fd_set
    __swig_getmethods__["fd"] = _presto.psrparams_fd_get
    if _newclass:
        fd = _swig_property(_presto.psrparams_fd_get, _presto.psrparams_fd_set)
    __swig_setmethods__["fdd"] = _presto.psrparams_fdd_set
    __swig_getmethods__["fdd"] = _presto.psrparams_fdd_get
    if _newclass:
        fdd = _swig_property(_presto.psrparams_fdd_get, _presto.psrparams_fdd_set)
    __swig_setmethods__["orb"] = _presto.psrparams_orb_set
    __swig_getmethods__["orb"] = _presto.psrparams_orb_get
    if _newclass:
        orb = _swig_property(_presto.psrparams_orb_get, _presto.psrparams_orb_set)

    def __init__(self):
        this = _presto.new_psrparams()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_psrparams
    __del__ = lambda self: None
psrparams_swigregister = _presto.psrparams_swigregister
psrparams_swigregister(psrparams)


def get_psr_at_epoch(psrname, epoch, psr):
    return _presto.get_psr_at_epoch(psrname, epoch, psr)
get_psr_at_epoch = _presto.get_psr_at_epoch

def get_psr_from_parfile(parfilenm, epoch, psr):
    return _presto.get_psr_from_parfile(parfilenm, epoch, psr)
get_psr_from_parfile = _presto.get_psr_from_parfile

def mjd_to_datestr(mjd, datestr):
    return _presto.mjd_to_datestr(mjd, datestr)
mjd_to_datestr = _presto.mjd_to_datestr

def fresnl(xxa):
    return _presto.fresnl(xxa)
fresnl = _presto.fresnl
class rderivs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rderivs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rderivs, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pow"] = _presto.rderivs_pow_set
    __swig_getmethods__["pow"] = _presto.rderivs_pow_get
    if _newclass:
        pow = _swig_property(_presto.rderivs_pow_get, _presto.rderivs_pow_set)
    __swig_setmethods__["phs"] = _presto.rderivs_phs_set
    __swig_getmethods__["phs"] = _presto.rderivs_phs_get
    if _newclass:
        phs = _swig_property(_presto.rderivs_phs_get, _presto.rderivs_phs_set)
    __swig_setmethods__["dpow"] = _presto.rderivs_dpow_set
    __swig_getmethods__["dpow"] = _presto.rderivs_dpow_get
    if _newclass:
        dpow = _swig_property(_presto.rderivs_dpow_get, _presto.rderivs_dpow_set)
    __swig_setmethods__["dphs"] = _presto.rderivs_dphs_set
    __swig_getmethods__["dphs"] = _presto.rderivs_dphs_get
    if _newclass:
        dphs = _swig_property(_presto.rderivs_dphs_get, _presto.rderivs_dphs_set)
    __swig_setmethods__["d2pow"] = _presto.rderivs_d2pow_set
    __swig_getmethods__["d2pow"] = _presto.rderivs_d2pow_get
    if _newclass:
        d2pow = _swig_property(_presto.rderivs_d2pow_get, _presto.rderivs_d2pow_set)
    __swig_setmethods__["d2phs"] = _presto.rderivs_d2phs_set
    __swig_getmethods__["d2phs"] = _presto.rderivs_d2phs_get
    if _newclass:
        d2phs = _swig_property(_presto.rderivs_d2phs_get, _presto.rderivs_d2phs_set)
    __swig_setmethods__["locpow"] = _presto.rderivs_locpow_set
    __swig_getmethods__["locpow"] = _presto.rderivs_locpow_get
    if _newclass:
        locpow = _swig_property(_presto.rderivs_locpow_get, _presto.rderivs_locpow_set)

    def __init__(self):
        this = _presto.new_rderivs()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_rderivs
    __del__ = lambda self: None
rderivs_swigregister = _presto.rderivs_swigregister
rderivs_swigregister(rderivs)

class fourierprops(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fourierprops, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fourierprops, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _presto.fourierprops_r_set
    __swig_getmethods__["r"] = _presto.fourierprops_r_get
    if _newclass:
        r = _swig_property(_presto.fourierprops_r_get, _presto.fourierprops_r_set)
    __swig_setmethods__["rerr"] = _presto.fourierprops_rerr_set
    __swig_getmethods__["rerr"] = _presto.fourierprops_rerr_get
    if _newclass:
        rerr = _swig_property(_presto.fourierprops_rerr_get, _presto.fourierprops_rerr_set)
    __swig_setmethods__["z"] = _presto.fourierprops_z_set
    __swig_getmethods__["z"] = _presto.fourierprops_z_get
    if _newclass:
        z = _swig_property(_presto.fourierprops_z_get, _presto.fourierprops_z_set)
    __swig_setmethods__["zerr"] = _presto.fourierprops_zerr_set
    __swig_getmethods__["zerr"] = _presto.fourierprops_zerr_get
    if _newclass:
        zerr = _swig_property(_presto.fourierprops_zerr_get, _presto.fourierprops_zerr_set)
    __swig_setmethods__["w"] = _presto.fourierprops_w_set
    __swig_getmethods__["w"] = _presto.fourierprops_w_get
    if _newclass:
        w = _swig_property(_presto.fourierprops_w_get, _presto.fourierprops_w_set)
    __swig_setmethods__["werr"] = _presto.fourierprops_werr_set
    __swig_getmethods__["werr"] = _presto.fourierprops_werr_get
    if _newclass:
        werr = _swig_property(_presto.fourierprops_werr_get, _presto.fourierprops_werr_set)
    __swig_setmethods__["pow"] = _presto.fourierprops_pow_set
    __swig_getmethods__["pow"] = _presto.fourierprops_pow_get
    if _newclass:
        pow = _swig_property(_presto.fourierprops_pow_get, _presto.fourierprops_pow_set)
    __swig_setmethods__["powerr"] = _presto.fourierprops_powerr_set
    __swig_getmethods__["powerr"] = _presto.fourierprops_powerr_get
    if _newclass:
        powerr = _swig_property(_presto.fourierprops_powerr_get, _presto.fourierprops_powerr_set)
    __swig_setmethods__["sig"] = _presto.fourierprops_sig_set
    __swig_getmethods__["sig"] = _presto.fourierprops_sig_get
    if _newclass:
        sig = _swig_property(_presto.fourierprops_sig_get, _presto.fourierprops_sig_set)
    __swig_setmethods__["rawpow"] = _presto.fourierprops_rawpow_set
    __swig_getmethods__["rawpow"] = _presto.fourierprops_rawpow_get
    if _newclass:
        rawpow = _swig_property(_presto.fourierprops_rawpow_get, _presto.fourierprops_rawpow_set)
    __swig_setmethods__["phs"] = _presto.fourierprops_phs_set
    __swig_getmethods__["phs"] = _presto.fourierprops_phs_get
    if _newclass:
        phs = _swig_property(_presto.fourierprops_phs_get, _presto.fourierprops_phs_set)
    __swig_setmethods__["phserr"] = _presto.fourierprops_phserr_set
    __swig_getmethods__["phserr"] = _presto.fourierprops_phserr_get
    if _newclass:
        phserr = _swig_property(_presto.fourierprops_phserr_get, _presto.fourierprops_phserr_set)
    __swig_setmethods__["cen"] = _presto.fourierprops_cen_set
    __swig_getmethods__["cen"] = _presto.fourierprops_cen_get
    if _newclass:
        cen = _swig_property(_presto.fourierprops_cen_get, _presto.fourierprops_cen_set)
    __swig_setmethods__["cenerr"] = _presto.fourierprops_cenerr_set
    __swig_getmethods__["cenerr"] = _presto.fourierprops_cenerr_get
    if _newclass:
        cenerr = _swig_property(_presto.fourierprops_cenerr_get, _presto.fourierprops_cenerr_set)
    __swig_setmethods__["pur"] = _presto.fourierprops_pur_set
    __swig_getmethods__["pur"] = _presto.fourierprops_pur_get
    if _newclass:
        pur = _swig_property(_presto.fourierprops_pur_get, _presto.fourierprops_pur_set)
    __swig_setmethods__["purerr"] = _presto.fourierprops_purerr_set
    __swig_getmethods__["purerr"] = _presto.fourierprops_purerr_get
    if _newclass:
        purerr = _swig_property(_presto.fourierprops_purerr_get, _presto.fourierprops_purerr_set)
    __swig_setmethods__["locpow"] = _presto.fourierprops_locpow_set
    __swig_getmethods__["locpow"] = _presto.fourierprops_locpow_get
    if _newclass:
        locpow = _swig_property(_presto.fourierprops_locpow_get, _presto.fourierprops_locpow_set)

    def __init__(self):
        this = _presto.new_fourierprops()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_fourierprops
    __del__ = lambda self: None
fourierprops_swigregister = _presto.fourierprops_swigregister
fourierprops_swigregister(fourierprops)

class foldstats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, foldstats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, foldstats, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numdata"] = _presto.foldstats_numdata_set
    __swig_getmethods__["numdata"] = _presto.foldstats_numdata_get
    if _newclass:
        numdata = _swig_property(_presto.foldstats_numdata_get, _presto.foldstats_numdata_set)
    __swig_setmethods__["data_avg"] = _presto.foldstats_data_avg_set
    __swig_getmethods__["data_avg"] = _presto.foldstats_data_avg_get
    if _newclass:
        data_avg = _swig_property(_presto.foldstats_data_avg_get, _presto.foldstats_data_avg_set)
    __swig_setmethods__["data_var"] = _presto.foldstats_data_var_set
    __swig_getmethods__["data_var"] = _presto.foldstats_data_var_get
    if _newclass:
        data_var = _swig_property(_presto.foldstats_data_var_get, _presto.foldstats_data_var_set)
    __swig_setmethods__["numprof"] = _presto.foldstats_numprof_set
    __swig_getmethods__["numprof"] = _presto.foldstats_numprof_get
    if _newclass:
        numprof = _swig_property(_presto.foldstats_numprof_get, _presto.foldstats_numprof_set)
    __swig_setmethods__["prof_avg"] = _presto.foldstats_prof_avg_set
    __swig_getmethods__["prof_avg"] = _presto.foldstats_prof_avg_get
    if _newclass:
        prof_avg = _swig_property(_presto.foldstats_prof_avg_get, _presto.foldstats_prof_avg_set)
    __swig_setmethods__["prof_var"] = _presto.foldstats_prof_var_set
    __swig_getmethods__["prof_var"] = _presto.foldstats_prof_var_get
    if _newclass:
        prof_var = _swig_property(_presto.foldstats_prof_var_get, _presto.foldstats_prof_var_set)
    __swig_setmethods__["redchi"] = _presto.foldstats_redchi_set
    __swig_getmethods__["redchi"] = _presto.foldstats_redchi_get
    if _newclass:
        redchi = _swig_property(_presto.foldstats_redchi_get, _presto.foldstats_redchi_set)

    def __init__(self):
        this = _presto.new_foldstats()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _presto.delete_foldstats
    __del__ = lambda self: None
foldstats_swigregister = _presto.foldstats_swigregister
foldstats_swigregister(foldstats)


def gen_fvect(nl):
    return _presto.gen_fvect(nl)
gen_fvect = _presto.gen_fvect

def gen_cvect(nl):
    return _presto.gen_cvect(nl)
gen_cvect = _presto.gen_cvect

def power_arr(dft):
    return _presto.power_arr(dft)
power_arr = _presto.power_arr

def phase_arr(dft):
    return _presto.phase_arr(dft)
phase_arr = _presto.phase_arr

def frotate(data, bins_to_left):
    return _presto.frotate(data, bins_to_left)
frotate = _presto.frotate

def drotate(data, bins_to_left):
    return _presto.drotate(data, bins_to_left)
drotate = _presto.drotate

def keplers_eqn(t, p_orb, e, Eacc):
    return _presto.keplers_eqn(t, p_orb, e, Eacc)
keplers_eqn = _presto.keplers_eqn

def E_to_phib(E, orb):
    return _presto.E_to_phib(E, orb)
E_to_phib = _presto.E_to_phib

def E_to_v(E, orb):
    return _presto.E_to_v(E, orb)
E_to_v = _presto.E_to_v

def E_to_p(E, p_psr, orb):
    return _presto.E_to_p(E, p_psr, orb)
E_to_p = _presto.E_to_p

def E_to_z(E, p_psr, T, orb):
    return _presto.E_to_z(E, p_psr, T, orb)
E_to_z = _presto.E_to_z

def E_to_phib_BT(E, orb):
    return _presto.E_to_phib_BT(E, orb)
E_to_phib_BT = _presto.E_to_phib_BT

def dorbint(Eo, numpts, dt, orb):
    return _presto.dorbint(Eo, numpts, dt, orb)
dorbint = _presto.dorbint

def binary_velocity(T, orbit):
    return _presto.binary_velocity(T, orbit)
binary_velocity = _presto.binary_velocity

def r_resp_halfwidth(accuracy):
    return _presto.r_resp_halfwidth(accuracy)
r_resp_halfwidth = _presto.r_resp_halfwidth

def z_resp_halfwidth(z, accuracy):
    return _presto.z_resp_halfwidth(z, accuracy)
z_resp_halfwidth = _presto.z_resp_halfwidth

def w_resp_halfwidth(z, w, accuracy):
    return _presto.w_resp_halfwidth(z, w, accuracy)
w_resp_halfwidth = _presto.w_resp_halfwidth

def bin_resp_halfwidth(ppsr, T, orbit):
    return _presto.bin_resp_halfwidth(ppsr, T, orbit)
bin_resp_halfwidth = _presto.bin_resp_halfwidth

def gen_r_response(roffset, numbetween, numkern):
    return _presto.gen_r_response(roffset, numbetween, numkern)
gen_r_response = _presto.gen_r_response

def gen_z_response(roffset, numbetween, numkern, z):
    return _presto.gen_z_response(roffset, numbetween, numkern, z)
gen_z_response = _presto.gen_z_response

def gen_w_response(roffset, numbetween, numkern, z, w):
    return _presto.gen_w_response(roffset, numbetween, numkern, z, w)
gen_w_response = _presto.gen_w_response

def gen_w_response2(roffset, numbetween, numkern, z, w):
    return _presto.gen_w_response2(roffset, numbetween, numkern, z, w)
gen_w_response2 = _presto.gen_w_response2

def gen_bin_response(roffset, numbetween, numkern, ppsr, T, orbit):
    return _presto.gen_bin_response(roffset, numbetween, numkern, ppsr, T, orbit)
gen_bin_response = _presto.gen_bin_response

def get_localpower(data, r):
    return _presto.get_localpower(data, r)
get_localpower = _presto.get_localpower

def get_localpower3d(data, r, z, w):
    return _presto.get_localpower3d(data, r, z, w)
get_localpower3d = _presto.get_localpower3d

def get_derivs3d(data, numdata, r, z, w, localpower, result):
    return _presto.get_derivs3d(data, numdata, r, z, w, localpower, result)
get_derivs3d = _presto.get_derivs3d

def calc_props(data, r, z, w, result):
    return _presto.calc_props(data, r, z, w, result)
calc_props = _presto.calc_props

def calc_binprops(props, T, lowbin, nfftbins, result):
    return _presto.calc_binprops(props, T, lowbin, nfftbins, result)
calc_binprops = _presto.calc_binprops

def calc_rzwerrs(props, T, result):
    return _presto.calc_rzwerrs(props, T, result)
calc_rzwerrs = _presto.calc_rzwerrs

def extended_equiv_gaussian_sigma(logp):
    return _presto.extended_equiv_gaussian_sigma(logp)
extended_equiv_gaussian_sigma = _presto.extended_equiv_gaussian_sigma

def log_asymtotic_incomplete_gamma(a, z):
    return _presto.log_asymtotic_incomplete_gamma(a, z)
log_asymtotic_incomplete_gamma = _presto.log_asymtotic_incomplete_gamma

def log_asymtotic_gamma(z):
    return _presto.log_asymtotic_gamma(z)
log_asymtotic_gamma = _presto.log_asymtotic_gamma

def equivalent_gaussian_sigma(logp):
    return _presto.equivalent_gaussian_sigma(logp)
equivalent_gaussian_sigma = _presto.equivalent_gaussian_sigma

def chi2_logp(chi2, dof):
    return _presto.chi2_logp(chi2, dof)
chi2_logp = _presto.chi2_logp

def chi2_sigma(chi2, dof):
    return _presto.chi2_sigma(chi2, dof)
chi2_sigma = _presto.chi2_sigma

def candidate_sigma(power, numsum, numtrials):
    return _presto.candidate_sigma(power, numsum, numtrials)
candidate_sigma = _presto.candidate_sigma

def power_for_sigma(sigma, numsum, numtrials):
    return _presto.power_for_sigma(sigma, numsum, numtrials)
power_for_sigma = _presto.power_for_sigma

def switch_f_and_p(arg1, ind, indd):
    return _presto.switch_f_and_p(arg1, ind, indd)
switch_f_and_p = _presto.switch_f_and_p

def chisqr(data, avg, var):
    return _presto.chisqr(data, avg, var)
chisqr = _presto.chisqr

def print_candidate(cand, dt, N, nph, numerrdigits):
    return _presto.print_candidate(cand, dt, N, nph, numerrdigits)
print_candidate = _presto.print_candidate

def print_bin_candidate(cand, numerrdigits):
    return _presto.print_bin_candidate(cand, numerrdigits)
print_bin_candidate = _presto.print_bin_candidate

def read_rzw_cand(file, cands):
    return _presto.read_rzw_cand(file, cands)
read_rzw_cand = _presto.read_rzw_cand

def get_rzw_cand(filenm, candnum, cand):
    return _presto.get_rzw_cand(filenm, candnum, cand)
get_rzw_cand = _presto.get_rzw_cand

def read_bin_cand(file, cands):
    return _presto.read_bin_cand(file, cands)
read_bin_cand = _presto.read_bin_cand

def get_bin_cand(filenm, candnum, cand):
    return _presto.get_bin_cand(filenm, candnum, cand)
get_bin_cand = _presto.get_bin_cand

def next2_to_n(x):
    return _presto.next2_to_n(x)
next2_to_n = _presto.next2_to_n

def is_power_of_10(n):
    return _presto.is_power_of_10(n)
is_power_of_10 = _presto.is_power_of_10

def choose_good_N(orig_N):
    return _presto.choose_good_N(orig_N)
choose_good_N = _presto.choose_good_N

def dms2rad(deg, min, sec):
    return _presto.dms2rad(deg, min, sec)
dms2rad = _presto.dms2rad

def hms2rad(hour, min, sec):
    return _presto.hms2rad(hour, min, sec)
hms2rad = _presto.hms2rad

def hours2hms(hours):
    return _presto.hours2hms(hours)
hours2hms = _presto.hours2hms

def deg2dms(degrees):
    return _presto.deg2dms(degrees)
deg2dms = _presto.deg2dms

def sphere_ang_diff(ra1, dec1, ra2, dec2):
    return _presto.sphere_ang_diff(ra1, dec1, ra2, dec2)
sphere_ang_diff = _presto.sphere_ang_diff

def corr_rz_plane(data, numbetween, startbin, zlo, zhi, numz, fftlen, accuracy):
    return _presto.corr_rz_plane(data, numbetween, startbin, zlo, zhi, numz, fftlen, accuracy)
corr_rz_plane = _presto.corr_rz_plane

def corr_rzw_vol(data, numbetween, startbin, zlo, zhi, numz, wlo, whi, numw, fftlen, accuracy):
    return _presto.corr_rzw_vol(data, numbetween, startbin, zlo, zhi, numz, wlo, whi, numw, fftlen, accuracy)
corr_rzw_vol = _presto.corr_rzw_vol

def max_r_arr(data, rin, derivs):
    return _presto.max_r_arr(data, rin, derivs)
max_r_arr = _presto.max_r_arr

def max_rz_arr(data, rin, zin, derivs):
    return _presto.max_rz_arr(data, rin, zin, derivs)
max_rz_arr = _presto.max_rz_arr

def max_rz_arr_harmonics(data, rin, zin, derivdata):
    return _presto.max_rz_arr_harmonics(data, rin, zin, derivdata)
max_rz_arr_harmonics = _presto.max_rz_arr_harmonics

def max_rzw_arr_harmonics(data, rin, zin, win, derivdata):
    return _presto.max_rzw_arr_harmonics(data, rin, zin, win, derivdata)
max_rzw_arr_harmonics = _presto.max_rzw_arr_harmonics

def max_rzw_arr(data, rin, zin, win, derivs):
    return _presto.max_rzw_arr(data, rin, zin, win, derivs)
max_rzw_arr = _presto.max_rzw_arr

def barycenter(topotimes, barytimes, voverc, ra, dec, obs, ephem):
    return _presto.barycenter(topotimes, barytimes, voverc, ra, dec, obs, ephem)
barycenter = _presto.barycenter

def nice_output_1(output, val, err, len):
    return _presto.nice_output_1(output, val, err, len)
nice_output_1 = _presto.nice_output_1

def nice_output_2(output, val, err, len):
    return _presto.nice_output_2(output, val, err, len)
nice_output_2 = _presto.nice_output_2
# This file is compatible with both classic and new-style classes.


