import FWCore.ParameterSet.Config as cms

CorrectedElectronTrkiso = cms.EDProducer('CorrectedElectronTrkisoProducers',
     # input collections
     electronsLabel = cms.InputTag('gedGsfElectrons'),
     generalTracksLabel= cms.InputTag('generalTracks'),
     beamSpotLabel = cms.InputTag('offlineBeamSpot')
)
