import FWCore.ParameterSet.Config as cms

#
# All units are cm and radians
#
# UNITS:
#
# TimeOffset in nanoseconds
# spacial displacement in cm

# common parameters
VtxSmearedCommon = cms.PSet(
    src = cms.InputTag("generator", "unsmeared"),
    readDB = cms.bool(False)
)
# Gaussian smearing
GaussVtxSmearingParameters = cms.PSet(
    MeanX = cms.double(0.0),
    MeanY = cms.double(0.0),
    MeanZ = cms.double(0.0),
    SigmaY = cms.double(0.0015),
    SigmaX = cms.double(0.0015),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0)
)
# Gaussian smearing
GaussVtxSigmaZ4cmSmearingParameters = cms.PSet(
    MeanX = cms.double(0.0),
    MeanY = cms.double(0.0),
    MeanZ = cms.double(0.0),
    SigmaY = cms.double(0.0015),
    SigmaX = cms.double(0.0015),
    SigmaZ = cms.double(4.0),
    TimeOffset = cms.double(0.0)
)

# Flat Smearing
FlatVtxSmearingParameters = cms.PSet(
    MaxZ = cms.double(5.3),
    MaxX = cms.double(0.0015),
    MaxY = cms.double(0.0015),
    MinX = cms.double(-0.0015),
    MinY = cms.double(-0.0015),
    MinZ = cms.double(-5.3),
    TimeOffset = cms.double(0.0)
)
#############################################
# Beta functions smearing (pp 7+7 TeV)
#
# Values taken from LHC optics simulation V6.5:
# see http://proj-lhc-optics-web.web.cern.ch/proj-lhc-optics-web/V6.500/IR5.html
# alpha = angle of the crossing plane 0 degrees means XZ plane
# phi = half-crossing beam angle
#
# Emittance is the no normalized emittance in cm = normalized emittance/gamma (beta=1)
# 
# length variables are in cm
#

# 900 GeV collisions, transverse beam size = 293 microns 
Early900GeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(1.564e-06),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(7.4),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
#  2.2 TeV collisions, transverse beam size 188 microns
Early2p2TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(6.4e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.5),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
#  7 TeV collisions, transverse beam size with betastar=  11m is 105 microns,
Early7TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(2.0e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.2),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
#  7 TeV collisions, transverse beam size with betastar=  2m is  45 microns,
Nominal7TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(200.0),
    Emittance = cms.double(2.0e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.2),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# 900 GeV realistic 2010 collisions, transverse beam size is 200 microns
Realistic900GeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1000.0),
    Emittance = cms.double(8.34e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(6.17),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2452),
    Y0 = cms.double(0.3993),
    Z0 = cms.double(0.8222)
)
# 7 TeV realistic collisions, beamspot width ~28 microns - appropriate for 2nd half of Commissioning10
Realistic7TeVCollisionComm10VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(200.0),
    Emittance = cms.double(0.804e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.50),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 7 TeV realistic collisions, beamspot width ~43 microns - appropriate for 2010A
Realistic7TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(350.0),
    Emittance = cms.double(1.072e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(6.26),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 7 TeV realistic collisions, beamspot width ~38 microns - appropriate for 2010B
Realistic7TeVCollision2010BVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(350.0),
    Emittance = cms.double(0.804e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.40),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 7 TeV realistic collisions, updated for 2011
# normalized emittance 2.5 microns, transverse beam size is 32 microns
Realistic7TeV2011CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(150.0),
    Emittance = cms.double(0.67e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.22),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# HI realistic collisions, updated for 2011
# estimated beamspot width 31-35 microns
RealisticHI2011CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(100.0),
    Emittance = cms.double(2.04e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(7.06),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2245),
    Y0 = cms.double(0.4182),
    Z0 = cms.double(0.0847)
)
# 2.76 TeV estimated collisions, 11m beta*
# normalized emittance 2.5 microns, transverse beam size is 140 microns
Realistic2p76TeV2011CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(1.70e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.22),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 2.76 TeV estimated collisions for 2013, 11m beta*
# sigmaZ set to 8 cm
Realistic2p76TeV2013CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(1.70e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(8.0),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# HI realistic pPb collisions, updated for 2013
# 
RealisticHIpPb2013CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(80.0),
    Emittance = cms.double(6.25e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(8.0),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 7 TeV centered collisions with parameters for 2011
# normalized emittance 2.5 microns, transverse beam size is 32 microns
Centered7TeV2011CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(150.0),
    Emittance = cms.double(0.67e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.22),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.0),
    Y0 = cms.double(0.0),
    Z0 = cms.double(0.0)
)
# 8 TeV realistic collisions, transverse beam width size is 20 microns
Realistic8TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(70.0),
    Emittance = cms.double(0.586e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(6.16),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 8 TeV realistic collisions, transverse beam width size is 20 microns, updated for observed SigmaZ
Realistic8TeV2012CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(70.0),
    Emittance = cms.double(0.586e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.8),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.2440),
    Y0 = cms.double(0.3929),
    Z0 = cms.double(0.4145)
)
# 10 TeV collisions, transverse beam size = 46 microns
Early10TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y100VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0100),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y250VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0250),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y500VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0500),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y1000VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.1),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y5000VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.5),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
# Test offset
Early10TeVX322Y10000VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(300.0),
    Emittance = cms.double(1.406e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.8),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(1.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)

EarlyCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(200.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.0322),
    Z0 = cms.double(0.0)
)
NominalCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.000142),
    BetaStar = cms.double(55.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.0),
    X0 = cms.double(0.05),
    Z0 = cms.double(0.0)
)
NominalCollision1VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(55.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.025),
    X0 = cms.double(0.05),
    Z0 = cms.double(0.0)
)
NominalCollision2VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.000142),
    BetaStar = cms.double(55.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.025),
    X0 = cms.double(0.05),
    Z0 = cms.double(0.0)
)
NominalCollision3VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(55.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.025),
    X0 = cms.double(0.1),
    Z0 = cms.double(0.0)
)
NominalCollision4VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(55.0),
    Emittance = cms.double(1.006e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    Y0 = cms.double(0.025),
    X0 = cms.double(0.2),
    Z0 = cms.double(0.0)
)
NominalCollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.0322),
    Y0 = cms.double(0.0),
    Z0 = cms.double(0.0)
)
ZeroTeslaRun247324CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(80.0),
    Emittance = cms.double(1.070e-5),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.125),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.08621),
    Y0 = cms.double(0.1657),
    Z0 = cms.double(-1.688)
)

# From 2015A 0T data
# Centroid absolute positions extracted from fills:
# X = 0.059395  cm
# Y = 0.099686  cm
# Z = -1.722240 cm
#
# BPIX absolute position extracted from first collision alignment:
# X = -0.0259503 cm
# Y = -0.07004   cm
# Z = -0.498917  cm
Realistic50ns13TeVCollisionZeroTeslaVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.08533),
    Y0 = cms.double(0.16973),
    Z0 = cms.double(-1.2230)
)

# From 2015B 3.8T data
# Centroid absolute positions extracted from fill 4008:
# X =  0.07798 cm
# Y =  0.09714 cm
# Z = -1.610   cm
#
# BPIX absolute position extracted from PCL-like alignment run after magnet ramp-up:
# X = -0.026837  cm
# Y = -0.0715252 cm
# Z = -0.511453  cm
Realistic50ns13TeVCollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.10482),
    Y0 = cms.double(0.16867),
    Z0 = cms.double(-1.0985)
)

# From 2015B 3.8T data, beta*=90m (700 bunches fills)
# Centroid absolute positions extracted from 700 bunches fills 4499-4511:
# X = 0.068357 cm
# Y = 0.109159 cm
# Z = 0.131811 cm
#
# BPIX absolute position extracted from Prompt Reco alignment of run 259352
# X = -0.041651 cm
# Y = -0.199279 cm
# Z = -0.565093 cm
#
# Emittance has been calculated to match a BeamWidht of O(10um) with: https://lpc.web.cern.ch/lumi2.html
#
Realistic100ns13TeVCollisionBetaStar90mVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(9121.0),
    Emittance = cms.double(0.12e-7),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.9),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.11000),
    Y0 = cms.double(0.30844),
    Z0 = cms.double(0.69690)
)

# From 2015B 3.8T data, beta*=90m (42/240 bunches fills)
# Centroid absolute positions extracted from 42/240 bunches fills 4495-4496:
# X = 0.064925 cm
# Y = 0.112761 cm
# Z = 0.170413 cm
#
# BPIX absolute position extracted from Prompt Reco alignment of run 259202
# X = -0.041651 cm
# Y = -0.199279 cm
# Z = -0.565093 cm
#
# Emittance has been calculated to match a BeamWidht of O(10um) with: https://lpc.web.cern.ch/lumi2.html
#
Realistic100ns13TeVCollisionBetaStar90mLowBunchesVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(9121.0),
    Emittance = cms.double(0.12e-7),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.24),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.10658),
    Y0 = cms.double(0.31204),
    Z0 = cms.double(0.735506)
)

# From 2016B 3.8T data
# BS parameters extracted from fills 4895 - 4935:
# X0         = 0.064870 +/- 4.9575E-07 [cm]
# Y0         = 0.093639 +/- 4.9233E-07 [cm]
# Z0         = 0.420085 +/- 4.1102E-04 [cm]
# sigmaZ0    = 3.645533 +/- 2.9064E-04 [cm]
#
# From LHC calculator, emittance is 4.906e-8 cm 
# https://lpc.web.cern.ch/lpc/lumi2.html
# 
# BPIX absolute position:
# X = -0.0267572 cm
# Y = -0.0759102 cm
# Z = -0.511428  cm
Realistic25ns13TeV2016CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(40.0),
    Emittance = cms.double(4.906e-8),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.65),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.09163),
    Y0 = cms.double(0.16955),
    Z0 = cms.double(0.9315 )
)

# From 2017A 3.8T data
# BS parameters extracted from run 295463 (from offline DQM, i.e. PCL):
# X0         =  0.08497  [cm]
# Y0         = -0.03976  [cm]
# Z0         =  1.6      [cm] ==> 0.5 adjusted after cogging tuning by LHC, see  https://hypernews.cern.ch/HyperNews/CMS/get/beamspot/159/1.html
# sigmaZ0    =  3.5      [cm]
#
# From LHC calculator, emittance is 3.319e-8 cm 
# https://lpc.web.cern.ch/lpc/lumi2.html
# 
# BPIX absolute position (https://hypernews.cern.ch/HyperNews/CMS/get/tif-alignment/657/1/1.html):
# X = 0.109725 cm
# Y = -0.108993 cm
# Z = -0.32054  cm
Reaslistic25ns13TeVEarly2017CollisionVtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(40.0),
    Emittance = cms.double(3.319e-8),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(3.5),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(-0.024755),
    Y0 = cms.double(0.069233 ),
    Z0 = cms.double(0.82054  )
)

# Test HF offset
ShiftedCollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(1.0),
    Y0 = cms.double(0.0),
    Z0 = cms.double(0.0)
)
Shifted5mmCollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.5),
    Y0 = cms.double(0.0),
    Z0 = cms.double(0.0)
)
Shifted15mmCollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(65.0),
    Emittance = cms.double(5.411e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.3),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(1.5),
    Y0 = cms.double(0.0),
    Z0 = cms.double(0.0)
)

# Estimate for 2015 PbPb collisions, based on feedback from accelerator                                                                                  
# Beamspot centroid shifted to match pp expectation for 2015                                                                                             
NominalHICollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(60.0),
    Emittance = cms.double(1.70e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(7.06),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.0322),
    Y0 = cms.double(0.),
    Z0 = cms.double(0.)
)

# updated numbers based on beamspot fits to 2015 PbPb data
RealisticHICollision2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(60.0),
    Emittance = cms.double(1.70e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.2278),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.1025),
    Y0 = cms.double(0.1654),
    Z0 = cms.double(3.2528)
)

# Estimate for 2015 pp collisions at 5.02 TeV, based on feedback from accelerator:  beta* ~ 400cm, normalized emittance = 2.5 um, SigmaZ similar to RunIIWinter15GS
Nominal5TeVpp2015VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(400.0),
    Emittance = cms.double(1.0e-07),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(5.5),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.1044),
    Y0 = cms.double(0.1676),
    Z0 = cms.double(0.6707)
)

# From fit to 5 TeV pPb data
Realistic5TeVPACollision2016VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(1100.0),
    Emittance = cms.double(6.75e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(6.4891),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.0889),
    Y0 = cms.double(0.1820),
    Z0 = cms.double(1.6066)    
)

# From fit to 8 TeV pPb data
Realistic8TeVPACollision2016VtxSmearingParameters = cms.PSet(
    Phi = cms.double(0.0),
    BetaStar = cms.double(60.0),
    Emittance = cms.double(6.75e-08),
    Alpha = cms.double(0.0),
    SigmaZ = cms.double(4.6914),
    TimeOffset = cms.double(0.0),
    X0 = cms.double(0.0836),
    Y0 = cms.double(0.1837),
    Z0 = cms.double(1.3577)    
)

# Parameters for HL-LHC operation at 13TeV
HLLHCVtxSmearingParameters = cms.PSet(
    MeanXIncm = cms.double(0.),
    MeanYIncm = cms.double(0.),
    MeanZIncm = cms.double(0.),
    TimeOffsetInns = cms.double(0.0),
    EprotonInGeV = cms.double(6500.0),
    CrossingAngleInurad = cms.double(510.0),
    CrabFrequencyInMHz = cms.double(400.0),
    RF800 = cms.bool(False),
    BetaCrossingPlaneInm = cms.double(0.20),
    BetaSeparationPlaneInm = cms.double(0.20),
    HorizontalEmittance = cms.double(2.5e-06),
    VerticalEmittance = cms.double(2.05e-06),
    BunchLengthInm = cms.double(0.090),
    CrabbingAngleCrossingInurad = cms.double(380.0),
    CrabbingAngleSeparationInurad = cms.double(0.0)    
)

# Parameters for HL-LHC Crab-kissing operation 13 TeV
HLLHCCrabKissingVtxSmearingParameters = cms.PSet(    
    MeanXIncm = cms.double(0.),
    MeanYIncm = cms.double(0.),
    MeanZIncm = cms.double(0.),
    TimeOffsetInns = cms.double(0.0),
    EprotonInGeV = cms.double(6500.0),
    HalfCrossingAngleInurad = cms.double(200.0),
    CrabAngleCrossingPlaneInurad = cms.double(200.0),
    CrabFrequencyCrossingPlaneInMHz = cms.double(400.0),
    NormalizedEmittanceCrossingPlaneInum = cms.double(2.5),
    BetaStarCrossingPlaneInm = cms.double(0.30),
    CrabAngleParallelPlaneInurad = cms.double(100.0),
    CrabFrequencyParallelPlaneInMHz = cms.double(400.0),
    NormalizedEmittanceParallelPlaneInum = cms.double(2.5),
    BetaStarParallelPlaneInm = cms.double(0.075),
    ZsizeInm = cms.double(0.15),
    BeamProfile=cms.string("Flat")
)
