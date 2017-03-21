#! /usr/bin/env python

import ROOT
import sys
import os

nBunches = 1.
nPU_min = 30.
nPU_max = 50.
nEventsMax = 1000000

ROOT.gStyle.SetOptStat(0)

dir_path = sys.argv[1]

print "Get the trees from eos"
eos_command = "eos ls " + dir_path + "/ | grep root | awk '{print \"rfio:/eos/cms" + dir_path + "/\"$0 }'"
file_list = os.popen(eos_command).read()
mytree = ROOT.TChain("HltTree")
for filename in file_list.split():
    mytree.Add(filename)

def get_scale_factor(_nZeroBias, _nBunches):

    if _nZeroBias != 0:
        scal = 11246.
        scal /= _nZeroBias
        scal *= _nBunches
        return scal

    return 0.

print "Preparing plotting stuff"
nbins_mupt = 131
nbins_jetpt = 250

h_l1rate = dict()
h_l1rate["MuPt"]      = ROOT.TH1F("MuPt","L1_SingleMu p_{T} distribution", nbins_mupt, -0.5, 130.5)
h_l1rate["MuErPt"]    = ROOT.TH1F("MuErPt","L1_SingleMuER p_{T} distribution", nbins_mupt, -0.5, 130.5)
h_l1rate["nMuVsPt"]   = ROOT.TH1F("nMuVsPt","L1_SingleMu rate vs p_{T} threshold", nbins_mupt, -0.5, 130.5)
h_l1rate["nMuErVsPt"] = ROOT.TH1F("nMuErVsPt","L1_SingleMuER rate vs p_{T} threshold", nbins_mupt, -0.5, 130.5)
h_l1rate["nMuVsEta"]  = ROOT.TH1F("nMuVsEta","L1_SingleMu16 rate vs #eta", 24, -2.4, 2.4)
h_l1rate["nMuVsPhi"]  = ROOT.TH1F("nMuVsPhi","L1_SingleMu16 rate vs #phi", 31, -3.14, 3.14)

h_l1rate["EGPt"]      = ROOT.TH1F("EGPt","L1_SingleEG p_{T} distribution", nbins_mupt, -0.5, 130.5)
h_l1rate["EGErPt"]    = ROOT.TH1F("EGErPt","L1_SingleEGER p_{T} distribution", nbins_mupt, -0.5, 130.5)
h_l1rate["nEGVsPt"]   = ROOT.TH1F("nEGVsPt","L1_SingleEG rate vs p_{T} threshold", nbins_mupt, -0.5, 130.5)
h_l1rate["nEGErVsPt"] = ROOT.TH1F("nEGErVsPt","L1_SingleEGER rate vs p_{T} threshold", nbins_mupt, -0.5, 130.5)
h_l1rate["nEGVsEta"]  = ROOT.TH1F("nEGVsEta","L1_SingleEG16 rate vs #eta", 24, -2.4, 2.4)
h_l1rate["nEGVsPhi"]  = ROOT.TH1F("nEGVsPhi","L1_SingleEG16 rate vs #phi", 31, -3.14, 3.14)

h_l1rate["JetPt"]        = ROOT.TH1F("JetPt","L1_SingleJet E_{T} distribution", nbins_jetpt, -0.5, 250.5)
h_l1rate["JetCPt"]       = ROOT.TH1F("JetCPt","L1_SingleJetCentral E_{T} distribution", nbins_jetpt, -0.5, 250.5)
h_l1rate["nJetVsPt"]     = ROOT.TH1F("nJetVsPt","L1_SingleJet rate vs E_{T} threshold", nbins_jetpt, -0.5, 250.5)
h_l1rate["nJet32VsEta"]  = ROOT.TH1F("nJet32VsEta","L1_SingleJet32 rate vs #eta", 70, -5.5, 5.5)
h_l1rate["nJet32VsPhi"]  = ROOT.TH1F("nJet32VsPhi","L1_SingleJet32 rate vs #phi", 30, -3.14, 3.14)
h_l1rate["nJet64VsEta"]  = ROOT.TH1F("nJet64VsEta","L1_SingleJet64 rate vs #eta", 70, -5.5, 5.5)
h_l1rate["nJet64VsPhi"]  = ROOT.TH1F("nJet64VsPhi","L1_SingleJet64 rate vs #phi", 30, -3.14, 3.14)
h_l1rate["nJet120VsEta"] = ROOT.TH1F("nJet120VsEta","L1_SingleJet120 rate vs #eta", 70, -5.5, 5.5)
h_l1rate["nJet120VsPhi"] = ROOT.TH1F("nJet120VsPhi","L1_SingleJet120 rate vs #phi", 30, -3.14, 3.14)

h_l1rate["TauErPt"]       = ROOT.TH1F("TauErPt","L1_SingleTauER E_{T} distribution", nbins_jetpt, -0.5, 250.5)
h_l1rate["nTauErVsPt"]    = ROOT.TH1F("nTauErVsPt","L1_SingleTauER rate vs E_{T} threshold", nbins_jetpt, -0.5, 250.5)
h_l1rate["nTau32VsEta"]   = ROOT.TH1F("nTau32VsEta","L1_SingleTau32 rate vs #eta", 45, -4., 4.)
h_l1rate["nTauEr32VsPhi"] = ROOT.TH1F("nTauEr32VsPhi","L1_SingleTau32ER rate vs #phi", 31, -3.14, 3.14)

h_l1rate["MuPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["MuErPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nMuVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nMuErVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["EGPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["EGErPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nEGVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nEGErVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["JetPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["JetCPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nJetVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["TauErPt"].GetXaxis().SetTitle("p_{T} [GeV]")
h_l1rate["nTauErVsPt"].GetXaxis().SetTitle("p_{T} [GeV]")

h_l1rate["nMuVsEta"].GetXaxis().SetTitle("#eta")
h_l1rate["nEGVsEta"].GetXaxis().SetTitle("#eta")
h_l1rate["nJet32VsEta"].GetXaxis().SetTitle("#eta")
h_l1rate["nJet64VsEta"].GetXaxis().SetTitle("#eta")
h_l1rate["nJet120VsEta"].GetXaxis().SetTitle("#eta")
h_l1rate["nTau32VsEta"].GetXaxis().SetTitle("#eta")

h_l1rate["nMuVsPhi"].GetXaxis().SetTitle("#phi")
h_l1rate["nEGVsPhi"].GetXaxis().SetTitle("#phi")
h_l1rate["nJet32VsPhi"].GetXaxis().SetTitle("#phi")
h_l1rate["nJet64VsPhi"].GetXaxis().SetTitle("#phi")
h_l1rate["nJet120VsPhi"].GetXaxis().SetTitle("#phi")
h_l1rate["nTauEr32VsPhi"].GetXaxis().SetTitle("#phi")

for hname in h_l1rate:
    h_l1rate[hname].SetLineColor(ROOT.kRed)
    h_l1rate[hname].SetMarkerStyle(21)
    

nZeroBias = 0.

print "Starting the loop over the events"
for jentry in xrange(mytree.GetEntriesFast()):
    ientry = mytree.LoadTree(jentry)
    if ientry < 0:
        break
    nb = mytree.GetEntry(jentry)
    if nb <=0:
        continue

    npubx0 = mytree.NPUgenBX0
    if npubx0 < nPU_min or npubx0 > nPU_max:
        continue

    nZeroBias += 1.

    if nZeroBias % 50000 == 0 :
        print "Processing event number = ", nZeroBias

    if nZeroBias > nEventsMax and nEventsMax != -1:
        break

    #Get the leading objects of the event
    maxmu_pt  = mytree.L1muon_pt
    maxmu_eta = mytree.L1muon_eta
    maxmu_phi = mytree.L1muon_phi

    maxeg_pt  = mytree.L1egamma_pt
    maxeg_eta = mytree.L1egamma_eta
    maxeg_phi = mytree.L1egamma_phi

    maxjet_pt  = mytree.L1jet_pt
    maxjet_eta = mytree.L1jet_eta
    maxjet_phi = mytree.L1jet_phi

    maxtau_pt  = mytree.L1tau_pt
    maxtau_eta = mytree.L1tau_eta
    maxtau_phi = mytree.L1tau_phi

    ##Fill the histos
    h_l1rate["MuPt"].Fill(maxmu_pt)
    h_l1rate["EGPt"].Fill(maxeg_pt)
    h_l1rate["JetPt"].Fill(maxjet_pt)

    if(abs(maxmu_eta) <= 2.1):
        h_l1rate["MuErPt"].Fill(maxmu_pt)
    if(abs(maxeg_eta) <= 2.1):
        h_l1rate["EGErPt"].Fill(maxeg_pt)
    if(abs(maxjet_eta) <= 2.4):
        h_l1rate["JetCPt"].Fill(maxjet_pt)
    if(abs(maxtau_eta) <= 2.4):
        h_l1rate["TauErPt"].Fill(maxtau_pt)

    ##Fill the histos for rate vs threshold
    for ptcut in xrange(nbins_mupt):
        if  maxmu_pt>= ptcut :
            h_l1rate["nMuVsPt"].Fill(ptcut)
            if abs(maxmu_eta) <= 2.1 :
                h_l1rate["nMuErVsPt"].Fill(ptcut)

        if maxeg_pt >= ptcut :
            h_l1rate["nEGVsPt"].Fill(ptcut)
            if abs(maxeg_eta) <= 2.1 :
                h_l1rate["nEGErVsPt"].Fill(ptcut)

    for ptcut in xrange(nbins_jetpt):
        if maxjet_pt >= ptcut :
            h_l1rate["nJetVsPt"].Fill(ptcut)
        if maxtau_pt >= ptcut and abs(maxtau_eta) <= 2.4 :
            h_l1rate["nTauErVsPt"].Fill(ptcut)

    #Fill the histos for rate vs eta
    if maxmu_pt >= 16. :
        if maxmu_eta > -5. :
            h_l1rate["nMuVsEta"].Fill(maxmu_eta)
        if maxmu_phi > -5. :
            h_l1rate["nMuVsPhi"].Fill(maxmu_phi)

    if maxeg_pt >= 16. :
        if maxeg_eta > -5. :
            h_l1rate["nEGVsEta"].Fill(maxeg_eta)
        if maxeg_phi > -5. :
            h_l1rate["nEGVsPhi"].Fill(maxeg_phi)

    if maxjet_pt >= 32. :
        if maxjet_eta > -5. :
            h_l1rate["nJet32VsEta"].Fill(maxjet_eta)
        if maxjet_phi > -5. :
            h_l1rate["nJet32VsPhi"].Fill(maxjet_phi)

    if maxjet_pt >= 64. :
        if maxjet_eta > -5. :
            h_l1rate["nJet64VsEta"].Fill(maxjet_eta)
        if maxjet_phi > -5. :
            h_l1rate["nJet64VsPhi"].Fill(maxjet_phi)

    if maxjet_pt >= 120. :
        if maxjet_eta > -5. :
            h_l1rate["nJet120VsEta"].Fill(maxjet_eta)
        if maxjet_phi > -5. :
            h_l1rate["nJet120VsPhi"].Fill(maxjet_phi)

    if maxtau_pt >= 32. :
        if maxtau_eta > -5. :
            h_l1rate["nTau32VsEta"].Fill(maxtau_eta)
        if maxtau_phi > -5. and abs(maxtau_eta) <= 2.4:
            h_l1rate["nTauEr32VsPhi"].Fill(maxtau_phi)


print "End of event loop"


if not os.path.exists("results"):
    os.makedirs("results")

fOut_histos = ROOT.TFile("results/l1rates_histos.root","RECREATE")
scale_factor_std = get_scale_factor(nZeroBias,nBunches)

for hname in h_l1rate:
    h_l1rate[hname].Scale(scale_factor_std)
    h_l1rate[hname].GetYaxis().SetTitle("Rate/bunch x-ing [Hz]")
    h_l1rate[hname].Write()

    c1 = ROOT.TCanvas()
    c1.cd()
    if "Pt" in hname:
        c1.SetLogy()
    h_l1rate[hname].Draw("PE")
    c1.SaveAs("results/" + hname + ".gif")

fOut_histos.Close()

print "Number of events analyzed = ", nZeroBias
