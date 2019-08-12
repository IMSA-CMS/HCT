#ifndef ROOPOISSONFIXED_H
#define ROOPOISSONFIXED_H

#include "RooPoisson.h"

class RooArgSet;

class RooPoissonFixed : public RooPoisson
{
public:
  using RooPoisson::RooPoisson;
  RooPoissonFixed():RooPoisson(){}
  RooPoissonFixed(const char *name, const char *title, RooAbsReal& _x, RooAbsReal& _mean, Bool_t noRounding=kFALSE):RooPoisson(name, title, _x, _mean, noRounding){}
  RooPoissonFixed(const RooPoissonFixed& other, const char* name=0):RooPoisson(other, name){}
  virtual TObject* clone(const char* newname) const { return new RooPoissonFixed(*this,newname); }
  Double_t getLogVal(const RooArgSet* set=0) const;

private:
  ClassDef(RooPoissonFixed, 1)
};

#endif
