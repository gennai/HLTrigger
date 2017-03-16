#ifndef HLTINFO_H
#define HLTINFO_H

#include "TChain.h"

// CMSSW
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/TriggerResults.h"

#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"

#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"

#include "DataFormats/L1Trigger/interface/Muon.h"
#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/L1Trigger/interface/Jet.h"
#include "DataFormats/L1Trigger/interface/Tau.h"
#include "DataFormats/L1Trigger/interface/EtSum.h"

//namespace edm {
//  class ConsumesCollector;
//  class ParameterSet;
//}

/** \class HLTInfo
  *  
  * $Date: November 2006
  * $Revision: 
  * \author P. Bargassa - Rice U.
  * $Date: April 2016                                                                                                                                             
  * $Revision:     
  * \author G. Karapostoli - ULB    
  */

class HLTInfo {
public:
  template <typename T>
    HLTInfo(edm::ParameterSet const& pset,
	    edm::ConsumesCollector&& iC,
	    T& module);
  
  template <typename T>
    HLTInfo(edm::ParameterSet const& pset,
	    edm::ConsumesCollector& iC,
	    T& module);  
  
  void setup(const edm::ParameterSet& pSet, TTree* tree);
  void beginRun(const edm::Run& , const edm::EventSetup& );

  /** Analyze the Data */
  void analyze(const edm::Handle<edm::TriggerResults>      & hltresults,
	       const edm::Handle<GlobalAlgBlkBxCollection> & l1results,
               const edm::Handle<l1t::MuonBxCollection>    & l1muons,
	       const edm::Handle<l1t::EGammaBxCollection>  & l1egamma,
	       const edm::Handle<l1t::JetBxCollection>     & l1jets,
	       const edm::Handle<l1t::TauBxCollection>     & l1taus,
	       const edm::Handle<l1t::EtSumBxCollection>   & l1etsums,
	       edm::EventSetup const& eventSetup,
	       edm::Event const& iEvent,
	       TTree* tree);

private:

  HLTInfo();

  // Tree variables
  int L1EvtCnt,HltEvtCnt;

  bool *trigflag, *l1flag;
  int *trigPrescl, *l1Prescl; 

  float l1mumax_pt;
  float l1mumax_eta;
  float l1mumax_phi;

  float l1egmax_pt;
  float l1egmax_eta;
  float l1egmax_phi;

  float l1jetmax_pt;
  float l1jetmax_eta;
  float l1jetmax_phi;

  float l1taumax_pt;
  float l1taumax_eta;
  float l1taumax_phi;

  float l1totalet_pt;
  float l1totalet_eta;
  float l1totalet_phi;

  float l1totalht_pt;
  float l1totalht_eta;
  float l1totalht_phi;

  TString *algoBitToName;
  std::vector<std::string> dummyBranches_;

  std::unique_ptr<HLTPrescaleProvider> hltPrescaleProvider_;
  std::string processName_;

  bool _Debug;
};

template <typename T>
HLTInfo::HLTInfo(edm::ParameterSet const& pset,
		 edm::ConsumesCollector&& iC,
		 T& module) :
    HLTInfo(pset, iC, module) {
}
 
template <typename T>
HLTInfo::HLTInfo(edm::ParameterSet const& pset,
		 edm::ConsumesCollector& iC,
		 T& module) :
    HLTInfo() {
    hltPrescaleProvider_.reset(new HLTPrescaleProvider(pset, iC, module));
}

#endif
