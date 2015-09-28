import math
import numpy as np

def eloss(ene, anumbe):
    """
    calculate energe loss in a collision, using the isotropic/S-wave
    approximation. round up any energy below 0.1 eV to 0.02 eV (thermal)
    """
    
    if (ene < 1e-7):
        eneaft = 2e-8
    else:
        eremax = ((4.*anumbe)/((1.+anumbe)**2))*ene
        rn1 = np.random.rand() 
        eremax = eremax*rn1
        eneaft = ene - eremax

    if (ene < 1e-7):
        rn1 = np.random.rand()
        angl = math.acos((2.*rn1)-1.)
    else:
        eta = math.acos(math.sqrt((eremax/ene)*(((1.+anumbe)**2.)/(4.*anumbe))))
        angl = math.atan((math.sin(2.*eta))/((1./anumbe)-math.cos(2.*eta)))

    return angl, eneaft

def energy():
    """
    use von Neumann's "hit and miss" method to calculate the energy of a 
    neutron emitted from a fission source.
    """
    while (True):
        rn1 = np.random.rand() 
        rn1 = rn1*9.999 #prob = 0 above ~10 MeV
        prob = math.sqrt(rn1)*math.exp(-rn1/1.4) #Maxwell spectrum
        rn2 = np.random.rand()
        rn2 = rn2*0.5
        if (rn2 < prob):
            break
    ene = rn1
    return ene

def xsect(ene):
    """
    returns the approximate cross sections (in barns) for absorption and 
    elastic scattering in carbon.
    Input: energy, in MeV 
    """
    x = ene*1e6 #convert energy to eV
    if (x<1e4):
        xelast = 5.0
    else:
        xelast = 10.5-(1.346*math.log10(x))
    xelast = xelast*1e-24 #convert to barns

    if (x<1e3):
        xabsor = (6.442e-4)*(x**(-0.49421))
    elif (x<1e5):
        xabsor = 1.5e-5
    elif (x<1e6):
        xabsor = 2.5e-5
    else:
        xabsor = (4e-6)*math.exp(x*3.2189e-7)
    xabsor = xabsor*1e-24 #convert to barns

    return xelast, xabsor

def euler(ex, ey, ez, angl):
    """
    Takes the initial trajectory, rotates it to lie along the z-axis, 
    generates a vector at zenith angle theta equal to the scattering vector,
    with a random azimuthal angle phi. Then the initial axis is rotated 
    back, taking the scattered vector with it. This gives the scattered 
    direction vector (sx, sy, sz).
    This function uses Euler angles to carry out the transformation.
    """

    s = math.sqrt(ex**2 + ey**2 + ez**2)
    ex = ex/s
    ey = ey/s
    ez = ez/s
    beta = math.acos(ez)

    #these approximations are for compton scattering
    if (abs(beta) < 0.027):
        alpha = 0.0
    else:
        arg = ey/math.sin(beta)
        aarg = abs(arg)
        if (aarg < 1.0):
            alpha = math.asin(arg)
        else:
            arg = arg/(1.0001*aarg)
    sco1 = math.cos(alpha)*math.sin(beta) + ex
    sco1 = abs(sco1)
    sco2 = abs(ex)
    if (sco1 < sco2):
        beta = -beta
        alpha = -alpha
    gamma = 0.0
    # alpha, beta, gamma are the euler angles of rotation from the z-axis
    # to the direction of the initial particle.
    theta = angl
    rn1 = np.random.rand()
    phi = 2*math.pi*rn1

    # now calculate the roation matrix to rotate the scattered direction
    # back to the original axes.
    r11 = math.cos(alpha)*math.cos(beta)*math.cos(gamma) - math.sin(alpha)*math.sin(gamma)
    r12 = math.cos(beta)*math.sin(alpha)*math.cos(gamma) + math.cos(alpha)*math.sin(gamma)
    r13 = -math.sin(beta)*math.cos(gamma)
    r21 = -math.sin(gamma)*math.cos(beta)*math.cos(alpha) - math.sin(alpha)*math.cos(gamma)
    r22 = -math.sin(gamma)*math.cos(beta)*math.sin(alpha) + math.cos(alpha)*math.cos(gamma)
    r23 = math.sin(beta)*math.sin(gamma)
    r31 = math.sin(beta)*math.cos(alpha)
    r32 = math.sin(alpha)*math.sin(beta)
    r33 = math.cos(beta)
    sox = math.sin(theta)*math.cos(phi)
    soy = math.sin(theta)*math.sin(phi)
    soz = math.cos(theta)
    sx = r11*sox + r21*soy + r31*soz
    sy = r12*sox + r22*soy + r32*soz
    sz = r13*sox + r23*soy + r33*soz
    # sx, sy, sz is the unit propagation vector of the scattered particle
    # in the original fram.
    return sx, sy, sz
