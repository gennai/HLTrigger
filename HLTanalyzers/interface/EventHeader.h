#ifndef EVTHDR_H
#define EVTHDR_H

#include "TChain.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/Luminosity/interface/LumiSummary.h" 

/** \class EventHeader
  *  
  * $Date: November 2006
  * $Revision: 
  * \author V. Rekovic - UMinn
  */

class EventHeader {
public:
  EventHeader();
  ~EventHeader();

  void setup(edm::ConsumesCollector && iC, TTree* tree);

  /** Analyze the Data */
  void analyze(edm::Event const& iEvent, TTree* tree);

private:

  // Tree variables
  unsigned long long fEvent;
  int fLumiBlock;
  int fRun;
  int fBx;
  int fOrbit;
  double fAvgInstDelLumi;

  // input variables
  bool _Debug;
  edm::EDGetTokenT<LumiSummary> lumi_Token;

};

#endif
